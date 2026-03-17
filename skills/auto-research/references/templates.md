# Auto Research Templates

## Scorecard Template

```md
# Objective

## Outcome
- What is the task trying to achieve?

## Primary Metric
- Main number or rubric:
- Better direction:
- Baseline:

## Guardrails
- Max budget:
- Max time per round:
- Safety and policy constraints:
- Quality floor:

## Action Surface
- The agent may change:

## Frozen Surface
- The agent must not change:

## Approval Gates
- Requires human approval before:

## Stop Conditions
- Pause when:
```

## TSV Log Template

```tsv
round	status	primary_metric	delta	cost	change_summary	notes
1	baseline	0.0000	0.0000	0	initial state	starting point
```

Status values:

- `baseline`
- `keep`
- `discard`
- `retry`
- `escalate`

## Round Note Template

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

## Frontier Summary Template

```md
# Frontier Summary

## Current best state
- Best metric:
- Winning configuration:

## Confirmed wins
- ...

## Confirmed losses
- ...

## Open questions
- ...

## Next queue
1. ...
2. ...
3. ...
```

## Handoff Template

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
