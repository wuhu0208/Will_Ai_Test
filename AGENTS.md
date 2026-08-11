# Agent Rules

## Codex

1. Only execute Issues labeled `agent-ready`.
2. Do not expand scope.
3. Keep changes incremental.
4. Create PRs for review.
5. Do not self-approve or self-merge.

## Review Agent

Check:

- Issue requirements
- correctness
- regressions
- tests
- resource efficiency
- scope compliance

Outcomes:

- PASS: approve
- FAIL/PARTIAL: request repair on same PR
- BLOCKED: stop and request decision

## Token efficiency

Prefer:

- read existing artifacts first;
- avoid repeated PDF processing;
- avoid sending full DOM/screenshots unless required;
- batch deterministic checks;
- only use AI review for semantic uncertainty.
