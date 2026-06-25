# Correctness Check Rubric

Use this reference when running a CSPaper-style Correctness Check. The goal is to verify load-bearing claims against evidence and surface objective risks.

## Claim Ledger

Create a ledger before writing findings.

| ID | Claim | Location | Type | Required Evidence | Status | Notes |
|---|---|---|---|---|---|---|

Claim types:

- `novelty`: first, new, unlike prior work, state of the art.
- `method`: algorithm, architecture, training, pipeline, system behavior.
- `theory`: theorem, proof, derivation, convergence, complexity, bound.
- `experiment`: empirical result, comparison, ablation, statistic.
- `dataset`: data source, annotation, filtering, leakage, benchmark construction.
- `metric`: metric definition, scoring, aggregation, validity.
- `efficiency`: cost, latency, memory, scalability, resource usage.
- `generalization`: cross-domain, robustness, transfer, real-world applicability.
- `limitation`: stated caveat or threat.
- `conclusion`: final takeaway or implication.

## Evidence Status Labels

Use exactly these labels:

- `supported`: evidence directly supports the claim as written.
- `partially-supported`: evidence supports a narrower or weaker version.
- `unsupported`: needed evidence is missing or irrelevant.
- `contradicted`: paper evidence or external facts conflict with the claim.
- `unclear`: evidence may exist but the paper's reporting is too ambiguous.
- `needs-external-verification`: internal evidence is not enough because the claim depends on prior work, dataset facts, benchmark rules, or outside metadata.

## Severity Rules

- `P0 fatal`: central result likely invalid, proof assumption broken, benchmark invalid, major leakage, or conclusion directly contradicted.
- `P1 major`: core claim materially overstates evidence; missing critical baseline, ablation, proof step, statistical test, or confound control.
- `P2 moderate`: important ambiguity, underreported method detail, limited external validity, incomplete analysis, or weaker overclaim.
- `P3 minor`: local wording, missing clarification, typo in math notation, or non-core reporting issue.

Severity depends on how load-bearing the claim is, not how easy the fix is.

## Experiment Audit Checklist

Check:

- Are baselines appropriate, recent, and fairly tuned?
- Are comparisons apples-to-apples on data, compute, prompts, model size, training budget, or access?
- Are datasets split correctly, with no leakage or contamination?
- Are metrics defined and suitable for the claim?
- Are ablations sufficient to attribute gains to the proposed component?
- Are negative results, variance, significance, confidence intervals, or repeated runs needed?
- Are hyperparameters, prompts, seeds, hardware, and preprocessing reported enough for verification?
- Do tables/figures match textual claims?
- Are limitations acknowledged where the evidence is narrow?

Red flags:

- SOTA claim without strong baselines.
- Large conclusion from one dataset or small sample.
- Benchmark numbers without protocol details.
- Improvement attributed to the method when multiple changes vary.
- User study or annotation claims without inter-rater reliability or sampling detail.
- Claims about real-world deployment from toy or synthetic settings.

## Theory And Math Audit Checklist

Check:

- Are definitions precise and used consistently?
- Are theorem assumptions stated before the theorem?
- Does each lemma prove what later steps need?
- Are edge cases covered, including zero, empty, non-iid, degenerate, adversarial, or boundary inputs?
- Do asymptotic, probabilistic, or approximation claims match the proof conditions?
- Are empirical conclusions separated from theorem guarantees?
- Are notation, dimensions, and quantifiers consistent?

Red flags:

- The theorem claims more generality than assumptions allow.
- A proof relies on independence, convexity, smoothness, stationarity, or boundedness without stating it.
- A result is shown for one setting but claimed for all settings.
- Complexity omits dominant preprocessing, search, training, or inference cost.

## Method And System Audit Checklist

Check:

- Is the method implementable from the description?
- Are algorithm steps, prompts, data transformations, and model choices specified?
- Are dependencies and external tools described accurately?
- Are failure modes and fallback behavior clear?
- Does the evaluation isolate the proposed method from engineering conveniences?
- Are compute and latency claims measured under realistic conditions?

## External Verification Triggers

Browse or use bibliographic sources when checking:

- "first", "novel", "SOTA", "no prior work", or "unlike existing methods";
- benchmark rules, leaderboards, dataset versions, licenses, or contamination;
- citation claims about what another paper proves or evaluates;
- tool or API behavior that may have changed;
- suspicious reference metadata.

Keep external checks targeted. This skill is not a full literature survey unless the claim requires it.

## Finding Template

```markdown
**[P1] Claim overstates the experiment**
- Claim: [quote/paraphrase with location]
- Evidence checked: [table/figure/section]
- Problem: [specific mismatch]
- Why it matters: [impact on main contribution]
- Fix: [narrow claim, add experiment, add baseline, clarify assumption]
- Status: [partially-supported/unsupported/etc.]
```

## Output Template

```markdown
**Verdict**
[technical soundness summary and confidence]

**Load-Bearing Claims**
| ID | Claim | Type | Required Evidence | Status | Severity |
|---|---|---|---|---|---|

**Highest-Risk Findings**
1. [P0/P1 finding]

**Experiment / Proof / Method Audit**
- Baselines:
- Ablations:
- Metrics:
- Statistics:
- Reproducibility:
- Theory assumptions:

**Overclaiming And Scope**
- [claim that should be narrowed]

**Questions For Authors**
1. [precise question]

**Reviewer-Style Summary**
[optional concise review paragraph]
```

## Common Failure Modes

- Listing every possible missing experiment without tying it to a claim.
- Treating weak writing as incorrectness.
- Assuming a claim is false because evidence is incomplete.
- Calling novelty weak without checking close prior work.
- Ignoring limitations that already narrow a claim.
- Giving a "reject" recommendation instead of a correctness audit when the user asked for verification.
