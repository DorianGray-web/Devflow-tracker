# FAQ

**Why not just use Obsidian / Notion / Logseq?**  
Those are general knowledge tools. Engram is purpose-built for software engineering lifecycles, with first-class concepts for Engineering Activities, Evidence, Engineering Journal Entries, Decisions, multi-AI Perspectives, and explicit Relations to Git commits, releases, and code. It lives inside the project repository as a sibling to the code (`.engram/` workspace).

**Why not just write ADRs?**  
ADRs are excellent but narrow. Engram’s Engineering Journal Entries and Decision records are richer, support Evidence from multiple AI Perspectives, preserve rejected decisions, link to Activities and (later) telemetry, and provide a full searchable history of how knowledge evolved.

**Is this another time tracker?**  
No. While duration is one optional attribute of an Engineering Activity, the primary goal is preserving engineering reasoning, Decisions, and making “why” and “how did we get here?” questions instantly answerable. Time tracking is deliberately deprioritized for v0.1–v0.2.

**Will it send my data to the cloud?**  
No. Engram is local-first and privacy-respecting by design. The `.engram/` workspace is private by default. Optional selective publishing of reviewed public Journal entries, Decisions, and Knowledge Artifacts is under full user control.

**How does it handle multiple AI models?**  
Each AI conversation is stored as Evidence tagged with the model and Perspective. Multiple (even conflicting) viewpoints can coexist until a reviewed Decision or Engineering Journal Entry synthesizes them. This multi-perspective history is preserved.

**How does it distinguish Evidence from Knowledge?**  
Strictly. Raw AI chats, notes, and logs are imported as Evidence. Only after explicit human review and approval do insights become Engineering Journal Entries, Decisions, or Knowledge Artifacts. This is a core principle (**Evidence before Knowledge**).

**What about rejected decisions?**  
They are first-class. Preserving them prevents repeating the same discussion when conditions have not materially changed.

**What is the license?**  
MIT (see LICENSE).

**Clarifications**:
- **Product name**: Engram
- **Workspace folder**: `.engram/`
- **Core domain objects**: Engineering Activity, Evidence, Engineering Journal Entry, Decision, Knowledge Artifact, Perspective, Relation
- **Private vs public**: `.engram/` is private by default; selective publish to main repo docs.
- **Project repo vs Engineering Memory workspace**: Git repo for product code; `.engram/` for engineering memory.

More questions will be added to this file as they arise — each answer will be backed by a linked Journal entry or Decision in the project’s own `.engram/` workspace.