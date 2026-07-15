# Architecture Decisions

## ADR-001: Track development effort instead of IDE time

**Status:** Accepted  
**Date:** 2026-07-15

### Context

Modern AI-assisted development includes analysis, agent interaction,
testing, debugging, review, and technical decision-making outside the IDE.

### Decision

DevFlow Tracker will measure project-related development effort rather
than only coding or foreground IDE time.

### Consequences

- Mobile activity may represent valid development work.
- Multiple tools may belong to one semantic work segment.
- Project attribution requires correlated evidence.
- Coding time becomes only one analytical dimension.