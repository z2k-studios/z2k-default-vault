---
feature_number: "146"
description: "When Where Who block template — date/location/who context anchor for memory cards"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/146 - When Where Who/"
---

# Feature 146 — When Where Who

## Description
The When Where Who template is a block template in the Memories domain that provides a reusable date, location, and people context anchor for memory cards. It captures the temporal, spatial, and social dimensions of a memory — when it happened, where it took place, and who was involved — as an embeddable block that can be included in document templates.

## Requirements
### 146-001 — Template file exists `[quantitative]`
Template file exists at `Memories/Templates/When Where Who.md`.

### 146-002 — All fields have fieldInfo declarations `[quantitative]`
Every user-prompted field in the template has a corresponding `{{fieldInfo}}` declaration.

### 146-003 — Renders correctly via Command Queue `[quantitative]`
Template renders without error when invoked via Command Queue JSON packet with standard test data. Output matches expected golden file after dynamic field normalization.

### 146-004 — Quality meets scorecard threshold `[qualitative]`
AI quality scorecard assessment meets or exceeds the 70% passing threshold.
