# Architecture

PAVAN CODEX OS uses layered context rather than one giant prompt.

## Layer 1 — Durable instructions
`AGENTS.md` defines behavior that should remain true across most engineering tasks.

## Layer 2 — Skills
Each skill contains a narrowly triggered workflow. Detail belongs in references so unrelated tasks do not pay the context cost.

## Layer 3 — Subagents
Custom agents provide independent architecture, review, QA, and visual-review perspectives. The parent agent remains responsible for integration.

## Layer 4 — Project overlays
Stack-specific `AGENTS.md` files can be copied into relevant repositories to add local guidance without polluting global instructions.

## Layer 5 — Verification
Executable evidence closes the loop. The system treats unverified success as PARTIAL, not PASS.

## Design principle
Context should be relevant, hierarchical, and cheap. More text is not automatically more intelligence.