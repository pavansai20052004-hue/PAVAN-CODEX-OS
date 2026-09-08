---
name: deep-deliberation
description: Use for hard architecture, ambiguous debugging, migrations, concurrency, security-sensitive changes, or other C2/C3 work that benefits from deliberate alternatives, falsification, and independent critique.
---

# Deep Deliberation

1. Define the exact success condition, constraints, and non-goals.
2. Build a small evidence table: verified facts, assumptions, unknowns.
3. Generate 2-3 plausible hypotheses or approaches only where the choice is material.
4. For each, identify the strongest failure case and the cheapest evidence that could eliminate it.
5. Prefer experiments, tests, traces, and repository evidence over speculation.
6. Choose the smallest robust option; record concise tradeoffs and rollback/recovery implications.
7. Implement in reversible slices with checkpoints.
8. Ask an independent `reasoning-critic`, architect, systems-thinker, or domain specialist to challenge the decision when risk warrants it.
9. Resolve material critiques with evidence, then run required validation.

Do not expose hidden chain-of-thought. Surface only concise rationale, evidence, decisions, and unresolved risks.
