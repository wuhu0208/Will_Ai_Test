# Codex Developer Automation

## Cycle entry

1. Read `AGENTS.md`, this file, `AUTOMATION_CADENCE_POLICY.md`, all applicable
   `docs/question-bank/` standards, and `docs/SOURCE_CATALOG.md` from latest `main`.
2. Query open Issues and open pull requests.
3. Prefer an Issue labeled `repair-needed` with an existing open PR. Continue
   that same branch and PR.
4. Otherwise select one `agent-ready` Issue. If none exists, output `NO_ACTION`
   and stop.
5. Verify there is not another principal `agent-working` product task. If there
   is a state conflict, apply `blocked`, report the evidence, and stop.

## Work cycle

1. Replace `agent-ready` with `agent-working` when claiming new work.
2. Create or resume the Issue branch and its single PR.
3. Execute only the next incomplete Work Package and preserve completed work.
4. Reuse valid artifacts and input-hash caches.
5. Run the necessary deterministic validations and focused tests.
6. Commit and push meaningful progress.
7. Create or update the same PR with tests, evidence, and Cycle Checkpoint.
8. If the Issue remains incomplete, leave a resumable checkpoint and stop.
9. If all acceptance criteria are met, remove `agent-working`, apply
   `waiting-review`, provide the Review Handoff, and stop.

## Cycle Checkpoint

Record: completed Work Packages, changed files, commands and results, input and
artifact hashes when relevant, unresolved risks, exact next action, and whether
all acceptance criteria are satisfied.

## Hard stops

- Do not self-review, approve, merge, close as accepted, or activate the next Issue.
- Do not create a new Issue or PR merely because a review failed.
- Do not start work labeled `blocked` or `product-decision`.
- Do not change source scope, delivery format, or core scoring rules without a
  user decision.
