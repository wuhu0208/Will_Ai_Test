# Question Bank Standard

## 1. Canonical rule

Each authoritative `doc/<PDF_STEM>.pdf` maps to exactly one final business file:
`question_banks/<PDF_STEM>.md`. The Markdown is self-contained and must not
depend on a Gold JSONL, CSV, second Markdown, or private scoring file.

Internal build artifacts may exist only in ignored working directories such as
`.cache/`, `.work/`, `build/`, or `tmp/`.

## 2. Front matter

Every canonical file begins with:

```yaml
---
schema_version: will-ai-question-bank/v1
source_pdf: VFH_R00_2023KW_C1N.pdf
source_sha256: 64-lowercase-hex-characters
source_pages: 22
question_bank_version: V1
product_scope: VFH
status: DRAFT
---
```

Allowed status values are `DRAFT`, `WAITING_REVIEW`, and `APPROVED`.

## 3. Document structure

The file must contain these sections in order:

1. `# <PDF_STEM> 题库与判定标准`
2. `## 1. Source Information`
3. `## 2. Scope`
4. `## 3. Question Statistics`
5. `## 4. Questions`

Question statistics include `Total` and every type actually present, including
as applicable: `FACT`, `SPEC_LOOKUP`, `TABLE`, `MODEL`, `CALCULATION`, `CHART`,
`PROCEDURE`, `CAUTION`, and other declared types.

## 4. Question structure

Every question uses a stable unique ID such as `VFH-Q-0001` and contains all of:

```markdown
## VFH-Q-0001

### Target

- Binding: EXACT_MODEL | MODEL_FAMILY | PRODUCT_SERIES | DOCUMENT_COMMON
- Product: ...
- Model / Scope: ...

### Question

...

### Standard Answer

...

### Scoring Standard

- P1 [40]: one atomic required fact
- P2 [60]: one atomic required fact

### Accepted Variants

- N/A

### Forbidden Errors

- N/A

### Tolerance

- N/A

### Source

- PDF: VFH_R00_2023KW_C1N.pdf
- Physical page: 1
- Printed page: N/A
- Section: ...
- Local scope path: ...
- Evidence type: TEXT
- Evidence: precise paraphrase or locator
```

No required field may be omitted. Source evidence follows
[SOURCE_TRUTH_STANDARD.md](SOURCE_TRUTH_STANDARD.md); scoring follows
[SCORING_STANDARD.md](SCORING_STANDARD.md).

## 5. Self-contained binding

A question must uniquely identify its answer target without relying on prior
questions or conversational context.

- `EXACT_MODEL`: only when a specific model is necessary for a unique answer.
- `MODEL_FAMILY`: when a fact applies to a defined model family.
- `PRODUCT_SERIES`: when a fact applies to the entire product series.
- `DOCUMENT_COMMON`: for genuinely document-wide material or a common appendix.

Do not use ambiguous phrases such as “该型号”, “这个产品”, or “这种情况下”.
Do not force a specific model when the source fact applies more broadly.

## 6. Source-first coverage

Coverage proceeds from the PDF to high-value facts, mappings, testable objects,
and representative questions. Coverage of a generated object list is not proof
of PDF coverage. Every `HIGH` or `MEDIUM` testable fact must have an explicit
disposition.

Cover applicable specifications, models, tables, formulae, charts, installation,
operation, cautions, maintenance, safety, limits, consequences, and variants.
There is no fixed question count. Avoid duplicates and simple numeric swaps;
normally use no more than three representative questions per knowledge object.

## 7. Execution neutrality

The canonical Markdown defines what is asked and how correctness is judged. It
must not require a browser or API, new conversations, timeouts, retries,
Playwright, Selenium, test order, checkpoint format, or any other recipient-side
execution method.

## 8. Freeze

After independent approval, question text, standard answer, scoring, tolerance,
forbidden errors, source, and ID are baseline data. Any later change requires a
dedicated Issue and review.
