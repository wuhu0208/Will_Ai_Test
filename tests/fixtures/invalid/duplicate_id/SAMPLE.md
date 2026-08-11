---
schema_version: will-ai-question-bank/v1
source_pdf: SAMPLE.pdf
source_sha256: 0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
source_pages: 1
question_bank_version: V1
product_scope: SAMPLE
status: DRAFT
---

# SAMPLE 题库与判定标准

## 1. Source Information

- Source PDF: SAMPLE.pdf

## 2. Scope

Fixture scope.

## 3. Question Statistics

- Total: 1
- FACT: 1

## 4. Questions

## SAMPLE-Q-0001

### Target

- Binding: PRODUCT_SERIES
- Product: SAMPLE
- Model / Scope: Entire series

### Question

What is the documented fixture value for the SAMPLE product series?

### Standard Answer

The documented value is 10 kN.

### Scoring Standard

- P1 [70]: Gives the value 10.
- P2 [30]: Gives the unit kN.

### Accepted Variants

- 10 kilonewtons

### Forbidden Errors

- N/A

### Tolerance

- Exact value and unit; no numerical tolerance.

### Source

- PDF: SAMPLE.pdf
- Physical page: 1
- Printed page: N/A
- Section: Fixture
- Local scope path: Fixture > Value
- Evidence type: TEXT
- Evidence: The fixture states 10 kN for the series.

## SAMPLE-Q-0001
