---
name: auto-research
description: Structures long-horizon, open-ended, research-heavy, and optimization-driven tasks as constrained iterative loops with scorecards, experiment logs, and keep-or-revert decisions. Use when progress should come from repeated exploration, measurement, and frontier management rather than a one-shot answer.
---

# Auto Research

## Overview

Use this skill to turn a vague or ambitious task into a constrained research loop. It is for execution flow, not any one domain.

## Trigger Conditions

Trigger this skill when most of the following are true:

- The task is expected to take multiple rounds, not one pass.
- The best approach is unknown and should be discovered empirically.
- There is a meaningful metric or scorecard that can guide decisions.
- The agent can test small changes safely and compare outcomes.
- Progress should be logged so future rounds can build on prior evidence.

Do not trigger this skill for:

- Simple one-shot tasks.
- Tasks with no measurable notion of progress.
- High-risk actions where repeated autonomous trials would be unsafe.

For concrete trigger examples, read `references/examples.md`.

## Quick Workflow

Copy this checklist into the work if the task is complex enough to benefit from progress tracking:

```text
Auto Research Progress:
- [ ] Step 1: Define the scorecard
- [ ] Step 2: Establish a baseline
- [ ] Step 3: Queue 2-5 hypotheses
- [ ] Step 4: Run one bounded round
- [ ] Step 5: Log result and decide keep/discard/retry/escalate
- [ ] Step 6: Update the frontier summary
```

### Step 1: Define the scorecard before acting

Before doing substantial work, define:

- Objective: what outcome matters.
- Primary metric: the main number or rubric used to compare runs.
- Guardrails: cost, time, safety, brand, legal, or approval limits.
- Action surface: what the agent is allowed to change.
- Frozen surface: what must stay fixed so results remain comparable.
- Episode size: the budget for one experiment round.
- Stop conditions: when to pause, escalate, or hand back.

If the task is externally risky, require approval before side effects. Examples: sending messages, spending money, publishing content, financial actions, account creation, or contacting users.

For a new task workspace, use `scripts/init_loop.py` to scaffold a standard loop folder.

### Step 2: Establish a baseline

Run the cheapest honest baseline first. Do not optimize before you know the current state.

Record:

- starting assumptions
- baseline metric
- current bottlenecks
- first 2-5 hypotheses worth testing

### Step 3: Iterate in short rounds

Each round should follow the same pattern:

1. Pick one hypothesis.
2. Make the smallest meaningful change.
3. Run the experiment or investigation.
4. Record the result in the loop log.
5. Decide `keep`, `discard`, `retry`, or `escalate`.

Prefer many cheap rounds over one giant rewrite. Keep the action surface narrow enough that outcomes remain interpretable.

### Step 4: Advance only on evidence

Keep a change only if it improves the primary metric or clearly improves simplicity, reliability, or cost without harming the goal.

Discard or revert when:

- the metric gets worse
- the result is inconclusive and the change adds complexity
- the change violates a guardrail
- the experiment was malformed and should be rerun cleanly

### Step 5: Maintain a frontier

After every few rounds, compress what has been learned:

- winning patterns
- losing patterns
- open questions
- next best hypotheses

Do not allow the loop to drift into random exploration. Every round should either improve the frontier or sharpen the understanding of why a direction failed.

## Decision Points

- If the task has no usable metric, create a rubric before experimenting.
- If the task has meaningful side effects, design the loop first and gate execution behind approval.
- If one round changes too many things, split it into smaller rounds before running it.
- If the current evaluator keeps changing, freeze it or explicitly start a new research track.

## Feedback Loop

Before marking a round `keep`, review:

1. Did the round change only one main variable?
2. Was the evaluator comparable to prior rounds?
3. Was the result actually logged?
4. Is the added complexity worth carrying forward?
5. Should the frontier summary now change?

## Operating Rules

- Optimize the loop, not just the artifact.
- Keep the evaluator stable whenever possible.
- Separate the editable surface from the fixed surface.
- Make experiments cheap, reversible, and comparable.
- Log enough detail that another agent could continue the work.
- Use browsing or primary sources when the task depends on changing external facts.
- For high-stakes domains, bias toward human approval and tighter constraints.

## Resources

- Read `references/loop-design.md` when you need the full research philosophy, scorecard design, or decision rules.
- Read `references/templates.md` when you need ready-to-use templates for scorecards, TSV logs, checkpoints, or handoff notes.
- Read `references/examples.md` when you need concrete trigger examples or example reframings.
- Use `scripts/init_loop.py` to initialize a reusable loop workspace for a new objective.
