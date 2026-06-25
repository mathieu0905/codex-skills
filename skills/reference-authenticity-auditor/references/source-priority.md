# Source Priority And Evidence Rules

Use this reference when deciding what counts as evidence for a reference-authenticity audit.

## Authority Order

Prefer sources in this order:

1. DOI resolver landing page and Crossref/DataCite metadata.
2. Publisher or proceedings page, such as ACM Digital Library, IEEE Xplore, Springer, Elsevier, USENIX, ACL Anthology, PMLR, OpenReview, arXiv, NeurIPS/ICML/ICLR pages, or official conference proceedings.
3. DBLP for computer-science title, author, venue, and year checks.
4. Semantic Scholar, OpenAlex, Google Scholar, library catalogs, or university pages.
5. Search snippets, personal pages, slides, or PDFs hosted on arbitrary domains.

Search snippets can identify candidates but should not be the only evidence for `verified` unless no better source exists and the report says confidence is low.

## Metadata Matching Rules

Normalize before comparing:

- lowercase title;
- remove punctuation, braces, LaTeX commands, and repeated whitespace;
- normalize Unicode accents cautiously;
- compare first author and year before treating a fuzzy title match as the same work;
- treat subtitles and conference suffixes as possible but checkable variations.

High-severity mismatches:

- DOI resolves to a different title;
- first author differs;
- year differs by more than online-first vs proceedings timing;
- venue is a different conference, journal, or track;
- title points to a different study;
- arXiv ID belongs to a different paper.

Lower-severity mismatches:

- capitalization;
- missing page range;
- shortened conference name;
- author initials vs full names;
- online-first year vs issue/proceedings year, if explainable.

## Search Patterns

Use targeted queries:

- exact title in quotes;
- exact title plus first author;
- title keywords plus year plus venue;
- DOI string;
- arXiv ID;
- BibTeX key plus title keywords;
- `site:dblp.org <title keywords> <first author>`;
- `site:doi.org <doi>` or DOI resolver;
- publisher-specific search when venue is known.

When a title is not found exactly, search distinctive noun phrases, method names, dataset names, and first author plus year.

## Citation Support Rules

Classify citation support as:

- `direct`: source explicitly supports the claim.
- `narrower`: source supports a weaker or more specific version.
- `background`: source is related but does not prove the claim.
- `contradicts`: source conflicts with the claim.
- `unchecked`: source could not be inspected enough to decide.

High-risk claim verbs require stronger evidence:

- "prove", "show", "demonstrate", "establish";
- "first", "only", "state-of-the-art", "widely used";
- "all", "most", "always", "never";
- "significantly improves", "outperforms", "solves".

If the source only provides background, recommend rewriting the sentence or finding a more direct citation.

## Reporting Standards

Every flagged item should include:

- local key or bibliography number;
- status label;
- current metadata;
- evidence source URL or source name;
- mismatch or support problem;
- recommended action.

Use `not-found` only after several targeted searches fail. Use `unverified` when time, access, or source availability is the limiting factor.
