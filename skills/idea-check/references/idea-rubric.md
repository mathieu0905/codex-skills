# Idea Check Rubric

Use this reference when running a CSPaper-style Idea Check. The goal is to show where an idea stands in the recent literature, not to predict acceptance or prove absolute novelty.

## Input Triage

Proceed when the input contains at least:

- a research problem or target phenomenon;
- a proposed mechanism, hypothesis, method, resource, benchmark, theorem, or system;
- enough context to infer the field.

Ask for clarification when the input is only:

- a broad keyword;
- a question with no proposed approach;
- a literature topic rather than a research idea;
- a plan whose novelty depends on unavailable implementation details.

If the user wants a rough scan anyway, label the result `low confidence`.

## Idea Signature Template

```text
Problem:
Target field / venue family:
Input-output contract:
Proposed contribution:
Claimed novelty:
Likely closest communities:
Search keywords:
```

## Search Protocol

Search in widening rings:

1. Exact phrase search for the core method/problem name.
2. Synonym search for task plus mechanism.
3. Venue-specific search for recent top papers.
4. Citation and related-work expansion from the closest hits.
5. Optional frontier search on arXiv or OpenReview when the idea is very new.

Use authoritative pages when possible: venue proceedings, publisher pages, arXiv, OpenReview, ACL Anthology, CVF, ACM, IEEE, DBLP, Semantic Scholar, OpenAlex, or official project pages.

## Close-Match Test

A paper is a close neighbor if it matches at least two of:

- same task or problem;
- same input-output contract;
- same method family or theoretical object;
- same dataset, benchmark, metric, or evaluation object;
- same assumptions or constraints;
- same claimed contribution type;
- same failure mode or limitation.

If it only shares broad area words such as "LLM", "graph", "fairness", "security", or "benchmark", label it `tangential`.

## Match Labels

- `suggested`: must-read neighbor; likely citation or novelty threat.
- `worth-a-look`: relevant paper that helps position the idea but does not subsume it.
- `tangential`: broad background or adjacent method; useful context, weak novelty evidence.
- `missing-info`: metadata or abstract suggests relevance, but the paper could not be inspected enough.

Avoid percentage scores unless the user asks for them. If using percentages, define them as match strength, not quality.

## Field Landscape Checklist

Report:

- dominant theme across close papers;
- method spectrum, from theory to empirical systems if applicable;
- common assumptions, datasets, metrics, tasks, or proof settings;
- venue/year mix and whether the area is active or sparse;
- what the closest papers already solved;
- what they consistently leave open;
- confidence level and why.

Confidence:

- `high`: several close accepted papers were inspected and agree on the landscape.
- `medium`: enough close work exists, but coverage is partial or mixed.
- `low`: few close papers, mostly metadata-only evidence, or an underspecified idea.

## Novelty Delta Categories

Classify the user's strongest difference as one or more of:

- `new problem`: asks a question prior work did not address;
- `new setting`: same problem under different assumptions, data, constraints, or deployment context;
- `new mechanism`: different algorithm, architecture, proof technique, system design, or intervention;
- `new evidence`: stronger evaluation, new benchmark, broader study, or replication that changes understanding;
- `new resource`: dataset, benchmark, tool, taxonomy, or measurement apparatus;
- `new synthesis`: useful integration of known pieces, but novelty depends on execution;
- `weak reframing`: mostly renaming or repackaging existing work.

Do not treat "we use LLMs", "we add a benchmark", or "we improve performance" as novel without a specific delta against close neighbors.

## Gap Quality

Good gaps:

- are absent from multiple close papers, not just one;
- matter to the field's core problem;
- can be tested, proved, built, or analyzed;
- connect directly to the user's idea.

Weak gaps:

- are merely future work boilerplate;
- require unrealistic assumptions;
- are outside the field's actual interest;
- depend on a search miss.

## Output Template

```markdown
**Idea Signature**
- Problem:
- Proposed contribution:
- Claimed novelty:
- Closest communities:
- Confidence:

**Your Idea In Context**
[one paragraph positioning the idea against the closest cluster]

**Field Landscape**
- Dominant theme:
- Method spectrum:
- Common evaluation/theory setting:
- Venue/year mix:
- Confidence note:

**Closest Related Papers**
| Label | Paper | Venue/Year | Why It Matches | What Sets It Apart | Relevance To This Idea |
|---|---|---|---|---|---|

**Open Gaps And Opportunities**
1. [gap] - grounded in [papers].

**Novelty Risks**
- [risk] - what the author should cite or narrow.

**Next Steps**
- Read:
- Revise claim:
- Evidence needed:
```

## Common Failure Modes

- Overcalling novelty because search found no identical title.
- Comparing only with broad famous papers instead of closest neighbors.
- Penalizing an idea for not solving every limitation in the field.
- Treating weak paper execution as an idea problem.
- Confusing "paper not accepted yet" with "idea has no value."
- Forgetting to tell the author which missing citations are most dangerous.
