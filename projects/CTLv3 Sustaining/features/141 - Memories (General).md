---
feature_number: "141"
description: "Memories (General) document template — domain default for the Memories domain"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/141 - Memories (General)/"
---

# Feature 141 — Memories (General)

## Description
The Memories (General) template is the domain default document template for the Memories domain. It captures personal memories, experiences, and recollections with structured fields for recording what happened, when, where, and the emotional or contextual significance of the memory.

## Requirements
### 141-001 — Template file exists `[quantitative]`
Template file exists at `Memories/Templates/Memories (General).md`.

### 141-002 — All fields have fieldInfo declarations `[quantitative]`
Every user-prompted field in the template has a corresponding `{{fieldInfo}}` declaration.

### 141-003 — Renders correctly via Command Queue `[quantitative]`
Template renders without error when invoked via Command Queue JSON packet with standard test data. Output matches expected golden file after dynamic field normalization.

### 141-004 — Quality meets scorecard threshold `[qualitative]`
AI quality scorecard assessment meets or exceeds the 70% passing threshold.
