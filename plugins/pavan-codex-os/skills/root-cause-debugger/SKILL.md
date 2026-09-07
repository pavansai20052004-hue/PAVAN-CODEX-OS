---
name: root-cause-debugger
description: Diagnose and fix bugs by reproducing symptoms, tracing evidence to root cause, applying the smallest correct change, and verifying regressions.
---

# Root Cause Debugger

## Method
1. Capture the exact symptom, error, failing input, or regression.
2. Reproduce or establish a deterministic evidence path.
3. Trace from failure outward: caller, state, data, configuration, environment, dependency.
4. Form a falsifiable root-cause hypothesis.
5. Confirm it before editing when practical.
6. Make the smallest durable fix.
7. Add a regression test when the failure is testable.
8. Run focused validation, then relevant broader checks.

## Never
- swallow exceptions to hide failure
- delete tests because they fail
- replace real behavior with hard-coded success
- claim root cause from the first suspicious line without evidence
