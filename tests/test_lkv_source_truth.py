from decimal import Decimal, ROUND_HALF_UP
import hashlib
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "question_banks/LKV_R01_2023KW_C1N.md"
SOURCE = ROOT / "doc/LKV_R01_2023KW_C1N.pdf"


def question_block(text: str, question_id: str) -> str:
    match = re.search(
        rf"(?ms)^## {re.escape(question_id)}\s*$\n(.*?)(?=^## LKV-Q-|\Z)",
        text,
    )
    if not match:
        raise AssertionError(f"missing question block: {question_id}")
    return match.group(1)


class LkvSourceTruthRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = BANK.read_text(encoding="utf-8")

    def test_source_identity_and_question_set_are_frozen(self):
        expected_hash = (
            "d6f28ce00837cefa6af489b9f08a92eaf4e4edb2a9bd47a6ad1e2e72fcd061b5"
        )
        self.assertIn("source_pdf: LKV_R01_2023KW_C1N.pdf", self.text)
        self.assertIn(f"source_sha256: {expected_hash}", self.text)
        self.assertIn("source_pages: 52", self.text)
        self.assertEqual(hashlib.sha256(SOURCE.read_bytes()).hexdigest(), expected_hash)

        ids = re.findall(r"(?m)^## (LKV-Q-\d{4})$", self.text)
        expected_ids = [f"LKV-Q-{index:04d}" for index in range(1, 24)]
        self.assertEqual(ids, expected_ids)

    def test_business_question_answer_and_scoring_blocks_are_chinese(self):
        for heading in ("Question", "Standard Answer", "Scoring Standard"):
            blocks = re.findall(
                rf"(?ms)^### {heading}\s*$\n(.*?)(?=^### |^## LKV-Q-|\Z)",
                self.text,
            )
            self.assertEqual(len(blocks), 23)
            self.assertTrue(all(re.search(r"[\u3400-\u9fff]", block) for block in blocks))

    def test_question_scoring_is_atomic_and_totals_100(self):
        for index in range(1, 24):
            question_id = f"LKV-Q-{index:04d}"
            block = question_block(self.text, question_id)
            scoring = re.search(
                r"(?ms)^### Scoring Standard\s*$\n(.*?)(?=^### Accepted Variants)",
                block,
            )
            self.assertIsNotNone(scoring, question_id)
            points = re.findall(
                r"(?m)^- P(\d+) \[(\d+)]\s*:\s*(\S.*)$", scoring.group(1)
            )
            self.assertTrue(points, question_id)
            self.assertEqual(
                [int(point_id) for point_id, _, _ in points],
                list(range(1, len(points) + 1)),
                question_id,
            )
            self.assertEqual(
                sum(int(weight) for _, weight, _ in points), 100, question_id
            )

    def test_calculation_gold_is_deterministic(self):
        force = Decimal("16.70") * Decimal("4.0") / (
            Decimal("70") - Decimal("21")
        )
        rounded = force.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
        back_substitution = force * Decimal("49") / Decimal("16.70")

        self.assertEqual(rounded, Decimal("1.4"))
        self.assertLessEqual(abs(back_substitution - Decimal("4.0")), Decimal("1e-24"))

        block = question_block(self.text, "LKV-Q-0009")
        for required in (
            "F=(16.70×4.0)/(70-21)",
            "1.363265306122448979591836735 kN",
            "ROUND_HALF_UP",
            "1.4 kN",
            "反代",
        ):
            self.assertIn(required, block)

    def test_chart_gold_keeps_visual_evidence_and_tolerances(self):
        force = question_block(self.text, "LKV-Q-0010")
        eccentricity = question_block(self.text, "LKV-Q-0017")

        for block in (force, eccentricity):
            self.assertIn("**Type: CHART**", block)
            self.assertIn("曲线约读值", block)
            self.assertIn("CHART tolerance", block)

        self.assertIn("- Evidence type: CHART", force)
        self.assertIn("`0.8-1.0 kN`", force)
        self.assertIn("页面视觉读取", force)
        self.assertIn("LKV0480 标准型约 `14 mm`", eccentricity)
        self.assertIn("LKV0480-H 约 `55 mm`", eccentricity)
        self.assertIn("标准型接受 `12-15 mm`", eccentricity)
        self.assertIn("H 型接受 `52-58 mm`", eccentricity)

    def test_model_grammar_keeps_order_and_combination_boundary(self):
        block = question_block(self.text, "LKV-Q-0001")
        for required in (
            "LKV<主体尺寸>0-C<压板方向>E[-<选配件>]",
            "LKV0550-CLE-H",
            "固定字母 `E`",
            "声称任意主体尺寸、压板方向和选配件组合均已被资料批准",
        ):
            self.assertIn(required, self.text if required.startswith("LKV<") else block)

    def test_document_common_bindings_are_page_bounded(self):
        expected = {
            "LKV-Q-0012": ("27", "1725"),
            "LKV-Q-0020": ("28", "1726"),
            "LKV-Q-0021": ("29", "1727"),
        }
        for question_id, (physical, printed) in expected.items():
            block = question_block(self.text, question_id)
            self.assertIn("- Binding: DOCUMENT_COMMON", block)
            self.assertIn(
                "- Model / Scope: LKV_R01_2023KW_C1N.pdf :: ", block
            )
            self.assertIn(f"- Physical page: {physical}", block)
            self.assertIn(f"- Printed page: {printed}", block)

    def test_high_and_medium_coverage_rows_are_reconciled(self):
        rows = [
            line
            for line in self.text.splitlines()
            if line.startswith("| LKV-SI-") and ("| HIGH |" in line or "| MEDIUM |" in line)
        ]
        self.assertEqual(len(rows), 18)
        for row in rows:
            self.assertRegex(row, r"LKV-Q-\d{4}")

    def test_state_and_accessory_boundaries_are_frozen(self):
        state = question_block(self.text, "LKV-Q-0016")
        bzl = question_block(self.text, "LKV-Q-0022")
        sensor = question_block(self.text, "LKV-Q-0023")

        self.assertIn("两路空气传感器输出均为 OFF", state)
        self.assertIn("使用过的 BZL 不得再用于其他夹紧器", bzl)
        normalized_sensor = re.sub(r"\s+", "", sensor)
        self.assertIn(
            "清洁A端口后部检测回路时，LKV必须处于释放状态",
            normalized_sensor,
        )

    def test_delivery_has_no_construction_artifacts(self):
        forbidden = (
            "artifacts/",
            "runs/",
            "checkpoint",
            "next work package",
            "developer notes",
            "Playwright",
            "Selenium",
            "WP1",
            "WP2",
            "WP3",
            "WP4",
            "WP5",
        )
        for token in forbidden:
            self.assertNotIn(token, self.text)


if __name__ == "__main__":
    unittest.main()
