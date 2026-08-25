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
7. Follow [LOCAL_WORKSPACE_POLICY.md](docs/agent/LOCAL_WORKSPACE_POLICY.md):
   keep the primary user-visible checkout on `main`, isolate Issue branches in
   linked worktrees, and safely fast-forward the primary checkout after a
   reviewed merge when local access is available.

## Codex Developer

- Follow [CODEX_AUTOMATION.md](docs/agent/CODEX_AUTOMATION.md).
- Use staged automation bootstrap in this order:
  `LIGHTWEIGHT_TASK_DISCOVERY`, `ACTIVE_INVOCATION_GUARD`, then
  `FULL_BOOTSTRAP` only when executable or recoverable work exists.
- Stage 0 reads only latest `AGENTS.md`, latest `CODEX_AUTOMATION.md`, open
  Issues, open PRs, workflow labels, and the smallest metadata needed to map
  them. Do not load the full project rules before task discovery.
- Stage 0 workflow-state authority is the live remote GitHub state for exactly
  `wuhu0208/Will_Ai_Test`. A local checkout, local branch state, cached search,
  previous tool result, or conversation memory cannot prove that no executable
  Issue exists. Before returning `NO_EXECUTABLE_ISSUE`, the invocation must prove
  that live reads of open Issues, open PRs, and current workflow labels for that
  exact repository succeeded. A successful empty result is different from a
  failed, unavailable, stale, wrong-repository, or otherwise unproven read.
- If the live remote workflow-state read cannot be proven, fail closed instead of
  converting the failure into an empty Issue set. Output:

  ```text
  STATUS: RETRYABLE_FAILURE
  WORK_CLASS: CONTROL_PLANE
  ISSUE: UNKNOWN
  STOP_REASON: REMOTE_WORKFLOW_STATE_UNAVAILABLE
  ```

  Then stop before Stage 1/2 and do not mutate labels, branches, PRs, or product
  files. `NO_EXECUTABLE_ISSUE` is legal only after successful remote readback.
- One legal open `agent-ready` Issue is executable even when it has no PR yet;
  the PR is created only after the Developer claims the Issue and begins work.
- A scheduler trigger is a discovery opportunity, not an execution timeout or
  an instruction to restart or resume work.
- Prefer `repair-needed`, then the unique recoverable `agent-working` Issue,
  then one `agent-ready` Issue. Stop on workflow conflict.
- Continue the same Issue, branch, and PR across cycles. A healthy ACTIVE Cycle
  Lease prevents a second Developer invocation from modifying that boundary.
- Work Packages are durable checkpoint/recovery units, not mandatory invocation
  stop boundaries. After completing and checkpointing one Work Package, continue
  the next adjacent executable Work Package in the same invocation when scope,
  lease ownership, resource policy, and remaining execution budget are healthy.
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
- Source PDF identity is the delivery boundary. Keep every model and option from
  the same PDF in that PDF's single canonical Markdown; keep distinct PDFs in
  distinct canonical Markdown files even when they share a product family or
  common appendix pages.
- Intermediate JSON, JSONL, CSV, render caches, and calculation artifacts are
  build materials, not additional final business deliverables.
- Do not generate or modify a product question bank unless its Issue is
  executable under the workflow state machine.
