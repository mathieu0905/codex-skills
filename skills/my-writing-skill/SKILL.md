---
name: my-writing-skill
description: Edit, review, or rewrite articles, essays, papers, manuscripts, reports, proposals, and long-form prose with a global logic audit. Use when the user asks to improve coherence, argument flow, section order, paragraph transitions, concept introduction order, consistency across sections, claim-evidence alignment, method-limitation correspondence, or when prose sounds locally plausible but globally scattered or self-contradictory. Also use for Chinese requests about 改文章, 文章逻辑, 不连贯, 前后不一致, 概念突然出现, 顺序问题, or 方法和 limitation 不对应.
---

# My Writing Skill

## Overview

Use this skill to revise long-form writing from a whole-document perspective while still reading from front to back. Maintain explicit audit notes so the article's thesis, concepts, claims, methods, limitations, and unresolved questions stay visible throughout the edit.

## Non-Negotiables

- Do not start by polishing sentences. First build a document-level understanding and a forward-reading audit trail.
- Treat every paragraph as doing a job in an argument. If the job is unclear, overlapping, misplaced, or unsupported, record that before rewriting.
- Track introduced concepts, promised contributions, evidence, assumptions, limitations, and open loops. Do not let later edits contradict earlier commitments.
- Preserve the author's intended claims unless the user asks for a stronger rewrite. When changing claims, make the logic for the change explicit.
- Prefer structural fixes over cosmetic transitions when the underlying order or support is broken.

## Audit Workspace

For multi-section writing, manuscripts, academic papers, or any text longer than roughly 1,200 words, create a local audit workspace before revising:

```bash
python <skill-dir>/scripts/init_article_audit.py --source <article-path-or-title> --out <audit-dir>
```

If the article is pasted in chat or no file path exists, still create the workspace with a short title:

```bash
python <skill-dir>/scripts/init_article_audit.py --source "pasted-article" --out article-logic-audit
```

Use these files as living notes:

- `00-reading-protocol.md`: task framing and reading rules.
- `01-global-map.md`: thesis, audience, contribution, section-level argument map.
- `02-forward-reading-log.md`: paragraph-by-paragraph observations in document order.
- `03-concept-ledger.md`: first mentions, definitions, dependencies, unexplained jumps.
- `04-claim-evidence-ledger.md`: claims, evidence, support status, contradictions.
- `05-method-limitation-ledger.md`: method promises, evaluation coverage, limitations, unmatched items.
- `06-revision-plan.md`: prioritized edits tied to audit evidence.
- `07-final-consistency-pass.md`: final checks after editing.

For short texts, a compact in-message version of the same ledgers is acceptable, but still reason in this order.

## Workflow

### 1. Frame The Edit

Identify the user's requested depth:

- **Audit only**: report problems and proposed fixes.
- **Light edit**: improve transitions and local coherence without changing structure much.
- **Structural edit**: reorder, merge, split, or rewrite sections.
- **Full rewrite**: rebuild the article while preserving the intended argument.

If the user did not specify, choose the least invasive level that solves the logical problem. Note the chosen level.

### 2. First Pass: Global Map

Read the title, abstract/introduction, headings, conclusion, and any explicit contribution or limitation statements. Fill `01-global-map.md` with:

- likely central thesis;
- target reader and expected background;
- article promise: what the reader is led to expect;
- section jobs: what each section appears to contribute;
- terms or claims that must be tracked later.

This pass is provisional. Mark uncertain items as hypotheses, not facts.

### 3. Second Pass: Forward Reading Log

Read from the beginning to the end without jumping around to patch individual sentences. For each paragraph or small paragraph group, record:

- current paragraph's job;
- what it depends on from earlier text;
- what it introduces for later text;
- whether its position is justified;
- any abrupt concept, unsupported claim, contradiction, repetition, or dangling promise.

Update the concept, claim-evidence, and method-limitation ledgers as soon as each item appears. This prevents later reasoning from erasing the reader's actual experience of encountering the text in order.

### 4. Diagnose Global Failures

Use `references/audit-checklists.md` when the issue is subtle or the text is long. Classify problems by type:

- **Missing bridge**: each sentence may be true, but the inference between them is not stated.
- **Wrong order**: a concept, motivation, method, result, or limitation appears before the reader has the needed setup.
- **Unpaid promise**: the introduction, roadmap, or method section promises something later sections do not deliver.
- **Unsupported escalation**: the prose moves from observation to strong claim without enough evidence.
- **Duplicate job**: two paragraphs or sections serve the same purpose without advancing the argument.
- **Inconsistent vocabulary**: the same thing is named differently, or one term is used for multiple things.
- **Method-limitation mismatch**: a limitation is named but not reflected in method/evaluation, or the method claims to solve an issue that the limitation section later admits remains open.
- **Conclusion drift**: the final takeaway no longer matches the evidence or scope of the article.

### 5. Build The Revision Plan

Write `06-revision-plan.md` before editing. Group changes by priority:

- **P0: argument integrity**: contradictions, missing prerequisites, wrong claims, unsupported core conclusions.
- **P1: structure and sequence**: section order, paragraph order, roadmap, topic progression.
- **P2: local coherence**: transitions, signposting, paragraph topic sentences, repeated phrasing.
- **P3: style**: concision, tone, grammar, word choice.

Every planned edit should cite the relevant audit file entry. If an edit cannot be tied to a recorded logical issue, treat it as optional style work.

### 6. Revise

Make edits in the lowest-risk form appropriate to the user's request:

- For feedback requests, return a diagnosis with concrete rewrite examples.
- For direct revision requests, edit the document or produce a revised version.
- For `.docx`, PDF, LaTeX, Markdown, spreadsheet, or presentation files, use the relevant file-format skill or tool to preserve formatting; this skill governs the logical review.

When rewriting, move from structure to paragraphs to sentences:

1. Fix section and paragraph order.
2. Add or remove conceptual setup.
3. Align claims, evidence, methods, and limitations.
4. Improve transitions and topic sentences.
5. Polish wording only after the structure works.

### 7. Final Consistency Pass

After revision, read the edited article's skeleton again: title, abstract/introduction, headings, topic sentences, conclusion, and limitation/future-work sections. Fill `07-final-consistency-pass.md` and verify:

- all important concepts are introduced before use;
- terminology stays stable;
- every stated contribution has corresponding method/evidence/result support;
- limitations match the actual method and evidence scope;
- the conclusion does not overclaim;
- no new contradiction was introduced by the edit;
- transitions reflect real logical relationships rather than decorative connective words.

## Output Style

When reporting to the user, lead with the highest-impact global diagnosis, not line-level copyedits. Include:

- a brief statement of the article's intended argument as understood;
- the main coherence failures;
- the proposed structure or revision strategy;
- the revised text, patch, or annotated feedback requested by the user;
- any unresolved assumptions or parts that require author judgment.

Do not overwhelm the user with the full audit workspace unless they ask for it. Use it to make the edit reliable.

## Resources

- `scripts/init_article_audit.py`: create the audit workspace and markdown ledgers.
- `references/audit-checklists.md`: detailed prompts for global coherence, forward reading, concept order, and correspondence checks.
