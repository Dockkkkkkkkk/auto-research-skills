# Auto Research Examples

## Trigger Examples

Use this skill for requests like:

- "Figure out the best prompt strategy for this support workflow over several rounds."
- "Explore ways to improve signup conversion without changing the whole product at once."
- "Research three possible GTM angles, test the strongest ones, and keep a log of what works."
- "Iteratively improve this brittle automation instead of rewriting everything in one pass."
- "Run a long-horizon investigation into why this onboarding flow underperforms."

Do not use this skill for requests like:

- "Summarize this article."
- "Fix this one bug in a known file."
- "Translate this paragraph."

## Example Reframing

### User request

"Help me figure out how to grow qualified leads."

### Reframed with this skill

- Objective: increase qualified leads
- Primary metric: qualified leads per week
- Guardrails: fixed budget, no spam, no outbound without approval
- Action surface: landing page copy, offer framing, channel hypotheses
- Frozen surface: lead qualification rules, reporting window, brand constraints
- First rounds: baseline current funnel, test one offer angle, test one CTA, compare results

### User request

"Keep improving this agent workflow until it is reliable."

### Reframed with this skill

- Objective: improve workflow reliability
- Primary metric: success rate on fixed scenarios
- Guardrails: no production-side effects, bounded runtime
- Action surface: prompts, branching logic, validation steps
- Frozen surface: evaluation scenarios and pass criteria
- First rounds: establish baseline failure modes, test one validation change at a time
