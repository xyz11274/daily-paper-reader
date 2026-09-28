import io
import json
import os
from pathlib import Path
import subprocess
import sys
from unittest.mock import Mock, patch

import pytest
import requests
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import query_candidates as query
from local_debug_server import Handler


CANDIDATES = {
    "tag": "agents",
    "description": "智能体经验记忆",
    "keywords": [{"keyword": "agent memory", "query": "agent experience memory", "keyword_cn": "智能体记忆"}],
    "intent_queries": [{"query": "How do agents learn from experience?", "query_cn": "智能体如何积累经验？"}],
}
ENV = {
    "SUMMARY_API_KEY": "test-summary-key",
    "SUMMARY_BASE_URL": "https://ark.cn-beijing.volces.com/api/plan/v3",
    "SUMMARY_MODEL": "deepseek-v4.1-flash",
    "DEEPSEEK_API_KEY": "stale-key",
    "DEEPSEEK_BASE_URL": "https://api.deepseek.com",
    "GITHUB_TOKEN": "test-github-token",
    "GITHUB_REPOSITORY": "tester/papers",
    "GITHUB_SHA": "a" * 40,
    "GITHUB_RUN_ID": "42",
    "QUERY_REQUEST_ID": "test-request-123456",
    "QUERY_PROMPT": "Return JSON retrieval candidates for agent memory.",
}


@pytest.fixture(autouse=True)
def env():
    with patch.dict(os.environ, ENV, clear=True):
        yield


def test_uses_summary_group_and_short_non_thinking_request():
    def chat(client, messages, response_format=None):
        assert client.api_key == ENV["SUMMARY_API_KEY"]
        assert client.base_url == ENV["SUMMARY_BASE_URL"]
        assert client.model == ENV["SUMMARY_MODEL"]
        assert client.kwargs["thinking"] == {"type": "disabled"}
        assert client.kwargs["max_tokens"] == 8192
        assert len(client._iter_retry_bases()) == 1
        assert response_format == {"type": "json_object"}
        return {"content": json.dumps(CANDIDATES), "finish_reason": "stop"}

    with patch.object(query.CandidateClient, "chat", chat):
        assert query.generate_candidates(ENV["QUERY_PROMPT"]) == CANDIDATES


@pytest.mark.parametrize("response", [
    {"content": json.dumps(CANDIDATES), "finish_reason": "length"},
    {"content": '{"keywords":[', "finish_reason": "stop"},
    {"content": json.dumps({**CANDIDATES, "keywords": []}), "finish_reason": "stop"},
    {"content": json.dumps({**CANDIDATES, "keywords": [{"keyword": "记忆", "query": "memory"}]}), "finish_reason": "stop"},
    {"content": json.dumps({**CANDIDATES, "intent_queries": "invalid"}), "finish_reason": "stop"},
])
def test_does_not_publish_partial_or_invalid_candidates(response):
    with patch.object(query.CandidateClient, "chat", return_value=response):
        with pytest.raises(query.CandidateError):
            query.generate_candidates(ENV["QUERY_PROMPT"])


def test_missing_summary_key_cannot_borrow_legacy_key():
    with patch.dict(os.environ, {"SUMMARY_API_KEY": ""}):
        with pytest.raises(query.CandidateError, match="SUMMARY_API_KEY"):
            query.generate_candidates(ENV["QUERY_PROMPT"])


@pytest.mark.parametrize("prompt", [None, "", "词" * 8001])
def test_rejects_invalid_prompt_before_model_request(prompt):
    with patch.object(query.CandidateClient, "chat") as chat:
        with pytest.raises(query.CandidateError):
            query.generate_candidates(prompt)
        chat.assert_not_called()


def test_action_returns_result_for_exact_request_without_secrets():
    with patch.object(query, "generate_candidates", return_value=CANDIDATES), patch.object(query.requests, "post", return_value=Mock(ok=True)) as post:
        assert query.run_action() == 0
    payload = post.call_args.kwargs["json"]
    assert payload["name"] == "dpr-query-" + ENV["QUERY_REQUEST_ID"]
    assert payload["head_sha"] == ENV["GITHUB_SHA"]
    assert payload["details_url"].endswith("/actions/runs/42")
    assert payload["conclusion"] == "success"
    assert json.loads(payload["output"]["text"])["candidates"] == CANDIDATES
    assert json.loads(payload["output"]["text"])["run_id"] == "42"
    assert "test-summary-key" not in json.dumps(payload)
    assert "test-github-token" not in json.dumps(payload)


def test_failure_result_does_not_echo_raw_provider_error():
    response = requests.Response()
    response.status_code = 401
    error = requests.HTTPError("raw diagnostic test-summary-key", response=response)
    with patch.object(query.CandidateClient, "chat", side_effect=error), patch.object(query.requests, "post", return_value=Mock(ok=True)) as post:
        assert query.run_action() == 1
    payload = post.call_args.kwargs["json"]
    assert payload["conclusion"] == "failure"
    assert json.loads(payload["output"]["text"])["run_id"] == "42"
    assert "SUMMARY_API_KEY" in payload["output"]["text"]
    assert "test-summary-key" not in json.dumps(payload)


def test_workflow_uses_summary_secrets_and_does_not_write_repository():
    path = Path(__file__).resolve().parents[1] / ".github/workflows/generate-query.yml"
    config = yaml.safe_load(path.read_text())
    assert config["permissions"] == {"contents": "read", "checks": "write"}
    step = config["jobs"]["generate"]["steps"][-1]
    for field in ("API_KEY", "BASE_URL", "MODEL"):
        assert step["env"]["SUMMARY_" + field] == "${{ secrets.SUMMARY_" + field + " }}"
    assert "${{" not in step["run"], "untrusted prompt must be passed through env, never shell interpolation"


def make_handler(payload, origin="http://127.0.0.1:8080"):
    handler = object.__new__(Handler)
    raw = json.dumps(payload).encode()
    handler.headers = {"Content-Length": str(len(raw)), "Origin": origin, "Host": "127.0.0.1:8567"}
    handler.rfile = io.BytesIO(raw)
    handler._json = Mock()
    return handler


def test_local_handler_returns_candidates_from_server_configuration():
    handler = make_handler({"prompt": ENV["QUERY_PROMPT"], "secret": {"apiKey": "browser-old-key"}})
    result = {"ok": True, "candidates": CANDIDATES}
    with patch("local_debug_server.subprocess.run", return_value=Mock(stdout=json.dumps(result))) as run:
        handler._generate_query_candidates()
    handler._json.assert_called_once_with(result, status=200)
    assert run.call_args.kwargs["input"] == ENV["QUERY_PROMPT"]
    assert "browser-old-key" not in str(run.call_args)


def test_local_handler_rejects_external_origin():
    handler = make_handler({"prompt": ENV["QUERY_PROMPT"]}, "https://unrelated.example")
    with patch("local_debug_server.subprocess.run") as run:
        handler._generate_query_candidates()
        run.assert_not_called()
    assert handler._json.call_args.kwargs["status"] == 403


def test_local_timeout_is_reported():
    handler = make_handler({"prompt": ENV["QUERY_PROMPT"]})
    with patch("local_debug_server.subprocess.run", side_effect=subprocess.TimeoutExpired("query", 270)):
        handler._generate_query_candidates()
    assert handler._json.call_args.kwargs["status"] == 504
