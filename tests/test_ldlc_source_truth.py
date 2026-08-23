from decimal import Decimal, ROUND_HALF_UP
import hashlib
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "question_banks/LDLC_R00_2026KW_C1N.md"
SOURCE = ROOT / "doc/LDLC_R00_2026KW_C1N.pdf"


def question_block(text: str, question_id: str) -> str:
    match = re.search(
        rf"(?ms)^## {re.escape(question_id)}\s*$\n(.*?)(?=^## LDLC-Q-|\Z)",
        text,
    )
    if not match:
        raise AssertionError(f"missing question block: {question_id}")
    return match.group(1)


class LdlcSourceTruthRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = BANK.read_text(encoding="utf-8")

    def test_source_identity_and_question_set_are_frozen(self):
        expected_hash = (
            "12fba84b296d827658e4ae67377be48bacfa1519748a23e81217a613111b5b02"
        )
        self.assertIn("source_pdf: LDLC_R00_2026KW_C1N.pdf", self.text)
        self.assertIn(f"source_sha256: {expected_hash}", self.text)
        self.assertIn("source_pages: 100", self.text)
        self.assertEqual(hashlib.sha256(SOURCE.read_bytes()).hexdigest(), expected_hash)

        ids = re.findall(r"(?m)^## (LDLC-Q-\d{4})$", self.text)
        expected_ids = [f"LDLC-Q-{index:04d}" for index in range(1, 25)]
        self.assertEqual(ids, expected_ids)

    def test_business_question_answer_and_scoring_blocks_are_chinese(self):
        for heading in ("Question", "Standard Answer", "Scoring Standard"):
            blocks = re.findall(
                rf"(?ms)^### {heading}\s*$\n(.*?)(?=^### |^## LDLC-Q-|\Z)",
                self.text,
            )
            self.assertEqual(len(blocks), 24)
            self.assertTrue(all(re.search(r"[\u3400-\u9fff]", block) for block in blocks))

    def test_question_scoring_is_atomic_and_totals_100(self):
        for index in range(1, 25):
            block = question_block(self.text, f"LDLC-Q-{index:04d}")
            scoring = re.search(
                r"(?ms)^### Scoring Standard\s*$\n(.*?)(?=^### Accepted Variants)",
                block,
            )
            self.assertIsNotNone(scoring)
            points = re.findall(r"(?m)^- P(\d+) \[(\d+)]\s*:\s*(\S.*)$", scoring.group(1))
            self.assertTrue(points)
            self.assertEqual(
                [int(point_id) for point_id, _, _ in points],
                list(range(1, len(points) + 1)),
            )
            self.assertEqual(sum(int(weight) for _, weight, _ in points), 100)

    def test_calculation_gold_is_deterministic(self):
        support_force = (Decimal("3.2") * Decimal("1.5")).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        bolt_mass = (
            Decimal("4.7") * Decimal("0.30") / Decimal("9.807")
        ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        self.assertEqual(support_force, Decimal("4.80"))
        self.assertEqual(bolt_mass, Decimal("0.14"))

        support = question_block(self.text, "LDLC-Q-0012")
        bolt = question_block(self.text, "LDLC-Q-0013")
        self.assertIn("3.2 kN x 1.5 = 4.80 kN", support)
        self.assertIn("4.7 N x 0.30 / 9.807 m/s2 = 0.143774... kg", bolt)
        self.assertIn("`ROUND_HALF_UP`", bolt)
        self.assertIn("`0.14 kg`", bolt)

    def test_chart_gold_keeps_visual_evidence_and_tolerances(self):
        ld_chart = question_block(self.text, "LDLC-Q-0014")
        lc_chart = question_block(self.text, "LDLC-Q-0015")
        for block in (ld_chart, lc_chart):
            self.assertIn("- Evidence type: CHART", block)
            self.assertIn("视觉读取", block)
        self.assertIn("- Physical page: 9", ld_chart)
        self.assertIn("6-8 um", ld_chart)
        self.assertIn("`7 um ±1 um`", ld_chart)
        self.assertIn("- Physical page: 37", lc_chart)
        self.assertIn("13-17 um", lc_chart)
        self.assertIn("`15 um ±2 um`", lc_chart)

    def test_document_common_bindings_are_page_bounded(self):
        blocks = [
            question_block(self.text, question_id)
            for question_id in re.findall(r"(?m)^## (LDLC-Q-\d{4})$", self.text)
        ]
        common = [block for block in blocks if "- Binding: DOCUMENT_COMMON" in block]
        self.assertEqual(len(common), 4)
        for block in common:
            self.assertRegex(
                block,
                r"- Model / Scope: LDLC_R00_2026KW_C1N\.pdf :: 物理页 \d+ ",
            )

    def test_corrected_source_locations_remain_bound(self):
        expected = {
            "LDLC-Q-0004": ("5-6", "963-964"),
            "LDLC-Q-0005": ("31-32", "989-990"),
            "LDLC-Q-0007": ("8", "966"),
            "LDLC-Q-0008": ("36", "994"),
        }
        for question_id, (physical, printed) in expected.items():
            block = question_block(self.text, question_id)
            self.assertIn(f"- Physical page: {physical}", block)
            self.assertIn(f"- Printed page: {printed}", block)

    def test_bzs_port_direction_and_adjustment_risk_are_frozen(self):
        block = question_block(self.text, "LDLC-Q-0024")
        for required in (
            "P1 油口必须接油压供给侧",
            "P2 油口必须接夹紧器侧",
            "K 值至 C 值范围内调整",
            "到达 `max.C` 位置后不得继续旋松",
            "调压螺钉和内部弹簧可能脱落",
            "- Physical page: 81",
            "- Evidence type: DRAWING + TEXT",
        ):
            self.assertIn(required, block)

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
