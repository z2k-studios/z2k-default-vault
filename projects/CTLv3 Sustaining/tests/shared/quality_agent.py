from __future__ import annotations

"""
CTLv3 Sustaining — Qualitative Assessment Agent

Invokes Claude (via the `claude` CLI or Anthropic API) to evaluate a template
against the Template Quality Scorecard. Returns a structured result.

Usage:
    from quality_agent import assess_template
    result = assess_template(template_content, scorecard_content, feature_requirements)

    # With active item filtering (zero-weight items excluded):
    result = assess_template(..., active_item_ids=["021-001", "021-002", ...])
"""

import json
import os
import subprocess
import sys
import textwrap
from dataclasses import dataclass, field
from pathlib import Path

from config import QUALITY_THRESHOLD_PERCENT


@dataclass
class QualityResult:
    score_percent: float            # Simple average of raw item scores (0–100)
    threshold_percent: float
    item_results: list[dict] = field(default_factory=list)  # [{id, score, notes}]
    suggestions: list[str] = field(default_factory=list)
    raw_response: str = ""
    error: str | None = None

    @property
    def passed(self) -> bool:
        return self.score_percent >= self.threshold_percent


def assess_template(
    template_content: str,
    scorecard_content: str,
    feature_requirements: str,
    threshold: float = QUALITY_THRESHOLD_PERCENT,
    active_item_ids: list[str] | None = None,
) -> QualityResult:
    """
    Invoke Claude to evaluate a template against the quality scorecard.

    Calls `claude` CLI with a structured prompt. Falls back to Anthropic API
    if the CLI is not available. Returns a QualityResult.

    Parameters
    ----------
    active_item_ids
        If provided, only these scorecard item IDs are evaluated. Items with
        weight=0 should be excluded by the caller before passing this list.
        If None, all items in the scorecard are evaluated.

    The AI returns a JSON block with the following shape:
        {
          "item_results": [
            {"id": "021-001", "score": 75, "notes": "..."},
            ...
          ],
          "suggestions": ["...", "..."]
        }

    score_percent on the returned QualityResult is the simple (unweighted)
    average of all item scores. Weighted scoring is computed by the caller.
    """
    prompt = _build_prompt(
        template_content, scorecard_content, feature_requirements, active_item_ids
    )

    # Try `claude` CLI first.
    # Unset CLAUDECODE so the CLI doesn't refuse to run inside an existing Claude Code session.
    # Pipe the prompt via stdin (safer than a positional arg for large prompts).
    cli_env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}
    try:
        result = subprocess.run(
            ["claude", "--print", "--output-format", "text"],
            input=prompt,
            capture_output=True,
            text=True,
            timeout=120,
            env=cli_env,
        )
        if result.returncode == 0:
            return _parse_response(result.stdout, threshold)
        print(f"claude CLI returned exit code {result.returncode}", file=sys.stderr)
        print(result.stderr, file=sys.stderr)
    except FileNotFoundError:
        print("claude CLI not found; attempting Anthropic API directly.", file=sys.stderr)
    except subprocess.TimeoutExpired:
        return QualityResult(
            score_percent=0,
            threshold_percent=threshold,
            error="Quality assessment timed out after 120s.",
        )

    # Fallback: Anthropic API via anthropic package
    try:
        import anthropic  # type: ignore
        client = anthropic.Anthropic()
        message = client.messages.create(
            model="claude-opus-4-6",
            max_tokens=2048,
            messages=[{"role": "user", "content": prompt}],
        )
        response_text = message.content[0].text
        return _parse_response(response_text, threshold)
    except ImportError:
        return QualityResult(
            score_percent=0,
            threshold_percent=threshold,
            error=(
                "Neither the `claude` CLI nor the `anthropic` Python package is available. "
                "Install one to enable qualitative testing."
            ),
        )
    except Exception as exc:
        return QualityResult(
            score_percent=0,
            threshold_percent=threshold,
            error=f"Anthropic API error: {exc}",
        )


def _build_prompt(
    template_content: str,
    scorecard_content: str,
    feature_requirements: str,
    active_item_ids: list[str] | None = None,
) -> str:
    if active_item_ids is not None:
        id_list = ", ".join(active_item_ids)
        scope_instruction = (
            f"Only evaluate the following scorecard items: {id_list}. "
            "Skip any other items — they are inactive (weight = 0) and must not appear in your output."
        )
    else:
        scope_instruction = "Evaluate all scorecard items."

    return textwrap.dedent(f"""
        You are evaluating a Z2K Templates Handlebars template against the CTLv3 Template Quality Scorecard.

        ## Template Source
        ```
        {template_content}
        ```

        ## Quality Scorecard
        {scorecard_content}

        ## Feature Requirements (for context)
        {feature_requirements}

        ## Instructions

        {scope_instruction}

        For each active scorecard item, assign a numeric score from 0 to 100 using the rubric
        defined in the scorecard for that item. Use the anchor values (0, 25, 50, 75, 100) as
        reference points; intermediate values are permitted.

        For each item's "notes" field, write 2–4 sentences that:
        1. Cite specific evidence from the template (e.g., quote a comment, name a field, describe a structural choice)
        2. Identify which rubric aspects are met and which are not
        3. Justify the numeric score you assigned

        For N/A items (defined per item in the scorecard), assign score = 100 and note the N/A condition with one sentence.

        Do NOT compute a weighted total — return only the raw per-item scores.

        Return your assessment as a JSON block, and nothing else after it:
        ```json
        {{
          "item_results": [
            {{"id": "<scorecard item id>", "score": <0-100>, "notes": "<2-4 sentence explanation with specific evidence>"}},
            ...
          ],
          "suggestions": ["<concrete improvement suggestion referencing specific template sections>", ...]
        }}
        ```
    """).strip()


def _parse_response(response: str, threshold: float) -> QualityResult:
    """Extract the JSON assessment block from the AI response."""
    import re
    match = re.search(r'```json\s*(\{.*?\})\s*```', response, re.DOTALL)
    if not match:
        # Try bare JSON object starting with item_results or score_percent
        match = re.search(r'(\{[^{}]*"item_results".*\})', response, re.DOTALL)

    if not match:
        return QualityResult(
            score_percent=0,
            threshold_percent=threshold,
            raw_response=response,
            error="Could not parse JSON from AI response.",
        )

    try:
        data = json.loads(match.group(1))
        item_results = data.get("item_results", [])

        # Compute simple average of item scores (caller handles weighted total)
        scores = [float(r.get("score", 0)) for r in item_results if "score" in r]
        avg_score = sum(scores) / len(scores) if scores else 0.0

        return QualityResult(
            score_percent=avg_score,
            threshold_percent=threshold,
            item_results=item_results,
            suggestions=data.get("suggestions", []),
            raw_response=response,
        )
    except (json.JSONDecodeError, ValueError) as exc:
        return QualityResult(
            score_percent=0,
            threshold_percent=threshold,
            raw_response=response,
            error=f"JSON parse error: {exc}",
        )
