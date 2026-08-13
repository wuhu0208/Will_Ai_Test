# Automation Cadence Policy

Scheduler cadence controls discovery latency, not execution duration. A trigger
is an opportunity to inspect fresh state; it is not a restart, resume command,
heartbeat deadline, lease timeout, or proof that the previous invocation failed.

A 30-minute or 60-minute scheduler may coexist with a healthy 40-90 minute
Developer cycle. Overlapping triggers must be resolved by the workflow state
machine and Active Invocation Guard. A second invocation skips when the
principal Cycle Lease is healthy. Do not lengthen cadence to the maximum task
duration merely to avoid overlap.

## Recommended work budget

- First 35-40 minutes: production work or substantive review.
- Final 5-10 minutes: focused validation, checkpoint, commit/push, and PR update.

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
Issue across multiple cycles. Divide it into coherent Work Packages, save
meaningful checkpoints, and resume without redoing completed packages.
