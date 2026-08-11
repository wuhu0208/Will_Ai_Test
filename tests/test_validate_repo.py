from pathlib import Path
import tempfile
import unittest

from tools.validate_repo import validate_repo, validate_source_catalog


class RepositoryValidationTests(unittest.TestCase):
    def test_agent_task_workflow_label_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            template = root / ".github/ISSUE_TEMPLATE/agent-task.yml"
            template.parent.mkdir(parents=True)
            template.write_text(
                'name: Agent task\nlabels: ["agent-ready"]\n', encoding="utf-8"
            )
            (root / "doc").mkdir()
            (root / "question_banks").mkdir()
            errors = validate_repo(root)
        self.assertTrue(
            any("must not auto-apply workflow labels" in error for error in errors)
        )

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

    def test_valid_looking_wrong_catalog_hash_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "doc").mkdir()
            (root / "docs").mkdir()
            (root / "doc/SAMPLE.pdf").write_bytes(b"%PDF-1.4 catalog fixture\n")
            (root / "docs/SOURCE_CATALOG.md").write_text(
                "# Source Catalog\n\n"
                "| Source PDF | SHA-256 | Pages | Product Scope | "
                "Canonical Question Bank Path | Notes |\n"
                "|---|---|---:|---|---|---|\n"
                "| `SAMPLE.pdf` | "
                "`0000000000000000000000000000000000000000000000000000000000000000` "
                "| 1 | SAMPLE | `question_banks/SAMPLE.md` | Fixture. |\n",
                encoding="utf-8",
            )
            errors = validate_source_catalog(root)
        self.assertTrue(any("SHA-256 mismatch" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
