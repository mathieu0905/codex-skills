#!/usr/bin/env python3
"""Create a reference authenticity audit workspace."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path


FILES = {
    "00-audit-protocol.md": """# Reference Audit Protocol

- Source: {source}
- Created: {created}
- Requested scope:
- Manuscript files:
- Bibliography files:
- External sources checked:

## Evidence Rules

- Do not verify from memory alone.
- Record every source used for verification.
- Separate existence, metadata accuracy, and citation support.
- Preserve uncertainty with `unverified` or `ambiguous` when evidence is incomplete.
""",
    "01-reference-inventory.csv": """key,index,raw_reference,title,authors,year,venue,doi,arxiv_id,url,entry_type,cited,status,notes
""",
    "02-citation-contexts.csv": """citation_key,location,section,sentence_or_claim,paragraph_context,appears_to_support,needs_source_check,notes
""",
    "03-verification-log.md": """# Verification Log

Add one section per reference. Keep raw evidence here so the final report can stay concise.

## Template

### Key:

- Current metadata:
- Search/source trail:
- Best matching external record:
- Metadata comparison:
- Evidence level:
- Notes:
""",
    "04-mismatch-report.md": """# Metadata And Authenticity Mismatches

| Key | Status | Problem | Evidence source | Recommended action |
| --- | --- | --- | --- | --- |
""",
    "05-citation-support-report.md": """# Citation Support Report

| Citation | Location | Manuscript claim | Source support level | Problem | Recommended action |
| --- | --- | --- | --- | --- | --- |
""",
    "06-final-reference-audit.md": """# Final Reference Audit

## Summary

- References checked:
- Verified:
- Metadata mismatch:
- Citation misuse:
- Ambiguous:
- Unverified:
- Not found:

## Highest-Risk Items

- 

## Required Author Actions

- 

## Notes On Limits

- 
""",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create files for a reference authenticity audit."
    )
    parser.add_argument(
        "--source",
        required=True,
        help="Manuscript, bibliography path, or short source label.",
    )
    parser.add_argument(
        "--out",
        default="reference-authenticity-audit",
        help="Output directory for the audit workspace.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing audit files in the output directory.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    out_dir = Path(args.out).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    created = datetime.now().astimezone().isoformat(timespec="seconds")
    written: list[Path] = []
    skipped: list[Path] = []

    for name, template in FILES.items():
        path = out_dir / name
        if path.exists() and not args.force:
            skipped.append(path)
            continue
        path.write_text(
            template.format(source=args.source, created=created),
            encoding="utf-8",
        )
        written.append(path)

    print(f"Reference audit workspace: {out_dir}")
    if written:
        print("Written:")
        for path in written:
            print(f"  - {path.name}")
    if skipped:
        print("Skipped existing files, use --force to overwrite:")
        for path in skipped:
            print(f"  - {path.name}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
