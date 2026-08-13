# Architecture

## High-level Overview

Engram is deliberately kept simple, local-first, and file-based so it feels like a natural extension of any Git repository.

### Storage
- All data lives in a `.engram/` directory at the project root (private by default).
- Primary format: Markdown files with YAML front-matter for metadata and structure.
- Lightweight index files (YAML or JSON) are generated only for fast lookup and cross-references (Relations).
- The entire workspace is Git-friendly and can be committed (or kept private via `.gitignore`).

### Core Folders (initial proposal)
```
.engram/
├── activities/     # Lightweight Engineering Activities
├── journal/        # Curated Engineering Journal Entries
├── decisions/      # First-class Decision records
├── evidence/       # Imported raw material (requires review)
├── knowledge/      # Derived, reviewed Knowledge Artifacts
├── relations/      # Explicit link index (or embedded in files)
├── config/         # Project-specific settings
└── index/          # Generated cross-reference and search helpers
```

### Layers
1. **Core Engine / CLI** – Commands for `engram init`, `journal`, `decide`, `import`, `review`, `link`, `query`, `publish`.
2. **Import Layer** – Pluggable importers for AI chat exports, meeting notes, Git metadata, etc.
3. **Curation Layer** – Tools and workflow to turn Evidence into reviewed Engineering Journal Entries and Decisions (human approval required).
4. **Query Layer** – Simple full-text + link-graph traversal. Later optional semantic search.
5. **Publish Layer** – Selective export of reviewed public Journal entries, Decisions, and Knowledge Artifacts to the main repository’s documentation (e.g. `docs/engineering/`).

### Key Design Decisions
- No background daemon, heavy telemetry, or real-time monitoring in v0.1.
- No cloud or real-time cross-device sync initially (use Git to synchronize the `.engram/` folder).
- Multi-perspective AI Evidence is preserved side-by-side.
- All architecture and design choices for Engram itself are recorded as Decisions inside its own workspace.
- Architecture remains project-agnostic and avoids any hard dependency on specific IDEs, AI providers, or platforms.

**Clarifications**:
- **Product name**: Engram
- **Workspace folder**: `.engram/`
- **Core domain objects**: Engineering Activity, Evidence, Engineering Journal Entry, Decision, Knowledge Artifact, Perspective, Relation
- **Private vs public**: `.engram/` private by default; selective publish to main repo docs.
- **Project repo vs Engineering Memory workspace**: Git repo = product code/history; `.engram/` = engineering memory.

This architecture will evolve only after real usage feedback is captured and recorded in the project’s own Engineering Journal and Decisions.