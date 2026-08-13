# Engram

> Engineering Memory Platform for software projects and AI-assisted development.

## Project Status

Concept / Pre-MVP (Documentation refined)

## Project Inception

2025-07-15 (updated from original placeholder)

## 1. Problem

Traditional tools capture *what* changed (Git), *what was released* (CHANGELOG), or *how long* someone typed (time trackers). They lose the *why*: the reasoning, rejected alternatives, multi-perspective debates (human + AI), evidence that led to decisions, and how knowledge evolved.

In modern AI-assisted and agentic workflows this invisible work is even larger. Knowledge evaporates when people or models change.

## 2. Solution

Engram provides a lightweight, local-first `.engram/` workspace that lives alongside any Git repository without polluting the product code.

It records:
- Engineering Activities
- Evidence (from multiple AI Perspectives)
- Curated Engineering Journal Entries
- Decisions (accepted, rejected, superseded)
- Knowledge Artifacts
- Explicit Relations to commits, releases, and code

The Engineering Journal becomes the searchable memory of the project, answering questions such as “Why was this decision made?” or “When did this idea first appear and how did it evolve?”

## 3. Core Principle

**Evidence before Knowledge**: Conversation and raw AI output are evidence, not knowledge. Only after human review and approval do extracted insights become permanent Engineering Journal Entries, Decisions, or Knowledge Artifacts.

Time is merely one attribute of an Engineering Activity. The primary goal is preserving and making accessible the engineering reasoning across the full project lifecycle.

## 4. How Engram Complements Existing Tools

- **Git repository**: product code and commit history (the *what*).
- **CHANGELOG / Releases**: user-visible changes.
- **ADRs**: selected architectural decisions (Engram’s Journal and Decisions are richer, include evidence + rejected options).
- **Jira / Linear**: tasks and execution tracking.
- **Obsidian / Notion / Logseq**: general notes (Engram is purpose-built for engineering memory with first-class links to code).
- **AI chats**: raw conversations (imported as Evidence only; reviewed parts become Journal).

Engram does not replace any of them. It provides the missing engineering memory layer.

## 5. Naming Decision

The original name “DevFlow Tracker” no longer fits. The product is **Engram** — a persistent trace of engineering memory. The workspace folder is `.engram/`.

All future design decisions will be recorded inside the project’s own `.engram/` workspace once initialized.

See `VISION.md`, `MISSION.md`, `DESIGN_PRINCIPLES.md`, `DOMAIN_MODEL.md`, `ENGINEERING_MODEL.md`, `ARCHITECTURE.md`, and `ROADMAP.md` for the full foundation.

This document will be superseded by richer Journal entries as the project matures.