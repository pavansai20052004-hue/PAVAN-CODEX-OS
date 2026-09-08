# Adaptive Intelligence

PAVAN CODEX OS v3 improves effective reasoning by allocating compute and independent review according to task difficulty instead of forcing maximum reasoning everywhere.

## Complexity levels

| Level | Typical work | Reasoning pattern |
|---|---|---|
| C0 | rename, tiny CSS, obvious one-file fix | direct edit + narrow check |
| C1 | normal feature, CRUD, ordinary component/API change | short plan + focused validation |
| C2 | architecture choice, difficult bug, cross-layer feature, performance issue | evidence + alternatives + specialist + independent verification |
| C3 | auth/security, migration, concurrency, multi-service change, critical demo/release | deep deliberation + multiple independent perspectives + staged validation |

## Escalation gates
Escalate when the task combines security/auth, irreversible data changes, distributed state, concurrency, unclear contracts, external integrations, production incidents, or large blast radius.

## Reasoning profiles
- `pavan-economy`: long sessions and routine work.
- `pavan-balanced`: normal development.
- `pavan-deep`: high execution reasoning with xhigh Plan mode when the selected model supports it.
- `pavan-maximum`: xhigh execution and Plan mode; model-dependent and intentionally expensive.

The normal default remains balanced. Higher reasoning is valuable only when it changes the decision or reduces rework.

## Why this is smarter
The system combines stronger reasoning effort with decomposition, competing hypotheses, falsification, domain specialists, adversarial review, and executable verification. These mechanisms improve reliability more than simply adding a longer prompt.
