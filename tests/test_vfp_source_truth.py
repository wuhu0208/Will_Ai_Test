from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "question_banks/VFP_R03_2023KW_C1N.md"


def question_block(text: str, question_id: str) -> str:
    match = re.search(
        rf"^## {re.escape(question_id)}\n(.*?)(?=^## VFP-Q-|\Z)",
        text,
        flags=re.MULTILINE | re.DOTALL,
    )
    return match.group(1) if match else ""


class VfpSourceTruthRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = BANK.read_text(encoding="utf-8")

    def test_workpiece_weight_gold_uses_decimal_and_final_rounding(self):
        force_n = Decimal("3600")
        efficiency = Decimal("0.25")
        gravity = Decimal("9.8")
        friction = Decimal("0.20")
        quantum = Decimal("0.1")

        horizontal = force_n * efficiency / (friction * gravity)
        vertical = force_n * efficiency / gravity

        self.assertEqual(
            horizontal.quantize(quantum, rounding=ROUND_HALF_UP),
            Decimal("459.2"),
        )
        self.assertEqual(
            vertical.quantize(quantum, rounding=ROUND_HALF_UP),
            Decimal("91.8"),
        )

        block = question_block(self.text, "VFP-Q-0006")
        for required in ("459.183673", "459.2 kg", "91.836734", "91.8 kg"):
            self.assertIn(required, block)

    def test_air_sensor_chart_gold_is_visual_and_state_bound(self):
        block = question_block(self.text, "VFP-Q-0007")
        for required in (
            "**Type: CHART**",
            "Physical page: 5-6",
            "Evidence type: CHART + STATE_DIAGRAM + TEXT",
            "真实视觉读取",
            "释放完成时空气传感器为 ON",
            "定位状态下空气传感器为 OFF",
            "不要求从图中插值",
        ):
            self.assertIn(required, block)

    def test_vfp_model_grammar_keeps_legal_and_illegal_examples(self):
        for required in (
            "VFP0300-D",
            "VFP0600-C",
            "VFP0600-D-M",
            "VFP1200-C-M",
            "VFP0350-D",
            "VFP0601-D",
            "VFP0600-M-D",
            "VFP0600-DC",
        ):
            self.assertIn(required, self.text)


if __name__ == "__main__":
    unittest.main()
