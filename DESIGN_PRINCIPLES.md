# Design Principles

1. **Local-first and privacy respecting**  
   Metadata over content. Full prompts or sensitive data are never collected automatically. Everything stays on the developer’s machine by default. The `.engram/` workspace is private by default.

2. **Separation of concerns**  
   Git repository = product code and history (the *what*).  
   `.engram/` workspace = engineering reasoning and memory (the *why*).  
   They live side-by-side but never mix.

3. **Simplicity over completeness**  
   Prefer plain Markdown files and a minimal folder structure. Add complexity only when real usage proves it necessary.

4. **Human-in-the-loop curation (Evidence before Knowledge)**  
   AI systems produce Evidence. Only after human review and approval do insights become Engineering Journal Entries, Decisions, or Knowledge Artifacts. Multiple AI Perspectives are preserved rather than merged.

5. **Linkability first**  
   Every Engineering Journal Entry, Decision, Knowledge Artifact, and Relation must be easily referenceable from code comments, commit messages, or other entries.

6. **Incremental adoption**  
   `engram init` should be zero-config. Users can start with a simple Engineering Activity log and gradually deepen into a full knowledge platform.

7. **Vendor and tool neutrality**  
   No hard dependencies on specific AI providers, IDEs, or platforms. Importers are pluggable.

8. **Decisions are first-class and self-documenting**  
   All significant design choices for Engram itself are recorded inside its own Engineering Journal and Decisions.

**Clarifications**:
- **Product name**: Engram
- **Workspace folder**: `.engram/`
- **Core domain objects**: Engineering Activity, Evidence, Engineering Journal Entry, Decision, Knowledge Artifact, Perspective, Relation
- **Private vs public**: `.engram/` is private by default; selective publish of reviewed artifacts to main repo documentation.
- **Project repo vs Engineering Memory workspace**: Git repo for product code; `.engram/` for engineering memory.