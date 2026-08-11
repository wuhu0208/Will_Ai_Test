# Automation Cadence Policy

Web Automation is expected to run about once per hour. Each Developer or Review
cycle should therefore target roughly 40-50 minutes of useful work, without
artificially consuming time.

## Recommended budget

- First 35-40 minutes: production work or substantive review.
- Final 5-10 minutes: validation, tests, checkpoint, commit/push, and PR update.

Finish early when the useful work and delivery checks are complete. Never fill
time with repeated PDF parsing, unnecessary expensive tests, rereading unchanged
content, unrelated refactoring, duplicate screenshots, or manufactured work.

## Work packaging

An independent task estimated under 20 minutes should normally be combined with
adjacent work under the same business goal. For example, source, model, table,
and formula inventories form one meaningful Work Package rather than four tiny
Issues.

Large question-bank work may use one Issue across multiple cycles. Divide it
into coherent Work Packages, save checkpoints, and resume without redoing
completed packages. Cadence is a planning target, not a reason to lower quality
or force an exact cycle count.
