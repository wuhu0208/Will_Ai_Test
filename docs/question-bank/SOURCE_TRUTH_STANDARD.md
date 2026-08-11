# Source Truth Standard

## Evidence is not a normalized fact

A normalized fact is a structured technical claim. Source evidence is the
specific PDF content that supports that claim. A matching string in the PDF
text layer is not sufficient to mark a fact `SOURCE_SUPPORTED`.

For text evidence, verify the same subject, model, technical object, predicate,
value, unit, conditions, negation, causal direction, and local scope.

## Local scope

Every evidence record carries a `local_scope_path`: document section,
subsection, numbered item, table/figure, and local heading as applicable. Bare
conditional or normative statements such as “if”, “otherwise”, “exceeds”,
“must”, or “must not” must remain attached to their local technical object.

Do not transfer a consequence from one component or procedure to another merely
because wording is nearby or similar.

## Evidence requirements

- `TEXT`: subject, model, predicate, condition, qualifier, unit, and negation match.
- `TABLE`: table identity, row, column, model, value, and unit are bound together.
- `FORMULA`: formula, variables, units, and applicable model/scope are explicit.
- `CHART`: axes, series, input, visual output, and chart-reading uncertainty are explicit.
- `DRAWING`: drawing location and the relevant dimension or state are explicit.
- `STATE_DIAGRAM`: states, transition, conditions, and direction are explicit.

Every question Source block includes PDF name, physical page, printed page,
section, local scope path, evidence type, and precise evidence. “See PDF”, an
unqualified page number, or a detached quote is not adequate evidence.

## Source-first audit

Maintain a source inventory before claiming coverage. Map high-value facts to
testable objects and then to questions. Unmapped, excluded, or non-testable facts
must have an explicit reason. Visual evidence and extracted text are separate
verification paths.
