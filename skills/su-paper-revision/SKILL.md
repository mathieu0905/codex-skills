---
name: su-paper-revision
description: Structural academic paper revision workflow distilled from SU-style supervisor comments. Use when Codex needs to revise, critique, mine, or rewrite research-paper sections after comments about weak story, unclear motivation, unnatural or AI-like writing, repeated RQs, poor section organization, insufficient methodological detail, vague benchmark positioning, unconvincing contributions, table/figure readability, excessive claim strength, or reviewer/supervisor comments marked as su/SU/Zhensu. Especially relevant for LaTeX manuscripts, CS/SE empirical papers, benchmark papers, results sections, RQs, introductions, related work, methodology, threats, response letters, and paper-wide narrative repair before prose polishing.
---

# SU Paper Revision

## Core Rule

Treat comments as structural signals first, not copy-edit requests. Before polishing sentences, identify what role the paragraph, subsection, table, figure, or section must play in the paper's argument, then revise the content so that role is clear.

For detailed revision principles distilled from prior SU comments, read `references/su_revision_principles.md` when the task involves more than a small local sentence edit.

Respect the user's collaboration mode. If the user asks only for translation, diagnosis, or paragraph-by-paragraph review, do not edit the manuscript yet. Give a faithful translation or critique, let the user react, and only modify files after they ask to "change", "revise", "改", or otherwise approve the edit.

When the user gives iterative feedback, generalize it before editing. A complaint such as "I still do not know whether the method is usable" is usually a claim-evidence problem, not a request for a stronger adjective. Decide what the current metrics can actually support, then state that supported claim plainly and consistently across abstract, results, discussion, and conclusion.

## Workflow

1. **Collect the local context.** Read the target passage, surrounding section, section title, labels, figures/tables referenced nearby, and any comments such as `\su{...}`, reviewer notes, TODOs, or inline author remarks.
2. **Honor the requested interaction mode.** If the user is reading through a section, translate or explain the passage first and keep proposed rewrites separate from file edits. Treat "改" or an equivalent approval as the point where editing becomes appropriate.
3. **Mine historical SU comments when requested or useful.** If the user asks to learn from prior SU comments, search git history for `\su{...}` rather than only the current tree. Deduplicate repeated Overleaf comments, strip resolved markers such as `-- DONE`, group comments by section and revision pattern, and generalize the pattern without hard-coding one paper's results.
4. **Classify the problem.** Decide whether the issue is mainly story/motivation, section architecture, RQ framing, reproducibility detail, result interpretation, metric definition, terminology, table/figure self-containment, related-work positioning, threat scoping, claim strength, or prose naturalness.
5. **Extract the supportable claim.** Before rewriting results, map each metric to what it can and cannot support. For example, replay validity supports structural executability, reference-based grouping supports alignment with a maintained reference, behavior probes support practical containment, and robustness checks support stability of the pattern. Combine these signals into the strongest honest claim.
6. **Repair the argument before the wording.** If a paragraph's purpose is unclear, rewrite around a simple claim-evidence-implication shape. For each RQ or result block, make the sequence explicit: why the question matters, what comparison or experiment answers it, what the result is, and what the reader should conclude.
7. **Respect section duties.** Do not let the introduction become methodology, the methodology become results, or the results repeat RQs without answering them. Move or compress material when a section is carrying the wrong burden.
8. **Make technical details reproducible where needed.** Method and evaluation sections should describe constraints, filtering, validation, metrics, thresholds, tools, commands or command classes, and protocols concretely enough that a reader could reproduce the study from the text.
9. **Make tables and figures standalone.** Check whether each table/figure is referenced in the text, has legible naming and units, defines abbreviations, and has a caption that explains the takeaway or metric meanings rather than merely naming the artifact. For important figures, inspect the rendered output before treating the edit as done.
10. **Naturalize the prose last.** Avoid robotic fragments, over-compressed formulas in main text, short phrase piles, slogan-like contribution bullets, and repeated defensive contrast templates such as "not X but Y" or "rather than". Prefer connected sentences that explain claim, evidence, and implication.
11. **Preserve evidence boundaries.** Do not strengthen claims beyond the data, invent missing citations, hide limitations, or turn a benchmark observation into a general model ranking unless the design supports it. Put necessary limitations in the right place; do not make Results read like a rebuttal unless the caveat is needed to interpret the number.
12. **Return an edit with rationale.** When editing files, keep the final response brief: say which sections were changed, what structural problem was addressed, and what checks were run or skipped.

## Revision Heuristics

- Define a new task or construct at first use, then separate it from adjacent tasks.
- Motivate benchmark dimensions by explaining the new observation they enable, not by overstating that prior work is weak.
- Limit examples to the minimum needed to make the abstraction concrete.
- Frame RQs as questions readers would naturally want answered, then order them from prevalence or capability to impact, mechanism, and practical value.
- In results, make each RQ answer a reader concern. Introduce why the question matters, state what experiment or comparison answers it, report the result, and translate the result into a practical implication.
- When a task has no unique ground truth, do not write as if the reference is a gold answer. Describe reference metrics as alignment signals, then use complementary behavioral or robustness checks to support usability claims.
- When the user asks "so what?" or "is it usable?", convert metric values into a bounded practical reading, such as a draft artifact a human can inspect, a reliable gate, or a diagnostic signal. Do not leave the reader with only a table ranking.
- In interactive revision, separate "understand the current text" from "rewrite the current text". A faithful translation is useful because it exposes logic gaps without prematurely changing the author's intent.
- In methodology, explain both what was done and why a design choice is needed. Name the exact unit of comparison, dataset or benchmark, agents/models, execution settings, budget levels, validation protocol, and metric definitions when they affect interpretation.
- In related work, use a small number of functional buckets instead of many thin subsections.
- In threats, keep the categories few and tied to the paper's actual design risks.
- In contributions, use natural full sentences backed by concrete evidence; avoid disconnected noun phrases that sound like slide fragments.
- In the introduction, avoid naming every mode, metric, or implementation detail if it increases reader burden before the story is established.
- For tables and figures, check readability, sizing, column naming, centered numeric values, and whether the caption defines enough context for the artifact to be understood without rereading the main text.
- For figures, prefer the paper's normal column width unless the visual claim truly needs a two-column artifact. If a two-column figure creates large whitespace, check `figure*`, `FloatBarrier`, and float placement before shrinking an important figure.
- For terminology, prefer the official benchmark or venue term when available, such as "resolve rate" instead of an informal substitute if that is the benchmark's name.
- For response letters and revised manuscripts, keep the manuscript narrative paper-facing. Remove or rewrite prose that sounds like reviewer-response scaffolding.

## Historical SU Comment Mining

When asked to improve this skill or infer SU preferences from a repository:

1. Search both the current tree and git history for `\su{...}` comments. A useful starting point is `git grep -n -E '\\su\\{' $(git rev-list --all) -- '*.tex'`.
2. Normalize the comments before analysis: strip duplicate commits, remove `-- DONE` suffixes, collapse whitespace, and keep a sample location for each unique comment.
3. Classify comments into durable patterns, not paper-specific facts. For example, keep "define trial-and-error at first use" as a rule, but do not encode the specific RQ answer or numeric result from one paper unless the user asks for that paper.
4. Use frequent comments as priority signals. In the RunLess history, SU repeatedly emphasized section summaries, method reproducibility, result-first writing, metric/table definitions, official terminology, and cautious claim strength.
5. After updating this skill, leave the user's manuscript files untouched unless they explicitly asked for manuscript revision too.

## Output Modes

If the user asks for a critique, give prioritized findings with concrete rewrite direction and file/line references when available.

If the user asks to revise the manuscript, edit the files directly. Keep comments only if they represent unresolved author decisions; remove or update comments that the revision has addressed.

If the user asks to turn comment style into a reusable process, update this skill or its reference file rather than changing the paper.
