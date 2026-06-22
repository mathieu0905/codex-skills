# SU Revision Principles

Use this reference when a manuscript has supervisor/reviewer comments that point to narrative, organization, or evidence problems rather than simple grammar.

## Comment-to-Action Map

| Comment pattern | Revision action |
| --- | --- |
| "Do not change it; only translate / let me react first" | Switch to review mode. Translate or diagnose faithfully, separate any rewrite suggestion from file edits, and wait for explicit approval before changing the manuscript. |
| "Clearly define X at the beginning" | Open the section with a compact definition, scope boundary, and contrast with adjacent concepts. |
| "Argument is hard to understand" | Add the missing causal bridge: why this problem matters, why the proposed setting follows, and what the reader should infer. |
| "Avoid comparison / benchmark argument not strong" | Reframe as a new benchmark dimension or observation target; avoid attacking prior work unless the evidence directly supports it. |
| "Too many examples" | Keep one or two representative examples, then generalize. |
| "Text looks AI generated / not natural" | Replace stacked short claims and slogan fragments with connected prose that explains claim, evidence, and implication. |
| "Do not write formulas like PASS and FAIL in main text" | Translate symbolic criteria into reader-facing prose; keep formal notation for tables, algorithms, or definitions only when necessary. |
| "Structure should be overview, steps, metrics" | Rebuild the subsection so the reader sees the dataset/protocol summary first, then construction steps, then scoring/evaluation details. |
| "Need rationale for two ways" | Explain what question each design variant answers and why both are necessary. |
| "Missing details / should be reproducible" | Add operational details: constraints, commands or command classes, filtering criteria, validation checks, metrics, thresholds, and exclusion rules. |
| "RQs are not insightful" | Rewrite RQs around high-interest empirical unknowns. Avoid process questions that only mirror the method. |
| "Update these RQs based on the new content" | Reconcile RQ wording with the actual analyses and findings before polishing; remove stale RQs that describe an older paper structure. |
| "Just agents with different backend LLMs?" | Define the unit of comparison precisely, including framework, model, prompt/harness, and residual confounds. |
| "Results repeat RQs" | Start each result subsection with the empirical answer, then show numbers and interpretation. |
| "Introduce the main conclusion first" | Open the paragraph, subsection, or takeaway with the answer; follow with representative numbers and then the implication. |
| "I still do not know whether this is usable" | Translate metric evidence into a bounded practical claim, such as usable draft output, diagnostic value, or deployment readiness; state what the artifact can support and what still needs human inspection. |
| "The reference is not a standard answer" | Reframe reference-based scores as alignment with one maintained or plausible reference. Support practical claims with complementary signals such as behavioral probes, robustness checks, or alternative references. |
| "This sounds defensive" | Remove rebuttal scaffolding from the main narrative. Keep the necessary evidence boundary, but express it as part of the measurement design or threats rather than repeated "not X but Y" sentences. |
| "Why this metric / why these checks?" | Close the loop from construct to metric: state what each metric observes, what it cannot observe, and why the combination supports the paper's claim. |
| "Describe findings under this template" | Use a compact trend-example-conclusion pattern: state the general trend, give one concrete result, then state the bounded takeaway. |
| "Tables too small / figure too large" | Adjust sizing and density so text is legible in the target format; captions should state the message. |
| "Every table needs to be self-explained" | Define abbreviations, metric meanings, units, thresholds, and row/column semantics in the caption or nearby text so the table is understandable on its own. |
| "This figure is not mentioned in the paper" | Either cite and interpret the figure in the main text or remove it. Do not leave standalone visual artifacts. |
| "This figure seems unnecessary" | Remove the figure unless it carries a claim that prose or an existing table cannot communicate efficiently. |
| "The figure/table is ugly or too dense" | Prefer a clearer visual decomposition, improved sizing, or a simpler plot. Render the artifact and inspect it before editing prose around it. |
| "Two subsections are enough" | Merge related work into broad functional strands that support the paper's positioning. |
| "Keep threats to three points" | Group threats into a few meaningful categories instead of listing every caveat separately. |
| "Words like A=7 are not good language" | Use natural prose such as "seven cases..." or "the seven affected cases..." rather than code-like variable notation in narrative text. |
| "For intro, don't name each setting" | Reduce reader memory burden in the introduction; describe the dimension or spectrum first and defer names, prompts, and variants to Method. |
| "Change Dataset to Benchmark" | Use terminology that matches the artifact and community convention; do not use approximate synonyms when the distinction matters. |
| "Official name is Resolve Rate, not Pass Rate" | Prefer benchmark-official metric names and define them once, rather than inventing local labels. |
| "More details are needed. How is similarity measured?" | Specify the exact measurement procedure, preprocessing, thresholds, and what is excluded, such as formatting-only differences or comments. |
| "What is the classifier? rule-based or neural?" | State the implementation type and decision rules for any classifier/parser/analyzer introduced in the method. |
| "Trial-and-error appears for the first time" | Define any new construct at first use before using it to interpret a table or result. |
| "Turn down the tune" | Weaken claims that exceed the evidence. Replace prescriptive or absolute wording with bounded, evidence-linked statements. |
| "Use sentences. Avoid short phrases" | Convert slide-like fragments into complete prose with verbs and logical links. |
| "This sentence describes data, not a conclusion" | Rewrite takeaways so they interpret what the data means, not only repeat numbers. |

## Section-Specific Strategy

### Introduction

Build the arc in this order:

1. Real-world problem and why it persists.
2. Why existing practice does not fully solve it.
3. The paper's task or construct, defined plainly.
4. Why the construct creates a meaningful evaluation question.
5. What the paper studies and what evidence it contributes.

Do not spend the introduction on peripheral design variables unless they are central to the paper's story. Contributions should read like claims backed by the paper, not isolated labels.

Keep reader burden low. It is often enough to say that the study varies a capability or constraint along a spectrum; defer the exact mode names, prompts, budget levels, implementation commands, and table-heavy details to Method or Evaluation.

For RQ previews and findings, use an answer-oriented template:

1. General trend or answer.
2. Representative statistic or example.
3. Bounded implication for the paper's thesis.

When the actual analyses change, update the RQs and contribution bullets before polishing prose. A stale RQ creates a story problem even if the sentences are grammatical.

### Motivation or Problem Definition

Define the core task immediately. Give only enough examples to make the task concrete. Separate the task from adjacent areas such as bug repair, build repair, migration, or benchmarking by explaining the boundary conditions.

If linking the task to a broader trend such as agentic software engineering, state the mechanism. For example: old tools remain useful, wrappers expose them to new workflows, but wrappers do not fix compatibility faults inside the underlying library.

### Benchmark Construction and Method

Use a reader-reproducible order:

1. Dataset scale and high-level admission rule.
2. Source pools and filtering criteria.
3. Validation protocol.
4. Evaluation protocol and constraints.
5. Metrics and scoring.
6. Rationale for design variants.

When constraints matter, describe them technically. Say what is blocked, what is stripped post hoc, what is rerun, what files are allowed to change, and what threshold defines success.

Historical SU comments repeatedly ask for concrete method details. Before treating Method as done, check whether the text names:

- Agents, models, frameworks, and access mode.
- Benchmarks or datasets, including subset selection and ordering.
- Experimental settings, prompts or constraints, and budget levels.
- Metric definitions, official benchmark terminology, thresholds, and units.
- Analyzer/classifier implementation, such as rule-based patterns versus a learned classifier.
- What counts as an included or excluded operation, especially for execution, validation, localization, or exploration commands.

If a subsection has been retitled, update the opening paragraph and order of details so the subsection actually answers the new title. Do not leave terminology in a separate subsection if the reader needs it before understanding the experimental settings.

### Research Questions

RQs should be answerable, interesting before the reader sees the results, and aligned with the narrative. A common progression for empirical systems papers is:

1. Prevalence or capability: how often does the phenomenon occur, or can the approach do the task?
2. Impact or tradeoff: how does the intervention change effectiveness, cost, or reliability?
3. Mechanism or difficulty: what explains success, failure, or limited impact?
4. Practical value: what deployment or design implication follows under realistic constraints?

If two older RQs have been merged, do not simply concatenate them. Decide what final answer the merged RQ needs, then choose only analyses that support that answer.

### Results

Start with the answer, not the setup. Each result subsection should follow:

1. One-sentence answer to the RQ.
2. Primary quantitative evidence.
3. Interpretation that distinguishes capability, compliance, confounds, and practical meaning.
4. A concrete example only if it clarifies the mechanism.
5. A finding statement that is specific and bounded.

However, "lead with the answer" does not mean hiding the experimental logic. A strong result subsection should still make the sequence clear:

1. What reader concern or empirical unknown motivates this RQ.
2. What comparison, slice, metric, or probe is used to answer it.
3. What the result shows.
4. What practical or conceptual claim follows.

If the user says the paragraph feels like "numbers dropped from nowhere", add the experimental action before the numeric result. If the user says the paragraph feels defensive, keep the same evidence boundary but remove repeated contrast scaffolding.

Avoid leaderboard-only framing when the design observes behavior, constraints, shortcut use, or usability beyond pass/fail.

In paragraph-by-paragraph review, first translate the current paragraph literally enough that the user can judge whether the logic is understandable. After the user identifies the gap, revise only the necessary logical bridge or claim sentence. This prevents the revision from drifting away from the author's intended argument.

For empirical result paragraphs, SU-style comments often expect this shape:

1. Main observation in one sentence.
2. Quantitative support with the key numbers.
3. Comparison across important conditions, agents, or benchmarks.
4. Explanation of why the observation matters.
5. A specific, cautious takeaway.

Do not introduce a new behavioral category, assumption, or metric inside a result table without defining it first. If the result depends on a derived measure such as similarity, actionable feedback, trial-and-error, single-edit ratio, or no-useful-output, define how it is computed and what edge cases are excluded.

If a claim rules out an alternative explanation such as memorization, data contamination, or leakage, state the evidence boundary. Similar but non-identical patches do not alone prove genuine reasoning; they provide evidence against exact memorization under the chosen similarity measure.

For cost-effectiveness results, give both sides of the tradeoff. State the effectiveness delta and the resource savings, then identify whether the pattern is statistically significant, practically equivalent, or merely suggestive.

Use official metric names consistently. In SWE-bench-style repair papers, prefer "resolve rate" when referring to the official harness outcome; reserve "pass" for test-run outcomes only if the distinction is explicit.

When writing takeaways, avoid a bullet that only restates a table cell. The sentence should say what the table implies for the RQ.

#### Non-Unique References and Usability Claims

Many benchmark and empirical tasks have no single correct output. In those cases:

- Do not call the observed output, developer trace, or human choice "ground truth" unless the study design justifies that status.
- Use terms such as "reference", "observed history", "human-maintained organization", "alignment", or "agreement" for reference-based metrics.
- Explain what the reference-based metric can support. For example, ARI-like grouping scores support similarity to a maintained partition, not absolute semantic correctness.
- Combine metrics to support a practical claim. A validity gate can show that the output is executable; a reference score can show human-aligned structure; a behavioral probe can show task-relevant containment; alternative references or clean subsets can show that the pattern is not an artifact of one labeling choice.
- State the claim at the highest supported level. "Usable draft histories" may be supported when outputs are replayable, structured, and behaviorally meaningful; "fully automatic high-quality histories" usually needs stronger evidence.
- Avoid saying the method "fails to match the true boundary" when the paper has already argued that no unique true boundary exists. Say that stronger methods show greater alignment with a maintained reference, or that precise boundary agreement remains variable.

When a reader asks "so what do the metrics prove?", answer in prose before adding more numbers. A useful template is:

"Together, these signals indicate that the system can produce [bounded artifact] that is [validity property] and [alignment/practical property]. The strongest setting exceeds [meaningful simple baseline], while weaker settings remain [bounded comparison]."

### Tables and Figures

Tables and figures must be understandable as standalone paper artifacts.

Check:

- The artifact is mentioned and interpreted in the main text.
- The caption explains abbreviations, units, thresholds, and non-obvious row/column names.
- Numeric columns are aligned and readable in the target format.
- Column names are not over-abbreviated when space allows.
- A multi-row or grouped header is used when it clarifies related columns.
- One row or cell is explained in prose if the table encodes a new metric.
- The caption states either the takeaway or enough metric semantics for the takeaway to be recoverable.

Remove a figure if it repeats a table without adding an interpretive visual pattern. Keep a figure only when it makes comparison, trend, or tradeoff easier to see.

For paper-facing figures:

- Render and inspect the actual PDF/PNG before finalizing. Code that looks reasonable can still produce overlapping labels or unreadable text after LaTeX scaling.
- First decide whether the figure should be single-column or double-column. Use the paper's normal column width by default; reserve `figure*` for visuals whose information would be lost in one column.
- If a double-column figure creates a large blank region, inspect float barriers and placement before shrinking the figure. `\FloatBarrier` near `figure*` often forces awkward page breaks.
- If a single-column figure is crowded, reduce label density, increase height, direct-label only the most important series, or split unrelated claims into separate figures.
- Do not put all result dimensions into one figure if each panel supports a different claim. A smaller set of focused figures is usually easier to read.
- Captions should do enough semantic work that a reader can understand what is being compared and why the comparison matters.

### Related Work

Organize by the function prior work serves in the argument, not by every keyword. Two or three broad strands are usually stronger than many thin subsections. Use comparison tables only when each column supports a concrete distinction needed for the paper.

### Threats

Group threats into a few categories such as construct/comparison, dataset/harness integrity, and external validity. State how the design bounds the threat; do not bury the reader in generic caveats.

## Prose Naturalness Checks

- Replace repeated one-sentence paragraphs with connected explanations.
- Avoid strings of noun phrases where verbs would explain the relation.
- Avoid exaggerated claims such as "fills a critical gap" unless the evidence justifies them.
- Avoid overly symbolic wording in narrative prose.
- Do not overuse "not merely X but Y" or other contrast templates.
- Keep technical specificity, but make the sentence read like a human expert explaining the point.
- Avoid informal system-name formulas in prose when they read like log labels. Use formal names and parenthetical model details where needed.
- Avoid prescriptive "guidelines" language unless the paper actually validates guidelines. Prefer "implications", "design considerations", or "suggests that future agents could...".
- Do not say a cause is clear if the study did not directly investigate that cause. For example, avoid saying problem descriptions are clear unless clarity was measured.

## Evidence Discipline

- Distinguish benchmark observations from general claims about a model or framework.
- Name confounds when model and harness are coupled.
- Keep admission criteria, validation checks, and scoring rules separate.
- Do not let a pass/fail result imply semantic correctness unless the evaluation tests that behavior.
- State when examples are illustrative rather than representative.
- When a conclusion is "limited impact", show both why the headline difference is small and why execution still helps some cases.
- When discussing execution feedback, separate attempts, completed runs, actionable signals, and official evaluation outcomes.
- When an analysis uses manual inspection or crafted metrics to test assumptions, state the assumptions and the corresponding metric or inspection protocol.
