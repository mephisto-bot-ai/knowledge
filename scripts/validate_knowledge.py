#!/usr/bin/env python3
"""Validate the machine-readable governance layer of the knowledge base."""
from __future__ import annotations

import pathlib
import re
import sys
from datetime import date

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def load_yaml(path: pathlib.Path, key: str) -> list[dict]:
    if not path.exists():
        ERRORS.append(f"missing required registry: {path.relative_to(ROOT)}")
        return []
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    entries = data.get(key, [])
    if not isinstance(entries, list):
        ERRORS.append(f"{path.relative_to(ROOT)}: '{key}' must be a list")
        return []
    return entries


def parse_frontmatter(path: pathlib.Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        ERRORS.append(f"{path.relative_to(ROOT)}: missing frontmatter")
        return {}
    try:
        end = text.index("\n---", 4)
    except ValueError:
        ERRORS.append(f"{path.relative_to(ROOT)}: unterminated frontmatter")
        return {}
    data = yaml.safe_load(text[4:end]) or {}
    return data if isinstance(data, dict) else {}


def main() -> int:
    claims = load_yaml(ROOT / "claims/registry.yaml", "claims")
    gaps = load_yaml(ROOT / "gaps/registry.yaml", "gaps")
    conflicts = load_yaml(ROOT / "conflicts/registry.yaml", "conflicts")

    claim_ids: set[str] = set()
    for claim in claims:
        cid = claim.get("id")
        if not cid or cid in claim_ids:
            ERRORS.append(f"claims/registry.yaml: missing or duplicate claim id: {cid!r}")
        claim_ids.add(cid)
        if not claim.get("note") or not claim.get("text"):
            ERRORS.append(f"claim {cid!r}: note and text are required")
        if claim.get("status") in {"active", "disputed"} and not claim.get("evidence"):
            ERRORS.append(f"claim {cid!r}: active/disputed claims need evidence")
        confidence = claim.get("confidence")
        if not isinstance(confidence, (int, float)) or not 0 <= confidence <= 1:
            ERRORS.append(f"claim {cid!r}: confidence must be between 0 and 1")
        for evidence in claim.get("evidence", []) or []:
            if not evidence.get("url") or not evidence.get("accessed"):
                ERRORS.append(f"claim {cid!r}: each evidence item needs url and accessed")

    gap_ids: set[str] = set()
    for gap in gaps:
        gid = gap.get("id")
        if not gid or gid in gap_ids:
            ERRORS.append(f"gaps/registry.yaml: missing or duplicate gap id: {gid!r}")
        gap_ids.add(gid)
        required = ["topic", "type", "priority", "status", "requested_outcome", "acceptance_criteria"]
        for field in required:
            if not gap.get(field):
                ERRORS.append(f"gap {gid!r}: {field} is required")
        if gap.get("status") in {"claimed", "in-progress"} and not gap.get("owner"):
            ERRORS.append(f"gap {gid!r}: claimed or in-progress gaps need an owner")

    for conflict in conflicts:
        fid = conflict.get("id")
        linked = conflict.get("claims", []) or []
        if not fid or len(linked) < 2:
            ERRORS.append(f"conflict {fid!r}: id and at least two claim IDs are required")
        unknown = [cid for cid in linked if cid not in claim_ids]
        if unknown:
            ERRORS.append(f"conflict {fid!r}: unknown claim IDs: {', '.join(unknown)}")
        if conflict.get("status") == "resolved" and not conflict.get("resolution"):
            ERRORS.append(f"conflict {fid!r}: resolved conflicts need a resolution")

    for note_path in sorted((ROOT / "wiki").rglob("*.md")):
        frontmatter = parse_frontmatter(note_path)
        for cid in frontmatter.get("claim_ids", []) or []:
            if cid not in claim_ids:
                ERRORS.append(f"{note_path.relative_to(ROOT)}: unknown claim_id {cid!r}")
        updated = frontmatter.get("updated")
        if updated and isinstance(updated, date) and updated > date.today():
            ERRORS.append(f"{note_path.relative_to(ROOT)}: updated date is in the future")

    if ERRORS:
        print("Knowledge governance validation failed:")
        print("\n".join(f"- {error}" for error in ERRORS))
        return 1

    print(f"Knowledge governance validation passed: {len(claims)} claims, {len(gaps)} gaps, {len(conflicts)} conflicts.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
