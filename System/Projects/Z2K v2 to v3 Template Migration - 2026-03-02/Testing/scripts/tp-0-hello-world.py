#!/usr/bin/env python3
"""TP-0.2 — Hello World Command Queue validation test.

Writes a minimal command to the testing vault's command queue,
then polls for the output file.

Usage:
  1. Run this script to write the command file
  2. In Obsidian, trigger "Process Command Queue Now" from the Command Palette
  3. Script polls for output and reports pass/fail
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.runner import write_command_file, poll_for_output

TESTING_VAULT = Path("Data/Vaults/z2k-testing-vaults/Z2K System Vault Testing")
QUEUE_DIR = TESTING_VAULT / ".obsidian/plugins/z2k-plugin-templates/command-queue"
OUTPUT_FILE = TESTING_VAULT / "hello-world-output.md"
DONE_DIR = QUEUE_DIR / "done"

# Hello World command payload
payload = {
    "cmd": "new",
    "templateContents": "Hello {{Name}}!",
    "fileTitle": "hello-world-output",
    "prompt": "none",
    "finalize": True,
    "Name": "World"
}


def main():
    # Clean up previous run if present
    if OUTPUT_FILE.exists():
        OUTPUT_FILE.unlink()
        print(f"Cleaned up previous output: {OUTPUT_FILE}")

    # Write command file
    cmd_path = write_command_file(str(QUEUE_DIR), "hello-world.json", payload)
    print(f"Command file written: {cmd_path}")
    print()
    print(">>> Please trigger 'Process Command Queue Now' in Obsidian <<<")
    print()

    # Poll for output
    try:
        content = poll_for_output(str(OUTPUT_FILE), timeout_s=120)
        print(f"Output file created: {OUTPUT_FILE}")
        print(f"Content:\n{content}")

        # Verify content
        if "Hello World!" in content:
            print("\nPASS: Hello World output matches expected content")
        else:
            print(f"\nFAIL: Expected 'Hello World!' in output, got:\n{content}")
            sys.exit(1)

        # Check command moved to done/
        if DONE_DIR.exists() and any(DONE_DIR.iterdir()):
            print("PASS: Command file moved to done/")
        else:
            print("WARN: Could not confirm command file in done/ — check manually")

    except TimeoutError:
        print("FAIL: Timed out waiting for output. Did you trigger 'Process Command Queue Now'?")
        sys.exit(1)


if __name__ == "__main__":
    main()
