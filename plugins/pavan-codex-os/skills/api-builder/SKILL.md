---
name: api-builder
description: Design and implement HTTP APIs with explicit contracts, validation, error semantics, authentication/authorization boundaries, persistence behavior, and tests.
---

# API Builder

1. Inspect existing routing, schema, auth, service, and persistence conventions.
2. Define request/response contracts and status/error semantics before implementation.
3. Validate untrusted input at the boundary.
4. Keep business logic testable outside transport code where practical.
5. Enforce authorization server-side.
6. Handle idempotency, pagination, concurrency, and transactions when relevant.
7. Add tests for valid and invalid behavior.
8. Update API documentation/types consumed by clients when needed.
