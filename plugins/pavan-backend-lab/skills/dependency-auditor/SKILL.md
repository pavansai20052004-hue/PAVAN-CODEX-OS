---
name: dependency-auditor
description: Review project dependencies for necessity, versions, duplication, security exposure, bundle/runtime cost, and upgrade risk.
---

# Dependency Auditor

1. Inspect declared and actually imported dependencies.
2. Identify unused, duplicate-purpose, abandoned, vulnerable, or disproportionately heavy packages.
3. Prefer removing a dependency over replacing it when platform/native capabilities suffice.
4. For upgrades, read migration notes when available and change one risk cluster at a time.
5. Run build/tests after dependency changes.
6. Do not perform broad version churn without a concrete benefit.
