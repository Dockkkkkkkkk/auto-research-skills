#!/usr/bin/env python3
"""
为新的长周期目标初始化自动研究工作区。

Usage:
    python scripts/init_loop.py --name "线索增长实验"
    python scripts/init_loop.py --name "提示词优化" --path .auto-research
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


SCORECARD_TEMPLATE = """# Objective

## Outcome
- TODO

## Primary Metric
- 主指标或评分规则：TODO
- 优化方向：TODO
- Baseline：TODO

## Guardrails
- 最大预算：TODO
- 单轮最大时间：TODO
- 安全与合规限制：TODO
- 质量下限：TODO

## Action Surface
- agent 可以改动：
  - TODO

## Frozen Surface
- agent 不可改动：
  - TODO

## Approval Gates
- 以下动作必须人工批准：
  - TODO

## Stop Conditions
- 以下情况必须暂停：
  - TODO
"""


RUNBOOK_TEMPLATE = """# Research Runbook

这个目录是单个长周期目标的操作面。

## Loop
1. 在 `scorecard.md` 中定义或更新记分卡。
2. 在 `frontier-summary.md` 中记录当前 frontier。
3. 在 `results.tsv` 中记录每一轮结果。
4. 在 `journal.md` 中写简短结论。
5. 只有证据足够时才把结果推进为 `keep`。

## Decision Vocabulary
- baseline
- keep
- discard
- retry
- escalate
"""


FRONTIER_TEMPLATE = """# Frontier Summary

## 当前最好状态
- 最佳指标：TODO
- 当前最优配置：TODO

## 已确认有效
- TODO

## 已确认无效
- TODO

## 未解决问题
- TODO

## 下一批候选
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
1\tbaseline\t0.0000\t0.0000\t0\t初始状态\t起点
"""


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value or "research-loop"


def write_file(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="初始化自动研究工作区")
    parser.add_argument("--name", required=True, help="目标名称")
    parser.add_argument(
        "--path",
        default=".auto-research",
        help="工作区父目录",
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

    print(f"[ok] 已初始化自动研究工作区: {loop_dir}")
    for filename in files:
        print(f"- {loop_dir / filename}")


if __name__ == "__main__":
    main()
