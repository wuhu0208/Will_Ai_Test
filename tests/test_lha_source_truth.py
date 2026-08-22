from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "question_banks/LHA_R00_2023KW_C1N.md"


def question_block(text: str, question_id: str) -> str:
    match = re.search(
        rf"(?ms)^## {re.escape(question_id)}\s*$\n(.*?)(?=^## LHA-Q-|\Z)",
        text,
    )
    if not match:
        raise AssertionError(f"missing question block: {question_id}")
    return match.group(1)


class LhaSourceTruthRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = BANK.read_text(encoding="utf-8")

    def test_source_identity_and_representative_set_are_frozen(self):
        self.assertIn("source_pdf: LHA_R00_2023KW_C1N.pdf", self.text)
        self.assertIn(
            "source_sha256: 662f538ada8c6b218e89e59b519079738cde290a3e1c1657116ef3618113947f",
            self.text,
        )
        self.assertIn("source_pages: 68", self.text)
        ids = re.findall(r"(?m)^## (LHA-Q-\d{4})$", self.text)
        self.assertEqual(len(ids), 127)
        self.assertEqual(len(ids), len(set(ids)))

    def test_business_question_answer_and_scoring_blocks_are_chinese(self):
        for heading in ("Question", "Standard Answer", "Scoring Standard"):
            blocks = re.findall(
                rf"(?ms)^### {heading}\s*$\n(.*?)(?=^### |^## LHA-Q-|\Z)",
                self.text,
            )
            self.assertEqual(len(blocks), 127)
            self.assertTrue(all(re.search(r"[\u3400-\u9fff]", block) for block in blocks))

    def test_model_grammar_keeps_order_and_combination_boundary(self):
        self.assertIn("`LHA0480-CL`", self.text)
        self.assertIn("`LHA0550-CR-P`", self.text)
        self.assertIn("不得写成 `LHA0550-C-R-P`", self.text)
        block = question_block(self.text, "LHA-Q-0028")
        self.assertIn("不能", block)
        self.assertIn("另行垂询确认", block)

    def test_calculation_gold_keeps_formula_rounding_and_back_substitution(self):
        forward = question_block(self.text, "LHA-Q-0203")
        inverse = question_block(self.text, "LHA-Q-0206")
        self.assertIn("F=P×(1-0.0011×L)/(1.0039+0.0011×L)", forward)
        self.assertIn("3.288 kN", forward)
        self.assertIn("ROUND_HALF_UP", forward)
        self.assertIn("所需压力=6.900 MPa", inverse)
        self.assertIn("可行性结论为可行", inverse)
        self.assertIn("ROUND_HALF_UP", inverse)

    def test_chart_gold_keeps_visual_evidence_and_tolerance(self):
        for question_id in ("LHA-Q-0199", "LHA-Q-0200", "LHA-Q-0201"):
            block = question_block(self.text, question_id)
            self.assertIn("- Evidence type: CHART", block)
            self.assertIn("图表读数允许误差", block)

    def test_scope_excludes_nontechnical_contact_questions(self):
        self.assertNotIn("LHA-Q-0068", self.text)
        self.assertNotIn("LHA-Q-0069", self.text)
        self.assertIn("公司地址、销售网点等非技术联系信息不收录", self.text)

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
