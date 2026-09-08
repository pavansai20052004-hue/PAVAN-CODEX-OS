---
name: observability-readiness
description: Add or review logs, metrics, traces, health checks, correlation, and operational signals needed to debug production behavior.
---

# Observability Readiness

1. Identify critical user journeys and failure modes.
2. Add structured logs at boundaries and state transitions; never log secrets or sensitive payloads unnecessarily.
3. Define actionable metrics for latency, errors, saturation, throughput, queue depth, and domain outcomes when relevant.
4. Preserve request/job correlation across async boundaries.
5. Distinguish liveness from readiness/health.
6. Make failures diagnosable without flooding logs.
7. Verify signal behavior locally or in a safe environment before release.
