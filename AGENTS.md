# Agent Rules

These rules apply to every Agent working in this repository. The latest files
on `main` are authoritative.

## Shared controls

1. Read the Issue, this file, the role-specific rules, and applicable
   `docs/question-bank/` standards before changing anything.
2. Work only from a formal Issue and preserve its scope, authoritative inputs,
   non-goals, acceptance criteria, and resource constraints.
3. Keep `main` as the accepted baseline. Use the Issue branch and pull request.
4. Reuse verified artifacts and caches when their input hashes still match.
5. Record deterministic evidence for claims; do not treat reports as runtime proof.
6. Stop on `blocked` or `product-decision`. Do not invent source truth or change
   product scope, delivery format, or scoring principles without user approval.
7. Never expose credentials, cookies, tokens, session storage, or `.env` data.

## Codex Developer

- Follow [CODEX_AUTOMATION.md](docs/agent/CODEX_AUTOMATION.md).
- Prefer `repair-needed`; otherwise claim one `agent-ready` Issue.
- Continue the same Issue, branch, and PR across cycles.
- Run relevant tests and update the PR checkpoint before stopping.
- Do not approve, independently review, merge, or start the next Issue.

## Independent Review Agent

- Follow [REVIEW_AUTOMATION.md](docs/agent/REVIEW_AUTOMATION.md).
- Review a `waiting-review` PR against its Issue, diff, CI, source PDF, canonical
  Markdown, validators, and repository rules.
- Return `PASS`, `PARTIAL_PASS`, `FAIL`, `BLOCKED`, or `PRODUCT_DECISION` with evidence.
- A failing review returns work to the same branch and PR.

## Question-bank delivery

- Follow all files under `docs/question-bank/`.
- One source PDF maps to one canonical Markdown file with the identical stem.
- Intermediate JSON, JSONL, CSV, render caches, and calculation artifacts are
  build materials, not additional final business deliverables.
- Do not generate or modify a product question bank unless its Issue is
  executable under the workflow state machine.
