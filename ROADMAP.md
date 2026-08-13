# Roadmap

## v0.1 – Engineering Memory Foundation
- Project initialization (`engram init`) — see ENG_INIT_DESIGN.md for the cleaned, consistent workflow
- Basic CLI for creating and linking Engineering Journal Entries and Decisions
- Simple Markdown-based schema for Journal, Decisions, Evidence, and Relations
- Manual import of AI conversation snippets as Evidence
- Basic query and search over the `.engram/` workspace
- Self-documenting: every design decision recorded in the project’s own `.engram/decisions/`
- Comprehensive initial documentation (this set of Markdown files)
- Human review workflow for turning Evidence into Engineering Journal Entries

## v0.2 – Journal & Decision Index
- Searchable titles, tags, and decision statuses (including rejected/superseded)
- Rich linking (Relations) between Journal entries, Decisions, Evidence, and Git artifacts
- Selective publish command to export reviewed entries to the main repo’s documentation
- Improved command-line and (optional early) VS Code support for creating entries

## v0.3 – Evidence Import & Curation
- Pluggable importers for major AI chat histories, meeting notes, and logs
- Tools to detect potential Decisions or Journal entries from Evidence
- Multi-perspective view and human approval workflow
- Structured handover / shift-log support for multi-agent or human-AI handovers

## v0.4 – Knowledge Graph & Search
- Explicit Relation graph for “why”, “how did this evolve?”, and “what alternatives were rejected?” queries
- Basic visualization of links
- Knowledge Artifact extraction and maintenance

## v0.5 – Integrations & Telemetry (optional)
- Git commit and release linking
- Privacy-first importers for coding activity, AI token usage, test runs, or CI events
- Basic retrospective generation from the Engineering Journal

## v1.0 – Stable Engineering Memory Platform
- Mature CLI, solid schema, import/review/publish workflow, and self-hosted example projects

**Postponed (after v1.0 or community-driven)**
- Cloud sync or SaaS dashboard
- Full semantic search / advanced knowledge graph UI
- Complex multi-agent orchestration
- Complete IDE plugin ecosystem
- Automatic publication to Git without review
- Public vs private permission system beyond simple `.gitignore`

**Clarifications**:
- **Product name**: Engram
- **Workspace folder**: `.engram/`
- **Core domain objects**: Engineering Activity, Evidence, Engineering Journal Entry, Decision, Knowledge Artifact, Perspective, Relation
- **Private vs public**: `.engram/` private by default; selective publish of reviewed artifacts.
- **Project repo vs Engineering Memory workspace**: Git repo for product code; `.engram/` for engineering memory.

Progress, trade-off decisions, and adjustments will be tracked and justified inside the project’s own `.engram/` workspace. Each roadmap item must have a linked Decision record before significant implementation begins.
