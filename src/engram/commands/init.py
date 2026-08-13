"""Implementation of `engram init` command."""

import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict

# --- File contents (derived from ENG_INIT_DESIGN.md) ---

README_CONTENT = """# .engram Workspace

This directory is the **engineering memory workspace** for this Git repository.

It stores:
- Decisions (with context, alternatives, rationale)
- Engineering Journal Entries
- Raw Evidence (AI conversations, logs, notes — requires review)
- Templates for consistent recording

## Privacy

Raw evidence, personal drafts, and local configuration are kept private by default
(see `.engram/.gitignore`).

Only reviewed and curated content should be committed.

## Usage

- `engram init` (already done)
- Future: `engram journal`, `engram decide`, `engram import`, etc.

The source of truth stays in `.engram/`. Curated content can later be selectively
published to the main repository documentation.

See `DECISIONS.md` (pre-init) and `.engram/decisions/` for the project's own decisions.
"""

CONFIG_CONTENT = """{
  "version": "0.1",
  "created_at": null,
  "project": null,
  "default_perspective": "human"
}
"""

TEMPLATE_DECISION = """# Decision {{id}} – {{title}}

**Status**: {{status}} (Accepted | Rejected | Superseded)
**Date**: {{date}}
**Related**: [Journal-{{link}}], Evidence-{{link}}

## Context
{{context}}

## Alternatives Considered
{{alternatives}}

## Decision
{{decision}}

## Rationale
{{rationale}}

## Consequences
{{consequences}}

## Evidence
- Links to raw Evidence files

**Perspectives**:
- Human: ...
- AI (Model-Name): ...
"""

TEMPLATE_JOURNAL = """# Engineering Journal Entry – {{date}} – {{title}}

**Type**: {{type}} (Research | Architecture | Debugging | AI Brainstorm | etc.)
**Duration**: {{hours}}h
**Related Decisions**: ...

## Problem / Context
...

## Discussion & Perspectives
...

## Insights / Outcomes
...

## Next Actions
- ...

**Linked Evidence**:
- ...

**Knowledge Artifacts Updated**:
"""

TEMPLATE_EVIDENCE = """# Evidence {{id}} – {{title}}

**Source**: {{source}} (AI Chat | Log | Meeting | etc.)
**Date**: {{date}}
**Linked To**: Decision-{{id}} | Journal-{{id}}

## Raw Content
...
"""

GITIGNORE_CONTENT = """# Engram privacy defaults
# Do not commit raw data or user-specific files

# Local configuration
config.local.json

# Raw evidence (AI chats, logs, screenshots, etc.)
evidence/*
!evidence/.gitkeep

# Unreviewed journal drafts
journal/drafts/

# Any local variants
**/*.local.*
"""

EVIDENCE_GITKEEP = "# This file keeps the evidence/ directory in Git.\n# Actual evidence files are ignored.\n"

DECISION_0005_CONTENT = """# Decision 0005 – Minimal engram init Workflow

**Status**: Accepted
**Date**: 2026-08-13
**Related**: 

## Context
The first product value is not automation, but creating a consistent engineering memory structure beside an existing project. Before any CLI existed, design decisions were tracked in the root `DECISIONS.md`. A proper `engram init` command is needed to bootstrap the `.engram/` workspace with the correct structure, privacy rules, and first decision record.

## Alternatives Considered
- Start with full AI importers, telemetry, or cloud sync immediately.
- Use a general note-taking tool (Obsidian, Logseq) without project-specific structure.
- Put everything directly in the main repo docs/ folder.

## Decision
Implement a minimal, local-first `engram init` command that:
- Detects the Git repository root.
- Creates the exact `.engram/` structure defined in ENG_INIT_DESIGN.md.
- Creates only tracked-safe files (templates, config.json, README, .gitignore, first decision).
- Does not create any user-specific config (config.local.json is never written by init).
- Enforces privacy via `.engram/.gitignore` for evidence, drafts, and config.local.json.
- Supports `--dry-run` and refuses to overwrite existing `.engram/`.

No raw evidence files or user-specific config are created.

## Rationale
This solves the chicken-and-egg problem: we can now record engineering rationale using the same tool we are building. It enforces "Evidence before Knowledge" from day one and makes the project self-documenting. All future decisions will live in `.engram/decisions/`.

## Consequences
- The root `DECISIONS.md` becomes a historical bootstrap document.
- After init, new decisions must be created as individual files in `.engram/decisions/`.
- Future commands (`journal`, `decide`, etc.) will operate inside this structure.
- Raw/private data stays out of the main repository history by default.

## Evidence
- ENG_INIT_DESIGN.md
- DOMAIN_MODEL.md
- Pre-init DECISIONS.md

**Perspectives**:
- Human: Initial design and implementation of the bootstrap command.
- AI: Assisted with structure, templates, and consistency with design docs.
"""


def get_git_root() -> Path:
    """Return the root of the current Git repository."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            check=True,
            cwd=Path.cwd(),
        )
        return Path(result.stdout.strip())
    except (subprocess.CalledProcessError, FileNotFoundError, OSError):
        raise RuntimeError(
            "Not inside a Git repository. "
            "Run 'git init' first, or use --force (not recommended)."
        )


def _build_files_to_create() -> Dict[str, str]:
    """Return mapping of relative paths (inside .engram/) to their content."""
    files: Dict[str, str] = {
        "README.md": README_CONTENT,
        "config.json": CONFIG_CONTENT,
        "templates/decision.md": TEMPLATE_DECISION,
        "templates/journal.md": TEMPLATE_JOURNAL,
        "templates/evidence.md": TEMPLATE_EVIDENCE,
        "decisions/0005-minimal-engram-init-workflow.md": DECISION_0005_CONTENT,
        ".gitignore": GITIGNORE_CONTENT,
        "evidence/.gitkeep": EVIDENCE_GITKEEP,
    }
    return files


def init_command(dry_run: bool = False, force: bool = False) -> int:
    """Create the .engram/ workspace or simulate it."""
    root: Path
    try:
        root = get_git_root()
    except RuntimeError as exc:
        if force:
            root = Path.cwd()
            print("Warning: --force used. Initializing outside of a detected Git repository.")
        else:
            print(f"Error: {exc}")
            return 1

    engram_dir = root / ".engram"

    if engram_dir.exists():
        print("Error: .engram/ already exists in this repository.")
        print("       Remove it or use a different location. (Future: engram status)")
        return 1

    files = _build_files_to_create()

    if dry_run:
        print("Dry run — no files will be written.")
        print(f"Would create .engram/ at: {engram_dir}")
        print("Files and directories:")
        for rel_path in sorted(files.keys()):
            print(f"  .engram/{rel_path}")
        # Also note empty structural dirs
        print("  .engram/journal/ (empty)")
        print("  .engram/knowledge/ (empty)")
        return 0

    # Actually create
    engram_dir.mkdir(parents=True, exist_ok=False)

    for rel_path, content in files.items():
        target = engram_dir / rel_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

    # Ensure structural empty directories exist (for future use)
    (engram_dir / "journal").mkdir(exist_ok=True)
    (engram_dir / "knowledge").mkdir(exist_ok=True)

    print(f"Initialized Engram workspace at {engram_dir}")
    print("Created:")
    for rel_path in sorted(files.keys()):
        print(f"  .engram/{rel_path}")
    print("\nNext steps: review .engram/decisions/0005-minimal-engram-init-workflow.md")
    return 0


if __name__ == "__main__":
    sys.exit(init_command())
