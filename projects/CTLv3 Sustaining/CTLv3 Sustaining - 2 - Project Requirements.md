---
Description: Project Requirements Document for the CTLv3 Sustaining project — describes the structural conventions for features and requirements rather than listing individual requirements.
document_type: Project Requirements
status: Draft
---

# Project Requirements - CTLv3 Sustaining


## 1. Purpose

This document defines the structural conventions for how features and their requirements are organized within this sustaining project. Individual feature requirements live in their respective feature files inside the `features/` folder — this document does not index or duplicate them.

The feature files are self-documenting: the `features/` folder serves as the living registry of all validated capabilities, and each file's YAML frontmatter provides a machine-greppable summary.


## 2. Feature File Conventions

### 2.1 Location and Naming

Feature files reside in the `features/` subfolder of the Primary Project Folder. Each file is named:

```
NNN - <Feature Name>.md
```

Where `NNN` is a zero-padded three-digit number assigned sequentially (001, 002, 003, ...).


### 2.2 YAML Frontmatter

Every feature file must include YAML frontmatter with at minimum:

```yaml
---
feature_number: "NNN"
description: "<Brief one-line description of the feature>"
status: "<Current status in the per-feature cycle>"
date_added: "<YYYY-MM-DD>"
test_folder: "tests/NNN - <Feature Name>/"
---
```

This enables quick discovery via YAML grep (e.g., `grep "status: Complete" features/*.md` to find all completed features, or `grep "description:" features/*.md` for a one-line summary of every feature).


### 2.3 Feature Status Values

Feature status tracks progression through the per-feature implementation cycle defined in the SoW's Project Framework:

| Status | Meaning |
|---|---|
| `Describing` | Feature description being fleshed out from drop folder input |
| `Requirements` | Requirements being defined and iterated with the user |
| `Testing` | Test plan and scripts being developed |
| `Implementing` | External implementation in progress (handoff) |
| `Acceptance` | Acceptance testing in progress |
| `Complete` | All tests passing, feature fully validated |
| `Failed` | Feature failed acceptance, needs iteration |


### 2.4 Requirement Conventions

Within each feature file, requirements are listed under a `## Requirements` section. Each requirement has:

- A three-digit ID (forming a compound `NNN-RRR` identifier with the feature number)
- A heading in the format `### NNN-RRR — <Requirement Name>`
- A description of the expected behavior, outcome, or aspect
- Sufficient specificity to be independently testable


### 2.5 Requirement IDs

The compound ID `NNN-RRR` (feature number–requirement number) uniquely identifies every requirement across the project. For example:

- `002-001` = Feature 002, Requirement 001
- `002-003` = Feature 002, Requirement 003

These IDs are referenced by test plans and test scripts for traceability.


## 3. Feature Numbering Scheme

| Range | Purpose | Count |
|---|---|---|
| 001–004 | Infrastructure | 4 features (Infrastructure Test, Working System, Directory Structure, System Blocks) |
| 020 | Cross-cutting quality | 1 feature (Global Template Quality [quantitative]) |
| 900 | Quality gate | 1 feature (Template Quality Gate — validates all individual template qualitative results are present, recent, and passing) |
| 040–052 | Domain-level | 13 features (one per CTL domain) |
| 100–179 | Individual templates | 71 features (one per template file: 58 document + 13 block) |

Total: 90 features.


## 4. Cross-Cutting Requirements

Cross-cutting requirements are captured in dedicated features rather than in this document:

- **Feature 020 — Global Template Quality** — quantitative checks that apply to every template (valid syntax, metadata, naming conventions, field declarations, source type validation, etc.). Its test suite iterates over all templates in the vault.
- **Feature 900 — Template Quality Gate** — aggregation gate that validates all individual template features (100–899) have recent, passing qualitative results. Does not perform AI assessment itself — each individual template feature owns its own qualitative check against the Template Quality Scorecard.

Qualitative assessment (documentation, readability, capability showcase, modularity, edge case handling, etc.) is performed per-template as part of each individual template feature's requirements (e.g., 100-004, 107-004). The Template Quality Scorecard defines the scoring criteria used by the AI quality agent.


## 5. Domain Knowledge

The CTLv3 library spans 13 top-level domains plus 1 subdomain. Each domain has a `.system-block.md` for YAML injection and a `Templates/` subfolder for its templates.

| Domain | Templates (doc + block) | System Block Fields | Notes |
|---|---|---|---|
| Information | 21 + 5 | domain, ratings | Largest domain; podcast architecture (generic + 6 host-specific presets) |
| Thoughts | 7 + 0 | domain, ratings | |
| Beliefs | 1 + 0 | domain, ratings | Simplest domain (default template only) |
| Memories | 4 + 1 | domain, ratings | Block: When Where Who |
| Interactions | 6 + 1 | domain | Block: Logistics |
| Journals | 2 + 0 | domain, privacy (Journal) | Daily Journal absorbs retired Ideas domain |
| Logs | 5 + 0 | domain, privacy (Log) | |
| Locations | 1 + 0 | domain | |
| Projects | 3 + 0 | domain, system-block-stop | Templates use non-z2k YAML structure |
| Projects/My Writings | 3 + 0 | (inherits; has own .system-block-stop) | Subdomain; "(General)" postfix = GH #182 workaround |
| Entities | 1 + 0 | domain | Minimal; full CRM deferred (CTLP-001) |
| Body | 1 + 1 | domain | Block: Health Log (Flame fields preserved) |
| AI | 0 + 0 | domain, perspective (AI) | System block only; templates deferred (CTLP-002) |
| System | 1 + 0 | domain | |

Root `Templates/` folder: 2 document + 5 block = 7 cross-domain templates.

**Total: 58 document templates + 13 block templates + 14 system blocks = 85 artifacts.**

For the complete template inventory with paths, source types, authors, and privacy settings, see `User Feedback/Migration Project Mining Results.md` §1.


## 6. Feature Discovery

To get a quick overview of all features and their statuses:

- **List the `features/` folder** — file names provide feature numbers and names
- **Grep `description:`** across feature files to get one-line summaries
- **Grep `status:`** across feature files to filter by lifecycle stage

No separate index document is maintained — the folder structure is the index.
