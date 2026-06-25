---
name: reference-authenticity-auditor
description: Audit academic references and citations for authenticity, metadata accuracy, and claim support. Use when Codex is asked to verify whether references are real, detect fabricated or hallucinated citations, check BibTeX or bibliography entries, validate DOI/title/author/year/venue consistency, inspect citation contexts, confirm that cited papers support manuscript claims, or prepare a reference-integrity report for LaTeX, Markdown, Word, PDF, BibTeX, RIS, CSL JSON, or plain-text manuscripts.
---

# Reference Authenticity Auditor

## Overview

Use this skill to verify that references exist, are described accurately, and are cited for claims they actually support. Treat the task as evidence collection, not bibliography formatting.

## Core Rules

- Do not mark a reference as real from memory alone. Use an external bibliographic source, publisher page, DOI resolver, official proceedings page, arXiv/OpenReview page, Semantic Scholar/OpenAlex/Crossref metadata, or the paper PDF.
- Distinguish existence from correctness. A real paper can still have wrong authors, year, venue, title, DOI, page range, or claim usage.
- Distinguish reference authenticity from citation support. A citation can point to a real paper but fail to support the sentence where it is used.
- Preserve uncertainty. Use `unverified` when sources are incomplete, paywalled, ambiguous, or conflicting.
- Prefer primary or bibliographic authority sources over search snippets. Search results are leads, not proof.
- Never invent missing metadata. If a field cannot be verified, mark it missing or uncertain.

## Evidence Levels

Use exactly these status labels:

- `verified`: the work exists and key metadata match a credible source.
- `metadata-mismatch`: the work exists but one or more important fields disagree.
- `citation-misuse`: the cited work exists, but the manuscript claim is unsupported, overstated, or contradicted by the source.
- `ambiguous`: multiple works plausibly match, or sources conflict.
- `unverified`: not enough evidence was found within available sources.
- `not-found`: targeted searches across likely sources fail to find the work.

## Audit Workspace

For manuscripts with more than a few references, create a workspace:

```bash
python <skill-dir>/scripts/init_reference_audit.py --source <manuscript-or-bib-path> --out <audit-dir>
```

Use these files as living records:

- `00-audit-protocol.md`: task scope, source files, authority sources, and evidence rules.
- `01-reference-inventory.csv`: one row per bibliography item.
- `02-citation-contexts.csv`: citation keys and surrounding manuscript claims.
- `03-verification-log.md`: source-by-source evidence notes.
- `04-mismatch-report.md`: metadata errors, suspicious entries, missing fields, and likely fixes.
- `05-citation-support-report.md`: whether the cited source supports the sentence or paragraph.
- `06-final-reference-audit.md`: user-facing summary and required author actions.

When a `.bib` file is available, run the bundled extractor first:

```bash
python <skill-dir>/scripts/extract_bib_inventory.py references.bib --out <audit-dir>/01-reference-inventory.csv
```

The extractor is a first pass only. It does not prove authenticity.

## Workflow

### 1. Define Scope

Identify what the user wants:

- **Existence check**: whether each reference is real.
- **Metadata check**: whether title, authors, venue, year, DOI, pages, arXiv ID, or URL are correct.
- **Citation support check**: whether each citation supports the surrounding claim.
- **Full audit**: all of the above.

If the user does not specify, choose full audit for papers under submission and metadata plus existence check for quick bibliography cleanup.

### 2. Inventory References

Extract every bibliography entry from `.bib`, LaTeX `.bbl`, Markdown references, Word bibliography, PDF reference section, or plain text. Record:

- local key or index;
- raw reference string;
- title;
- authors;
- year;
- venue or publisher;
- DOI, arXiv ID, OpenReview forum, URL, ISBN/ISSN if present;
- entry type;
- cited in manuscript? yes/no/unknown.

Do not silently drop uncited references or citations missing from the bibliography. Record them separately.

### 3. Extract Citation Contexts

For each in-text citation, record the local citation key, sentence, paragraph, section, and the claim being supported. For grouped citations, split the group and decide what each citation appears to support.

Pay special attention to high-risk contexts:

- claims about "first", "state of the art", "widely used", "proved", "shown", or "demonstrated";
- negative claims about prior work;
- benchmark, dataset, tool, model, or metric descriptions;
- related-work positioning;
- method justification;
- threats and limitations.

### 4. Verify Existence And Metadata

Use targeted sources in this order when possible:

1. DOI resolver or Crossref for DOI-bearing entries.
2. Publisher, ACM/IEEE/Springer/USENIX/ACL/OpenReview/arXiv official page.
3. DBLP for CS venue/year/authors.
4. Semantic Scholar, OpenAlex, Google Scholar, or library catalogs as secondary checks.
5. The PDF itself, if available.

For each reference, compare normalized title, first author, author set, year, venue, DOI/arXiv ID, and page/article number. Record mismatches explicitly. If the DOI resolves to a different title or paper, treat it as `metadata-mismatch` or `not-found` depending on the rest of the evidence.

### 5. Verify Citation Support

When claim support matters, inspect the cited paper's abstract, introduction, method, results, limitations, and relevant tables/figures. Decide whether the cited source:

- directly supports the claim;
- supports a narrower version;
- is merely related background;
- contradicts or complicates the claim;
- cannot be checked from available material.

If a citation is used for a strong claim but only supports a weaker one, mark `citation-misuse` and suggest a narrower wording or a better source.

### 6. Diagnose Common Fabrication Patterns

Flag entries with:

- plausible title but no discoverable record;
- DOI prefix or suffix that resolves to another work;
- author/year/venue combination that does not exist;
- impossible venue volume, issue, page range, or conference year;
- title that combines terms from several real papers;
- arXiv ID format mismatch or ID assigned to a different paper;
- non-existent workshop, journal, or proceedings;
- copied BibTeX where title and DOI belong to different papers.

Do not assume fabrication when metadata is merely incomplete. Use the evidence levels.

### 7. Report

Lead with a concise risk summary:

- number of references checked;
- counts by evidence level;
- highest-risk entries;
- whether any manuscript claims need citation changes;
- unresolved items requiring author PDF access, library access, or manual confirmation.

For each problem entry, include the local key, current reference, evidence found, status label, and recommended action. Keep raw search trails in the audit workspace instead of overwhelming the final response.

## Resources

- `scripts/init_reference_audit.py`: create the audit workspace files.
- `scripts/extract_bib_inventory.py`: parse BibTeX-like entries into a CSV inventory.
- `references/source-priority.md`: authority-source guidance, evidence levels, and search patterns.
