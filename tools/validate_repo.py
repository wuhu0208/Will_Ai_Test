#!/usr/bin/env python3
"""Validate repository structure and canonical delivery boundaries."""

from __future__ import annotations

import hashlib
import re
import subprocess
from pathlib import Path

try:
    from .validate_question_bank import validate_question_bank
except ImportError:  # Direct execution: python tools/validate_repo.py
    from validate_question_bank import validate_question_bank


REQUIRED_PATHS = (
    "README.md",
    "AGENTS.md",
    ".gitignore",
    ".github/ISSUE_TEMPLATE/agent-task.yml",
    ".github/ISSUE_TEMPLATE/product-decision.yml",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/workflows/ci.yml",
    "docs/SOURCE_CATALOG.md",
    "docs/agent/CODEX_AUTOMATION.md",
    "docs/agent/REVIEW_AUTOMATION.md",
    "docs/agent/AUTOMATION_CADENCE_POLICY.md",
    "docs/agent/WORKFLOW_STATE_MACHINE.md",
    "docs/agent/RESOURCE_POLICY.md",
    "docs/question-bank/QUESTION_BANK_STANDARD.md",
    "docs/question-bank/SOURCE_TRUTH_STANDARD.md",
    "docs/question-bank/SCORING_STANDARD.md",
    "docs/question-bank/DELIVERY_STANDARD.md",
    "tools/validate_repo.py",
    "tools/validate_question_bank.py",
)
FORBIDDEN_SPLIT_PATTERNS = (
    re.compile(r"_GOLD\.jsonl$", re.IGNORECASE),
    re.compile(r"_TEST_STANDARD\.md$", re.IGNORECASE),
    re.compile(r"_QUESTION_BANK\.md$", re.IGNORECASE),
)
FORBIDDEN_NAMES = {".env", "cookies.json", "cookie.json"}
FORBIDDEN_SUFFIXES = {".pyc", ".pyo", ".zip"}
TEXT_SUFFIXES = {".csv", ".json", ".jsonl", ".md", ".py", ".txt", ".yaml", ".yml"}
SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{40,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
)
WORKFLOW_STATE_LABELS = {
    "accepted",
    "agent-ready",
    "agent-working",
    "blocked",
    "product-decision",
    "repair-needed",
    "waiting-review",
}
SOURCE_CATALOG_HEADER = (
    "| Source PDF | SHA-256 | Pages | Product Scope | "
    "Canonical Question Bank Path | Notes |"
)
SOURCE_CATALOG_ROW_RE = re.compile(
    r"(?m)^\|\s*`(?P<pdf>[^`]+\.pdf)`\s*\|\s*`(?P<sha>[^`]+)`\s*\|"
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_source_catalog(root: Path) -> list[str]:
    errors: list[str] = []
    catalog = root / "docs/SOURCE_CATALOG.md"
    if not catalog.is_file():
        return errors

    text = catalog.read_text(encoding="utf-8")
    if SOURCE_CATALOG_HEADER not in text:
        errors.append(
            "Source Catalog header must contain only stable source metadata; "
            "dynamic Status/Issue/PR columns are forbidden"
        )

    entries: dict[str, str] = {}
    for match in SOURCE_CATALOG_ROW_RE.finditer(text):
        pdf, expected_sha256 = match.group("pdf"), match.group("sha")
        if pdf in entries:
            errors.append(f"duplicate Source Catalog PDF row: {pdf}")
        entries[pdf] = expected_sha256
        if not re.fullmatch(r"[0-9a-f]{64}", expected_sha256):
            errors.append(f"Source Catalog SHA-256 is invalid for {pdf}")

    actual_pdfs = {path.name for path in (root / "doc").glob("*.pdf")}
    missing_catalog = sorted(actual_pdfs - set(entries))
    missing_files = sorted(set(entries) - actual_pdfs)
    if missing_catalog:
        errors.append("PDFs missing from Source Catalog: " + ", ".join(missing_catalog))
    if missing_files:
        errors.append("Source Catalog PDFs missing from doc/: " + ", ".join(missing_files))

    for pdf in sorted(actual_pdfs & set(entries)):
        expected_sha256 = entries[pdf]
        if not re.fullmatch(r"[0-9a-f]{64}", expected_sha256):
            continue
        actual_sha256 = sha256_file(root / "doc" / pdf)
        if expected_sha256 != actual_sha256:
            errors.append(
                f"Source Catalog SHA-256 mismatch for {pdf}: "
                f"expected {expected_sha256}, actual {actual_sha256}"
            )
    return errors


def _tracked_or_present_files(root: Path) -> list[Path]:
    try:
        output = subprocess.run(
            ["git", "ls-files", "-z"],
            cwd=root,
            check=True,
            capture_output=True,
        ).stdout
        if output:
            return [root / item.decode() for item in output.split(b"\0") if item]
    except (OSError, subprocess.CalledProcessError, UnicodeDecodeError):
        pass
    return [path for path in root.rglob("*") if path.is_file()]


def validate_repo(root: Path) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_PATHS:
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")

    files = _tracked_or_present_files(root)
    for path in files:
        relative = path.relative_to(root)
        parts = set(relative.parts)
        if "__pycache__" in parts or path.suffix in {".pyc", ".pyo"}:
            errors.append(f"compiled Python artifact is forbidden: {relative}")
        if path.name in FORBIDDEN_NAMES or path.suffix in FORBIDDEN_SUFFIXES:
            errors.append(f"temporary or sensitive file is forbidden: {relative}")
        if path.name.startswith(".env."):
            errors.append(f"environment file is forbidden: {relative}")
        if path.suffix.lower() in TEXT_SUFFIXES:
            try:
                content = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError):
                errors.append(f"cannot scan text file as UTF-8: {relative}")
            else:
                if any(pattern.search(content) for pattern in SECRET_PATTERNS):
                    errors.append(f"possible secret material is forbidden: {relative}")

    agent_template = root / ".github/ISSUE_TEMPLATE/agent-task.yml"
    if agent_template.is_file():
        template = agent_template.read_text(encoding="utf-8")
        label_lines = re.findall(r"(?m)^labels:\s*(.+)$", template)
        for label_line in label_lines:
            used = {label for label in WORKFLOW_STATE_LABELS if label in label_line}
            if used:
                errors.append(
                    "agent-task template must not auto-apply workflow labels: "
                    + ", ".join(sorted(used))
                )

    bank_dir = root / "question_banks"
    if not bank_dir.is_dir():
        errors.append("missing required directory: question_banks")
    else:
        for path in bank_dir.iterdir():
            if path.name == ".gitkeep":
                continue
            if path.is_dir() or path.suffix.lower() != ".md":
                errors.append(f"question_banks permits only canonical Markdown: {path.name}")
                continue
            if any(pattern.search(path.name) for pattern in FORBIDDEN_SPLIT_PATTERNS):
                errors.append(f"split business deliverable is forbidden: {path.name}")
                continue
            errors.extend(
                f"{path.relative_to(root)}: {error}"
                for error in validate_question_bank(path, root / "doc")
            )

    errors.extend(validate_source_catalog(root))

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate_repo(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Repository validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
