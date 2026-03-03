#!/usr/bin/env python3
"""YAML parsing and assertion helpers for CTL v3 testing."""

import re


def load_yaml_frontmatter(path):
    """Load YAML frontmatter from a markdown file. Returns dict of fields."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {}

    fields = {}
    for line in match.group(1).splitlines():
        # Simple key: value parsing (handles quoted and unquoted values)
        kv = re.match(r'^(\S+):\s*(.*)', line)
        if kv:
            key = kv.group(1)
            value = kv.group(2).strip()
            # Strip surrounding quotes
            if (value.startswith('"') and value.endswith('"')) or \
               (value.startswith("'") and value.endswith("'")):
                value = value[1:-1]
            fields[key] = value
    return fields


def load_raw_yaml(path):
    """Load YAML fields from a file without frontmatter fences (e.g., system blocks).
    Parses all key: value lines, ignoring comments and blank lines."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    fields = {}
    for line in content.splitlines():
        line_stripped = line.strip()
        if not line_stripped or line_stripped.startswith("#"):
            continue
        kv = re.match(r'^(\S+):\s*(.*)', line)
        if kv:
            key = kv.group(1)
            value = kv.group(2).strip()
            if (value.startswith('"') and value.endswith('"')) or \
               (value.startswith("'") and value.endswith("'")):
                value = value[1:-1]
            fields[key] = value
    return fields


def load_file_text(path):
    """Load full file content as text."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def assert_field_present(frontmatter, field):
    """Assert that a field exists in frontmatter. Returns (passed, message)."""
    if field in frontmatter:
        return True, f"Field '{field}' present"
    return False, f"Field '{field}' MISSING from frontmatter"


def assert_field_value(frontmatter, field, expected):
    """Assert that a field has the expected value. Returns (passed, message)."""
    if field not in frontmatter:
        return False, f"Field '{field}' MISSING from frontmatter"
    actual = frontmatter[field]
    if actual == expected:
        return True, f"Field '{field}' = '{expected}'"
    return False, f"Field '{field}': expected '{expected}', got '{actual}'"
