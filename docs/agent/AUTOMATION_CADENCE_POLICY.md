# Automation Cadence Policy

Scheduler cadence controls discovery latency, not execution duration. A trigger
is an opportunity to inspect fresh state; it is not a restart, resume command,
heartbeat deadline, lease timeout, or proof that the previous invocation failed.

A 20-minute, 30-minute, or 60-minute scheduler may coexist with a healthy
40-90 minute Developer cycle. Overlapping triggers must be resolved by the
workflow state machine and Active Invocation Guard. A second invocation skips
when the principal Cycle Lease is healthy. Do not lengthen cadence to the
maximum task duration merely to avoid overlap, and do not encode one external
scheduler interval as a mandatory repository execution duration.

## Recommended work budget

- First 35-40 minutes: production work or substantive review.
- Final 5-10 minutes: focused validation, durable checkpoint, commit/push, and
  PR/Cycle State update.

This is planning guidance, not a required duration. Finish early when useful
work and delivery checks are complete. Never fill time with repeated PDF
parsing, unnecessary tests, rereading unchanged content, unrelated refactoring,
duplicate screenshots, or manufactured work.

The minimum active-invocation freshness is 7,200 seconds and increases to twice
the predicted duration when that is longer. Cadence must never be substituted
for this freshness rule.

## Work packaging

An independent task estimated under 20 minutes should normally be combined with
adjacent work under the same business goal. Large question-bank work may use one
Issue across multiple cycles. Divide it into coherent Work Packages and persist
meaningful checkpoints so recovery never requires redoing completed packages.

A Work Package is a durable recovery boundary, not a mandatory invocation stop
boundary. When one Work Package is complete, the same Developer invocation
should continue directly into the next adjacent incomplete Work Package when all
of the following are true:

- the Issue, branch, and PR are unchanged and remain within the approved scope;
- the current invocation still owns the healthy Cycle Lease;
- no Review, stop label, conflicting owner, or external dependency requires a
  handoff;
- the next package can reuse existing source/cache/evidence safely;
- enough execution budget remains to reach another durable checkpoint without
  rushing validation or handoff.

After each completed Work Package, commit/push meaningful progress, update the
recoverable checkpoint and Cycle State, and keep the same invocation `ACTIVE` if
continuing. Intermediate focused/local deterministic validation is sufficient to
continue when risk-appropriate; do not wait for an intermediate CI run solely to
create scheduler idle time. Observe any CI failure that becomes known and stop
or repair as required. Final-head CI remains mandatory before `waiting-review`.

Stop at a durable checkpoint when remaining budget is insufficient, an external
result must be awaited, a blocker/product decision appears, scope/risk changes,
lease ownership is lost, or the Issue is complete. A later invocation resumes
from the latest completed Work Package rather than re-bootstrap or repeat it.
