#!/usr/bin/env python3
"""
Initialize a reusable auto-research workspace for a new objective.

Usage:
    python scripts/init_loop.py --name "lead-gen-experiment"
    python scripts/init_loop.py --name "prompt-optimization" --path .auto-research
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


SCORECARD_TEMPLATE = """# Objective

## Outcome
- TODO

## Primary Metric
- Main number or rubric: TODO
- Better direction: TODO
- Baseline: TODO

## Guardrails
- Max budget: TODO
- Max time per round: TODO
- Safety and policy constraints: TODO
- Quality floor: TODO

## Action Surface
- The agent may change:
  - TODO

## Frozen Surface
- The agent must not change:
  - TODO

## Approval Gates
- Requires human approval before:
  - TODO

## Stop Conditions
- Pause when:
  - TODO
"""


RUNBOOK_TEMPLATE = """# Research Runbook

Use this folder as the operating surface for one long-horizon objective.

## Loop
1. Define or update the scorecard in `scorecard.md`.
2. Record the current frontier in `frontier-summary.md`.
3. Log every round in `results.tsv`.
4. Write short conclusions in `journal.md`.
5. Advance only when the evidence justifies `keep`.

## Decision Vocabulary
- baseline
- keep
- discard
- retry
- escalate
"""


FRONTIER_TEMPLATE = """# Frontier Summary

## Current best state
- Best metric: TODO
- Winning configuration: TODO

## Confirmed wins
- TODO

## Confirmed losses
- TODO

## Open questions
- TODO

## Next queue
1. TODO
2. TODO
3. TODO
"""


JOURNAL_TEMPLATE = """# Journal

## Round 1
- Hypothesis: TODO
- Change: TODO
- Expected effect: TODO
- Actual result: TODO
- Decision: TODO
- Why: TODO
- Next best move: TODO
"""


RESULTS_TEMPLATE = """round\tstatus\tprimary_metric\tdelta\tcost\tchange_summary\tnotes
1\tbaseline\t0.0000\t0.0000\t0\tinitial state\tstarting point
"""


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value or "research-loop"


def write_file(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Initialize an auto-research loop workspace")
    parser.add_argument("--name", required=True, help="Human-readable objective name")
    parser.add_argument(
        "--path",
        default=".auto-research",
        help="Parent directory where the loop folder should be created",
    )
    args = parser.parse_args()

    root = Path(args.path).resolve()
    slug = slugify(args.name)
    loop_dir = root / slug
    loop_dir.mkdir(parents=True, exist_ok=True)

    files = {
        "scorecard.md": SCORECARD_TEMPLATE,
        "runbook.md": RUNBOOK_TEMPLATE,
        "frontier-summary.md": FRONTIER_TEMPLATE,
        "journal.md": JOURNAL_TEMPLATE,
        "results.tsv": RESULTS_TEMPLATE,
    }

    for filename, content in files.items():
        path = loop_dir / filename
        if not path.exists():
            write_file(path, content)

    print(f"[ok] initialized auto-research loop at {loop_dir}")
    for filename in files:
        print(f"- {loop_dir / filename}")


if __name__ == "__main__":
    main()
