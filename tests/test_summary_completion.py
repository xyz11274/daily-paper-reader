import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
spec = importlib.util.spec_from_file_location("summary_completion_gen", ROOT / "src/6.generate_docs.py")
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)


class SummaryCompletionTest(unittest.TestCase):
    def test_replacing_incomplete_block_preserves_notes(self):
        with tempfile.TemporaryDirectory() as directory:
            md = Path(directory) / "paper.md"
            md.write_text("# Paper\n\n---\n\n## 论文详细总结（自动生成）\n## 方法\n截断\n\n## 我的笔记\n保留这段笔记\n", encoding="utf-8")
            for _ in range(2):
                gen.upsert_auto_block(str(md), "论文详细总结（自动生成）", "## 方法\n完整内容\n（完）")
            text = md.read_text(encoding="utf-8")
        self.assertIn("## 我的笔记\n保留这段笔记", text)
        self.assertEqual(text.count("完整内容"), 1)
        self.assertEqual(text.count(gen.AUTO_BLOCK_END), 1)
        self.assertNotIn("我的笔记", gen.extract_section_tail(text, "论文详细总结（自动生成）"))

    def test_brief_uses_fallback_after_bounded_truncation_retries(self):
        client = Mock(kwargs={})
        client.chat.return_value = {"content": "不能发布的半句话", "finish_reason": "length"}
        with patch.object(gen, "LLM_CLIENT", client):
            summary = gen.build_daily_brief_summary("2026-09-28", [("paper", "Research", [])], [], 1, "完成")
        self.assertNotIn("不能发布", summary)
        self.assertIn("1 篇", summary)
        self.assertEqual(client.chat.call_count, 3)

    def test_filtered_response_is_not_published(self):
        client = Mock(kwargs={})
        client.chat.return_value = {"content": "partial", "finish_reason": "content_filter"}
        with self.assertRaises(ValueError):
            gen.call_llm_text(client, [], temperature=0.3, max_tokens=256)
        self.assertEqual(client.chat.call_count, 1)

    def test_inline_end_marker_is_not_complete(self):
        self.assertFalse(gen.is_complete_deep_summary("模型应该输出（完）但实际未完成"))

    def test_daily_brief_does_not_publish_length_truncated_response(self):
        client = Mock(kwargs={})
        client.chat.side_effect = [
            {"content": "今天推荐的研究方向包括", "finish_reason": "length"},
            {"content": "今天推荐一篇智能体研究论文。建议先阅读方法。", "finish_reason": "stop"},
        ]
        with patch.object(gen, "LLM_CLIENT", client):
            summary = gen.build_daily_brief_summary(
                "2026-09-28", [("paper", "Agent Research", [])], [], 1, "完成"
            )
        self.assertEqual(summary, "今天推荐一篇智能体研究论文。建议先阅读方法。")

    def test_exhausted_deep_summary_is_not_returned_as_complete(self):
        client = Mock(kwargs={})
        client.chat.return_value = {"content": "## 方法\n尚未完成的总结", "finish_reason": "length"}
        with tempfile.TemporaryDirectory() as directory:
            md = Path(directory) / "paper.md"
            txt = Path(directory) / "paper.txt"
            md.write_text("# Paper\n## Abstract\nAbstract", encoding="utf-8")
            txt.write_text("Original paper evidence", encoding="utf-8")
            with patch.object(gen.time, "sleep"):
                summary = gen.generate_deep_summary(str(md), str(txt), max_retries=1, client=client)
        self.assertIsNone(summary)

    def test_continuation_retains_original_paper(self):
        client = Mock(kwargs={})
        client.chat.side_effect = [
            {"content": "## 方法\n方法概述。", "finish_reason": "stop"},
            {"content": "## 局限\n实验范围有限。\n（完）", "finish_reason": "stop"},
        ]
        with tempfile.TemporaryDirectory() as directory:
            md = Path(directory) / "paper.md"
            txt = Path(directory) / "paper.txt"
            md.write_text("# Paper\n## Abstract\nAbstract", encoding="utf-8")
            txt.write_text("Original paper evidence", encoding="utf-8")
            summary = gen.generate_deep_summary(str(md), str(txt), max_retries=1, client=client)
        self.assertTrue(summary.endswith("（完）"))
        continuation = client.chat.call_args_list[1].kwargs["messages"]
        self.assertTrue(any("Original paper evidence" in m["content"] for m in continuation))


if __name__ == "__main__":
    unittest.main()
