---
Description: Template Quality Scorecard for CTLv3 Sustaining — defines the qualitative assessment criteria used by the AI quality agent. Derived from Feature 021 requirements. Source of truth for all qualitative scoring.
document_type: Template Quality Scorecard
status: Active
source_feature: "features/021 - Template Quality Standards.md"
global_threshold: 70
---

# Template Quality Scorecard — CTLv3 Sustaining

This scorecard is used by the AI quality agent during qualitative testing. Each item maps to a requirement in `features/021 - Template Quality Standards.md`. When the feature requirements change, update this scorecard to match.

The global passing threshold is **70%** (see Testing Plan §3.2.3). A template passes qualitative testing if its score meets or exceeds this threshold. Per-feature overrides are documented in each feature's `test_plan.md`.

---

## How to Use This Scorecard

The AI quality agent receives:
1. The full template source (`.md` file with YAML frontmatter and Handlebars body)
2. This scorecard
3. The feature's requirements file (for context)

For each scorecard item, the agent evaluates the template and assigns **Pass**, **Fail**, or **Partial**:
- **Pass** — fully meets the criterion
- **Partial** — partially meets it (counts as **0** toward the score)
- **Fail** — does not meet it

**Score = (number of Pass items) / (total items) × 100**

---

## Scorecard Items

### Item 021-001 — Documentation Quality
**Source:** Feature 021 requirement 021-001

Does the template contain Handlebars comments (`{{!-- ... --}}`) that explain non-obvious logic, field purposes, and structural choices?

**Pass if:** Comments are present and informative — they explain *why*, not just *what*. Field purposes are described. Non-obvious conditionals or helper usage is annotated.

**Fail if:** No comments exist, or comments are purely decorative (e.g., only `{{!-- Section Header --}}` with no explanatory content).

---

### Item 021-002 — Raw Markdown Readability
**Source:** Feature 021 requirement 021-002

Does the template look clean and organized when viewed as raw Markdown?

**Pass if:** Consistent indentation, comment break bars between sections where appropriate, logical grouping of related content, and no visual clutter from dense Handlebars expressions packed on a single line.

**Fail if:** Dense, unspaced Handlebars chains; inconsistent indentation; sections run together without visual separation.

---

### Item 021-003 — Capability Showcase
**Source:** Feature 021 requirement 021-003

Does the template use advanced Z2K Templates plugin features where appropriate?

**Pass if:** At least one of the following is used where appropriate for the template's purpose: multi-select fields, conditional rendering with Handlebars helpers, `formatStringBulletize` for optional sections, system block integration, block partial inclusion. The template demonstrates at least one level of complexity beyond the minimum needed.

**Fail if:** The template uses only bare field references (`{{FieldName}}`) with no helpers, conditionals, or advanced features, when the use case clearly warrants them.

**Note:** Simple block templates or minimal starter templates may score lower here by design. A `quality_override: pass` in the feature's `test_plan.md` is appropriate for such cases.

---

### Item 021-004 — AI-Awareness
**Source:** Feature 021 requirement 021-004

Is the template structured for AI processing?

**Pass if:** Field names are descriptive and self-documenting (not cryptic abbreviations). The YAML schema — combining system block fields plus template-specific `{{fieldInfo}}` declarations — provides enough context for an AI agent to understand the card's purpose and content without reading the body.

**Fail if:** Field names are abbreviated, ambiguous, or require the body text to understand. The YAML alone does not identify the card's domain or purpose.

---

### Item 021-005 — Edge Case Resilience
**Source:** Feature 021 requirement 021-005

Does the template degrade gracefully when fields are empty, contain special characters, or have unexpected but valid data?

**Pass if:** Optional sections use conditional blocks (`{{#if FieldName}}...{{/if}}`) or `formatStringBulletize` to suppress empty headers and orphaned formatting. The template does not produce broken Markdown (empty `#` headers, dangling `---` separators, or orphaned bullets) when optional fields are blank.

**Fail if:** Blank optional fields produce empty section headers, orphaned formatting, or visual artifacts in the rendered output.

---

### Item 021-006 — Modularity
**Source:** Feature 021 requirement 021-006

Can block insertions be toggled without breaking the template?

**Pass if:** Optional block partials (`{{> "BlockName"}}`) are either: (a) independently removable without breaking surrounding content, or (b) documented with the opt-in comment pattern (`{{!-- To include: {{> "Block"}} --}}`). Removing an optional block does not leave empty lines or broken formatting.

**Fail if:** Block partials are required for the template to render correctly; removing them causes errors or visual artifacts.

---

### Item 021-007 — Automation Readiness
**Source:** Feature 021 requirement 021-007

For templates expected to receive data from external automation, are fields structured for machine input?

**Pass if:** Fields intended for automation use `directives="no-prompt"` in their `{{fieldInfo}}` declarations. The JSON packet interface is clean: field names are predictable and the template can be fully populated without human interaction.

**N/A (counts as Pass):** Templates not in the Logs domain or otherwise not designed for automated data ingestion.

**Fail if:** Automation fields lack `no-prompt` directives, causing the plugin to prompt during automated rendering.

---

### Item 021-008 — Cross-Template Consistency
**Source:** Feature 021 requirement 021-008

Does the template follow the structural conventions of its domain?

**Pass if:** Section ordering, heading levels, and comment style match other templates in the same domain. Shared structural elements (e.g., `[!me]` callout sections, `[!source]` sections) use the same format across all templates.

**Fail if:** The template uses a different section order, heading style, or callout format than other templates in the same domain without documented justification.

---

### Item 021-009 — Block Consumer Documentation
**Source:** Feature 021 requirement 021-009
**Applies to:** Block templates only

Does the block template list which document templates include it?

**Pass if:** The block template contains a comment of the form `{{!-- Included by: [TemplateName], [TemplateName] --}}` or equivalent, listing all document templates that reference this block via `{{> "BlockName"}}`.

**N/A (counts as Pass):** Document templates (not block templates).

**Fail if:** The block template has no consumer list, making impact analysis difficult when the block changes.

---

### Item 021-010 — External Field Declarations
**Source:** Feature 021 requirement 021-010

Are fields populated by external automation properly declared?

**Pass if:** All fields populated by external processes (e.g., automation scripts, command queue data) have `{{fieldInfo}}` declarations with `directives="no-prompt"` or `value` as appropriate. No automation fields are bare `{{FieldName}}` references without metadata.

**N/A (counts as Pass):** Templates with no externally-populated fields.

**Fail if:** External automation fields are bare references with no `{{fieldInfo}}` declaration, leaving their purpose and behavior undocumented.

---

## Scoring Summary

| Item ID | Criterion | Weight |
|---|---|---|
| 021-001 | Documentation Quality | 1 |
| 021-002 | Raw Markdown Readability | 1 |
| 021-003 | Capability Showcase | 1 |
| 021-004 | AI-Awareness | 1 |
| 021-005 | Edge Case Resilience | 1 |
| 021-006 | Modularity | 1 |
| 021-007 | Automation Readiness | 1 |
| 021-008 | Cross-Template Consistency | 1 |
| 021-009 | Block Consumer Documentation | 1 |
| 021-010 | External Field Declarations | 1 |
| **Total** | | **10 items** |

All items are equally weighted. N/A items count as Pass.

**Minimum passing score: 70%** (7 of 10 items must Pass)
