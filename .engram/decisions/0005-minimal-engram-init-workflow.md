# Decision 0005 – Minimal engram init Workflow

**Status**: Accepted
**Date**: 2026-08-13
**Related**: 

## Context
The first product value is not automation, but creating a consistent engineering memory structure beside an existing project. Before any CLI existed, design decisions were tracked in the root `DECISIONS.md`. A proper `engram init` command is needed to bootstrap the `.engram/` workspace with the correct structure, privacy rules, and first decision record.

## Alternatives Considered
- Start with full AI importers, telemetry, or cloud sync immediately.
- Use a general note-taking tool (Obsidian, Logseq) without project-specific structure.
- Put everything directly in the main repo docs/ folder.

## Decision
Implement a minimal, local-first `engram init` command that:
- Detects the Git repository root.
- Creates the exact `.engram/` structure defined in ENG_INIT_DESIGN.md.
- Creates only tracked-safe files (templates, config.json, README, .gitignore, first decision).
- Enforces privacy via `.engram/.gitignore` for evidence, drafts, and config.local.json.
- Supports `--dry-run` and refuses to overwrite existing `.engram/`.

No raw evidence files or user-specific config are created.

## Rationale
This solves the chicken-and-egg problem: we can now record engineering rationale using the same tool we are building. It enforces "Evidence before Knowledge" from day one and makes the project self-documenting. All future decisions will live in `.engram/decisions/`.

## Consequences
- The root `DECISIONS.md` becomes a historical bootstrap document.
- After init, new decisions must be created as individual files in `.engram/decisions/`.
- Future commands (`journal`, `decide`, etc.) will operate inside this structure.
- Raw/private data stays out of the main repository history by default.

## Evidence
- ENG_INIT_DESIGN.md
- DOMAIN_MODEL.md
- Pre-init DECISIONS.md

**Perspectives**:
- Human: Initial design and implementation of the bootstrap command.
- AI: Assisted with structure, templates, and consistency with design docs.
