---
name: refactor-planner
description: Plan and execute safe refactors that reduce complexity while preserving behavior, contracts, tests, and deployability.
---

# Refactor Planner

1. State the concrete pain: duplication, coupling, unsafe boundaries, testability, performance, or change cost.
2. Map public contracts and callers before moving code.
3. Create seams and migrate incrementally rather than rewriting everything.
4. Keep behavior-preserving commits/steps separate from feature changes where practical.
5. Delete old paths only after callers and tests prove the migration.
6. Run focused regressions after each risky boundary change.
