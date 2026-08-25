from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ProjectInvariantTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        cls.delivery = (
            ROOT / "docs/question-bank/DELIVERY_STANDARD.md"
        ).read_text(encoding="utf-8")
        cls.local_workspace = (
            ROOT / "docs/agent/LOCAL_WORKSPACE_POLICY.md"
        ).read_text(encoding="utf-8")
        cls.review = (
            ROOT / "docs/agent/REVIEW_AUTOMATION.md"
        ).read_text(encoding="utf-8")
        cls.delivery_words = " ".join(cls.delivery.split())
        cls.local_workspace_words = " ".join(cls.local_workspace.split())

    def test_pdf_identity_is_the_frozen_delivery_boundary(self):
        for token in (
            "identity of the source PDF",
            "If one PDF contains multiple models",
            "Never split one PDF by model",
            "never merge distinct PDFs",
        ):
            self.assertIn(token, self.delivery_words)

        for token in (
            "all models and options contained in that PDF stay together",
            "distinct PDFs stay distinct",
            "conversations never split or merge canonical business deliverables",
        ):
            self.assertIn(token, self.local_workspace_words)

    def test_primary_checkout_and_issue_worktrees_have_distinct_roles(self):
        for token in (
            "primary user-visible repository checkout on local `main`",
            "linked worktree for every Issue branch",
            "git worktree list",
            "Never copy an unmerged canonical deliverable",
        ):
            self.assertIn(token, self.local_workspace_words)

    def test_post_merge_sync_is_fast_forward_and_non_destructive(self):
        for token in (
            "fetch current `origin/main`",
            "git merge --ff-only origin/main",
            "never delete, clean, overwrite, auto-stash, or force-reset",
            "LOCAL_MAIN_SYNC_PENDING",
        ):
            self.assertIn(token, self.local_workspace_words)

        self.assertIn(
            "LOCAL_WORKSPACE_POLICY.md", self.agents
        )
        self.assertIn(
            "post-merge local synchronization procedure", self.review
        )


if __name__ == "__main__":
    unittest.main()
