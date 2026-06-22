# My Writing Skill

A Codex skill for editing articles, essays, papers, manuscripts, reports, and long-form prose with a whole-document logic audit.

## What it does

- **Global coherence audit:** builds an article-level map before polishing sentences.
- **Forward reading:** reads from the beginning to the end and records what the reader knows at each point.
- **Concept order tracking:** catches concepts that appear before definition or before the reader has the needed setup.
- **Claim-evidence alignment:** checks whether claims are supported, overstated, contradicted, or misplaced.
- **Method-limitation correspondence:** verifies that limitations, methods, evaluation, and conclusions match each other.
- **Revision planning:** ties each major edit to an explicit audit entry.

## Layout

```text
SKILL.md                              # skill definition + workflow
agents/openai.yaml                    # Codex UI metadata
references/audit-checklists.md        # detailed logic audit prompts
scripts/init_article_audit.py         # creates markdown audit ledgers
```

## Install

Clone the skill collection, then symlink this skill into your Codex skills folder:

```bash
git clone https://github.com/mathieu0905/codex-skills.git
cd codex-skills
mkdir -p ~/.codex/skills
ln -s "$PWD/skills/my-writing-skill" ~/.codex/skills/my-writing-skill
```

## Usage

Inside Codex, ask for article-level revision or invoke the skill explicitly:

```text
Use $my-writing-skill to revise this article for global coherence, concept order, and section-level consistency.
```

To create an audit workspace manually:

```bash
python3 ~/.codex/skills/my-writing-skill/scripts/init_article_audit.py \
  --source "pasted-article" \
  --out article-logic-audit
```
