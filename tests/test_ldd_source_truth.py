from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "question_banks/LDD_R01_2023KW_C1N.md"


def question_block(text: str, question_id: str) -> str:
    match = re.search(
        rf"(?ms)^## {re.escape(question_id)}\s*$\n(.*?)(?=^## LDD-Q-|\Z)",
        text,
    )
    if not match:
        raise AssertionError(f"missing question block: {question_id}")
    return match.group(1)


class LddSourceTruthRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = BANK.read_text(encoding="utf-8")

    def test_source_identity_and_question_set_are_frozen(self):
        self.assertIn("source_pdf: LDD_R01_2023KW_C1N.pdf", self.text)
        self.assertIn(
            "source_sha256: a3a4a51f350d73b263e50739578582b69fa9f4f42a69163fb9a8b07aa40f732e",
            self.text,
        )
        self.assertIn("source_pages: 36", self.text)
        ids = re.findall(r"(?m)^## (LDD-Q-\d{4})$", self.text)
        self.assertEqual(len(ids), 125)
        self.assertEqual(len(ids), len(set(ids)))

    def test_business_question_answer_and_scoring_blocks_are_chinese(self):
        for heading in ("Question", "Standard Answer", "Scoring Standard"):
            blocks = re.findall(
                rf"(?ms)^### {heading}\s*$\n(.*?)(?=^### |^## LDD-Q-|\Z)",
                self.text,
            )
            self.assertEqual(len(blocks), 125)
            self.assertTrue(all(re.search(r"[\u3400-\u9fff]", block) for block in blocks))

    def test_forward_calculation_keeps_formula_input_unit_and_rounding(self):
        block = question_block(self.text, "LDD-Q-0040")
        self.assertIn("F=0.70×P-0.91", block)
        self.assertIn("P=5.0", block)
        self.assertIn("2.59kN", block)
        self.assertIn("ROUND_HALF_UP", block)
        self.assertIn("保留 2 位小数", block)

    def test_inverse_calculation_keeps_back_substitution(self):
        block = question_block(self.text, "LDD-Q-0042")
        self.assertIn("需要5.00MPa", block)
        self.assertIn("回代1.75×5.00-2.28=6.47kN", block)
        self.assertIn("P=(F+2.28)/1.75", block)

    def test_chart_gold_keeps_visual_evidence_and_tolerances(self):
        support = question_block(self.text, "LDD-Q-0046")
        displacement = question_block(self.text, "LDD-Q-0047")
        contact = question_block(self.text, "LDD-Q-0048")
        comparison = question_block(self.text, "LDD-Q-0049")
        self.assertIn("- Evidence type: CHART", support)
        self.assertIn("约3.8kN", support)
        self.assertIn("±0.25 kN", support)
        self.assertIn("±2 μm", displacement)
        self.assertIn("±2 N", contact)
        self.assertIn("LDD-Q行程加长型的变位程度更大", comparison)

    def test_model_grammar_keeps_legal_and_illegal_order(self):
        self.assertIn("`LDD0303-M-Q`", self.text)
        self.assertIn("`M-Q`，不得写为 `Q-M`", self.text)
        block = question_block(self.text, "LDD-Q-0023")
        self.assertIn("答案为：M-Q。", block)

    def test_delivery_has_no_construction_artifacts(self):
        forbidden = (
            "artifacts/",
            "runs/",
            "checkpoint",
            "next work package",
            "developer notes",
            "Playwright",
            "Selenium",
        )
        for token in forbidden:
            self.assertNotIn(token, self.text)


if __name__ == "__main__":
    unittest.main()
