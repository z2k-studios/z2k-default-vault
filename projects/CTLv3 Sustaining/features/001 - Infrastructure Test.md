---
feature_number: "001"
description: "Validates that the project structure, testing infrastructure, and Command Queue system are operational"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/001 - Infrastructure Test/"
---

# Feature 001 — Infrastructure Test

## Description

This is the foundational feature that validates the project's own testing infrastructure before any other tests run. A failure here means the testing system itself is broken and no other feature tests are trustworthy.

It checks three things:

1. **Project structure** — the CTLv3 Sustaining project folder contains all expected directories (`features/`, `tests/`, `drop/`, `tests/shared/`).
2. **Python environment** — Python 3.x is available and test scripts can execute.
3. **Command Queue smoke test** — a trivial "hello world" JSON packet is dropped into the Command Queue, processed by Obsidian, and the resulting output file is verified. This confirms that the rendering pipeline (JSON → Command Queue → Z2K Templates Plugin → output file) is operational.

If Feature 001 fails, no other tests should run. The regression script should abort early.


## Requirements

### 001-001 — Project folder structure exists `[quantitative]`

The following directories exist within the Primary Project Folder:
- `features/`
- `tests/`
- `tests/shared/`
- `drop/`

### 001-002 — Python 3.x available `[quantitative]`

`python3 --version` executes successfully and returns a version ≥ 3.8.

### 001-003 — Test scripts are executable `[quantitative]`

`tests/run_all_tests.py` exists and can be invoked without import errors (dry-run or `--help` flag).

### 001-004 — Command Queue is operational `[quantitative]`

A hello world JSON packet is created:
```json
{
  "cmd": "new",
  "templateContents": "Hello {{Name}}!",
  "fileTitle": "hello-world-test",
  "prompt": "none",
  "finalize": true,
  "Name": "World"
}
```
Dropped into the Command Queue folder, processed within 30 seconds, and the resulting output file contains "Hello World!". The output file is cleaned up after verification.

### 001-005 — Obsidian is running `[quantitative]`

The test script can detect that Obsidian is running (process check or Command Queue responsiveness from 001-004).

### 001-006 — Command Queue folder exists `[quantitative]`

The Command Queue watched directory exists and is writable.

### 001-007 — Error log monitoring is operational `[quantitative]`

The Z2K Templates Error Log file exists at `.obsidian/plugins/z2k-plugin-templates/error-log.md` within the vault. The test framework can record the log's byte offset before a test and read new entries after. The error log monitoring utility is validated by confirming it correctly detects newly written content (simulated by checking that the hello world Command Queue test in 001-004 did not produce any Warning-or-above log entries).
