from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
import hashlib
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "question_banks/VFJVFK_R00_2023KW_C1N.md"
SOURCE = ROOT / "doc/VFJVFK_R00_2023KW_C1N.pdf"


def question_block(text: str, question_id: str) -> str:
    match = re.search(
        rf"(?ms)^## {re.escape(question_id)}\s*$\n(.*?)(?=^## VFJVFK-Q-|\Z)",
        text,
    )
    if not match:
        raise AssertionError(f"missing question block: {question_id}")
    return match.group(1)


class VfjvfkSourceTruthRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = BANK.read_text(encoding="utf-8")

    def test_source_identity_and_question_set_are_frozen(self):
        expected_hash = (
            "3e754c4b1ee0170819f5a30a6606315f71b3b9de48ae68fcc96bacd3230fd777"
        )
        self.assertIn("source_pdf: VFJVFK_R00_2023KW_C1N.pdf", self.text)
        self.assertIn(f"source_sha256: {expected_hash}", self.text)
        self.assertIn("source_pages: 50", self.text)
        self.assertEqual(hashlib.sha256(SOURCE.read_bytes()).hexdigest(), expected_hash)

        ids = re.findall(r"(?m)^## (VFJVFK-Q-\d{4})$", self.text)
        self.assertEqual(ids, [f"VFJVFK-Q-{index:04d}" for index in range(1, 21)])

    def test_question_statistics_match_frozen_types(self):
        expected = {
            "MODEL": 2,
            "FACT": 2,
            "SPEC_LOOKUP": 2,
            "TABLE": 2,
            "CALCULATION": 2,
            "PROCEDURE": 5,
            "CAUTION": 5,
        }
        actual = Counter(re.findall(r"(?m)^\*\*Type: ([A-Z_]+)\*\*$", self.text))
        self.assertEqual(actual, Counter(expected))
        self.assertNotIn("**Type: CHART**", self.text)
        self.assertIn("- Total: 20", self.text)

    def test_scoring_ids_and_totals_are_structurally_valid(self):
        for index in range(1, 21):
            question_id = f"VFJVFK-Q-{index:04d}"
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

    def test_model_grammar_and_option_boundaries_are_frozen(self):
        vfj = question_block(self.text, "VFJVFK-Q-0001")
        vfk = question_block(self.text, "VFJVFK-Q-0002")
        options = question_block(self.text, "VFJVFK-Q-0011")
        for required in (
            "`VFJ2000-080-D-H20-MR`",
            "油压定位",
            "弹簧力",
            "释放动作确认型",
        ):
            self.assertIn(required, vfj)
        for required in (
            "`VFK3000-130-C-H25-BL`",
            "油压释放",
            "着座确认型",
        ):
            self.assertIn(required, vfk)
        for required in (
            "VFK2000-060/070 正确写为不能选 B。",
            "VFK2000-060/070 正确写为不能选 M。",
            "B 与 M 组合使用正确写为需另行询问厂家。",
        ):
            self.assertIn(required, options)

    def test_action_and_installation_scoring_are_semantically_atomic(self):
        action = question_block(self.text, "VFJVFK-Q-0004")
        install = question_block(self.text, "VFJVFK-Q-0016")
        action_scoring = re.search(
            r"(?ms)^### Scoring Standard\s*$\n(.*?)(?=^### Accepted Variants)",
            action,
        ).group(1)
        for required in (
            "VFK 搬入/搬出前撤除定位油压。",
            "VFK 搬入/搬出时供给释放油压。",
            "定位时 VFJ 供给定位油压。",
            "VFK 定位前解除释放油压。",
            "VFK 定位时供给定位油压。",
            "定位时活塞杆上升。",
            "定位时钢球扩径。",
        ):
            self.assertIn(required, action)
        self.assertNotIn("撤除定位油压并供给释放油压", action_scoring)
        self.assertNotIn("活塞杆上升并使钢球扩径", action_scoring)

        for required in (
            "正确写出 2 根安装螺栓。",
            "螺纹规格正确写为 M5×0.8。",
            "螺栓强度等级正确写为 12.9。",
            "紧固扭矩正确写为 6.3 N·m。",
            "正确禁止弹簧垫圈。",
            "正确禁止带齿垫圈。",
        ):
            self.assertIn(required, install)

    def test_calculation_gold_uses_exact_rounding_without_pseudo_tolerance(self):
        horizontal = Decimal("580") * Decimal("0.25") / (
            Decimal("0.20") * Decimal("9.8")
        )
        vertical = Decimal("650") * Decimal("0.25") / Decimal("9.8")
        self.assertEqual(
            horizontal.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
            Decimal("73.98"),
        )
        self.assertEqual(
            vertical.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
            Decimal("16.58"),
        )

        horizontal_block = question_block(self.text, "VFJVFK-Q-0008")
        vertical_block = question_block(self.text, "VFJVFK-Q-0009")
        for required in ("73.979591", "73.98 kg", "ROUND_HALF_UP"):
            self.assertIn(required, horizontal_block)
        for required in ("16.581632", "16.58 kg", "ROUND_HALF_UP"):
            self.assertIn(required, vertical_block)
        self.assertNotIn("±0.01 kg", horizontal_block)
        self.assertNotIn("±0.01 kg", vertical_block)

    def test_dual_series_source_locality_and_no_chart_invention_are_frozen(self):
        common = question_block(self.text, "VFJVFK-Q-0005")
        for required in (
            "- Physical page: 7, 23",
            "- Printed page: 1365, 1381",
            "VFJ/VFK > 规格 > 共通性能与使用压力",
            "两张规格表分别列出",
        ):
            self.assertIn(required, common)
        self.assertIn(
            "本 PDF 没有对 VFJ/VFK 给出可作为连续量 Gold 的性能曲线",
            self.text,
        )

    def test_high_and_medium_coverage_rows_are_reconciled(self):
        rows = {
            match.group(1): match.group(0)
            for match in re.finditer(r"(?m)^\| (VFJVFK-SI-\d{3}) \|.*\|$", self.text)
        }
        self.assertEqual(
            sorted(rows), [f"VFJVFK-SI-{index:03d}" for index in range(1, 14)]
        )
        for row_id, row in rows.items():
            if "| HIGH：" in row or "| MEDIUM：" in row:
                self.assertIn("VFJVFK-Q-", row, row_id)

    def test_document_common_binding_and_delivery_hygiene_are_frozen(self):
        common = question_block(self.text, "VFJVFK-Q-0019")
        self.assertIn("- Binding: DOCUMENT_COMMON", common)
        self.assertIn(
            "- Model / Scope: VFJVFK_R00_2023KW_C1N.pdf :: 液压施工与回路排气",
            common,
        )
        for token in (
            "internal checkpoint",
            "next work package",
            "developer notes",
            "Playwright",
            "Selenium",
            "WP1",
            "WP2",
        ):
            self.assertNotIn(token, self.text)


if __name__ == "__main__":
    unittest.main()
