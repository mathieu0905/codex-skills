# Codex Skills

A collection of Codex skills for research, reviewing, and long-form writing workflows.

## Skills

| Skill | What it does |
| --- | --- |
| `article-logic-editor` | Edits articles, essays, papers, manuscripts, reports, and long-form prose with a whole-document logic audit. |
| `correctness-check` | Audits paper correctness by extracting load-bearing claims and verifying them against internal and external evidence. |
| `idea-check` | Maps research ideas, abstracts, or drafts against close prior work to identify positioning, novelty deltas, and gaps. |
| `paper-review-evaluator` | Evaluates, compares, calibrates, and ranks research papers or LLM/foundation-model technical reports. |
| `reference-authenticity-auditor` | Verifies reference existence, metadata accuracy, and citation support. |
| `su-paper-revision` | Revises academic papers structurally using SU-style supervisor comment patterns before prose polishing. |

## Layout

```text
skills/
  article-logic-editor/
    SKILL.md
    agents/openai.yaml
    references/
    scripts/
  correctness-check/
    SKILL.md
    agents/openai.yaml
    references/
  idea-check/
    SKILL.md
    agents/openai.yaml
    references/
  paper-review-evaluator/
    SKILL.md
    agents/openai.yaml
    references/
    scripts/
  reference-authenticity-auditor/
    SKILL.md
    agents/openai.yaml
    references/
    scripts/
  su-paper-revision/
    SKILL.md
    agents/openai.yaml
    references/
```

Each directory under `skills/` is a standalone skill folder.

## Install

Clone the collection:

```bash
git clone https://github.com/mathieu0905/codex-skills.git
cd codex-skills
```

Then copy or symlink the skills you want into your Codex skills folder:

```bash
mkdir -p ~/.codex/skills
ln -s "$PWD/skills/article-logic-editor" ~/.codex/skills/article-logic-editor
ln -s "$PWD/skills/correctness-check" ~/.codex/skills/correctness-check
ln -s "$PWD/skills/idea-check" ~/.codex/skills/idea-check
ln -s "$PWD/skills/paper-review-evaluator" ~/.codex/skills/paper-review-evaluator
ln -s "$PWD/skills/reference-authenticity-auditor" ~/.codex/skills/reference-authenticity-auditor
ln -s "$PWD/skills/su-paper-revision" ~/.codex/skills/su-paper-revision
```

If a skill with the same name already exists, remove or rename the old folder first.

## Use

Invoke a skill explicitly:

```text
Use $article-logic-editor to revise this article for global coherence, concept order, and section-level consistency.
```

```text
Use $idea-check to map this research idea against close prior work and identify defensible gaps.
```

```text
Use $correctness-check to verify this paper's load-bearing claims against its evidence.
```

```text
Use $paper-review-evaluator to score and compare this paper against nearby accepted work.
```

```text
Use $reference-authenticity-auditor to audit this manuscript's references for authenticity, metadata accuracy, and citation support.
```

```text
Use $su-paper-revision to revise this paper section with structural critique before polishing.
```
