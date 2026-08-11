# Question Bank Standard

## Purpose

Convert each product PDF under `doc/` into a frozen Markdown question bank.

## Required outputs per PDF

- `<PRODUCT>_QUESTION_BANK.md`
- `<PRODUCT>_GOLD.jsonl`
- `<PRODUCT>_TEST_STANDARD.md`

## Question requirements

Each question must:

- identify exact product/model when ambiguity exists;
- include source location (PDF page and section);
- include standard answer;
- include required scoring points;
- include tolerance rules where applicable;
- include forbidden errors;
- be independently testable.

## Binding rule

Never create a question such as "this product" when the source contains multiple models. Bind the question to the exact model.

## Freeze rule

After review approval, question text, answer, scoring and source binding become baseline data and only change through a dedicated Issue.
