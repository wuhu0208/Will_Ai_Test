# Independent Review Automation

## Cycle entry

1. Read the latest `main` rules.
2. Find open PRs labeled `waiting-review` and choose one meaningful review scope.
3. If none exists, output `NO_ACTION` and stop.
4. Read the Issue, PR body, complete diff, CI, relevant source PDF, canonical
   Markdown, validator output, and prior review/checkpoint history.

## Review scope

Verify Issue requirements, source truth and local scope, question binding,
standard answers, atomic scoring, calculations, chart reads, model grammar,
duplicates, source-first coverage, regressions, resource efficiency, and scope
compliance. Confirm the PR delivers one PDF to one self-contained Markdown and
does not prescribe recipient test execution.

For a large PR, checkpoint evidence and resume the same review next cycle. Do
not issue a final result from a partial sample.

## Outcomes

- `PASS`: approve and merge; remove workflow-incompatible labels, mark the Issue
  `accepted`, and close it; then create or activate only the next source Issue as
  `agent-ready`. Do not edit `main` after merge to mirror lifecycle state in a
  Markdown file, and do not create a bookkeeping PR for label transitions.
- `PARTIAL_PASS` or `FAIL`: do not merge; give concrete findings, evidence, and
  repair requirements; remove `waiting-review`; apply `repair-needed`; keep the
  same Issue, branch, and PR.
- `BLOCKED`: apply `blocked`, explain the external dependency, and stop.
- `PRODUCT_DECISION`: apply `product-decision`, state the decision required and
  available evidence, and stop.

The Review Agent must not quietly change implementation or product rules while
acting as the independent reviewer.

## Lifecycle authority

GitHub Issue and PR labels are the sole authoritative workflow state. Before
adding `agent-ready`, remove `blocked` and `product-decision`, verify neither is
present, and verify there is no other principal `agent-ready` product Issue.
`agent-ready` must never coexist with either stop label. Canonical question-bank
front matter and the Source Catalog contain no mutable workflow status.

## Bootstrap handoff

For the control-plane Bootstrap PR, additionally confirm Developer/Reviewer
separation, state transitions, cadence policy, anti-fragmentation rules, real CI
negative tests, actual Source Catalog data, and that VFH remained blocked. Only
after Bootstrap is merged may the Review Agent remove `blocked` from the VFH
Issue and add `agent-ready`.
