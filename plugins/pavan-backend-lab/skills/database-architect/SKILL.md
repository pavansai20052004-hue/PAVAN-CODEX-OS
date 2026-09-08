---
name: database-architect
description: Design or review schemas, queries, indexes, transactions, migrations, integrity, and concurrency for application databases.
---

# Database Architect

1. Start from actual entities, invariants, read/write access patterns, scale, and consistency needs.
2. Define keys, relationships, nullability, uniqueness, constraints, and ownership deliberately.
3. Design indexes from query shapes; avoid speculative index collections.
4. Define transaction boundaries and concurrent update behavior.
5. Plan migrations with backward compatibility, data backfill, observability, and rollback.
6. Inspect generated ORM queries where performance matters.
7. Validate integrity and migration behavior with representative data.
