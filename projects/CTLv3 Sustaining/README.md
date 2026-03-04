---
description: "Sustaining project for the Z2K Core Template Library v3 (CTLv3) — validates every template in the library through feature-based automated and AI-assisted testing."
document_type: README
status: Active
---

# CTLv3 Sustaining

A sustaining project for the **Z2K Core Template Library v3 (CTLv3)**. Its purpose is to develop and maintain a comprehensive validation system ensuring every template works as intended: correct rendering, proper field resolution, consistent formatting, and adherence to quality standards.

## What This Project Does

The project validates the CTLv3 template library through a two-tier testing model:

- **Quantitative testing** — script-automated, deterministic. Templates are rendered via the Command Queue mechanism and diffed against expected outputs. Also includes static checks: Handlebars syntax, YAML metadata, field naming conventions, author attribution, and more.
- **Qualitative testing** — AI-assisted. The quality agent scores each template against the Template Quality Scorecard using a weighted rubric. Scores are 0–100 per item; the weighted total must meet or exceed 70% to pass.

Testing is organized around **features** — each representing a template, a domain of templates, or a cross-cutting quality concern.

## Prerequisites

- Python 3.x
- Obsidian running with the Z2K Templates plugin active (for Command Queue rendering tests)
- Command Queues enabled in Z2K Templates settings
- Claude CLI available (for qualitative tests)

## Running Tests

```bash
cd tests/

# Full regression (quantitative + qualitative AI scoring)
python3 run_all_tests.py

# Script-only (quantitative only — no AI calls, fast)
python3 run_all_tests.py --no-quality

# Single feature
python3 run_all_tests.py --feature 020

# Run a feature's tests directly
python3 "900 - Template Quality Gate/run_tests.py"
```

Exit codes: `0` = all pass, `1` = test failure(s), `2` = infrastructure error.

## Project Structure

```
CTLv3 Sustaining/
├── README.md                                      ← This file
├── CTLv3 Sustaining - 1 - Statement of Work.md   ← Project framework and processes
├── CTLv3 Sustaining - 2 - Project Requirements.md
├── CTLv3 Sustaining - 3 - Implementation Plan.md
├── CTLv3 Sustaining - 4 - Testing Plan.md        ← Test infrastructure and output contract
├── CTLv3 Sustaining - Template Quality Scorecard.md ← AI scoring rubric with weights
├── CTLv3 Sustaining - Project Phase Tracker.md   ← Session state and continuity
├── drop/          ← Intake for new feature descriptions
├── features/      ← One file per feature with requirements
├── library/       ← Reference artifacts (sample prompts, etc.)
├── tests/
│   ├── run_all_tests.py          ← Master regression script
│   ├── shared/                   ← Shared utilities and quality agent
│   │   ├── config.py
│   │   ├── test_utils.py
│   │   ├── quality_agent.py      ← AI qualitative assessment invocation
│   │   └── output_formatter.py
│   ├── 001 - Infrastructure Test/
│   ├── 002 - Working System/
│   ├── 020 - Global Template Quality/
│   ├── 1XX - <Individual Template>/  ← One per template (100–899)
│   ├── 900 - Template Quality Gate/  ← Aggregation gate (runs last)
│   └── ...
└── User Feedback/ ← Archived user feedback and design decisions
```

## Feature Numbering

| Range | Purpose |
|---|---|
| 001 | Infrastructure test (hello world, project structure) |
| 002–019 | System infrastructure (Working System, Directory Structure, System Blocks) |
| 020 | Cross-cutting quality (quantitative global checks) |
| 040–099 | Domain-level features (one per top-level CTL domain) |
| 100–899 | Individual template features (quantitative + qualitative per template) |
| 900 | Template Quality Gate (aggregation — validates all template qualitative results) |

## Key Documents

| Document | Purpose |
|---|---|
| Statement of Work | Defines the project, feature cycle, and all named processes |
| Testing Plan | Test infrastructure, output contract, and refresh procedure |
| Template Quality Scorecard | AI scoring rubric — 10 weighted items, 0–100 per item, 70% threshold |
| Project Phase Tracker | Current session state; read this first when resuming work |

## Current Status

Features 001, 003, and 020 have passing test suites. Feature 002 and 004 have known failures (missing root `.system-block.md`). Feature 900 (Template Quality Gate) is an aggregation gate — it validates results from individual template features (100–899), none of which have test infrastructure yet.

Vault location: `vaults/z2k-ctlv3-basic/` (relative to the repo root, as of 2026-03-03 reorganization).
