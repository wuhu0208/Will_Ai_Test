from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
import hashlib
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "question_banks/VFLVFM_R00_2023KW_C1N.md"
SOURCE = ROOT / "doc/VFLVFM_R00_2023KW_C1N.pdf"


def question_block(text: str, question_id: str) -> str:
    match = re.search(
        rf"(?ms)^## {re.escape(question_id)}\s*$\n(.*?)(?=^## VFLVFM-Q-|\Z)",
        text,
    )
    if not match:
        raise AssertionError(f"missing question block: {question_id}")
    return match.group(1)


class VflvfmSourceTruthRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = BANK.read_text(encoding="utf-8")

    def test_source_identity_and_question_set_are_frozen(self):
        expected_hash = (
            "711dfc7c3a7573f3e4da94a0c2c4ee99ea6aefe26fdf41c1722884ab671b8e2b"
        )
        self.assertIn("source_pdf: VFLVFM_R00_2023KW_C1N.pdf", self.text)
        self.assertIn(f"source_sha256: {expected_hash}", self.text)
        self.assertIn("source_pages: 52", self.text)
        self.assertEqual(hashlib.sha256(SOURCE.read_bytes()).hexdigest(), expected_hash)

        ids = re.findall(r"(?m)^## (VFLVFM-Q-\d{4})$", self.text)
        self.assertEqual(ids, [f"VFLVFM-Q-{index:04d}" for index in range(1, 21)])

    def test_question_statistics_match_frozen_types(self):
        expected = {
            "MODEL": 2,
            "FACT": 2,
            "SPEC_LOOKUP": 2,
            "TABLE": 2,
            "CALCULATION": 2,
            "CHART": 1,
            "PROCEDURE": 4,
            "CAUTION": 5,
        }
        actual = Counter(re.findall(r"(?m)^\*\*Type: ([A-Z_]+)\*\*$", self.text))
        self.assertEqual(actual, Counter(expected))
        self.assertIn("- Total: 20", self.text)
        for question_type, count in expected.items():
            self.assertIn(f"- {question_type}: {count}", self.text)

    def test_question_scoring_ids_and_totals_are_structurally_valid(self):
        for index in range(1, 21):
            question_id = f"VFLVFM-Q-{index:04d}"
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

    def test_repaired_scoring_boundaries_are_semantically_split(self):
        mechanism = question_block(self.text, "VFLVFM-Q-0003")
        action = question_block(self.text, "VFLVFM-Q-0004")
        installation = question_block(self.text, "VFLVFM-Q-0014")
        vertical = question_block(self.text, "VFLVFM-Q-0015")
        pitch = question_block(self.text, "VFLVFM-Q-0017")
        common = question_block(self.text, "VFLVFM-Q-0020")
        action_scoring = re.search(
            r"(?ms)^### Scoring Standard\s*$\n(.*?)(?=^### Accepted Variants)",
            action,
        ).group(1)

        for required in (
            "VFL 正确写为油压释放。",
            "VFL 正确归类为油压单动型。",
            "VFM 正确写为油压释放。",
            "VFM 正确归类为油压复动型。",
        ):
            self.assertIn(required, mechanism)

        for required in (
            "VFM 释放前撤除定位油压。",
            "VFM 释放时供给释放油压。",
            "VFM 恢复定位前撤除释放油压。",
            "VFM 恢复定位时供给定位油压。",
        ):
            self.assertIn(required, action)
        self.assertNotIn("撤除释放油压并供给定位油压", action_scoring)

        for required in (
            "主体尺寸 2/3 的螺栓规格为 M5×0.8。",
            "主体尺寸 2/3 的紧固力矩为 6.3 N·m。",
            "主体尺寸 4/5 的螺栓规格为 M6。",
            "主体尺寸 4/5 的紧固力矩为 10 N·m。",
            "主体尺寸 6 的螺栓规格为 M8。",
            "主体尺寸 6 的紧固力矩为 25 N·m。",
        ):
            self.assertIn(required, installation)

        self.assertIn("垂直使用时定期确认定位精度。", vertical)
        self.assertIn("定位精度超出容许范围时立即更换定位销。", vertical)
        self.assertIn("最终 Gold 明确为 ±0.08 mm。", pitch)
        self.assertIn("回代核对为 `0.02+0.08=0.10 mm`。", pitch)

        for required in (
            "后续维护应检查配管是否松动。",
            "后续维护应检查安装螺栓等紧固件是否松动。",
            "后续维护应检查液压油是否老化。",
            "发现异常后必须处理完成再继续使用。",
        ):
            self.assertIn(required, common)

    def test_exact_rounding_and_dual_series_source_locality_are_frozen(self):
        weight = question_block(self.text, "VFLVFM-Q-0008")
        common_specs = question_block(self.text, "VFLVFM-Q-0005")

        self.assertIn("使用 `ROUND_HALF_UP` 精确舍入到 1 位小数", weight)
        self.assertIn("不另设正负容差", weight)
        self.assertNotIn("±0.1 kg", weight)

        for required in (
            "- Physical page: 9 and 25",
            "- Printed page: 1333-1334 and 1347-1348",
            "VFL > 规格 > 共通使用条件",
            "VFM > 规格 > 共通使用条件",
            "物理页 9 的 VFL2000～VFL6000 规格表",
            "物理页 25 的 VFM2000～VFM6000 规格表",
        ):
            self.assertIn(required, common_specs)

    def test_calculation_gold_is_deterministic(self):
        force = Decimal("700")
        efficiency = Decimal("0.5")
        gravity = Decimal("9.8")
        friction = Decimal("0.2")
        horizontal = force * efficiency / (friction * gravity)
        vertical = force * efficiency / gravity

        self.assertEqual(
            horizontal.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP),
            Decimal("178.6"),
        )
        self.assertEqual(
            vertical.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP),
            Decimal("35.7"),
        )

        weight = question_block(self.text, "VFLVFM-Q-0008")
        pitch = question_block(self.text, "VFLVFM-Q-0017")
        for required in ("178.571... kg", "178.6 kg", "35.714... kg", "35.7 kg"):
            self.assertIn(required, weight)
        for required in ("0.10 − 0.02 = 0.08 mm", "±0.08 mm", "0.02 + 0.08 = 0.10 mm"):
            self.assertIn(required, pitch)

    def test_chart_gold_keeps_visual_evidence_and_tolerance(self):
        chart = question_block(self.text, "VFLVFM-Q-0009")
        self.assertIn("**Type: CHART**", chart)
        self.assertIn("- Evidence type: CHART", chart)
        for required in (
            "视觉读取",
            "`VFM6000-300`",
            "8000 N",
            "约为 **0.014 mm**",
            "接受范围 0.012～0.016 mm",
        ):
            self.assertIn(required, chart)

    def test_model_grammar_and_product_boundaries_are_frozen(self):
        vfl = question_block(self.text, "VFLVFM-Q-0001")
        vfm = question_block(self.text, "VFLVFM-Q-0002")
        for required in ("`VFL2000-080-D-H20-MR`", "弹簧定位", "释放动作确认型"):
            self.assertIn(required, vfl)
        for required in ("`VFM6000-300-C-H30-BL`", "油压定位", "着座确认型"):
            self.assertIn(required, vfm)

        common = question_block(self.text, "VFLVFM-Q-0020")
        self.assertIn("- Binding: DOCUMENT_COMMON", common)
        self.assertIn(
            "- Model / Scope: VFLVFM_R00_2023KW_C1N.pdf :: 液压安装施工、操作和维护",
            common,
        )

    def test_high_and_medium_coverage_rows_are_reconciled(self):
        rows = {
            match.group(1): match.group(0)
            for match in re.finditer(r"(?m)^\| (VFLVFM-SI-\d{3}) \|.*\|$", self.text)
        }
        self.assertEqual(
            sorted(rows), [f"VFLVFM-SI-{index:03d}" for index in range(1, 16)]
        )
        for row_id, row in rows.items():
            if "| HIGH：" in row or "| MEDIUM：" in row:
                self.assertIn("VFLVFM-Q-", row, row_id)

    def test_delivery_has_no_construction_or_execution_artifacts(self):
        forbidden = (
            "internal checkpoint",
            "next work package",
            "developer notes",
            "Playwright",
            "Selenium",
            "Timeout",
            "Retry",
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
