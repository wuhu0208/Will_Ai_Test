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

## Operational Cycle Lease

The PR comment marked `<!-- CODEX_CYCLE_STATE_V1 -->` is operational
coordination evidence only. It does not replace or change `agent-ready`,
`agent-working`, `repair-needed`, `waiting-review`, `blocked`,
`product-decision`, or `accepted`.

When workflow state is `agent-working` and a compatible ACTIVE Cycle Lease is
fresh, a second Developer invocation has no authority to modify the same Issue,
branch, PR, or Work Package boundary. It must return
`ACTIVE_INVOCATION_SKIP`. The scheduler trigger does not make the lease stale.

The minimum lease freshness is 7,200 seconds or twice
`predicted_duration_seconds`, whichever is greater. An expired, inconsistent,
or orphan lease permits recovery inspection, not blind duplicate work. Lease
acquisition must be re-read and owner-verified before branch mutation when no
atomic compare-and-swap is available.

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
authorized transition adds `agent-ready`. Multiple principal candidates are a
workflow conflict and must not be resolved by arbitrary selection. Do not start
a subsequent product Issue before the current PR passes independent review and
merges. Do not mirror label transitions into tracked Markdown or create
lifecycle-only bookkeeping PRs.
