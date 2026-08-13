# .engram Workspace

This directory is the **engineering memory workspace** for this Git repository.

It stores:
- Decisions (with context, alternatives, rationale)
- Engineering Journal Entries
- Raw Evidence (AI conversations, logs, notes — requires review)
- Templates for consistent recording

## Privacy

Raw evidence, personal drafts, and local configuration are kept private by default
(see `.engram/.gitignore`).

Only reviewed and curated content should be committed.

## Usage

- `engram init` (already done)
- Future: `engram journal`, `engram decide`, `engram import`, etc.

The source of truth stays in `.engram/`. Curated content can later be selectively
published to the main repository documentation.

See `DECISIONS.md` (pre-init) and `.engram/decisions/` for the project's own decisions.
