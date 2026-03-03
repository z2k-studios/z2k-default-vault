from __future__ import annotations

"""
CTLv3 Sustaining — Qualitative Assessment Agent

Invokes Claude (via the `claude` CLI or Anthropic API) to evaluate a template
against the Template Quality Scorecard. Returns a structured result.

Usage:
    from quality_agent import assess_template
    result = assess_template(template_content, scorecard_content, feature_requirements)
"""

import json
import subprocess
import sys
import textwrap
from dataclasses import dataclass, field
from pathlib import Path

from config import QUALITY_THRESHOLD_PERCENT


@dataclass
class QualityResult:
    score_percent: float
    threshold_percent: float
    item_results: list[dict] = field(default_factory=list)  # [{id, pass, notes}]
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
) -> QualityResult:
    """
    Invoke Claude to evaluate a template against the quality scorecard.

    Calls `claude` CLI with a structured prompt. Falls back to Anthropic API
    if the CLI is not available. Returns a QualityResult.

    The AI is instructed to return a JSON block with the following shape:
        {
          "score_percent": 85,
          "item_results": [
            {"id": "021-001", "pass": true, "notes": "..."},
            ...
          ],
          "suggestions": ["...", "..."]
        }
    """
    prompt = _build_prompt(template_content, scorecard_content, feature_requirements)

    # Try `claude` CLI first
    try:
        result = subprocess.run(
            ["claude", "--print", "--output-format", "text", prompt],
            capture_output=True,
            text=True,
            timeout=120,
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
) -> str:
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
        Evaluate the template against each scorecard item. For each item, determine whether the
        template passes, fails, or partially passes. Provide brief notes explaining your assessment.

        Then compute an overall score as the percentage of items that fully pass (partial = 0).

        Return your assessment as a JSON block (and nothing else after it):
        ```json
        {{
          "score_percent": <number 0-100>,
          "item_results": [
            {{"id": "<scorecard item id>", "pass": <true|false>, "notes": "<brief explanation>"}},
            ...
          ],
          "suggestions": ["<improvement suggestion>", ...]
        }}
        ```
    """).strip()


def _parse_response(response: str, threshold: float) -> QualityResult:
    """Extract the JSON assessment block from the AI response."""
    import re
    match = re.search(r'```json\s*(\{.*?\})\s*```', response, re.DOTALL)
    if not match:
        # Try bare JSON object
        match = re.search(r'(\{"score_percent".*\})', response, re.DOTALL)

    if not match:
        return QualityResult(
            score_percent=0,
            threshold_percent=threshold,
            raw_response=response,
            error="Could not parse JSON from AI response.",
        )

    try:
        data = json.loads(match.group(1))
        return QualityResult(
            score_percent=float(data.get("score_percent", 0)),
            threshold_percent=threshold,
            item_results=data.get("item_results", []),
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
