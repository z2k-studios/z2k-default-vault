---
feature_number: "116"
description: "Podcast Interview document template — generic podcast interview with prompted host/show fields"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/116 - Podcast Interview/"
---

# Feature 116 — Podcast Interview

## Description
The Podcast Interview template provides a generic structured format for capturing notes from podcast interviews. Unlike the host-specific podcast templates, this template does not preset host or show name fields — those are prompted at creation time. It uses the `{{> "Podcast Interview Content"}}` block partial to include the shared podcast content structure. Source type is set to `.:Z2K/SourceType/Podcast`. Located at `Information/Templates/Podcast Interview.md`, authored by Z2K Studios, LLC.

## Requirements
### 116-001 — Template file exists `[quantitative]`
### 116-002 — All fields have fieldInfo `[quantitative]`
### 116-003 — Renders correctly via Command Queue `[quantitative]`
### 116-004 — Quality meets scorecard threshold `[qualitative]`
### 116-005 — Source type is set to `.:Z2K/SourceType/Podcast` `[quantitative]`
### 116-006 — Uses `{{> "Podcast Interview Content"}}` block `[quantitative]`
### 116-007 — Does NOT preset host/show fields `[quantitative]`
