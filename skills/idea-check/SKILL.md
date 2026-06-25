---
name: idea-check
description: Map a CS or research-paper idea, abstract, proposal, or draft against recent top-venue prior work to judge where the idea sits in the field. Use when Codex is asked for CSPaper-style Idea Check, research idea validation, novelty/gap analysis, closest related papers, field landscape synthesis, "has this been done", "idea是否新", "这个idea有没有价值", or whether a planned paper idea has defensible positioning before implementation or submission.
---

# Idea Check

## Overview

Use this skill to produce a CSPaper-style idea map: closest accepted papers, field synthesis, overlap/difference analysis, and open gaps. Treat the result as a landscape map, not an accept/reject verdict.

## Core Rules

- Focus on idea position, novelty delta, and opportunity space. Do not turn this into a correctness, experiment, or paper-quality review.
- Prefer recent accepted or published work from strong venues as the comparison base. Use arXiv-only work only when it is clearly closest or the user asks for frontier preprints.
- Separate "closest prior work" from "broad background." A famous paper that shares only the general area is not a close neighbor.
- Explain both directions for every neighbor: what the prior paper contributes, and exactly how the user's idea overlaps and differs.
- Preserve uncertainty. If search coverage is thin, venue scope is narrow, or the idea is underspecified, lower confidence instead of inventing gaps.
- Do not claim an idea is novel merely because no identical title was found. Novelty depends on task, input/output contract, mechanism, evaluation object, assumptions, and claimed contribution.

## Workflow

### 1. Extract The Idea Signature

Read the idea, abstract, proposal, or draft and write a compact signature:

- problem and motivation;
- target domain and users;
- input/output contract;
- proposed mechanism, model, theorem, benchmark, dataset, system, or empirical claim;
- what the author seems to claim is new;
- expected venue family or field;
- 5-10 search keywords and synonyms.

If the input is only a broad topic, ask for a sharper idea unless a rough landscape scan is still useful.

### 2. Find Close Prior Work

Use local papers when supplied. Otherwise search the web and bibliographic sources. For current papers, venue status, and citation metadata, browse or query external sources; do not rely on memory.

Prioritize:

- recent top venues in the relevant area;
- accepted main-track papers, journals, and well-established proceedings;
- papers matching at least two of task, input/output contract, method family, evaluation object, assumptions, or target claim.

Aim for 6-10 neighbors. Label each as:

- `suggested`: very close and likely required reading;
- `worth-a-look`: useful overlap or adjacent mechanism;
- `tangential`: broad context, not a core novelty threat.

### 3. Build The Field Map

Before judging novelty, synthesize the retrieved field:

- dominant theme;
- methodological spectrum;
- common assumptions and evaluation settings;
- venue and year distribution;
- recurring baselines, datasets, metrics, theorems, or systems;
- confidence level: `high`, `medium`, or `low`.

Use `references/idea-rubric.md` for the detailed checklist and report template.

### 4. Position The User's Idea

Write one short "where this idea sits" paragraph. It should say:

- which cluster of prior work the idea belongs to;
- what seems genuinely different;
- whether the difference is a new problem, new mechanism, new setting, new evidence, new resource, or only a reframing;
- what evidence would be needed to defend the positioning.

Avoid final-sounding verdicts like "definitely novel" unless the search is unusually strong.

### 5. Identify Gaps And Risks

For each gap, make clear whether it is:

- a real open space suggested by multiple close papers;
- a potential paper angle that needs evidence;
- a weak gap caused by limited search coverage;
- a claim that may collapse if a missing neighbor is found.

Also list novelty risks: closest papers the author must cite, likely reviewer objections, and wording that should be narrowed.

## Output Shape

Use this order:

1. **Idea Signature**: 4-7 bullets.
2. **Your Idea In Context**: one concise positioning paragraph.
3. **Field Landscape**: dominant theme, method spectrum, venue/year mix, confidence.
4. **Closest Related Papers**: table with title, venue/year, match label, match rationale, what sets it apart, relevance to this idea.
5. **Open Gaps And Opportunities**: concrete directions, each tied to retrieved literature.
6. **Novelty Risks**: what could undermine the idea's claimed contribution.
7. **Actionable Next Steps**: readings, claim revisions, or experiments needed to make the idea defensible.

## Resources

- `references/idea-rubric.md`: detailed CSPaper-style criteria, search protocol, match labels, and output template.
