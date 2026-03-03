---
feature_number: "137"
description: "Ontology document template for the Thoughts domain taxonomy"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/137 - Ontology (Thoughts)/"
---

# Feature 137 — Ontology (Thoughts)

## Description
The Ontology (Thoughts) template is a document template in the Thoughts domain used for defining and organizing the domain's taxonomy. It provides structure for categorizing thought types, establishing hierarchical relationships between thought categories, and maintaining the domain's ontological framework.

## Requirements
### 137-001 — Template file exists `[quantitative]`
Template file exists at `Thoughts/Templates/Ontology.md`.

### 137-002 — All fields have fieldInfo declarations `[quantitative]`
Every user-prompted field in the template has a corresponding `{{fieldInfo}}` declaration.

### 137-003 — Renders correctly via Command Queue `[quantitative]`
Template renders without error when invoked via Command Queue JSON packet with standard test data. Output matches expected golden file after dynamic field normalization.

### 137-004 — Quality meets scorecard threshold `[qualitative]`
AI quality scorecard assessment meets or exceeds the 70% passing threshold.
