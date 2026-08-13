# Decisions

This file serves as the index of all significant architectural and design decisions for the Engram project.

All decisions are recorded as individual Markdown files in `.engram/decisions/` following the schema defined in `DOMAIN_MODEL.md` and `ENGINEERING_MODEL.md`.

**Current decisions recorded (in this pre-initialization phase):**

- 0001 – Project Rename from DevFlow Tracker to Engram
- 0002 – Initial Documentation Skeleton
- 0003 – Refinement of Concept, Domain Model, and Roadmap (this document set)
- 0004 – Terminology and Naming Consistency Across Documentation
- 0005 – Minimal `engram init` Workflow (see ENG_INIT_DESIGN.md)

**Decision 0005 – Minimal `engram init` Workflow**

**Status**: Accepted  
**Date**: 2026-08-13

**Reason**:  
The first product value is not automation, but creating a consistent engineering memory structure beside an existing project.

**Rejected**:  
Starting with IDE plugins, cloud sync, AI importers, or telemetry.

**Before the CLI exists**, `DECISIONS.md` in the repo root acts as a temporary bootstrap index.

**After `engram init`**, decisions must be stored as individual Markdown files inside `.engram/decisions/`, and `DECISIONS.md` becomes a generated human-readable index (with links).

Future decisions will be created via the CLI (once implemented) and automatically linked here.

See `.engram/decisions/` for the full, linkable, version-controlled records after `engram init` is run.

All decisions follow the **Evidence before Knowledge** principle: raw discussion lives as Evidence; only reviewed synthesis becomes a permanent Decision record. Rejected or superseded decisions are preserved.

**Clarifications**:
- **Product name**: Engram
- **Workspace folder**: `.engram/`
- **Core domain objects**: Engineering Activity, Evidence, Engineering Journal Entry, Decision, Knowledge Artifact, Perspective, Relation
- **Private vs public**: `.engram/` private by default; selective publish of reviewed content.
- **Project repo vs Engineering Memory workspace**: Git repo = product code/history; `.engram/` = engineering memory.
