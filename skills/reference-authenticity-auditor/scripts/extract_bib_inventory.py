#!/usr/bin/env python3
"""Extract a simple reference inventory from BibTeX-like files."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


ENTRY_START_RE = re.compile(r"@(?P<type>[A-Za-z]+)\s*\{\s*(?P<key>[^,\s]+)\s*,")
FIELD_RE = re.compile(
    r"(?P<name>[A-Za-z][A-Za-z0-9_-]*)\s*=\s*(?P<value>\{(?:[^{}]|\{[^{}]*\})*\}|\"(?:[^\"\\]|\\.)*\"|[^,\n]+)\s*,?",
    re.DOTALL,
)


def strip_wrapping(value: str) -> str:
    value = value.strip().rstrip(",").strip()
    if len(value) >= 2 and ((value[0] == "{" and value[-1] == "}") or (value[0] == '"' and value[-1] == '"')):
        value = value[1:-1]
    value = re.sub(r"\s+", " ", value)
    value = value.replace("\\&", "&")
    return value.strip()


def iter_entries(text: str):
    pos = 0
    while True:
        match = ENTRY_START_RE.search(text, pos)
        if not match:
            break
        start = match.start()
        body_start = match.end()
        depth = 1
        i = body_start
        while i < len(text) and depth:
            char = text[i]
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
            i += 1
        raw = text[start:i]
        body = text[body_start : i - 1]
        fields = {}
        for field in FIELD_RE.finditer(body):
            fields[field.group("name").lower()] = strip_wrapping(field.group("value"))
        yield {
            "key": match.group("key").strip(),
            "entry_type": match.group("type").lower(),
            "raw": re.sub(r"\s+", " ", raw).strip(),
            "fields": fields,
        }
        pos = i


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract BibTeX entries into a CSV reference inventory."
    )
    parser.add_argument("bib", help="Path to a .bib or BibTeX-like file.")
    parser.add_argument("--out", required=True, help="Output CSV path.")
    args = parser.parse_args()

    bib_path = Path(args.bib).expanduser()
    out_path = Path(args.out).expanduser()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    text = bib_path.read_text(encoding="utf-8", errors="replace")
    entries = list(iter_entries(text))

    fieldnames = [
        "key",
        "index",
        "raw_reference",
        "title",
        "authors",
        "year",
        "venue",
        "doi",
        "arxiv_id",
        "url",
        "entry_type",
        "cited",
        "status",
        "notes",
    ]

    with out_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for index, entry in enumerate(entries, start=1):
            fields = entry["fields"]
            venue = (
                fields.get("booktitle")
                or fields.get("journal")
                or fields.get("publisher")
                or fields.get("institution")
                or ""
            )
            writer.writerow(
                {
                    "key": entry["key"],
                    "index": index,
                    "raw_reference": entry["raw"],
                    "title": fields.get("title", ""),
                    "authors": fields.get("author", ""),
                    "year": fields.get("year", ""),
                    "venue": venue,
                    "doi": fields.get("doi", ""),
                    "arxiv_id": fields.get("eprint", ""),
                    "url": fields.get("url", ""),
                    "entry_type": entry["entry_type"],
                    "cited": "",
                    "status": "",
                    "notes": "",
                }
            )

    print(f"Wrote {len(entries)} entries to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
