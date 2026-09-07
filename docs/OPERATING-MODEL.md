# Operating Model

## Normal feature
Inspect → plan if needed → implement vertical slice → test → build → report.

## Bug
Reproduce → trace → prove root cause → minimal fix → regression test → validate.

## Major UI
Inspect product/reference → define design direction → implement → responsive pass → visual QA → fix → validate build.

## High-risk change
Ask architect subagent for constraints, implement incrementally, ask reviewer/QA subagents for independent checks, then integrate findings.

## Hackathon finalization
Protect core behavior first. Then optimize judge flow, readiness visibility, recovery, demo reliability, and evidence. Never fake external integrations.

## Status language
Use PASS only for verified required checks. Use PARTIAL when something material remains unverified.