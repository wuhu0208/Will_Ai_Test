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

## Issue/PR state-pair invariant

Before a PR exists, `agent-ready` is an Issue-only state. Once a unique open PR
exists for a principal product Issue, every in-flight lifecycle transition must
keep the unique Issue/PR pair synchronized for `agent-working`, `repair-needed`,
`waiting-review`, `blocked`, and `product-decision`.

A transition is complete only after the writer re-reads both objects and proves
that the intended principal label is present on both and incompatible principal
labels are absent. A Cycle State or Review Handoff does not substitute for this
label read-back.

If exactly one side of a unique completed Issue/PR pair is `waiting-review`, the
Reviewer may repair the missing label only when the Developer Cycle State is
TERMINAL, the Review Handoff is complete for the current PR head, final-head CI
is complete, no Independent Review exists, and no incompatible workflow/stop
label or active Developer owner exists. The Reviewer then re-reads both labels
and continues the review in the same invocation.

Ambiguous mappings, multiple candidates, incomplete completion evidence, active
leases, head/Handoff mismatch, or conflicting workflow labels are not safe
reconciliation cases. They must fail closed as workflow conflicts.

## PASS / merge ordering invariant

`accepted`, Issue closure, and activation of the next product Issue are all
post-merge states. They MUST NOT occur merely because Independent Review returned
`PASS`.

After `PASS`, the Reviewer must first persist durable review evidence for the
exact current PR head, merge that exact reviewed head, and re-read GitHub to prove
the PR is merged and the accepted result is on `main`. Only after successful
merge read-back may the current Issue become `accepted`/closed and the next
eligible product Issue become `agent-ready`.

If merge cannot be completed, the workflow fails closed as
`PASS_AWAITING_MERGE`: keep the current Issue open and the Issue/PR pair in
`waiting-review`, do not apply `accepted`, do not close the Issue, and do not
activate the next product Issue. Before declaring merge capability unavailable,
the Reviewer must perform real supported-action discovery/attempt rather than
infer tool absence from narration or prior sessions.

The invariant is one-way: lifecycle state may lag a successful merge briefly
while reconciliation finishes, but lifecycle state must never advance beyond an
unmerged PR.

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

The `waiting-review -> repair-needed` transition and the later
`repair-needed -> waiting-review` transition both follow the Issue/PR state-pair
invariant above.

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