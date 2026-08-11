from pathlib import Path
import tempfile
import unittest

from tools.validate_repo import validate_repo


class RepositoryValidationTests(unittest.TestCase):
    def test_illegal_split_delivery_fails(self):
        source_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for relative in (
                "README.md",
                "AGENTS.md",
                ".gitignore",
                ".github/ISSUE_TEMPLATE/agent-task.yml",
                ".github/ISSUE_TEMPLATE/product-decision.yml",
                ".github/PULL_REQUEST_TEMPLATE.md",
                ".github/workflows/ci.yml",
                "docs/SOURCE_CATALOG.md",
                "docs/agent/CODEX_AUTOMATION.md",
                "docs/agent/REVIEW_AUTOMATION.md",
                "docs/agent/AUTOMATION_CADENCE_POLICY.md",
                "docs/agent/WORKFLOW_STATE_MACHINE.md",
                "docs/agent/RESOURCE_POLICY.md",
                "docs/question-bank/QUESTION_BANK_STANDARD.md",
                "docs/question-bank/SOURCE_TRUTH_STANDARD.md",
                "docs/question-bank/SCORING_STANDARD.md",
                "docs/question-bank/DELIVERY_STANDARD.md",
                "tools/validate_repo.py",
                "tools/validate_question_bank.py",
            ):
                target = root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                original = source_root / relative
                target.write_text(original.read_text(encoding="utf-8"), encoding="utf-8")
            (root / "doc").mkdir()
            (root / "question_banks").mkdir()
            fixture = source_root / "tests/fixtures/invalid/illegal_split_delivery/SAMPLE_GOLD.jsonl"
            (root / "question_banks/SAMPLE_GOLD.jsonl").write_text(
                fixture.read_text(encoding="utf-8"), encoding="utf-8"
            )
            errors = validate_repo(root)
        self.assertTrue(any("permits only canonical Markdown" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
