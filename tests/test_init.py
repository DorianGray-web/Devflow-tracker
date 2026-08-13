"""Tests for `engram init` command."""

import os
import subprocess
import tempfile
from pathlib import Path

import pytest

from engram.commands.init import init_command


def _init_git_repo(tmp_path: Path) -> Path:
    """Create a temporary Git repository and return its root."""
    repo = tmp_path / "testrepo"
    repo.mkdir()
    subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.name", "Test User"], cwd=repo, check=True)
    return repo


def test_init_creates_expected_structure(tmp_path):
    """Successful init creates all required files and directories."""
    repo = _init_git_repo(tmp_path)
    original_cwd = Path.cwd()
    os.chdir(repo)
    try:
        exit_code = init_command(dry_run=False, force=False)
        assert exit_code == 0

        engram_dir = repo / ".engram"
        assert engram_dir.exists()
        assert (engram_dir / "README.md").exists()
        assert (engram_dir / "config.json").exists()
        assert (engram_dir / "templates" / "decision.md").exists()
        assert (engram_dir / "templates" / "journal.md").exists()
        assert (engram_dir / "templates" / "evidence.md").exists()
        assert (engram_dir / "decisions" / "0005-minimal-engram-init-workflow.md").exists()
        assert (engram_dir / ".gitignore").exists()
        assert (engram_dir / "evidence" / ".gitkeep").exists()

        # Structural dirs
        assert (engram_dir / "journal").exists()
        assert (engram_dir / "knowledge").exists()

        # Decision file should contain key text
        decision = (engram_dir / "decisions" / "0005-minimal-engram-init-workflow.md").read_text()
        assert "Decision 0005" in decision
        assert "Minimal engram init Workflow" in decision
        assert "Accepted" in decision
    finally:
        os.chdir(original_cwd)


def test_dry_run_creates_no_files(tmp_path):
    """--dry-run must not create any files or directories."""
    repo = _init_git_repo(tmp_path)
    original_cwd = Path.cwd()
    os.chdir(repo)
    try:
        exit_code = init_command(dry_run=True, force=False)
        assert exit_code == 0

        engram_dir = repo / ".engram"
        assert not engram_dir.exists()
    finally:
        os.chdir(original_cwd)


def test_init_refuses_if_already_exists(tmp_path):
    """Init should refuse when .engram/ already exists."""
    repo = _init_git_repo(tmp_path)
    original_cwd = Path.cwd()
    os.chdir(repo)
    try:
        # First init
        assert init_command(dry_run=False, force=False) == 0

        # Second init must fail
        exit_code = init_command(dry_run=False, force=False)
        assert exit_code == 1
        assert (repo / ".engram").exists()
    finally:
        os.chdir(original_cwd)


def test_gitignore_contains_privacy_defaults(tmp_path):
    """The generated .gitignore must protect private content."""
    repo = _init_git_repo(tmp_path)
    original_cwd = Path.cwd()
    os.chdir(repo)
    try:
        init_command(dry_run=False, force=False)
        gitignore = (repo / ".engram" / ".gitignore").read_text()

        assert "config.local.json" in gitignore
        assert "evidence/*" in gitignore or "evidence/" in gitignore
        assert "journal/drafts/" in gitignore or "drafts/" in gitignore
        assert "*.local.*" in gitignore or ".local." in gitignore
    finally:
        os.chdir(original_cwd)


def test_templates_are_created(tmp_path):
    """All three templates must be created with expected placeholder content."""
    repo = _init_git_repo(tmp_path)
    original_cwd = Path.cwd()
    os.chdir(repo)
    try:
        init_command(dry_run=False, force=False)
        engram = repo / ".engram"

        decision_t = (engram / "templates" / "decision.md").read_text()
        assert "Decision {{id}}" in decision_t
        assert "Perspectives" in decision_t

        journal_t = (engram / "templates" / "journal.md").read_text()
        assert "Engineering Journal Entry" in journal_t
        assert "{{type}}" in journal_t

        evidence_t = (engram / "templates" / "evidence.md").read_text()
        assert "Evidence {{id}}" in evidence_t
        assert "Raw Content" in evidence_t
    finally:
        os.chdir(original_cwd)


def test_decision_0005_is_created(tmp_path):
    """The bootstrap decision 0005 must be written with correct content."""
    repo = _init_git_repo(tmp_path)
    original_cwd = Path.cwd()
    os.chdir(repo)
    try:
        init_command(dry_run=False, force=False)
        decision_path = repo / ".engram" / "decisions" / "0005-minimal-engram-init-workflow.md"
        content = decision_path.read_text()

        assert "Decision 0005" in content
        assert "Minimal engram init Workflow" in content
        assert "chicken-and-egg problem" in content
        assert "ENG_INIT_DESIGN.md" in content
    finally:
        os.chdir(original_cwd)


def test_fails_outside_git_repo_without_force(tmp_path):
    """Command must fail clearly when not inside a Git repository."""
    non_git = tmp_path / "nongit"
    non_git.mkdir()
    original_cwd = Path.cwd()
    os.chdir(non_git)
    try:
        exit_code = init_command(dry_run=False, force=False)
        assert exit_code == 1
        assert not (non_git / ".engram").exists()
    finally:
        os.chdir(original_cwd)


def test_force_allows_non_git(tmp_path):
    """--force should allow init outside Git (with warning)."""
    non_git = tmp_path / "nongit"
    non_git.mkdir()
    original_cwd = Path.cwd()
    os.chdir(non_git)
    try:
        exit_code = init_command(dry_run=False, force=True)
        assert exit_code == 0
        assert (non_git / ".engram").exists()
    finally:
        os.chdir(original_cwd)
