---
name: ai-agent-builder
description: Build tool-using AI agent workflows with explicit contracts, bounded autonomy, state, evaluation, fallbacks, and cost-aware context management.
---

# AI Agent Builder

1. Define the task boundary, success criteria, failure modes, and what must remain deterministic.
2. Give tools narrow schemas and clear permissions; avoid giant do-everything tools.
3. Keep durable state separate from conversational history.
4. Retrieve context on demand instead of preloading everything.
5. Add approval boundaries for consequential actions.
6. Design retries, timeouts, fallback behavior, and idempotency.
7. Create representative eval cases before claiming reliability.
8. Track quality, latency, tool failures, and usage/cost where the platform exposes them.
