---
name: correctness-check
description: Audit a CS or research paper for CSPaper-style correctness, claim verification, technical soundness, and error discovery. Use when Codex is asked to check whether a paper's claims are supported, identify objective mistakes, verify experiments, equations, proofs, metrics, baselines, conclusions, limitations, or run a "Correctness Check", "claim verification", "技术正确性检查", "实验是否支撑结论", or "这篇文章有没有硬伤" review.
---

# Correctness Check

## Overview

Use this skill for verification-first paper review. Extract the paper's load-bearing claims, check each claim against the evidence inside the paper, and direct attention to likely correctness failures.

## Core Rules

- Start from claims, not vibes. A correctness review is anchored in explicit claims and the paper evidence that should support them.
- Separate objective correctness from taste, novelty, writing quality, and venue fit. Mention those only when they affect truth or support.
- Verify against the paper first: experiments, derivations, proofs, figures, tables, appendices, algorithms, and limitations.
- Use external sources for prior-work or novelty claims, dataset/tool facts, benchmark definitions, and suspicious metadata. Browse when those facts may have changed or require verification.
- Preserve uncertainty. Use `supported`, `partially-supported`, `unsupported`, `contradicted`, `unclear`, or `needs-external-verification`.
- Prefer a small number of high-confidence, evidence-backed findings over many speculative objections.

## Workflow

### 1. Scope The Check

Identify whether the user wants:

- **Quick triage**: top correctness risks only.
- **Full claim audit**: every load-bearing claim and its evidence.
- **Experiment audit**: baselines, metrics, datasets, statistics, ablations, and confounds.
- **Proof/math audit**: assumptions, lemma dependencies, derivation steps, edge cases.
- **Submission review**: correctness findings written in reviewer style.

If unspecified, run a full claim audit for manuscripts and a quick triage for pasted excerpts.

### 2. Extract Load-Bearing Claims

Read the abstract, introduction, contributions, method, theory, experiments, results, limitations, and conclusion. Build a claim ledger with:

- claim text or paraphrase;
- section/page/figure/table;
- claim type: `novelty`, `method`, `theory`, `experiment`, `system`, `dataset`, `metric`, `efficiency`, `generalization`, `limitation`, or `conclusion`;
- required evidence;
- why the claim matters to the paper.

Load-bearing claims are statements that, if false or unsupported, would materially weaken the paper.

### 3. Verify Internal Evidence

For each claim, check the cited or implied support:

- experiments: protocol, baselines, metrics, datasets, statistical treatment, ablations, error bars, splits, leakage, hyperparameters, and fairness of comparison;
- theory: definitions, assumptions, theorem statements, proof steps, boundary cases, and whether conclusions exceed assumptions;
- systems: architecture, implementation detail, resource accounting, scalability, and reproducibility;
- datasets/benchmarks: construction, labels, contamination, representativeness, licensing, and evaluation validity;
- conclusions: whether the result strength justifies the final wording.

Use `references/correctness-rubric.md` for the detailed checklist and report template.

### 4. Check External Facts When Needed

Use web or bibliographic sources when claims depend on:

- "first", "novel", "unlike prior work", or "state of the art";
- benchmark rules, dataset definitions, leaderboards, or tool behavior;
- citations and reference metadata;
- claims about what other papers did or did not show.

Do not expand this into a general literature review unless novelty support is central to correctness.

### 5. Prioritize Findings

Classify each issue by severity:

- `P0 fatal`: likely invalidates the main claim or result.
- `P1 major`: materially weakens a core claim, experiment, proof, or conclusion.
- `P2 moderate`: important missing control, ambiguity, or overclaim.
- `P3 minor`: local fix, reporting issue, or clarification.

Every finding must cite the claim and the evidence gap. If evidence is missing because the paper excerpt is incomplete, say so.

## Output Shape

Use this order:

1. **Verdict**: one paragraph on whether the paper appears technically sound, with confidence.
2. **Load-Bearing Claims**: compact table of claims and statuses.
3. **Highest-Risk Findings**: P0/P1 first, with evidence and recommended fix.
4. **Experiment/Proof/Method Checks**: whichever applies to the paper.
5. **Overclaiming And Scope**: claims that should be narrowed.
6. **Questions For Authors**: precise requests that would resolve uncertainty.
7. **Reviewer-Style Summary**: optional, when the user wants review text.

## Resources

- `references/correctness-rubric.md`: detailed claim-ledger protocol, evidence-status labels, severity rules, and output templates.
