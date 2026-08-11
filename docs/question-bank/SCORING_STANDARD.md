# Scoring Standard

## Required components

Every question contains a frozen Standard Answer, Required Points under Scoring
Standard, Accepted Variants, Forbidden Errors, and Tolerance.

## Required Points

1. Each point expresses one independently scoreable semantic fact.
2. Point identifiers are unique within the question.
3. Integer weights sum to exactly 100.
4. An `atomic_fact_count` assertion is not evidence of atomicity.
5. Multi-model results are split along the dimensions necessary to judge them.
6. Calculation questions score the final result explicitly.
7. Required units and required back-substitution each receive explicit scoring.
8. A Forbidden Error overrides partial credit when the stated failure condition occurs.

Accepted Variants list only semantically equivalent expressions. Forbidden
Errors list concrete critical mistakes. Use `- N/A` when either is unnecessary.

## Tolerance

Numerical questions specify expected value, unit, and either a true tolerance or
an exact rounding rule. Non-numerical questions use `- N/A`.

“Round to two decimal places” is a rounding rule, not `±0.01`. Prefer `Decimal`
and state the applicable mode, such as `ROUND_HALF_UP`, when required by the PDF.

## Deterministic calculation Gold

Calculation Gold is produced by a deterministic script with explicit inputs,
units, precision, and rounding. The model must not estimate Gold. The script may
be retained as a permanent tool only when the Issue requires it; otherwise it is
an ignored build artifact.

## Chart questions

A high-value Chart question requires a visual chart read. If the requested input
and output already appear as a discrete table lookup, classify it as a table
question. Formulae may sanity-check chart Gold but may not replace the visual
read. Use a stated `CHART` tolerance based on the chart resolution.

## Model questions

Validate model answers against a grammar derived from the PDF model notation:
field order, meaning, legal and illegal combinations, and family boundaries.
Example allowlists alone are insufficient.
