# Paper Review Evaluator

A Codex skill that evaluates, compares, and ranks research papers, submissions, and LLM / foundation-model technical reports from PDFs or extracted text. It can also auto-discover same-topic comparison papers from top venues.

## What it does

- **Auto-discovery (optional):** anchors on a target paper, derives its topic signature, and gathers ~5–8 closely-comparable, *already-accepted* papers from top venues (SE / ML / NLP / CV / Security …) using built-in `WebSearch` / `WebFetch`. Enforces a hard acceptance gate and prefers main-track, recent (~18-month) work, with OpenReview review scores used as a quality signal where available.
- **Extraction:** pulls text from every PDF into `analysis/text/` plus a `pdf_summaries.json`.
- **Anonymous multi-reviewer scoring:** spawns several blind reviewers with distinct evaluation styles (strict-rigor, innovation-focused, transferable-value, skeptical meta-reviewer) against one fixed rubric; the main agent acts as area chair to reconcile and rank.
- **Fixed rubric:** `Total = 0.40 × Innovation + 0.40 × Intrinsic Paper Value + 0.20 × Rigor`. Aesthetics is a reference-only column.
- **Output:** ranked table, per-paper rationales, optional five-tier list (`S 夯爆 / A 很夯 / B 够硬 / C 能打 / D 偏拉`), and optional A4 infographic image prompts.

## Layout

```
SKILL.md                          # skill definition + workflow
references/rubric.md              # detailed scoring prompts, tiers, output templates
scripts/extract_pdf_reports.py    # PDF → text extraction (PyMuPDF)
```

## Install

Clone the skill collection, then symlink this skill into your Codex skills folder:

```bash
git clone https://github.com/mathieu0905/codex-skills.git
cd codex-skills
mkdir -p ~/.codex/skills
ln -s "$PWD/skills/paper-review-evaluator" ~/.codex/skills/paper-review-evaluator
```

The extraction script needs PyMuPDF:

```bash
pip install pymupdf
```

## Usage

Inside Codex, ask to score, compare, rank, or gather comparison papers for a target paper, or invoke the skill explicitly:

```text
Use $paper-review-evaluator to score and compare this paper against nearby accepted work.
```

To extract PDFs manually:

```bash
python3 ~/.codex/skills/paper-review-evaluator/scripts/extract_pdf_reports.py .
```
