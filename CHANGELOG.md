# Changelog

All notable changes to the DevFlow Tracker project will be documented
in this file.

The project is currently in the concept and pre-MVP stage.

## [Unreleased]

### Added

- Initial project concept and problem definition.
- Initial activity model.
- Definition of development effort beyond direct code editing.
- Support concept for AI-assisted and agentic development workflows.
- Multi-application activity context.
- Multi-window and multi-monitor workspace concept.
- Cross-device project activity concept.
- Separation between human development effort and agent execution time.
- AI conversation-to-project linking concept.
- Metadata-first privacy principle.

### Changed

- Replaced the original flat `Project Session → Activity Event` model
  with a richer model containing semantic work segments and correlated
  activity evidence.
- Expanded project scope from IDE time tracking to project-oriented
  development effort tracking across tools and devices.
- Refined project attribution to use correlated signals rather than
  foreground application time alone.

### Known Design Questions

- How should semantic work segments be inferred without reading private
  project content?
- How should concurrent activity across multiple devices be merged?
- How should mobile AI conversation activity be linked to a project?
- How should human effort, agent runtime, and overlap be reported?
- How should session boundaries be detected automatically?