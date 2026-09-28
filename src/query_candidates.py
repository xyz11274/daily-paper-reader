"""网页检索词条生成：与流水线共用 SUMMARY_*，结果通过 Checks API 返回。"""

from __future__ import annotations

import contextlib
import io
import json
import os
import re
import sys

import requests

from llm import LLMClient
from llm_config import resolve_llm_config


class CandidateError(ValueError):
    """可以直接向网页展示的错误；不包含供应商原始响应或凭据。"""


class CandidateClient(LLMClient):
    def _iter_retry_bases(self, total_attempts: int = 6) -> list[str]:
        return super()._iter_retry_bases(min(total_attempts, 1))


def generate_candidates(prompt: str) -> dict:
    if not isinstance(prompt, str) or not prompt.strip() or len(prompt.encode("utf-8")) > 24000:
        raise CandidateError("检索需求为空或过长，请缩短后重试。")
    config = resolve_llm_config()
    if not config.api_key:
        raise CandidateError("请在仓库 Actions Secrets 中配置 SUMMARY_API_KEY。")
    client = CandidateClient(api_key=config.api_key, base_url=config.base_url, model=config.model)
    client.kwargs.update(max_tokens=8192, temperature=0.1)
    # 此步骤只需要短 JSON，DeepSeek 思考输出会增加等待和截断风险。
    if "deepseek" in config.model.lower():
        client.kwargs["thinking"] = {"type": "disabled"}
    messages = [
        {"role": "system", "content": "You are a retrieval planning assistant. Return valid JSON based only on the current user input."},
        {"role": "user", "content": prompt},
    ]
    try:
        # 不把供应商原始错误回显到公开的 workflow/check 输出。
        with contextlib.redirect_stdout(io.StringIO()):
            try:
                response = client.chat(messages, response_format={"type": "json_object"})
            except Exception as exc:
                if not client._is_structured_output_unsupported_error(exc):
                    raise
                response = client.chat(messages)
    except requests.HTTPError as exc:
        status = exc.response.status_code if exc.response is not None else None
        if status in {401, 403}:
            raise CandidateError("模型鉴权失败，请检查 SUMMARY_API_KEY 是否匹配 SUMMARY_BASE_URL。") from None
        if status == 429:
            raise CandidateError("模型服务限流或额度不足，请稍后重试并检查套餐额度。") from None
        raise CandidateError("模型请求失败，请检查 SUMMARY_BASE_URL 和 SUMMARY_MODEL。") from None
    except requests.RequestException:
        raise CandidateError("模型服务连接失败或超时，请稍后重试。") from None
    if response.get("refusal") or response.get("finish_reason") != "stop":
        raise CandidateError("模型未完整生成候选，请缩短需求后重试。")
    try:
        # 不修补截断 JSON，避免把缺失字段的半份结果当作生成成功。
        data = json.loads(client._strip_json_wrappers(response.get("content") or ""))
    except (ValueError, TypeError):
        raise CandidateError("模型返回的候选格式无效，请重试。") from None
    if not isinstance(data, dict):
        raise CandidateError("模型返回的候选格式无效，请重试。")
    keywords = data.get("keywords")
    intents = data.get("intent_queries")
    if not isinstance(keywords, list) or not 1 <= len(keywords) <= 12 or not isinstance(intents, list) or len(intents) > 4:
        raise CandidateError("模型未返回有效的关键词和意图查询，请重试。")
    for field, items in (("keyword", keywords), ("query", intents)):
        for item in items:
            for key in {field, "query"}:
                value = item.get(key) if isinstance(item, dict) else None
                if not isinstance(value, str) or not value.strip() or re.search(r"[\u3400-\u9fff\uf900-\ufaff]", value):
                    raise CandidateError("模型未返回有效英文检索词，请重试。")
    if len(json.dumps(data, ensure_ascii=False).encode("utf-8")) > 40000:
        raise CandidateError("模型返回的候选过长，请缩短需求后重试。")
    return data


def run_action() -> int:
    request_id = os.environ.get("QUERY_REQUEST_ID", "")
    repository = os.environ.get("GITHUB_REPOSITORY", "")
    if not re.fullmatch(r"[a-zA-Z0-9-]{16,64}", request_id) or not re.fullmatch(r"[\w.-]+/[\w.-]+", repository):
        raise CandidateError("无效的请求编号或仓库。")
    try:
        data = {"ok": True, "request_id": request_id, "candidates": generate_candidates(os.environ.get("QUERY_PROMPT", ""))}
    except CandidateError as exc:
        data = {"ok": False, "request_id": request_id, "error": str(exc)}
    except Exception:
        data = {"ok": False, "request_id": request_id, "error": "生成服务发生错误，请检查运行环境后重试。"}
    # 使用自己的结果字段关联 Actions，details_url 可能被 GitHub 改写。
    data["run_id"] = os.environ["GITHUB_RUN_ID"]
    run_url = f"https://github.com/{repository}/actions/runs/{os.environ['GITHUB_RUN_ID']}"
    response = requests.post(
        f"https://api.github.com/repos/{repository}/check-runs",
        headers={
            "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
        json={
            "name": f"dpr-query-{request_id}",
            "head_sha": os.environ["GITHUB_SHA"],
            "external_id": request_id,
            "details_url": run_url,
            "status": "completed",
            "conclusion": "success" if data["ok"] else "failure",
            "output": {
                "title": "检索词条生成",
                "summary": "候选已生成，请返回网页选择。" if data["ok"] else data["error"],
                "text": json.dumps(data, ensure_ascii=False),
            },
        },
        timeout=30,
    )
    if not response.ok:
        # 不重试写入，避免创建重复 check；网页会展示本次运行失败。
        print(f"结果回传失败（GitHub HTTP {response.status_code}），请检查 checks: write 权限。")
        return 1
    print("候选结果已回传。" if data["ok"] else data["error"])
    return 0 if data["ok"] else 1


if __name__ == "__main__":
    if sys.argv[1:] == ["--local"]:
        from local_env import load_local_env

        load_local_env()
        try:
            result = {"ok": True, "candidates": generate_candidates(sys.stdin.read(24001))}
        except CandidateError as exc:
            result = {"ok": False, "error": str(exc).replace("仓库 Actions Secrets", "本地 .env")}
        except Exception:
            result = {"ok": False, "error": "生成服务发生错误，请检查本地模型配置后重试。"}
        print(json.dumps(result, ensure_ascii=False))
    else:
        raise SystemExit(run_action())
