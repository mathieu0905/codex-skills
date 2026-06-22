#!/usr/bin/env python3
"""Create an article logic audit workspace."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path


FILES = {
    "00-reading-protocol.md": """# Reading Protocol

- Source: {source}
- Created: {created}
- Requested edit depth:
- Target audience:
- Article genre:
- Output expected by user:

## Rules

- Read from front to back before rewriting.
- Mark hypotheses as hypotheses until confirmed by later text.
- Record logical issues before proposing edits.
- Tie every major edit to an audit entry.
""",
    "01-global-map.md": """# Global Map

## Provisional Thesis


## Reader And Stakes


## Article Promise


## Section Jobs

| Section | Apparent job | Depends on | Sets up | Confidence |
| --- | --- | --- | --- | --- |

## Terms And Claims To Track

- 

## Open Questions

- 
""",
    "02-forward-reading-log.md": """# Forward Reading Log

Read in document order. Add one row per paragraph or paragraph group.

| Location | Paragraph job | Depends on earlier text | Introduces for later | Issue observed | Severity |
| --- | --- | --- | --- | --- | --- |
""",
    "03-concept-ledger.md": """# Concept Ledger

| Concept | First mention | First definition | Prerequisites | Later usage | Issue | Fix |
| --- | --- | --- | --- | --- | --- | --- |
""",
    "04-claim-evidence-ledger.md": """# Claim-Evidence Ledger

| Claim | Location | Evidence or reasoning | Support status | Scope problem | Contradiction | Fix |
| --- | --- | --- | --- | --- | --- | --- |
""",
    "05-method-limitation-ledger.md": """# Method-Limitation Ledger

| Method/design choice | Problem addressed | Evidence coverage | Limitation | Match status | Required revision |
| --- | --- | --- | --- | --- | --- |
""",
    "06-revision-plan.md": """# Revision Plan

## P0: Argument Integrity

- 

## P1: Structure And Sequence

- 

## P2: Local Coherence

- 

## P3: Style

- 

## Planned Edit Trace

| Edit | Audit evidence | Expected effect | Risk |
| --- | --- | --- | --- |
""",
    "07-final-consistency-pass.md": """# Final Consistency Pass

| Check | Pass/Fail | Notes |
| --- | --- | --- |
| Concepts introduced before use |  |  |
| Terminology stable |  |  |
| Contributions supported by method/evidence/results |  |  |
| Limitations match method and evidence scope |  |  |
| Conclusion avoids overclaiming |  |  |
| No new contradictions introduced |  |  |
| Transitions reflect real logical relationships |  |  |

## Remaining Author Decisions

- 
""",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create markdown ledgers for a whole-article logic audit."
    )
    parser.add_argument(
        "--source",
        required=True,
        help="Article path, title, or short source label.",
    )
    parser.add_argument(
        "--out",
        default="article-logic-audit",
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

    print(f"Audit workspace: {out_dir}")
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
