from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
README_ZH = ROOT / "README.zh-CN.md"
SKILL = ROOT / "skills" / "serenity-invest" / "SKILL.md"


class SerenityInvestSkillContractTests(unittest.TestCase):
    def test_skill_frontmatter_and_name(self):
        text = SKILL.read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"))
        self.assertIn("name: serenity-invest", text)
        self.assertIn("description:", text)
        self.assertIn("Serenity Invest Skills", text)

    def test_skill_uses_cli_and_public_context(self):
        text = SKILL.read_text(encoding="utf-8")
        self.assertIn("br --base-url https://bottleneckresearch.com", text)
        self.assertIn("decision-check", text)
        self.assertIn("candidates --chain", text)
        self.assertIn("freshness", text)

    def test_research_states_are_defined(self):
        text = SKILL.read_text(encoding="utf-8")
        for state in ["upstream_anchor", "scout_candidate", "pilot_candidate", "core_candidate", "no_chase"]:
            self.assertIn(state, text)

    def test_public_docs_are_bilingual_and_research_only(self):
        en = README.read_text(encoding="utf-8")
        zh = README_ZH.read_text(encoding="utf-8")
        self.assertIn("Serenity Invest Skills", en)
        self.assertIn("Serenity Invest Skills", zh)
        self.assertIn("not investment advice", en.lower())
        self.assertIn("不是", zh)
        self.assertIn("投资建议", zh)

    def test_no_personal_data_or_private_claims(self):
        corpus = "\n".join(
            path.read_text(encoding="utf-8")
            for path in [README, README_ZH, SKILL]
        )
        forbidden = [
            "sophoninc",
            "gmail.com",
            "portfolio holding",
            "personal holdings",
            "guaranteed return",
            "收益承诺",
            "个人持仓",
        ]
        for needle in forbidden:
            self.assertNotIn(needle.lower(), corpus.lower())


if __name__ == "__main__":
    unittest.main()
