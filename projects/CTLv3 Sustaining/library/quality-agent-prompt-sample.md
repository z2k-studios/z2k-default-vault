You are evaluating a Z2K Templates Handlebars template against the CTLv3 Template Quality Scorecard.

        ## Template Source
        ```
        ---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_author: "Z2K Studios, LLC"
z2k_template_suggested_title: "{{ConciseSummary}}"
z2k_card_source_type: ".:Z2K/SourceType/LifeLessons"
---
{{fieldInfo ConciseSummary "Briefly, what is this belief?" type="text" directives="required"}}
{{fieldInfo OverviewDetails "Describe this belief in detail" type="text"}}
{{fieldInfo PrerequisitesForUnderstanding "What do you need to know to understand this?" type="text"}}
{{fieldInfo FurtherDetails "Any additional details?" type="text"}}

{{ConciseSummary}}

---

# Overview
{{OverviewDetails}}

# Prerequisites
{{PrerequisitesForUnderstanding}}

# Details
{{FurtherDetails}}

{{!-- To include Card Fabric: {{> "Card Fabric"}} --}}

        ```

        ## Quality Scorecard
        ---
Description: Template Quality Scorecard for CTLv3 Sustaining — defines the qualitative assessment criteria used by the AI quality agent. Derived from Feature 021 requirements. Source of truth for all qualitative scoring.
document_type: Template Quality Scorecard
status: Active
source_feature: "features/021 - Template Quality Standards.md"
global_threshold: 70
---

# Template Quality Scorecard — CTLv3 Sustaining

This scorecard is used by the AI quality agent during qualitative testing. Each item maps to a requirement in `features/021 - Template Quality Standards.md`. When the feature requirements change, update this scorecard to match.

The global passing threshold is **70%** (see Testing Plan §3.2.3). A template passes qualitative testing if its weighted score meets or exceeds this threshold. Per-feature overrides are documented in each feature's `test_plan.md`.

---

## How to Use This Scorecard

The AI quality agent receives:
1. The full template source (`.md` file with YAML frontmatter and Handlebars body)
2. This scorecard (filtered to only active items — those with weight > 0)
3. The feature's requirements file (for context)

For each active scorecard item, the agent assigns a **numeric score from 0 to 100**:

| Score | Meaning |
|---|---|
| 0 | Does not meet the criterion at all; quality is entirely absent |
| 25 | Minimal attempt; criterion is poorly addressed with significant gaps |
| 50 | Partial compliance; criterion is met in some areas but meaningfully absent in others |
| 75 | Solid compliance; criterion is largely met with minor gaps or missed opportunities |
| 100 | Exemplary; criterion is fully and distinctly met |

Scores between these anchors are permitted (e.g., 60 or 90).

**N/A items count as 100.** When a criterion does not apply to a template (e.g., automation readiness for a non-Logs template), score it 100. The N/A condition is defined per item below.

**Weighted final score** = Σ (item_score × item_weight%) for all active items

---

## Scorecard Items

### Item 021-001 — Documentation Quality
**Weight: 15%**
**Source:** Feature 021 requirement 021-001

Does the template contain Handlebars comments (`{{!-- ... --}}`) that explain non-obvious logic, field purposes, and structural choices?

**Scoring rubric:**

| Score | Criteria |
|---|---|
| 0 | No comments at all, or only section-divider bars with no content |
| 25 | A single comment or only cosmetic labels; no explanatory content |
| 50 | Some explanatory comments present but major sections or non-obvious constructs are unexplained |
| 75 | Most non-obvious logic and field purposes are explained; minor gaps remain |
| 100 | Comprehensive comments throughout: field purposes described, non-obvious conditionals annotated, structural choices explained with *why* not just *what* |

---

### Item 021-002 — Raw Markdown Readability
**Weight: 10%**
**Source:** Feature 021 requirement 021-002

Does the template look clean and organized when viewed as raw Markdown?

**Scoring rubric:**

| Score | Criteria |
|---|---|
| 0 | Dense, unspaced Handlebars chains; sections run together with no visual separation; chaotic indentation |
| 25 | Minimal structure; occasional spacing but largely hard to scan |
| 50 | Readable in most places but inconsistent — some sections well-spaced, others cluttered |
| 75 | Consistently clean with minor inconsistencies (e.g., one section missing a break bar, slight indentation drift) |
| 100 | Exemplary readability: consistent indentation, comment break bars between sections, logical grouping, no visual clutter from dense Handlebars on a single line |

---

### Item 021-003 — Capability Showcase
**Weight: 15%**
**Source:** Feature 021 requirement 021-003

Does the template use advanced Z2K Templates plugin features where appropriate?

**Scoring rubric:**

| Score | Criteria |
|---|---|
| 0 | Only bare `{{FieldName}}` references; no helpers, conditionals, or blocks of any kind, despite the use case clearly warranting them |
| 25 | Uses one minor feature (e.g., a single `{{#if}}`) but could use several more; minimal beyond basics |
| 50 | Uses 2–3 advanced features but misses obvious opportunities for the template's use case |
| 75 | Uses several advanced features appropriately; demonstrates meaningful complexity |
| 100 | Showcases the full range of applicable features: multi-select, `formatStringBulletize`, system block integration, conditionals, block partials — at least one beyond the minimum needed |

**Note:** Simple block templates or minimal starters may score lower here by design. Use `quality_override: pass` in the feature's `test_plan.md` for intentionally simple templates.

---

### Item 021-004 — AI-Awareness
**Weight: 15%**
**Source:** Feature 021 requirement 021-004

Is the template structured for AI processing?

**Scoring rubric:**

| Score | Criteria |
|---|---|
| 0 | Field names are cryptic abbreviations; YAML alone gives no clue about the card's purpose or domain |
| 25 | Field names are partially legible but several are ambiguous or abbreviated; domain unclear from YAML |
| 50 | Most field names are descriptive; the card's purpose is identifiable but context is incomplete |
| 75 | Field names are self-documenting and the YAML schema clearly conveys purpose; minor gaps in field coverage |
| 100 | Fully AI-legible: every field name is unambiguous and descriptive, the YAML schema (system block + template fields) comprehensively identifies the card's domain, purpose, and data shape without needing the body |

---

### Item 021-005 — Edge Case Resilience
**Weight: 15%**
**Source:** Feature 021 requirement 021-005

Does the template degrade gracefully when fields are empty or contain unexpected but valid data?

**Scoring rubric:**

| Score | Criteria |
|---|---|
| 0 | Blank optional fields produce empty section headers, orphaned `---` separators, or broken Markdown structure |
| 25 | A few guards exist but most optional fields are bare references that produce visual artifacts when blank |
| 50 | Some optional sections are guarded with `{{#if}}` or `formatStringBulletize`; others are not |
| 75 | Most optional sections are properly guarded; one or two minor gaps remain |
| 100 | All optional sections use `{{#if FieldName}}...{{/if}}` or `formatStringBulletize`; blank fields produce no empty headers, orphaned bullets, or dangling separators |

---

### Item 021-006 — Modularity
**Weight: 10%**
**Source:** Feature 021 requirement 021-006

Can block insertions be toggled without breaking the template?

**Scoring rubric:**

| Score | Criteria |
|---|---|
| 0 | Block partials are structurally required; removing any one causes errors or broken rendering |
| 25 | Most blocks are entangled with surrounding content; removal causes visual artifacts |
| 50 | Some blocks are cleanly separable; others are not |
| 75 | All blocks are removable without breaking content; optional ones mostly use the opt-in comment pattern |
| 100 | Fully modular: optional blocks use `{{!-- To include: {{> "Block"}} --}}` opt-in pattern; all block partials are independently removable without leaving empty lines or broken formatting |

---

### Item 021-007 — Automation Readiness
**Weight: 5%**
**Source:** Feature 021 requirement 021-007

For templates expected to receive data from external automation, are fields structured for machine input?

**N/A (score 100):** Templates not in the Logs domain or otherwise not designed for automated data ingestion.

**Scoring rubric (Logs/automation templates only):**

| Score | Criteria |
|---|---|
| 0 | Automation fields are bare `{{FieldName}}` references with no `fieldInfo` declarations; plugin will prompt during automated rendering |
| 25 | A few automation fields declared with `no-prompt`; most are bare |
| 50 | Roughly half of automation fields properly declared |
| 75 | Most automation fields use `directives="no-prompt"`; minor gaps |
| 100 | All automation fields have `{{fieldInfo}}` declarations with `directives="no-prompt"`; the JSON packet interface is clean and all fields are machine-populatable without human interaction |

---

### Item 021-008 — Cross-Template Consistency
**Weight: 10%**
**Source:** Feature 021 requirement 021-008

Does the template follow the structural conventions of its domain?

**Scoring rubric:**

| Score | Criteria |
|---|---|
| 0 | Section ordering, heading levels, and comment style are completely idiosyncratic with no resemblance to other templates in the domain |
| 25 | Most structural conventions are ignored; one or two elements match the domain pattern |
| 50 | Partially consistent — core sections are standard but details (callout format, heading levels, break bar style) diverge |
| 75 | Consistent with domain conventions in most respects; one or two minor deviations |
| 100 | Exemplary consistency: section order, heading levels, callout formats, and comment style all match domain conventions; shared structural elements (e.g., `[!me]` callouts) use identical format across templates |

---

### Item 021-009 — Block Consumer Documentation
**Weight: 3%**
**Source:** Feature 021 requirement 021-009
**Applies to:** Block templates only

Does the block template list which document templates include it?

**N/A (score 100):** Document templates (not block templates).

**Scoring rubric (block templates only):**

| Score | Criteria |
|---|---|
| 0 | No consumer list; no indication of which templates reference this block |
| 50 | A partial or outdated consumer list is present |
| 100 | Complete consumer list in a comment of the form `{{!-- Included by: [TemplateName], ... --}}` listing all document templates that reference this block |

---

### Item 021-010 — External Field Declarations
**Weight: 2%**
**Source:** Feature 021 requirement 021-010

Are fields populated by external automation properly declared with `{{fieldInfo}}`?

**N/A (score 100):** Templates with no externally-populated fields.

**Scoring rubric:**

| Score | Criteria |
|---|---|
| 0 | External automation fields are bare `{{FieldName}}` references with no metadata |
| 50 | Some external fields have `{{fieldInfo}}` declarations; others do not |
| 100 | All externally-populated fields have `{{fieldInfo}}` declarations with `directives="no-prompt"` or `value` as appropriate |

---

## Scoring Summary

| Item ID | Criterion | Weight |
|---|---|---|
| 021-001 | Documentation Quality | 15% |
| 021-002 | Raw Markdown Readability | 10% |
| 021-003 | Capability Showcase | 15% |
| 021-004 | AI-Awareness | 15% |
| 021-005 | Edge Case Resilience | 15% |
| 021-006 | Modularity | 10% |
| 021-007 | Automation Readiness | 5% |
| 021-008 | Cross-Template Consistency | 10% |
| 021-009 | Block Consumer Documentation | 3% |
| 021-010 | External Field Declarations | 2% |
| **Total** | | **100%** |

Items with weight 0 are inactive — they are not sent to the AI agent and not included in scoring. To deactivate an item, set its weight to 0 here and regenerate the sample prompt file.

**Weighted final score** = Σ (item_score_i × weight_i / 100) for all active items (weight > 0)

**Minimum passing score: 70%**


        ## Feature Requirements (for context)
        ---
feature_number: "021"
description: "Cross-cutting qualitative quality requirements assessed by AI scorecard agent"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/021 - Template Quality Standards/"
---

# Feature 021 — Template Quality Standards

## Description

This feature defines the qualitative quality requirements that templates are assessed against by the AI quality scorecard agent. These are subjective criteria that cannot be reduced to a deterministic script — they require judgment about readability, documentation quality, complexity showcase, and design consistency.

The Template Quality Scorecard (`CTLv3 Sustaining - Template Quality Scorecard.md`) is derived from these requirements. Each requirement here maps to one or more scorecard items. When the scorecard is updated, these requirements are the source of truth.

The test suite for this feature invokes the AI quality agent against every template and aggregates scores. The global passing threshold is 70%.


## Requirements

### 021-001 — Templates are well-documented with comments `[qualitative]`

Templates contain Handlebars comments that explain non-obvious logic, field purposes, and structural choices. Comments are informative, not just section markers.

### 021-002 — Templates are readable in raw Markdown state `[qualitative]`

Templates look clean and organized when viewed as raw Markdown. This includes: consistent indentation, comment break bars between sections, logical grouping of related content, and no visual clutter from dense Handlebars expressions.

### 021-003 — Templates showcase Z2K Templates capabilities `[qualitative]`

Templates use advanced plugin features where appropriate: multi-select fields, conditional rendering with helpers, `formatStringBulletize` for optional sections, system block integration, block partial inclusion. Templates should demonstrate at least one level of complexity beyond the minimum needed, to serve as learning examples.

### 021-004 — Templates are AI-aware `[qualitative]`

Template YAML is structured for AI processing. Field names are descriptive and self-documenting. The YAML schema (inherited from system blocks plus template-specific fields) provides enough context for an AI agent to understand the card's purpose and content without reading the body.

### 021-005 — Templates handle edge cases gracefully `[qualitative]`

Templates degrade gracefully when fields are empty, contain special characters (quotes, backslashes, Unicode), or have unexpected but valid data. Optional sections don't produce empty headers or orphaned formatting when their fields are blank.

### 021-006 — Templates are modular `[qualitative]`

Block insertions can be toggled on/off by removing or commenting out the `{{> "BlockName"}}` call. Templates don't break when an optional block is excluded. The opt-in pattern (`{{!-- To include: {{> "Block"}} --}}`) is used for non-essential blocks.

### 021-007 — Templates support automated data ingestion `[qualitative]`

Templates that are expected to receive data from external automation (especially Logs domain) have fields structured for machine input. `fieldInfo` declarations use `directives="no-prompt"` for automation fields. The JSON packet interface is clean and documented.

### 021-008 — Consistent formatting across templates `[qualitative]`

Templates within the same domain follow a consistent structural pattern: same section ordering, same heading levels, same comment style. Cross-domain consistency is also maintained for shared structural elements (e.g., all templates with `[!me]` sections use the same callout format).

### 021-009 — Block templates document their consumers `[qualitative]`

Block templates include a comment listing which document templates include them via `{{> "BlockName"}}`. This enables impact analysis when a block changes.

### 021-010 — External fields are properly declared `[qualitative]`

Fields that are populated by external automation (e.g., Flame fields in Daily Log) have `{{fieldInfo}}` declarations with appropriate directives (`no-prompt`, `value`, or equivalent) rather than being bare field references with no metadata.


        ## Instructions

        Only evaluate the following scorecard items: 021-001, 021-002, 021-003, 021-004, 021-005, 021-006, 021-007, 021-008, 021-009, 021-010. Skip any other items — they are inactive (weight = 0) and must not appear in your output.

        For each active scorecard item, assign a numeric score from 0 to 100 using the rubric
        defined in the scorecard for that item. Use the anchor values (0, 25, 50, 75, 100) as
        reference points; intermediate values are permitted. Provide brief notes explaining
        your score for each item.

        For N/A items (defined per item in the scorecard), assign score = 100 and note the N/A condition.

        Do NOT compute a weighted total — return only the raw per-item scores.

        Return your assessment as a JSON block, and nothing else after it:
        ```json
        {
          "item_results": [
            {"id": "<scorecard item id>", "score": <0-100>, "notes": "<brief explanation>"},
            ...
          ],
          "suggestions": ["<improvement suggestion>", ...]
        }
        ```