# Independent Review Automation

## Lifecycle reconciliation preflight

Before concluding that no review exists, reconcile only a unique, evidence-backed
Issue/PR workflow split-brain state.

A safe reconciliation candidate exists only when all are true:

- exactly one open Issue/PR pair can be mapped uniquely;
- one side is labeled `waiting-review` and the other side is missing that label;
- neither side has `repair-needed`, `blocked`, `product-decision`, or another
  incompatible principal workflow label;
- the PR has one unique `<!-- CODEX_CYCLE_STATE_V1 -->` comment in `TERMINAL`
  state for that exact Issue/PR/branch;
- the terminal Cycle State points to a complete Review Handoff;
- the Review Handoff identifies the current PR head and final-head CI is complete;
- there is no active Developer owner and no existing Independent Review.

When those conditions are satisfied, restore the missing `waiting-review` label,
re-read both the Issue and PR, require the pair to match, and continue the review
in the same invocation. Do not return `NO_ACTION` after a successful safe
reconciliation.

If the mapping is ambiguous, more than one candidate exists, completion evidence
is incomplete, the Cycle State is ACTIVE, the current head differs from the
Handoff, or an intervention/stop label exists, fail closed and report the exact
workflow conflict rather than guessing or modifying labels.

## Cycle entry

1. Read the latest `main` rules.
2. Run the lifecycle reconciliation preflight above using only lightweight Issue,
   PR, label, Cycle State, Handoff, head, and CI metadata.
3. Find open PRs labeled `waiting-review` and choose one meaningful review scope.
4. If none exists after reconciliation, output `NO_ACTION` and stop.
5. Read the Issue, PR body, complete diff, CI, relevant source PDF, canonical
   Markdown, validator output, and prior review/checkpoint history only for the
   selected review.

## Developer overlap interpretation

The principal Developer state is the PR's unique comment marked
`<!-- CODEX_CYCLE_STATE_V1 -->`, together with workflow labels and the latest
meaningful Checkpoint. A later scheduler collision that returns
`ACTIVE_INVOCATION_SKIP` is healthy overlap prevention when the principal lease
is still ACTIVE, fresh, boundary-compatible, and unchanged by Review or workflow
events.

The Reviewer must not treat that collision terminal output as the principal
Developer execution state. A skip that does not overwrite the ACTIVE Cycle
State is not orphan, stale, failure, or lack of progress and must not trigger
resume, recovery, or duplicate implementation.

Recovery is considered only when the principal lease is expired, inconsistent,
or orphaned, or when labels, Independent Review, CI, PR head, or completion state
actually changed. Scheduler cadence alone is not evidence of failure.

## Review scope

Verify Issue requirements, source truth and local scope, question binding,
standard answers, atomic scoring, calculations, chart reads, model grammar,
duplicates, source-first coverage, regressions, resource efficiency, and scope
compliance. Confirm the PR delivers one PDF to one self-contained Markdown and
does not prescribe recipient test execution.

For a large PR, checkpoint evidence and resume the same review next cycle. Do
not issue a final result from a partial sample. Update a full review checkpoint
only after meaningful review progress or state change; `NO_ACTION` and collision
observations do not require a repeated full checkpoint.

## Outcomes

- `PASS`: approve and merge; remove workflow-incompatible labels, mark the Issue
  `accepted`, and close it; then create or activate only the next source Issue as
  `agent-ready`. Do not edit `main` after merge to mirror lifecycle state in a
  Markdown file, and do not create a bookkeeping PR for label transitions.
- `PARTIAL_PASS` or `FAIL`: do not merge; give concrete findings, evidence, and
  repair requirements; remove `waiting-review` from both the Issue and PR; apply
  `repair-needed` to both the Issue and PR; keep the same Issue, branch, and PR;
  then re-read both sides and require the pair to match before stopping.
- `BLOCKED`: apply `blocked`, explain the external dependency, and stop.
- `PRODUCT_DECISION`: apply `product-decision`, state the decision required and
  available evidence, and stop.

The Review Agent must not quietly change implementation or product rules while
acting as the independent reviewer.

## Lifecycle authority

GitHub Issue and PR labels are the sole authoritative workflow state. Once an
open PR exists for a principal product Issue, lifecycle transitions that apply
to the in-flight work (`agent-working`, `repair-needed`, `waiting-review`,
`blocked`, `product-decision`) must be synchronized across the unique Issue/PR
pair and read back. `agent-ready` may exist only on the Issue before the PR is
created; `accepted` is the terminal Issue state after merge.

Before adding `agent-ready`, remove `blocked` and `product-decision`, verify
neither is present, and verify there is no other principal `agent-ready` product
Issue. Canonical question-bank front matter and the Source Catalog contain no
mutable workflow status.

## Bootstrap handoff

For the control-plane Bootstrap PR, additionally confirm Developer/Reviewer
separation, state transitions, cadence policy, anti-fragmentation rules, real CI
negative tests, actual Source Catalog data, and that VFH remained blocked. Only
after Bootstrap is merged may the Review Agent remove `blocked` from the VFH
Issue and add `agent-ready`.