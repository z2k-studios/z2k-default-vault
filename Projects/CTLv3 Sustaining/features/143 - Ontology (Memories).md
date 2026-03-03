---
feature_number: "143"
description: "Ontology document template for the Memories domain taxonomy"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/143 - Ontology (Memories)/"
---

# Feature 143 — Ontology (Memories)

## Description
The Ontology (Memories) template is a document template in the Memories domain used for defining and organizing the domain's taxonomy. It provides structure for categorizing memory types, establishing hierarchical relationships between memory categories, and maintaining the domain's ontological framework.

## Requirements
### 143-001 — Template file exists `[quantitative]`
Template file exists at `Memories/Templates/Ontology.md`.

### 143-002 — All fields have fieldInfo declarations `[quantitative]`
Every user-prompted field in the template has a corresponding `{{fieldInfo}}` declaration.

### 143-003 — Renders correctly via Command Queue `[quantitative]`
Template renders without error when invoked via Command Queue JSON packet with standard test data. Output matches expected golden file after dynamic field normalization.

### 143-004 — Quality meets scorecard threshold `[qualitative]`
AI quality scorecard assessment meets or exceeds the 70% passing threshold.
