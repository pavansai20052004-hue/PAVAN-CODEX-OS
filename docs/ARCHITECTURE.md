# Architecture

PAVAN CODEX OS uses layered, optional context rather than one giant prompt.

## Layer 1 — Durable instructions
`AGENTS.md` defines behavior that should remain true across most engineering tasks, including the work-budget rules that prevent overusing deep reasoning and subagents.

## Layer 2 — Runtime profiles
Economy, balanced, and deep profiles change reasoning/output/subagent budgets without changing engineering standards.

## Layer 3 — Modular plugins and skills
Core engineering is separate from Design Studio and Backend Lab. Skills use short trigger descriptions; deep playbooks live in references so unrelated tasks do not pay the context cost.

## Layer 4 — Subagents
Specialists use different reasoning budgets. Architecture/security/data reviewers can spend more reasoning than routine QA. Concurrency is capped so parallelism stays useful rather than wasteful.

## Layer 5 — Project overlays
Stack-specific `AGENTS.md` files add local guidance without polluting global instructions.

## Layer 6 — Tool connections
MCP/plugins such as Figma, GitHub, browser developer tools, documentation, or deployment services are attached only where they improve the task. External authentication remains provider-controlled.

## Layer 7 — Verification
Executable evidence closes the loop. Unverified success is PARTIAL, not PASS.

## Design principle
Relevant context + appropriate reasoning + real tools + independent verification beats maximal context on every turn.
