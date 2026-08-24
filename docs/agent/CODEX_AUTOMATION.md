# Codex Developer Automation

Fresh state is mandatory. Full context is conditional. Every scheduled
invocation follows the three stages below in order.

## Stage 0 — LIGHTWEIGHT_TASK_DISCOVERY

Read only:

1. latest `main/AGENTS.md`;
2. latest `main/docs/agent/CODEX_AUTOMATION.md`;
3. open Issues;
4. open PRs;
5. current workflow labels;
6. the smallest Issue/PR metadata needed to establish a unique correspondence.

Do not read business content, PDFs, `SOURCE_CATALOG.md`, question-bank
standards, canonical question Markdown, Source Inventory, Model Grammar,
historical Review or Checkpoint content, a large PR diff, source code, render
cache, OCR, screenshots, CI logs, tests, builds, or a broad repository scan.

Principal candidate priority is:

1. one `repair-needed` Issue with its corresponding open PR;
2. one legally recoverable `agent-working` Issue with its corresponding open PR;
3. one legal `agent-ready` Issue.

`blocked` or `product-decision` always stops execution, even if another
executable label is also present. More than one candidate at any principal
priority, or a non-unique Issue/PR/branch mapping, is
`BLOCKED_WORKFLOW_STATE_CONFLICT`; do not choose one or modify labels.

If none of the three candidate classes exists, output exactly:

```text
STATUS: NO_ACTION
WORK_CLASS: NO_OP
ISSUE: NONE
STOP_REASON: NO_EXECUTABLE_ISSUE
```

Then stop without entering Stage 1 or Stage 2.

## Stage 1 — ACTIVE_INVOCATION_GUARD

Run this stage when Stage 0 finds one `agent-working` Issue and its unique open
PR. Do not interpret the scheduler trigger itself as proof that prior work was
interrupted.

### Cycle Lease

The PR must maintain one update-in-place comment with this marker:

```text
<!-- CODEX_CYCLE_STATE_V1 -->
```

The comment is operational coordination evidence, not workflow state. Its
payload must contain at least:

```yaml
schema: codex-cycle-state-v1
invocation_id:
state: ACTIVE | TERMINAL
issue:
branch:
pr:
head_at_start:
work_package:
started_at:
last_heartbeat_at:
lease_until:
predicted_duration_seconds:
checkpoint_ref:
next_action:
```

Create the marker comment once, then update that same comment. Do not create a
new comment for every heartbeat or scheduler cycle. An active owner refreshes
`last_heartbeat_at` and `lease_until` before expiry and after meaningful state
changes. The default active-invocation freshness is 7,200 seconds. When
`predicted_duration_seconds` is present, freshness is:

```text
max(7200, 2 * predicted_duration_seconds)
```

Scheduler cadence is never a stale timeout.

### Healthy-owner skip

Return `ACTIVE_INVOCATION_SKIP` only when all are true:

- Issue, PR, and branch match;
- the marker comment is unique and its state is `ACTIVE`;
- the lease has not expired under the freshness rule;
- workflow labels contain no new intervention state;
- there is no new Independent Review, `blocked`, or `product-decision`;
- no completed result has entered `waiting-review`;
- no known branch/head conflict exists;
- the requested work boundary is compatible with the lease.

Output:

```text
STATUS: NO_ACTION
WORK_CLASS: NO_OP
ISSUE: <issue>
PR: <pr>
STOP_REASON: ACTIVE_INVOCATION_SKIP
```

Then stop. Do not enter Full Bootstrap, check out or modify the branch, read a
PDF, run tests/build, repeat a Work Package, create a checkpoint, or overwrite
the principal ACTIVE Cycle State.

### Lease acquisition and race verification

If a lease must be acquired or recovered and the platform has no atomic
compare-and-swap operation, use this minimum protocol:

1. read the unique Cycle State comment and verify that it is claimable;
2. update it with this invocation's `invocation_id` and ACTIVE lease;
3. immediately read the comment again;
4. continue only if the re-read owner, Issue, PR, branch, and work boundary still
   match this invocation.

If another owner wins the re-read, stop with `ACTIVE_INVOCATION_SKIP` before any
branch change. Prefer a true atomic lease if the platform later provides it.
Multiple marker comments, missing required fields, mismatched boundaries, an
expired lease, or an ACTIVE lease whose owner cannot be reconciled is
inconsistent/orphan evidence and requires Stage 2 recovery inspection; it is
not permission to repeat work blindly.

## Stage 2 — FULL_BOOTSTRAP

Enter only for:

- the unique legal `agent-ready` Issue to be claimed;
- `agent-working` without a healthy active owner;
- `repair-needed`;
- an expired, inconsistent, or orphan lease;
- a real workflow, Review, CI, head, or completion change;
- work that genuinely requires resume or repair.

Re-read labels before mutation. For new work, replace `agent-ready` with
`agent-working`, establish and re-read-verify the ACTIVE Cycle Lease, then begin.
For repair, continue the same Issue, branch, and PR. For recovery, first inspect
whether the result is already complete and whether CI, Review, PR head, or the
latest meaningful Checkpoint changed; never assume the whole Work Package must
be repeated.

Only now read the current work's necessary subset of:

- `AUTOMATION_CADENCE_POLICY.md`, `RESOURCE_POLICY.md`, and
  `WORKFLOW_STATE_MACHINE.md`;
- the selected Issue and PR;
- latest relevant Independent Review and meaningful Cycle Checkpoint;
- current head and focused CI status;
- Acceptance Criteria and Work Package Plan;
- applicable `docs/question-bank/*`, `SOURCE_CATALOG.md`, and only the source or
  evidence needed by the current Work Package.

Do not default to all historical Issues, PRs, Reviews, Checkpoints, diffs, logs,
rules, PDFs, or source files.

## Work cycle and Checkpoint

A Work Package is a durable checkpoint/recovery unit, not a mandatory invocation
stop boundary. Start with the next incomplete Work Package. Reuse valid
artifacts, run only necessary deterministic validation, commit/push meaningful
progress, and update the same PR.

After each completed Work Package:

1. run focused/local deterministic validation appropriate to that package;
2. commit and push the meaningful completed boundary;
3. write/update a recoverable Checkpoint with completed scope, evidence reused,
   validation performed, current head, and the exact next incomplete package;
4. refresh the Cycle State while keeping the same invocation `ACTIVE` if it will
   continue;
5. decide whether the adjacent next Work Package is safe to execute immediately.

Continue directly into the next adjacent Work Package in the SAME invocation
when all are true:

- the same Issue, branch, and PR remain authoritative;
- the current invocation still owns the healthy Cycle Lease;
- the next package is inside the already-approved Issue scope and has no unmet
  external dependency or product decision;
- there is no new Independent Review, stop/intervention label, conflicting owner,
  or known branch/head conflict;
- existing source/cache/render/calculation evidence can be reused safely and the
  continuation will not repeat completed work;
- enough execution budget remains to reach another durable checkpoint without
  rushing validation, commit/push, or lifecycle handoff.

Do not stop merely because one Work Package completed. In particular, do not
turn a 5-15 minute package into scheduler idle time when an adjacent package is
immediately executable. Use the cadence policy's substantive-work budget as
planning guidance, not as a requirement to consume time.

Intermediate CI is asynchronous evidence, not a mandatory barrier between
adjacent Work Packages when focused/local deterministic validation passes and no
known CI failure exists. Do not sit idle waiting for intermediate CI solely to
end an invocation. If a CI failure becomes known, reconcile it before relying on
that head for later completion. Final-head CI remains mandatory before
`waiting-review`.

Stop at the latest durable checkpoint when any of these is true:

- remaining execution budget is insufficient to complete another coherent
  package plus validation/checkpoint/handoff safely;
- an external result must be awaited;
- `blocked`, `product-decision`, Review intervention, scope/risk change, or
  conflicting ownership appears;
- lease ownership can no longer be proven;
- the Issue is complete and final-head validation/CI/handoff must be finalized.

Write a full recoverable Checkpoint only when actual work occurred or when the
Work Package, commit/head, Review, CI, or recovery state meaningfully changed.
Do not write a full Checkpoint for `NO_ACTION` or `ACTIVE_INVOCATION_SKIP`; at
most record a lightweight operational observation outside the principal state.
Do not rewrite unchanged Checkpoint content every scheduler cycle.

Before a working invocation stops, update the Cycle State comment with the
latest checkpoint reference and exact next action. Set it to `TERMINAL` when the
invocation no longer owns active work. If the Issue remains incomplete, preserve
`agent-working`. Every later invocation still performs mandatory fresh Stage 0,
applicable Stage 1, and conditional Stage 2. After Stage 2 proves the resume is
authorized, continue from the latest completed checkpoint without repeating
completed Work Packages or reparsing, rerendering, or reloading unchanged
business evidence merely because a new scheduler trigger occurred.

If all acceptance criteria and final-head CI pass, transition to
`waiting-review`, provide the Review Handoff, set the lease `TERMINAL`, and stop.

### Completion transition invariant

A completed handoff is not valid until the workflow-state pair is synchronized.
For the unique selected Issue and its unique open PR:

1. remove incompatible principal workflow labels from both sides;
2. add `waiting-review` to both the Issue and the PR;
3. re-read both objects and require both to contain `waiting-review` and neither
   to contain `agent-ready`, `agent-working`, `repair-needed`, `blocked`, or
   `product-decision`;
4. only after that read-back succeeds may the Developer publish its terminal
   `next_action` for Independent Review and stop.

If either label write or read-back fails, do not report a successful handoff.
Keep the same Issue/PR mapping, record the exact workflow transition failure,
and leave the state recoverable; never start the next Issue or self-review.

## Deterministic state simulations

| Case | Input | Required outcome |
| --- | --- | --- |
| A | 0 open Issues, 0 open PRs | `NO_ACTION`; no Stage 2 or expensive reads/actions |
| B | one legal `agent-ready` Issue | Stage 2; recheck labels, claim, establish/re-read ACTIVE lease, work |
| C | one `agent-working` + fresh compatible ACTIVE lease | `ACTIVE_INVOCATION_SKIP`; no Stage 2 |
| D | one `agent-working` + expired lease | Stage 2 recovery inspection before any repeat work |
| E | `repair-needed` + existing PR | repair same Issue, branch, and PR |
| F | `blocked` + `agent-ready` | `BLOCKED`; no execution |
| G | multiple `agent-ready` candidates | `BLOCKED_WORKFLOW_STATE_CONFLICT`; no selection |
| H | collision skips while principal lease stays ACTIVE | Reviewer treats skip as healthy; no recovery |
| I | completed Issue is `waiting-review` but PR is not | Developer handoff is incomplete; synchronize and read back both labels before terminal success |
| J | WP1 completes quickly and WP2 is immediately executable under the same healthy lease | checkpoint WP1, keep the same invocation ACTIVE, and continue WP2 without waiting for another scheduler trigger |
| K | a completed WP is durably checkpointed but the invocation must stop before the next WP | set Cycle State TERMINAL with exact next package; next invocation resumes that package without repeating the completed WP |

## Hard stops

- Do not self-review, approve, merge, close as accepted, or activate the next Issue.
- Do not create a new Issue, branch, or PR merely because a review failed.
- Do not start work labeled `blocked` or `product-decision`.
- Do not change source scope, delivery format, or core scoring rules without a
  user decision.
- Do not write workflow status into canonical question-bank front matter or the
  Source Catalog; GitHub labels remain authoritative.
