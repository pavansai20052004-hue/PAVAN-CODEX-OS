---
name: fullstack-builder
description: Build or extend production-oriented full-stack features across frontend, API, persistence, auth, validation, tests, and integration while preserving existing architecture.
---

# Full-Stack Builder

1. Trace the existing request/data flow before editing.
2. Define contracts between UI, API, domain logic, and persistence.
3. Preserve compatibility unless the requested feature requires a migration.
4. Implement one vertical slice end-to-end before broadening.
5. Validate inputs at trust boundaries and handle errors explicitly.
6. Add or update tests at the cheapest layer that proves behavior; add integration coverage for risky boundaries.
7. Run compile/typecheck, tests, and production build as applicable.
8. Report any environment-dependent pieces separately from verified behavior.

Do not replace real integrations with mocks in production paths unless explicitly requested.