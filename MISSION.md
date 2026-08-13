# Mission

Build a lightweight, local-first, Git-friendly open-source platform that lets any software project initialize an `.engram/` workspace.

Engram records Engineering Activities, multi-perspective Evidence, Decisions with full rationale, Engineering Journal Entries, and Knowledge Artifacts without polluting the product repository.

It makes deep questions such as:

- “Why was this Decision made?”
- “What alternatives were considered and why were they rejected?”
- “When did this idea first appear and how did it evolve?”
- “Which AI models reviewed this and what Perspectives did they offer?”

instantly answerable from a single, version-controlled source of truth.

**Clarifications**:
- **Product name**: Engram
- **Workspace folder**: `.engram/`
- **Core domain objects**: Engineering Activity, Evidence, Engineering Journal Entry, Decision, Knowledge Artifact, Perspective, Relation
- **Private vs public**: `.engram/` is private by default. Reviewed content can be selectively published to the main repo’s documentation.
- **Project repo vs Engineering Memory workspace**: Git repo = product code and history. `.engram/` = engineering reasoning and memory. They live side-by-side but never mix.

Engram prioritizes simplicity, human curation, and privacy. AI conversations are preserved as Evidence; only reviewed engineering artifacts enter the Engineering Journal.