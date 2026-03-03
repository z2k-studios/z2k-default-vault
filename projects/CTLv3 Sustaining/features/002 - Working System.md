---
feature_number: "002"
description: "Validates that a real template can be rendered end-to-end via Command Queue with system block injection"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/002 - Working System/"
---

# Feature 002 — Working System

## Description

Feature 001 validates infrastructure with an inline template (`templateContents`). This feature goes further: it tests the full rendering pipeline using a real template file via `templatePath`, which triggers system block injection. This is the "real" hello world — confirming that the CTL template library can actually produce cards.

The test uses a simple, existing template (e.g., `Beliefs (General).md`) and verifies that:
- The rendered output file is created
- System block YAML from both the root `.system-block.md` and the domain `.system-block.md` is correctly injected
- Field values supplied in the JSON packet appear in the output
- The output matches the expected golden file

This feature is the gate between "testing infrastructure works" and "the template system works."


## Requirements

### 002-001 — Template renders via templatePath `[quantitative]`

A JSON packet using `templatePath` (pointing to a real template in the vault) produces an output file when processed by the Command Queue.

### 002-002 — Root system block YAML injected `[quantitative]`

The rendered output file contains YAML fields from the root `.system-block.md` (e.g., `z2k_metadata_version: 3.00`, `z2k_creation_library_version: "3.0.0"`).

### 002-003 — Domain system block YAML injected `[quantitative]`

The rendered output file contains the domain-specific `z2k_creation_domain` value from the domain's `.system-block.md`.

### 002-004 — Field values resolved `[quantitative]`

Field values supplied in the JSON packet (e.g., a description field) appear correctly in the rendered output body.

### 002-005 — Dynamic fields resolve `[quantitative]`

Built-in dynamic fields (`{{wikilink today}}`, `{{timestamp}}`, `{{wikilink creator}}`) resolve to actual values (not raw Handlebars expressions) in the output.

### 002-006 — Output matches expected `[quantitative]`

After normalizing dynamic fields (per the normalization rules in the Testing Plan), the rendered output matches the golden expected file.
