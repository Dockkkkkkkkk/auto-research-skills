# Auto Research Skills

This project extracts the most reusable idea from `autoresearch` and turns it into a pair of practical agent skills.

## Inspiration

This project is directly inspired by **Andrej Karpathy's** open-source project **`autoresearch`**:

- Project: `autoresearch`
- Author: Andrej Karpathy
- Repository: <https://github.com/karpathy/autoresearch>

What we borrow is not the training code itself, but the workflow philosophy behind it: scorecards, baselines, bounded rounds, logging, and keep-or-revert decisions.

Core idea:

- define a scorecard first
- establish a baseline
- run small bounded rounds
- keep only evidence-backed changes
- log failures as well as wins
- maintain a frontier instead of drifting randomly

## What this project contains

Two language versions of the same workflow pattern:

- `auto-research`
- `auto-research-zh`

Each skill includes:

- `SKILL.md`
- `references/loop-design.md`
- `references/templates.md`
- `references/examples.md`
- `scripts/init_loop.py`

## What this is for

These skills are useful when an agent should not attempt a one-shot answer, but should instead iterate through a measurable sequence of experiments, investigations, or refinements.

Good fits:

- prompt and workflow optimization
- growth or content experiments with clear guardrails
- reliability improvement for brittle automations
- long-horizon research and synthesis

Poor fits:

- one-shot tasks
- tasks with no meaningful metric
- high-risk actions that cannot be audited or rolled back

## Why we open-sourced it

What impressed us about `autoresearch` was not just "AI training itself".

The deeper idea was that exploratory work can be turned into an explicit agent loop:

- stable evaluator
- narrow action surface
- cheap rounds
- clear keep or discard logic
- ongoing frontier management

That pattern is useful far beyond model training.

## Example scenarios

These are illustrative scenarios, not customer case studies.

### Scenario 1: turning prompt work into an experiment system

Instead of generating many prompt variants in one pass, the agent measures one change at a time against a stable metric and keeps only the variants that actually improve outcomes.

### Scenario 2: hardening a fragile automation loop

The agent uses a fixed evaluator for success rate, runtime, and failure modes, then improves one validation step per round instead of rewriting the whole system blindly.

### Scenario 3: giving a team a lightweight "research department"

The agent gathers material, updates the frontier summary, prunes weak directions, and leaves humans to decide only on the highest-leverage questions.

## How to use it

Copy the desired skill folder into your runtime skill directory. For example:

```text
.agents/skills/
└── auto-research/
```

or:

```text
.agents/skills/
└── auto-research-zh/
```

To scaffold a fresh research loop workspace:

```bash
python skills/auto-research/scripts/init_loop.py --name "your-objective"
```

## About the team

We are **Aiwei Heli Digital Technology Co., Ltd.** We focus on helping organizations turn AI from an interesting idea into a usable business system.

Our work spans the full delivery chain:

- problem discovery and scenario framing
- requirement clarification and solution design
- implementation and system integration
- deployment and operational support
- iteration, enablement, and training

We are not interested in AI as a slide deck. We care about systems that can actually run inside real business environments.

We are also building a digital employee platform around:

- agent infrastructure
- tool governance
- permission and audit control
- multi-channel interaction
- long-running business workflows

take a fast-moving idea from the AI community, extract the reusable part, and ship it in a form teams can actually try.

If you are working on:

- enterprise AI workflows
- digital employee systems
- OpenClaw-related implementations
- real-world agent operations

we will probably have useful overlap.

## OpenClaw-related support

We are also actively following OpenClaw and the broader shift from impressive agent demos to operational business systems.

Areas where we can help include:

- OpenClaw-oriented research and implementation planning
- business adaptation and second-layer packaging
- browser and workflow-oriented scenario design
- workflow design for agent-driven operations
- integration with existing systems, data sources, and knowledge bases
- solution design for AI assistants and digital employee scenarios

What matters to real teams is usually not whether the agent looks impressive in a demo, but whether it can:

- plug into existing workflows
- reduce real manual work
- lower the cost of experimentation
- become a system people can keep using

## Contact

- Website: [official.ivheli.com](https://official.ivheli.com/)
- WeChat assistant: `xmaiyrjgzs`

### WeChat Assistant

![WeChat assistant QR](assets/wechat-qr.png)

### Official Account

![Official account QR](assets/official-account-qr.png)
