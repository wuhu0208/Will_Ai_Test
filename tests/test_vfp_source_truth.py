from decimal import Decimal, ROUND_HALF_UP
from difflib import SequenceMatcher
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

    def test_question_ids_and_scoring_are_atomic_and_complete(self):
        blocks = re.findall(
            r"^## (VFP-Q-(\d{4}))\n(.*?)(?=^## VFP-Q-|\Z)",
            self.text,
            flags=re.MULTILINE | re.DOTALL,
        )
        self.assertEqual([int(number) for _, number, _ in blocks], list(range(1, 14)))

        for question_id, _, block in blocks:
            points = re.findall(r"^- P(\d+) \[(\d+)\]:", block, flags=re.MULTILINE)
            self.assertTrue(points, question_id)
            self.assertEqual(
                [int(point_id) for point_id, _ in points],
                list(range(1, len(points) + 1)),
                question_id,
            )
            self.assertEqual(sum(int(weight) for _, weight in points), 100, question_id)

    def test_high_and_medium_inventory_rows_have_final_dispositions(self):
        rows = [
            [cell.strip() for cell in line.strip().strip("|").split("|")]
            for line in self.text.splitlines()
            if line.startswith("| VFP-SI-")
        ]
        self.assertEqual(len(rows), 16)

        for inventory_id, _, _, _, priority, _, disposition in rows:
            if priority in {"HIGH", "MEDIUM"}:
                self.assertTrue(
                    "VFP-Q-" in disposition
                    or "排除" in disposition
                    or "不单独设题" in disposition,
                    inventory_id,
                )

    def test_document_common_questions_are_page_bounded(self):
        expected = {
            "VFP-Q-0011": ("1725-1726", "25-26"),
            "VFP-Q-0012": ("1727-1728", "27-28"),
            "VFP-Q-0013": ("1729-1730", "29-30"),
        }
        for question_id, (printed_pages, physical_pages) in expected.items():
            block = question_block(self.text, question_id)
            self.assertIn("- Binding: DOCUMENT_COMMON", block)
            self.assertIn(
                "- Model / Scope: VFP_R03_2023KW_C1N.pdf :: 印刷页 ", block
            )
            self.assertIn(f"Printed page: {printed_pages}", block)
            self.assertIn(f"Physical page: {physical_pages}", block)

    def test_questions_do_not_repeat_the_same_semantic_prompt(self):
        questions = re.findall(
            r"^## (VFP-Q-\d{4}).*?^### Question\n\n(.*?)\n\n### Standard Answer",
            self.text,
            flags=re.MULTILINE | re.DOTALL,
        )
        normalized = {
            question_id: re.sub(r"[^\w]", "", question)
            for question_id, question in questions
        }
        self.assertEqual(len(normalized), 13)

        for left_id, left in normalized.items():
            for right_id, right in normalized.items():
                if left_id >= right_id:
                    continue
                similarity = SequenceMatcher(None, left, right).ratio()
                self.assertLess(similarity, 0.65, f"{left_id}/{right_id}: {similarity}")


if __name__ == "__main__":
    unittest.main()
