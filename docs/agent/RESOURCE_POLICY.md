# Token and Resource Policy

The mandatory priorities are `REUSE FIRST`, `INCREMENTAL FIRST`, `TEXT FIRST`,
and `EVIDENCE FIRST`.

## Resource fast paths

`NO_ACTION` and `ACTIVE_INVOCATION_SKIP` are resource fast paths. They must stop
before Full Bootstrap and must not perform:

- PDF parsing, full render, OCR, or visual inspection;
- business source audit or full question-bank rule loading;
- tests, builds, large diff reads, or broad source reads;
- full CI log inspection or historical Checkpoint loading;
- repeated Issue/PR history reads beyond minimal Stage 0/1 metadata.

If Stage 0 proves there is no executable work, do not load more context merely
to confirm the same conclusion. A collision skip must not overwrite the active
owner's Cycle State or create a full Checkpoint.

## Working-path controls

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
13. Load only the rules, source, Review, CI, diff, and Checkpoint evidence needed
    by the current Stage 2 work boundary.
