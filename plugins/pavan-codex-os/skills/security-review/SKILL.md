---
name: security-review
description: Review authorized application code for practical security weaknesses introduced or affected by a change, focusing on trust boundaries, auth, secrets, injection, data exposure, and unsafe defaults.
---

# Security Review

1. Scope the review to the authorized repository/change.
2. Identify trust boundaries: user input, network calls, files, database, authentication, authorization, secrets, third-party APIs.
3. Trace exploitability rather than listing generic best practices.
4. Prioritize concrete issues by severity and likelihood.
5. Recommend the smallest durable remediation and a regression test where practical.
6. Re-check the patched path after changes.

Do not invent vulnerabilities unsupported by evidence. Do not expose secret values found during review.