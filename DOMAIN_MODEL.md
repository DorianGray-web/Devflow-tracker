# Domain Model

## Core Concepts

- **Engineering Activity**  
  Lightweight record of intentional work. Includes type (Brainstorm, Research, Architecture Review, Coding, Debugging, AI Session, Meeting, Retrospective, etc.), timestamp, optional duration, participants (humans or specific AI models/Perspectives), links to Evidence, and tags. Time is only one attribute.

- **Evidence**  
  Raw, uncurated material linked to an Activity or Journal Entry. Examples: AI conversation snippet, meeting notes, log output, telemetry data, screenshot. Explicitly tagged as “AI-generated evidence – requires review” when applicable.

- **Engineering Journal Entry**  
  The curated, reviewed record of significant work or insight. Contains:
  - Title
  - Date
  - Problem / Context
  - Alternatives considered
  - Discussion (with multiple Perspectives)
  - Decision
  - Rationale
  - Consequences
  - Next Actions
  - Related Decisions, Commits, Releases, Tasks, Knowledge Artifacts, Evidence

- **Decision**  
  A first-class, specialized Engineering Journal Entry following a lightweight ADR-style format but richer, with explicit status (accepted, rejected, superseded, deferred, revisited). Rejected decisions are preserved and searchable.

- **Knowledge Artifact**  
  A distilled, reviewed, living fact or guideline derived from one or more Journal entries (e.g. “Playwright is used only for diagnostics because X, Y, Z”). These become the primary reference for newcomers and agents.

- **Perspective**  
  A viewpoint attached to Evidence or Discussion (e.g. “Claude-3.5-Sonnet – Architecture & Consistency Focus”, “Project Owner – Business Constraints”).

- **Relation**  
  Explicit, bidirectional, typed links between any objects, Git commits, files, external issues, or ADRs. Links enable powerful “why” and “how did this evolve?” queries.

## Principles
- Activities are cheap and quick to record.
- Journal Entries and Decisions are deliberate, reviewed, and high-value.
- AI output remains Evidence until explicitly curated.
- Everything is linkable, version-controlled via Git, and searchable.
- The model is project-agnostic and vendor-neutral.

**Clarifications**:
- **Product name**: Engram
- **Workspace folder**: `.engram/`
- **Core domain objects**: As listed above (standardized terminology).
- **Private vs public**: `.engram/` is private by default. Reviewed Journal Entries, Decisions, and Knowledge Artifacts can be selectively published to the main repository’s documentation.
- **Project repo vs Engineering Memory workspace**: Git repo = product code and history. `.engram/` = engineering reasoning, Evidence, Journal, Decisions, Knowledge Artifacts, and Relations.

This domain model will be refined and versioned inside the project’s own `.engram/` workspace (see `ENGINEERING_MODEL.md` for the broader engineering model). All changes will be recorded as Decisions in `.engram/decisions/`.