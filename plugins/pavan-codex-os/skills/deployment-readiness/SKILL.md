---
name: deployment-readiness
description: Prepare an application for deployment by validating build/runtime configuration, environment variables, health behavior, failure recovery, and release risks without performing an irreversible deployment unless requested.
---

# Deployment Readiness

1. Identify target platform and runtime constraints.
2. Verify production build locally when possible.
3. Enumerate required environment variables without exposing secret values.
4. Check start command, ports, asset paths, CORS/base URLs, persistence assumptions, and migrations.
5. Confirm health/startup behavior and useful logs.
6. Separate platform configuration from application bugs.
7. Produce a release checklist and blockers.

Do not deploy, publish, or change production credentials unless the user explicitly requests that external action.