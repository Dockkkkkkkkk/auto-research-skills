# Auto Research Loop Design

## Purpose

This skill packages a general pattern for agentic exploration:

1. Constrain the environment.
2. Define a scorecard.
3. Run short comparable rounds.
4. Keep or revert based on evidence.
5. Preserve a trail of decisions.

The philosophy is closer to "operate a research system" than "guess a brilliant plan."

## Core Pattern

### 1. Scorecard first

Every long-horizon task needs a scorecard before open-ended exploration. At minimum define:

- Objective
- Primary metric
- Secondary guardrails
- Baseline
- Action surface
- Frozen surface
- Budget per round
- Stop and approval conditions

Without this, the agent will rationalize drift as progress.

### 2. Stable evaluator

Try to hold the evaluator stable across rounds. If the metric itself changes every round, the loop stops being comparable.

Good evaluators:

- conversion rate under a fixed audience slice
- cost per useful lead under a fixed budget
- bug reproduction rate under a fixed test suite
- answer quality judged by a fixed rubric
- research coverage judged against a fixed checklist

Weak evaluators:

- "looks promising"
- "feels better"
- changing judge criteria every round

### 3. Narrow action surface

Do not let the agent change everything at once. Define what it may vary:

- prompts
- copy
- experiment setup
- target segment
- workflow branching logic
- code in one bounded module
- sourcing strategy

Also define what stays fixed:

- judge or metric
- budget cap
- policy constraints
- target persona
- data slice
- external interfaces

### 4. Small reversible rounds

Each round should be cheap enough to discard. The research loop should prefer:

- one hypothesis per round
- minimal edits
- explicit result logging
- explicit keep or discard decision

This is what makes long-running agent work interpretable.

## Decision Rules

Use this simple decision vocabulary:

- `keep`: improves the frontier and becomes the new baseline
- `discard`: worse than baseline or not worth the added complexity
- `retry`: experiment failed operationally and should be rerun cleanly
- `escalate`: blocked by risk, ambiguity, permissions, or approval

When in doubt, prefer `discard` over carrying speculative complexity forward.

## Safety and Governance

Use tighter approval gates when the loop can:

- spend money
- contact people
- publish externally
- modify production systems
- access sensitive data
- make legal, financial, or medical claims

In those cases, the agent can still research and propose experiments, but execution should be gated.

## Recommended Cadence

One round should usually include:

1. hypothesis
2. minimal intervention
3. run
4. metric capture
5. short written conclusion

Every 3-5 rounds:

1. update the frontier summary
2. prune bad branches
3. revise the next hypothesis queue

## Domain Adaptation Notes

### Coding

- Metric: tests passed, latency, failure rate, memory, benchmark score
- Action surface: one module, one config family, one optimization path

### Growth or monetization experiments

- Metric: qualified leads, net revenue, ROI, activation, retention
- Guardrails: budget, compliance, anti-spam, reputational limits
- Approval gates: paid spend, outbound contact, account creation, publishing

### Research and synthesis

- Metric: source coverage, confidence, contradiction resolution, decision usefulness
- Frozen surface: evaluation rubric and source quality threshold

### Workflow optimization

- Metric: cycle time, defect rate, manual touches, handoff delays
- Action surface: one stage or one policy at a time
