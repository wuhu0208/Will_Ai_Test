# Agent Rules

These rules apply to every Agent working in this repository. The latest files
on `main` are authoritative.

## Shared controls

1. Work only from a formal Issue and preserve its scope, authoritative inputs,
   non-goals, acceptance criteria, and resource constraints.
2. Keep `main` as the accepted baseline. Use the Issue branch and pull request.
3. Reuse verified artifacts and caches when their input hashes still match.
4. Record deterministic evidence for claims; do not treat reports as runtime proof.
5. Stop on `blocked` or `product-decision`. Do not invent source truth or change
   product scope, delivery format, or scoring principles without user approval.
6. Never expose credentials, cookies, tokens, session storage, or `.env` data.

## Codex Developer

- Follow [CODEX_AUTOMATION.md](docs/agent/CODEX_AUTOMATION.md).
- Use staged automation bootstrap in this order:
  `LIGHTWEIGHT_TASK_DISCOVERY`, `ACTIVE_INVOCATION_GUARD`, then
  `FULL_BOOTSTRAP` only when executable or recoverable work exists.
- Stage 0 reads only latest `AGENTS.md`, latest `CODEX_AUTOMATION.md`, open
  Issues, open PRs, workflow labels, and the smallest metadata needed to map
  them. Do not load the full project rules before task discovery.
- A scheduler trigger is a discovery opportunity, not an execution timeout or
  an instruction to restart or resume work.
- Prefer `repair-needed`, then the unique recoverable `agent-working` Issue,
  then one `agent-ready` Issue. Stop on workflow conflict.
- Continue the same Issue, branch, and PR across cycles. A healthy ACTIVE Cycle
  Lease prevents a second Developer invocation from modifying that boundary.
- Run relevant tests and update the PR checkpoint only after meaningful work or
  state change. `NO_ACTION` and `ACTIVE_INVOCATION_SKIP` do not create a full
  checkpoint.
- Do not approve, independently review, merge, or start the next Issue.

## Independent Review Agent

- Follow [REVIEW_AUTOMATION.md](docs/agent/REVIEW_AUTOMATION.md).
- Review a `waiting-review` PR against its Issue, diff, CI, source PDF, canonical
  Markdown, validators, and repository rules.
- Treat a collision invocation ending in `ACTIVE_INVOCATION_SKIP` as healthy
  overlap prevention when the principal Developer Cycle Lease remains ACTIVE.
- Return `PASS`, `PARTIAL_PASS`, `FAIL`, `BLOCKED`, or `PRODUCT_DECISION` with evidence.
- A failing review returns work to the same branch and PR.

## Question-bank delivery

- Follow all files under `docs/question-bank/` after Stage 2 determines they are
  applicable to the selected work.
- One source PDF maps to one canonical Markdown file with the identical stem.
- Intermediate JSON, JSONL, CSV, render caches, and calculation artifacts are
  build materials, not additional final business deliverables.
- Do not generate or modify a product question bank unless its Issue is
  executable under the workflow state machine.
