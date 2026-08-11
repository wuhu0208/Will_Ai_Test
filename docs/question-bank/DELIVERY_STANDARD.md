# Delivery Standard

## One PDF to one canonical Markdown

The only final business delivery for `doc/<PDF_STEM>.pdf` is:

`question_banks/<PDF_STEM>.md`

The stems must match exactly. Do not shorten, normalize, or rename a stem in a
way that loses document version identity.

The canonical Markdown contains the question, standard answer, scoring,
accepted variants, forbidden errors, tolerance, and source evidence. A recipient
must not need a Gold JSONL, CSV, second Markdown, or private scoring file.

## Internal materials

Temporary JSON, JSONL, CSV, source inventories, page caches, validator output,
rendered evidence, and deterministic calculation scripts may be used during
construction. Unless an Issue explicitly makes a reusable tool permanent, keep
them in ignored `.cache/`, `.work/`, `build/`, or `tmp/` locations.

Do not merge split product deliverables such as `*_GOLD.jsonl`,
`*_TEST_STANDARD.md`, or `*_QUESTION_BANK.md` into `question_banks/`.

## Storage

`doc/` is the current canonical source entry in GitHub. Do not create a second
Google Drive authority. If file size or repository storage becomes unsuitable,
open a `product-decision` Issue before changing the storage model.
