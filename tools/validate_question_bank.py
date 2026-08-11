#!/usr/bin/env python3
"""Validate a canonical one-PDF-one-Markdown question bank."""

from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path


FRONT_MATTER_KEYS = (
    "schema_version",
    "source_pdf",
    "source_sha256",
    "source_pages",
    "question_bank_version",
    "product_scope",
)
FORBIDDEN_WORKFLOW_KEYS = ("status", "workflow_status", "lifecycle_status")
DOCUMENT_SECTIONS = (
    "## 1. Source Information",
    "## 2. Scope",
    "## 3. Question Statistics",
    "## 4. Questions",
)
QUESTION_SECTIONS = (
    "Target",
    "Question",
    "Standard Answer",
    "Scoring Standard",
    "Accepted Variants",
    "Forbidden Errors",
    "Tolerance",
    "Source",
)
SOURCE_FIELDS = (
    "PDF",
    "Physical page",
    "Printed page",
    "Section",
    "Local scope path",
    "Evidence type",
    "Evidence",
)
QUESTION_ID_RE = re.compile(r"(?m)^## ([A-Z0-9_-]+-Q-\d{4})\s*$")
POINT_RE = re.compile(r"(?m)^- P(\d+) \[(\d+)]\s*:\s*(\S.*)$")
HASH_RE = re.compile(r"^[0-9a-f]{64}$")
TARGET_BINDINGS = "EXACT_MODEL|MODEL_FAMILY|PRODUCT_SERIES|DOCUMENT_COMMON"
PLACEHOLDER_VALUES = {"n/a", "na", "none", "tbd", "..."}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_front_matter(text: str) -> tuple[dict[str, str], str, list[str]]:
    errors: list[str] = []
    if not text.startswith("---\n"):
        return {}, text, ["missing opening front matter delimiter"]
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text, ["missing closing front matter delimiter"]
    values: dict[str, str] = {}
    for line_number, line in enumerate(text[4:end].splitlines(), start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            errors.append(f"front matter line {line_number} is not key: value")
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip().strip('"\'')
        if key in values:
            errors.append(f"duplicate front matter key: {key}")
        values[key] = value
    return values, text[end + 5 :], errors


def _section_body(block: str, heading: str) -> str | None:
    pattern = re.compile(
        rf"(?ms)^### {re.escape(heading)}\s*$\n(.*?)(?=^### |\Z)"
    )
    match = pattern.search(block)
    return match.group(1).strip() if match else None


def validate_question_bank(
    path: Path, source_root: Path | None = None
) -> list[str]:
    errors: list[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"cannot read UTF-8 Markdown: {exc}"]

    front, body, front_errors = parse_front_matter(text)
    errors.extend(front_errors)
    for key in FRONT_MATTER_KEYS:
        if not front.get(key):
            errors.append(f"missing front matter field: {key}")
    for key in FORBIDDEN_WORKFLOW_KEYS:
        if key in front:
            errors.append(
                f"front matter workflow field is forbidden: {key}; use GitHub labels"
            )

    if front.get("schema_version") not in (None, "will-ai-question-bank/v1"):
        errors.append("schema_version must be will-ai-question-bank/v1")
    if front.get("source_sha256") and not HASH_RE.fullmatch(front["source_sha256"]):
        errors.append("source_sha256 must be 64 lowercase hexadecimal characters")
    if front.get("source_pages"):
        try:
            if int(front["source_pages"]) <= 0:
                raise ValueError
        except ValueError:
            errors.append("source_pages must be a positive integer")
    source_pdf = front.get("source_pdf")
    if source_pdf:
        if not source_pdf.endswith(".pdf"):
            errors.append("source_pdf must end in .pdf")
        if path.stem != Path(source_pdf).stem:
            errors.append("question-bank filename stem must match source_pdf stem")
        if source_root is not None:
            source_path = source_root / source_pdf
            if not source_path.is_file():
                errors.append(f"source PDF does not exist: {source_path}")
            elif front.get("source_sha256") and HASH_RE.fullmatch(
                front["source_sha256"]
            ):
                actual_sha256 = sha256_file(source_path)
                if front["source_sha256"] != actual_sha256:
                    errors.append(
                        "source_sha256 does not match actual source PDF: "
                        f"expected {front['source_sha256']}, actual {actual_sha256}"
                    )

    positions = []
    for section in DOCUMENT_SECTIONS:
        position = body.find(section)
        if position < 0:
            errors.append(f"missing document section: {section}")
        positions.append(position)
    present_positions = [position for position in positions if position >= 0]
    if present_positions != sorted(present_positions):
        errors.append("document sections are out of order")

    matches = list(QUESTION_ID_RE.finditer(body))
    if not matches:
        errors.append("no question IDs found")
        return errors
    ids = [match.group(1) for match in matches]
    duplicates = sorted({question_id for question_id in ids if ids.count(question_id) > 1})
    if duplicates:
        errors.append(f"duplicate question IDs: {', '.join(duplicates)}")

    for index, match in enumerate(matches):
        question_id = match.group(1)
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        block = body[match.end() : end]
        section_bodies: dict[str, str] = {}
        for heading in QUESTION_SECTIONS:
            section_body = _section_body(block, heading)
            if section_body is None:
                errors.append(f"{question_id}: missing section {heading}")
            elif not section_body:
                errors.append(f"{question_id}: empty section {heading}")
            else:
                section_bodies[heading] = section_body

        target = section_bodies.get("Target", "")
        if target:
            binding_match = re.search(
                rf"(?m)^- Binding:\s*({TARGET_BINDINGS})\s*$", target
            )
            if not binding_match:
                errors.append(f"{question_id}: Target requires a valid Binding")

            target_values: dict[str, str] = {}
            for field in ("Product", "Model / Scope"):
                field_match = re.search(
                    rf"(?m)^- {re.escape(field)}:\s*(\S.*)$", target
                )
                if not field_match:
                    errors.append(f"{question_id}: Target requires non-empty {field}")
                    continue
                value = field_match.group(1).strip()
                if value.lower() in PLACEHOLDER_VALUES:
                    errors.append(f"{question_id}: Target {field} cannot be a placeholder")
                target_values[field] = value

            if binding_match and binding_match.group(1) == "DOCUMENT_COMMON":
                model_scope = target_values.get("Model / Scope", "")
                document, separator, scope = model_scope.partition("::")
                if (
                    not separator
                    or not source_pdf
                    or document.strip() != source_pdf
                    or not scope.strip()
                    or scope.strip().lower() in PLACEHOLDER_VALUES
                ):
                    errors.append(
                        f"{question_id}: DOCUMENT_COMMON Model / Scope must be "
                        "<source_pdf> :: <document or local scope>"
                    )

        scoring = section_bodies.get("Scoring Standard", "")
        if scoring:
            points = POINT_RE.findall(scoring)
            if not points:
                errors.append(f"{question_id}: no Required Points found")
            else:
                point_ids = [point_id for point_id, _, _ in points]
                if len(point_ids) != len(set(point_ids)):
                    errors.append(f"{question_id}: duplicate Required Point IDs")
                total = sum(int(weight) for _, weight, _ in points)
                if total != 100:
                    errors.append(
                        f"{question_id}: Required Point weights sum to {total}, expected 100"
                    )

        source = section_bodies.get("Source", "")
        for field in SOURCE_FIELDS:
            if source and not re.search(rf"(?m)^- {re.escape(field)}:\s*\S.*$", source):
                errors.append(f"{question_id}: missing Source field {field}")
        if source_pdf and source:
            match_pdf = re.search(r"(?m)^- PDF:\s*(\S.*?)\s*$", source)
            if match_pdf and match_pdf.group(1) != source_pdf:
                errors.append(f"{question_id}: Source PDF does not match front matter")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--source-root", type=Path, default=Path("doc"))
    args = parser.parse_args()

    failed = False
    for path in args.paths:
        errors = validate_question_bank(path, args.source_root)
        if errors:
            failed = True
            for error in errors:
                print(f"ERROR {path}: {error}")
        else:
            print(f"OK {path}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
