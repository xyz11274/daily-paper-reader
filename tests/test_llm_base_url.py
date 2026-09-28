import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from llm import LLMClient


class LlmBaseUrlTest(unittest.TestCase):
    @patch("llm.requests.post")
    def test_ark_plan_uses_v3_and_compatible_v41_parameters(self, mock_post):
        mock_post.return_value = self._mock_response()
        client = LLMClient(
            api_key="test-key", model="deepseek-v4.1-flash",
            base_url="https://ark.cn-beijing.volces.com/api/plan/v3",
        )
        client.chat([{"role": "user", "content": "hello"}])
        self.assertEqual(mock_post.call_args.args[0], "https://ark.cn-beijing.volces.com/api/plan/v3/chat/completions")
        payload = mock_post.call_args.kwargs["json"]
        self.assertEqual(payload["max_tokens"], 131072)
        self.assertEqual(payload["thinking"], {"type": "disabled"})
        self.assertNotIn("frequency_penalty", payload)
        self.assertNotIn("presence_penalty", payload)

    @patch("llm.requests.post")
    def test_ark_keeps_explicit_thinking_and_small_output_budget(self, mock_post):
        mock_post.return_value = self._mock_response()
        client = LLMClient("test-key", "deepseek-v4-1-flash-260910", "https://ark.cn-beijing.volces.com/api/plan/v3")
        client.kwargs.update(max_tokens=1024, thinking={"type": "enabled"})
        client.chat([{"role": "user", "content": "hello"}])
        payload = mock_post.call_args.kwargs["json"]
        self.assertEqual(payload["max_tokens"], 1024)
        self.assertEqual(payload["thinking"], {"type": "enabled"})

    def _mock_response(self):
        resp = MagicMock()
        resp.raise_for_status.return_value = None
        resp.json.return_value = {
            "choices": [
                {
                    "message": {
                        "content": "ok",
                    }
                }
            ],
            "usage": {
                "prompt_tokens": 1,
                "completion_tokens": 1,
                "total_tokens": 2,
            },
        }
        return resp

    @patch("llm.requests.post")
    def test_chat_auth_error_fails_without_retrying_other_bases(self, mock_post):
        resp = MagicMock()
        resp.status_code = 401
        resp.json.return_value = {
            "error": {
                "message": "Authentication Fails, Your api key is invalid",
                "type": "authentication_error",
            }
        }
        err = Exception("401 Client Error: Authorization Required")
        err.response = resp
        resp.raise_for_status.side_effect = err
        mock_post.return_value = resp

        client = LLMClient(
            api_key="bad-key",
            model="deepseek-v4-flash",
            base_url="https://api.deepseek.com,https://fallback.invalid",
        )

        with self.assertRaises(Exception):
            client.chat([{"role": "user", "content": "hello"}])

        self.assertEqual(mock_post.call_count, 1)

    @patch("llm.requests.post")
    def test_chat_appends_v1_when_base_is_root(self, mock_post):
        mock_post.return_value = self._mock_response()
        client = LLMClient(
            api_key="test-key",
            model="gpt-4.1-mini",
            base_url="https://api.openai.com",
        )

        client.chat([{"role": "user", "content": "hello"}])

        self.assertEqual(
            mock_post.call_args.args[0],
            "https://api.openai.com/v1/chat/completions",
        )

    @patch("llm.requests.post")
    def test_chat_keeps_versioned_base(self, mock_post):
        mock_post.return_value = self._mock_response()
        client = LLMClient(
            api_key="test-key",
            model="gpt-4.1-mini",
            base_url="https://api.openai.com/v1",
        )

        client.chat([{"role": "user", "content": "hello"}])

        self.assertEqual(
            mock_post.call_args.args[0],
            "https://api.openai.com/v1/chat/completions",
        )

    @patch("llm.requests.post")
    def test_chat_uses_full_endpoint_directly(self, mock_post):
        mock_post.return_value = self._mock_response()
        client = LLMClient(
            api_key="test-key",
            model="gpt-4.1-mini",
            base_url="https://api.openai.com/v1/chat/completions",
        )

        client.chat([{"role": "user", "content": "hello"}])

        self.assertEqual(
            mock_post.call_args.args[0],
            "https://api.openai.com/v1/chat/completions",
        )


if __name__ == "__main__":
    unittest.main()
