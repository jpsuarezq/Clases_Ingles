# AGENTS.md

Conventions for agents working in this repo.

## What this repo is

`Clases_Ingles` holds the full progress of an English course: from A2 to B2 over three
months, with daily exercises across reading, writing, speaking and listening.

Content is instructional material for a Spanish-speaking learner. Keep exercises
interactive and explanatory, always include real colloquial English, and for speaking
work ground phoneme drills in the Spanish → English contrast.

## Agent skills

### Issue tracker

Issues live in this repo's GitHub Issues, driven with the `gh` CLI. See `docs/agents/issue-tracker.md`.

### Triage labels

The five canonical triage roles, default vocabulary. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: one `GLOSSARY.md` and `docs/adr/` at the repo root. See `docs/agents/domain.md`.

## Repo layout

```
/
├── notas/        ← class notes, one folder per unit
├── ejercicios/   ← practice material
├── recursos/     ← links and reference material
└── docs/
    ├── agents/   ← agent config (tracker, labels, domain)
    └── adr/      ← decision records
```

## Conventions

- Folder names lowercase with hyphens; unit folders numbered: `unidad-01-present-simple/`
- File names: `clase-2026-03-12.md`
- Public repo: never commit credentials or personal data