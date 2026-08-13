# Engram Init Design

## 1. Problem `engram init` Solves

`engram init` creates the first viable engineering memory workspace (`.engram/`) for an existing Git repository. It bootstraps a consistent, private structure for recording Evidence, Engineering Journal Entries, Decisions, and Relations — without requiring full application logic, AI importers, or knowledge graph.

This solves the chicken-and-egg problem of documenting engineering rationale before the tool itself exists. It enforces "Evidence before Knowledge" from day one and makes the project self-documenting.

## 2. Files and Folders Created

```
.engram/
├── decisions/              # One Markdown file per Decision (0001-*.md)
├── journal/                # Engineering Journal Entries (YYYY-MM-DD-*.md)
├── evidence/               # Raw inputs (imported AI chats, logs, etc.)
├── knowledge/              # Distilled Knowledge Artifacts (optional, later)
├── relations.md            # Index of cross-links (or future graph)
├── config.json             # Project-level settings (tracked, safe)
├── templates/
│   ├── decision.md         # Template for new Decisions
│   ├── journal.md          # Template for Journal Entries
│   └── evidence.md         # Template for Evidence records
├── README.md               # Explains the workspace, private nature, and how to publish
└── .gitignore              # Ensures private files stay out of the main repo
```

## 3. Required Files

- `.engram/README.md`
- `.engram/config.json`
- `.engram/templates/decision.md`
- `.engram/templates/journal.md`
- `.engram/templates/evidence.md`
- `.engram/decisions/0005-*.md` (the init decision itself, created as first record)
- `.engram/.gitignore`
- `.engram/evidence/.gitkeep`

## 4. Optional Files

- Content inside `evidence/`, `journal/`, `knowledge/` (populated by user or later commands)
- `relations.md` (can be generated on first use)

## 5. What Should Be Git-Tracked

- The `.engram/` folder structure and its tracked files (templates, README, config.json, .gitignore, .gitkeep files, reviewed Decisions/Journal entries).
- Reviewed/published Journal Entries and Decisions (via future `engram publish` to main repo's docs).

This makes the engineering memory part of the project's history while keeping raw data private.

## 6. What Should Remain Private/Local

- All content inside `evidence/` (raw AI chats, logs, screenshots — ignored by default).
- Personal/un-reviewed Journal drafts.
- `config.local.json` (user-specific paths, perspectives, tokens).
- Draft files matching `*.local.*` or inside `journal/drafts/`.

## 7. How `.engram/` Relates to the Project Repository

`.engram/` lives **inside the project repository root** as a parallel workspace, next to `src/`, `docs/`, `tests/`, `ROADMAP.md`, etc.

It is part of the repository structure but does not mix with product code. Git-tracked portions become part of commit history. Raw/private files are excluded via `.engram/.gitignore`. Selective publish (future command) exports curated content to the main repo's documentation while the source of truth stays in `.engram/`.

## 8. Safety Checks Before Initialization

- Confirm the current directory is inside a Git repository (or allow `--force`).
- Check that `.engram/` does not already exist (error + suggestion to run `engram status`).
- Warn if there are uncommitted changes in the working tree.
- Validate write permissions in the workspace root.
- Offer a dry-run mode (`--dry-run`) that shows exactly what would be created without writing files.
- Respect any existing top-level `.gitignore` patterns.

## 9. First Generated Decision and Journal Templates

### Template: `templates/decision.md`
```markdown
# Decision {{id}} – {{title}}

**Status**: {{status}} (Accepted | Rejected | Superseded)
**Date**: {{date}}
**Related**: [Journal-{{link}}], Evidence-{{link}}

## Context
{{context}}

## Alternatives Considered
{{alternatives}}

## Decision
{{decision}}

## Rationale
{{rationale}}

## Consequences
{{consequences}}

## Evidence
- Links to raw Evidence files

**Perspectives**:
- Human: ...
- AI (Model-Name): ...
```

### Template: `templates/journal.md`
```markdown
# Engineering Journal Entry – {{date}} – {{title}}

**Type**: {{type}} (Research | Architecture | Debugging | AI Brainstorm | etc.)
**Duration**: {{hours}}h
**Related Decisions**: ...

## Problem / Context
...

## Discussion & Perspectives
...

## Insights / Outcomes
...

## Next Actions
- ...

**Linked Evidence**:
- ...

**Knowledge Artifacts Updated**:
```

### Template: `templates/evidence.md`
```markdown
# Evidence {{id}} – {{title}}

**Source**: {{source}} (AI Chat | Log | Meeting | etc.)
**Date**: {{date}}
**Linked To**: Decision-{{id}} | Journal-{{id}}

## Raw Content
...
```

These templates embed the core domain objects from `DOMAIN_MODEL.md` and enforce the "Evidence before Knowledge" principle (raw discussion lives as Evidence; reviewed synthesis becomes Decision/Journal).

---

**Pre- vs Post-Init Clarification**

Before the CLI exists, `DECISIONS.md` in the repo root acts as a temporary bootstrap index.

After `engram init`, all decisions must be stored as individual Markdown files inside `.engram/decisions/`, and `DECISIONS.md` becomes a generated human-readable index (with links).

This design is now unambiguous, consistent, and implementation-ready for the first CLI command. It directly supports v0.1 of the roadmap with no added features.
