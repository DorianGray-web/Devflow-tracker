# Engineering Model

> Core concepts for the Engram Engineering Memory Platform.

## Status

Version: 0.2  
Status: Refined after rename from original tracker-focused model

---

## Model Overview

Engram elevates engineering reasoning over raw activity tracking. The model distinguishes raw inputs (Evidence) from curated knowledge (Engineering Journal Entries, Decisions, Knowledge Artifacts).

Core objects (standardized terminology):

- **Engineering Activity** – lightweight record of intentional work.
- **Evidence** – raw material (AI conversations, notes, logs) that requires review.
- **Engineering Journal Entry** – curated, reviewed synthesis of significant work or decisions.
- **Decision** – first-class Journal Entry capturing alternatives, rationale, status (accepted/rejected/superseded), and consequences.
- **Knowledge Artifact** – distilled, living facts or guidelines derived from Journal entries.
- **Perspective** – specific viewpoint (human role or named AI model) attached to Evidence or Discussion.
- **Relation** – explicit bidirectional links between objects, commits, files, ADRs, releases, or tasks.

These objects live in a `.engram/` workspace alongside the Git repository.

## Key Principles

- **Evidence before Knowledge**: AI conversations, meeting notes, and telemetry are stored as Evidence. Only after human (or human-guided) review and approval do insights become Engineering Journal Entries, Decisions, or Knowledge Artifacts.
- **Multi-perspective preserved**: Different AI models or stakeholders can offer conflicting views; these coexist until a reviewed Decision synthesizes them.
- **Rejected decisions matter**: They prevent repeating discussions when conditions have not changed.
- **Links are first-class**: The ability to answer “why was this decision made?” and “how did this idea evolve?” depends on rich Relations.
- **Time is one attribute only**: Duration and timestamps are useful but not the primary focus.
- **Project-agnostic**: The same model works for Python, web, mobile, AI-agent, or documentation-heavy projects.

## Example Flow

AI Session (Engineering Activity) → Imported Chat (Evidence) → Multi-Perspective Analysis (Perspectives) → Human Review → Engineering Journal Entry / Decision → Derived Knowledge Artifact → Linked (Relation) to related Commit / ADR / Release.

Cross-device or multi-agent handovers are supported via structured Evidence and Journal Entries (similar to an engineering shift log).

**Clarifications**:
- **Product name**: Engram
- **Workspace folder**: `.engram/`
- **Core domain objects**: Standardized as listed above.
- **Private vs public**: `.engram/` is private by default; selective publish of reviewed artifacts.
- **Project repo vs Engineering Memory workspace**: Git repo for product code; `.engram/` for engineering memory.

This model will be versioned and refined inside the project’s own `.engram/journal/` and `.engram/decisions/` as Engram matures. All future changes will be recorded as Decisions.