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

Labels describe workflow state, not confidence. Do not apply `agent-ready` while
`blocked` remains. Do not start a subsequent product Issue before the current PR
passes independent review and merges.
