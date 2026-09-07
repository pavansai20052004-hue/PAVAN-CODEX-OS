---
name: production-qa
description: Perform final engineering verification before release, demo, merge, or handoff, using executable evidence and a truthful PASS/PARTIAL/FAIL report.
---

# Production QA

## Build a verification matrix
Include only relevant checks:
- compile/typecheck
- lint/static analysis
- unit tests
- integration/API tests
- production build
- database migration safety
- auth/security boundaries
- accessibility smoke checks
- responsive/visual QA
- startup/restart/recovery
- rollback or undo where applicable

Run the narrowest useful checks first. Do not waste time rerunning unchanged broad suites without reason.

## Final status
- PASS: required checks succeeded.
- PARTIAL: implementation is ready but one or more required checks could not be completed; state exactly why.
- FAIL: a required check failed or a blocking defect remains.

Never convert PARTIAL into PASS through wording.