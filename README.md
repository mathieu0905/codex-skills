# Codex Skills

A collection of Codex skills for research, reviewing, and long-form writing workflows.

## Skills

| Skill | What it does |
| --- | --- |
| `my-writing-skill` | Edits articles, essays, papers, manuscripts, reports, and long-form prose with a whole-document logic audit. |
| `llm-tech-report-evaluator` | Evaluates, compares, calibrates, and ranks research papers or LLM/foundation-model technical reports. |
| `su-paper-revision` | Revises academic papers structurally using SU-style supervisor comment patterns before prose polishing. |

## Layout

```text
skills/
  my-writing-skill/
    SKILL.md
    agents/openai.yaml
    references/
    scripts/
  llm-tech-report-evaluator/
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
ln -s "$PWD/skills/my-writing-skill" ~/.codex/skills/my-writing-skill
ln -s "$PWD/skills/llm-tech-report-evaluator" ~/.codex/skills/llm-tech-report-evaluator
ln -s "$PWD/skills/su-paper-revision" ~/.codex/skills/su-paper-revision
```

If a skill with the same name already exists, remove or rename the old folder first.

## Use

Invoke a skill explicitly:

```text
Use $my-writing-skill to revise this article for global coherence, concept order, and section-level consistency.
```

```text
Use $llm-tech-report-evaluator to score and compare this paper against nearby accepted work.
```

```text
Use $su-paper-revision to revise this paper section with structural critique before polishing.
```
