# Workflow State Machine

## Primary path

```text
agent-ready
  -> agent-working
  -> branch / pull request
  -> CI
  -> waiting-review
  -> Independent Review
  -> PASS
  -> merge
  -> accepted / Issue closed
  -> next Issue agent-ready
```

Only one principal product Issue may be `agent-ready` at a time.

GitHub Issue and PR labels are the sole authoritative workflow state. Generic
Issue templates add no workflow-state label. Only an explicit state transition
may add one.

## Repair path

```text
waiting-review
  -> PARTIAL_PASS or FAIL
  -> repair-needed
  -> Developer continues same branch / PR
  -> CI
  -> waiting-review
```

## Stop states

- `blocked`: an external dependency prevents progress. Stop.
- `product-decision`: a user decision on product scope or policy is required. Stop.
- `accepted`: reviewed work is merged and its Issue is closed.

Labels describe workflow state, not confidence. `agent-ready` must never coexist
with `blocked` or `product-decision`; remove and verify stop labels before an
authorized transition adds `agent-ready`. Do not start a subsequent product
Issue before the current PR passes independent review and merges. Do not mirror
label transitions into tracked Markdown or create lifecycle-only bookkeeping PRs.
