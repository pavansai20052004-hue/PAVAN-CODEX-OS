---
name: adaptive-orchestrator
description: Automatically classify a repository/task, choose the smallest useful workflow and reasoning depth, and route to relevant PAVAN skills or specialist agents before substantial engineering work.
---

# Adaptive Orchestrator

Use at the beginning of a new project/repository and before substantial multi-file work.

1. Inspect cheap signals first: manifests, build files, directory names, framework configs, README headings, and the files directly implicated by the task.
2. If available, run `python scripts/classify_project.py . --json` for a deterministic baseline; treat its output as evidence, not authority.
3. Classify project family, task type, complexity C0-C3, and risk gates.
4. Select only the relevant skills/plugins. Do not load Design Studio for backend-only work or Backend Lab for a CSS-only task.
5. C0: direct execution. C1: short plan. C2: use one specialist plus verification. C3: invoke deep-deliberation and independent adversarial verification; use multiple specialists only when their perspectives are genuinely different.
6. If Figma/design context exists and UI fidelity matters, route to `figma-roundtrip` or the design workflows.
7. If evidence contradicts the initial classification, reclassify once. Do not repeatedly reroute without new evidence.

Keep routing notes concise and continue to execution; classification is a means, not the deliverable.
