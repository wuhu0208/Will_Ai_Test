# Will_Ai_Test

GitHub is the canonical control plane for this project.

## What lives here

- `doc/` — source PDFs (authoritative source documents).
- `question_banks/` — one canonical Markdown question bank per source PDF.
- `docs/agent/` — Codex/Review Agent operating rules.
- `docs/question-bank/` — question-bank, source-truth, scoring, and test standards.
- `.github/` — Issue/PR templates and CI.
- `tools/` — deterministic validation utilities.

## Workflow

`Issue(agent-ready) → Codex → Branch/PR → CI → waiting-review → independent Review → merge/repair → next Issue`

`main` is the accepted baseline. After this one-time empty-repository bootstrap, product/question-bank changes must go through Issues and PRs.

Start with [AGENTS.md](AGENTS.md).
