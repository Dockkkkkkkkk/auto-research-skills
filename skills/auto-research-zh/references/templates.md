# 自动研究模板

## Scorecard 模板

```md
# Objective

## Outcome
- 想达成什么结果？

## Primary Metric
- 主指标或评分规则：
- 越大越好还是越小越好：
- 当前 baseline：

## Guardrails
- 最大预算：
- 单轮最大时间：
- 安全与合规限制：
- 质量下限：

## Action Surface
- agent 可以改动：

## Frozen Surface
- agent 不可改动：

## Approval Gates
- 以下动作必须人工批准：

## Stop Conditions
- 以下情况必须暂停：
```

## TSV 日志模板

```tsv
round	status	primary_metric	delta	cost	change_summary	notes
1	baseline	0.0000	0.0000	0	初始状态	起点
```

状态值：

- `baseline`
- `keep`
- `discard`
- `retry`
- `escalate`

## 单轮记录模板

```md
## Round N
- Hypothesis:
- Change:
- Expected effect:
- Actual result:
- Decision:
- Why:
- Next best move:
```

## Frontier Summary 模板

```md
# Frontier Summary

## 当前最好状态
- 最佳指标：
- 当前最优配置：

## 已确认有效
- ...

## 已确认无效
- ...

## 未解决问题
- ...

## 下一批候选
1. ...
2. ...
3. ...
```

## 交接模板

```md
# Handoff

## Goal
- ...

## Current frontier
- ...

## What was tried
- ...

## What to avoid repeating
- ...

## Recommended next experiments
1. ...
2. ...
3. ...
```
