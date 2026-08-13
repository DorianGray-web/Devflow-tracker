# Contributing to Engram

Thank you for considering contributing!

Engram is an open-source project that dogfoods its own philosophy: all design discussions, decisions, and rationale are recorded in the `.engram/` workspace (private by default; reviewed content can be selectively published).

## How to contribute

1. Read `VISION.md`, `MISSION.md`, `DESIGN_PRINCIPLES.md`, `DOMAIN_MODEL.md`, `ENGINEERING_MODEL.md`, and `ARCHITECTURE.md`.
2. Create or reference a Decision record in `.engram/decisions/` for any non-trivial change.
3. Keep changes small, well-linked (using Relations), and aligned with the Design Principles (simplicity first, Evidence before Knowledge).
4. All significant decisions must be reviewed and added to the Engineering Journal before merging.
5. Write clear commit messages that reference Journal entries or Decisions.

See `ARCHITECTURE.md` for the current technical approach and `ROADMAP.md` for priorities.

We welcome improvements to the documentation, the domain model, importers, and the CLI — always grounded in real usage stories recorded in the Engineering Journal.

Before submitting a large feature, please open a Discussion or create a Journal entry outlining the problem and proposed solution.

**Clarifications**:
- **Product name**: Engram
- **Workspace folder**: `.engram/`
- **Core domain objects**: Engineering Activity, Evidence, Engineering Journal Entry, Decision, Knowledge Artifact, Perspective, Relation
- **Private vs public**: `.engram/` private by default; selective publish.
- **Project repo vs Engineering Memory workspace**: Git repo for product code; `.engram/` for engineering memory.