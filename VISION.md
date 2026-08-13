# Vision

Engram is a universal, project-native engineering memory layer.

It captures the *why*, the trade-offs, the multi-perspective discussions (human and AI), and the evolution of knowledge across the entire lifecycle of a software project.

The Git repository stores the *what* (the code and its history). The `.engram/` workspace stores the *why* and *how we got here*.

By initializing a lightweight `.engram/` workspace alongside any Git repository, teams and solo developers (including those heavily using AI agents) create a persistent, searchable engineering memory that does not pollute the product source tree.

The long-term vision is that every mature open-source or commercial project ships with an Engram workspace that newcomers, future maintainers, and AI coding agents can consult to instantly understand past Decisions, rejected alternatives, and the rationale behind the current architecture.

Engram treats AI output as Evidence, not as final knowledge. Only reviewed and accepted artifacts become part of the permanent Engineering Journal.

**Engram makes institutional knowledge survive people, models, and time.**

**Clarifications**:
- **Product name**: Engram
- **Workspace folder**: `.engram/`
- **Core domain objects**: Engineering Activity, Evidence, Engineering Journal Entry, Decision, Knowledge Artifact, Perspective, Relation
- **Private vs public**: `.engram/` is private by default (local, developer-controlled). Reviewed Journal Entries, Decisions, and Knowledge Artifacts can be selectively published to the main repository’s documentation.
- **Project repo vs Engineering Memory workspace**: Git repo = product code and history (*what*). `.engram/` = engineering reasoning and memory (*why*). They live side-by-side but never mix.