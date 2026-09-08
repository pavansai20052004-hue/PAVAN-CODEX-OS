---
name: adversarial-verification
description: Independently try to disprove a hard task's implementation or PASS claim using counterexamples, failure-path tests, contract checks, and regression evidence before merge, release, or demo.
---

# Adversarial Verification

1. Restate the acceptance conditions in testable terms.
2. Inspect the actual diff/behavior, not the implementer's summary alone.
3. Search for counterexamples: invalid inputs, boundary values, stale state, retries, races, partial failures, auth bypasses, responsive breakpoints, and migration/recovery paths as relevant.
4. Run the cheapest targeted checks that can falsify the implementation.
5. Verify important claims against executable output or rendered UI when tools exist.
6. Separate blocker, major risk, minor issue, and untested area.
7. PASS only when required checks are green and no blocker remains.

Avoid duplicating broad test suites unless a discovered risk justifies them.
