# Will_Ai_Test

GitHub is the canonical development control plane for this project. `main` is
the accepted baseline; Issues define work, branches and pull requests deliver
it, CI verifies it, and an independent Review Agent decides whether it may be
merged.

## Repository layout

- `doc/`: authoritative source PDFs.
- `question_banks/`: one canonical Markdown question bank per source PDF.
- `docs/SOURCE_CATALOG.md`: source queue and delivery status.
- `docs/question-bank/`: question-bank, source-truth, scoring, and delivery rules.
- `docs/agent/`: Developer and Review Agent operating rules.
- `.github/`: Issue/PR templates and CI.
- `tools/`: deterministic repository and question-bank validators.
- `tests/`: validator unit tests and fixtures.

## Control loop

`Issue → Codex Developer → Branch/PR → CI → Independent Review → repair or merge → next Issue`

Only one principal product Issue should be `agent-ready` at a time. Developer
and Review roles are separate. Neither role may bypass the documented state
machine, and the Developer must never self-review or self-merge.

## Canonical delivery

Every `doc/<PDF_STEM>.pdf` has exactly one final business deliverable:
`question_banks/<PDF_STEM>.md`. That Markdown file contains questions, frozen
answers, scoring, accepted variants, forbidden errors, tolerances, and precise
source evidence. It does not prescribe how a recipient runs a test.

Start with [AGENTS.md](AGENTS.md), then read the linked rules for the role being
performed.
