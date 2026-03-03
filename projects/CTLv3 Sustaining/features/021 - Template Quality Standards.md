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
