"""查询扩充、评分、总结和导读共用的模型配置。"""

from dataclasses import dataclass, field
import os
from typing import Mapping


DEFAULT_BASE_URL = "https://ark.cn-beijing.volces.com/api/plan/v3"
DEFAULT_MODEL = "deepseek-v4.1-flash"


@dataclass(frozen=True)
class LLMConfig:
    api_key: str = field(repr=False)
    base_url: str
    model: str

    def require_api_key(self) -> str:
        if not self.api_key:
            raise RuntimeError("缺少 SUMMARY_API_KEY，请在模型配置中保存 API Key。")
        return self.api_key

    def as_env(self) -> dict[str, str]:
        return {
            "SUMMARY_API_KEY": self.api_key,
            "SUMMARY_BASE_URL": self.base_url,
            "SUMMARY_MODEL": self.model,
        }


def resolve_llm_config(
    environ: Mapping[str, str] | None = None, *, purpose: str = ""
) -> LLMConfig:
    env = os.environ if environ is None else environ

    def read(name: str) -> str:
        return str(env.get(name) or "").strip()

    # 按整组选择，不能将 SUMMARY 的 Key 与历史 DEEPSEEK 地址/模型拼在一起。
    # Actions 中未配置的 Secret 会是空串，不算启用一组配置。
    use_summary = any(read("SUMMARY_" + name) for name in ("API_KEY", "BASE_URL", "MODEL"))
    prefix = "SUMMARY_" if use_summary else "DEEPSEEK_"
    model = read(prefix + "MODEL")
    if not use_summary and purpose in {"filter", "rewrite"}:
        model = read("DEEPSEEK_" + purpose.upper() + "_MODEL") or model
    return LLMConfig(
        api_key=read(prefix + "API_KEY"),
        base_url=read(prefix + "BASE_URL") or DEFAULT_BASE_URL,
        model=model or DEFAULT_MODEL,
    )
