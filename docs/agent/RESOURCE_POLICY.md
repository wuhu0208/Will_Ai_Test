# Token and Resource Policy

The mandatory priorities are `REUSE FIRST`, `INCREMENTAL FIRST`, `TEXT FIRST`,
and `EVIDENCE FIRST`.

1. Do not reparse a PDF when its hash and required extraction version are unchanged.
2. Do not rerender pages while a valid page cache exists.
3. Use scripts for mechanical work, hashes, CSV/JSON validation, and deterministic Gold.
4. Use models only for genuine semantic or visual uncertainty.
5. Cache semantic review by complete input hash.
6. Checkpoint and resume; do not redo completed Work Packages.
7. Do not send complete DOM or HTML into model context.
8. Do not generate screenshots for large numbers of normal questions.
9. Report progress no more often than once per 25 processed items.
10. Small display or metadata changes do not trigger full business reruns.
11. Report wording changes do not trigger a complete PDF audit.
12. Keep temporary data under ignored working directories and never commit secrets.
