import importlib.util
import os
from pathlib import Path
import sys
from unittest.mock import patch

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from llm_config import DEFAULT_BASE_URL, DEFAULT_MODEL, resolve_llm_config

SUMMARY = {
    "SUMMARY_API_KEY": "summary-key",
    "SUMMARY_BASE_URL": "https://summary.example/v3",
    "SUMMARY_MODEL": "summary-model",
}
LEGACY = {
    "DEEPSEEK_API_KEY": "stale-key",
    "DEEPSEEK_BASE_URL": "https://api.deepseek.com",
    "DEEPSEEK_MODEL": "stale-model",
    "DEEPSEEK_FILTER_MODEL": "stale-filter",
    "DEEPSEEK_REWRITE_MODEL": "stale-rewrite",
}


def load_step(filename):
    name = "unified_" + filename.replace(".", "_")
    spec = importlib.util.spec_from_file_location(name, ROOT / "src" / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize("env", [SUMMARY, {**LEGACY, **SUMMARY}])
def test_summary_configuration_reaches_daily_calls(env):
    with patch.dict(os.environ, {**env, "DPR_DISABLE_DOTENV": "1"}, clear=True):
        generate = load_step("6.generate_docs.py")
        client = generate.create_llm_client()
        assert (client.api_key, client.base_url, client.model) == tuple(SUMMARY.values())
        refine = load_step("4.llm_refine_papers.py")
        assert refine.DEFAULT_FILTER_MODEL == SUMMARY["SUMMARY_MODEL"]
        assert refine.DEFAULT_DEEPSEEK_BASE_URL == SUMMARY["SUMMARY_BASE_URL"]
        enrich = load_step("0.enrich_config_queries.py")
        assert enrich.MODEL_NAME == SUMMARY["SUMMARY_MODEL"]
        assert enrich.BASE_URL == SUMMARY["SUMMARY_BASE_URL"]


@pytest.mark.parametrize("filename", [
    "daily-paper-reader.yml", "conference-paper-retrieval.yml",
    "starter-pack.yml", "topic-research.yml",
])
def test_each_workflow_exposes_summary_configuration(filename):
    workflow = yaml.safe_load((ROOT / ".github/workflows" / filename).read_text())
    jobs = [job for job in workflow["jobs"].values() if "DEEPSEEK_API_KEY" in job.get("env", {})]
    assert jobs
    for job in jobs:
        for key in SUMMARY:
            assert job["env"].get(key) == "${{ secrets." + key + " }}"


@pytest.mark.parametrize("purpose", ["", "filter", "rewrite"])
def test_summary_key_alone_never_inherits_stale_provider_fields(purpose):
    config = resolve_llm_config({**LEGACY, "SUMMARY_API_KEY": "new-key"}, purpose=purpose)
    assert (config.api_key, config.base_url, config.model) == ("new-key", DEFAULT_BASE_URL, DEFAULT_MODEL)
    assert "new-key" not in repr(config)


def test_incomplete_summary_config_does_not_borrow_legacy_key():
    config = resolve_llm_config({**LEGACY, "SUMMARY_BASE_URL": "https://new.example/v1"})
    with pytest.raises(RuntimeError, match="SUMMARY_API_KEY"):
        config.require_api_key()


def test_empty_github_secrets_fall_back_to_legacy_group():
    config = resolve_llm_config({**LEGACY, **{key: "  " for key in SUMMARY}}, purpose="filter")
    assert (config.api_key, config.base_url, config.model) == ("stale-key", "https://api.deepseek.com", "stale-filter")


def test_factory_uses_summary_even_with_legacy_llm_configuration():
    from llm import ClientFactory
    with patch.dict(os.environ, {**SUMMARY, **LEGACY, "LLM_MODEL": "deepseek/old-model", "LLM_API_KEY": "old-key"}, clear=True):
        client = ClientFactory.from_env()
    assert (client.api_key, client.base_url, client.model) == tuple(SUMMARY.values())


def test_starter_review_uses_summary_for_request_and_cache(tmp_path):
    from unittest.mock import Mock
    import starter_pack

    client = Mock(kwargs={})
    client.chat_structured.return_value = {"parsed": {"papers": [{
        "id": "p0", "score": 8, "scope_match": True, "evidence": "ATSP", "reason": "相关",
    }]}}
    with patch.dict(os.environ, {**SUMMARY, **LEGACY}, clear=True), patch("llm.DeepSeekClient", return_value=client) as factory:
        result = starter_pack.review_candidates(
            [{"id": "paper", "title": "ATSP", "abstract": "ATSP methods"}],
            {"tag": "ATSP"}, tmp_path, 1,
        )
        factory.assert_called_once_with(SUMMARY["SUMMARY_API_KEY"], SUMMARY["SUMMARY_MODEL"], SUMMARY["SUMMARY_BASE_URL"])
        assert result["new_reviews"] == 1
        again = starter_pack.review_candidates(
            [{"id": "paper", "title": "ATSP", "abstract": "ATSP methods"}],
            {"tag": "ATSP"}, tmp_path, 1,
        )
        assert again["new_reviews"] == 0
        factory.assert_called_once()
