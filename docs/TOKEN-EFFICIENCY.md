# Token and Usage Efficiency

The objective is not to make Codex think less; it is to spend deep reasoning only where it changes the outcome.

## Daily operating rules

1. Use Standard mode when maximizing session duration. Fast mode trades more credits for speed.
2. Prefer a lighter/high-usage model for routine edits when your plan exposes one; switch to the strongest model for architecture, difficult debugging, security, and final integration.
3. Keep default reasoning at low/medium. Raise it intentionally for hard tasks, then lower it again.
4. Do not spawn subagents for trivial changes. Normal work should use zero or one specialist; complex independent work may use two or three.
5. Search/read only the files needed to establish the current behavior. Do not dump the whole repository into context without a reason.
6. Keep skills narrow. Put detailed design catalogs, examples, and reference material under `references/` so they load only when selected.
7. Run the narrowest meaningful test first. Run the broad suite once near completion; do not repeat passing suites when code has not changed.
8. Keep final reports concise and avoid restating the entire implementation.
9. Start a fresh thread after a completed milestone when the old conversational history is no longer useful. Keep long-running threads only when continuity is genuinely valuable.
10. Disable or avoid attaching unrelated plugins/MCP servers to a task. Tool catalogs and server instructions are useful context only when the tools are relevant.

## Compaction

Codex supports automatic context compaction and exposes `model_auto_compact_token_limit`. PAVAN CODEX OS deliberately leaves the threshold unset so the active model/client can use its current defaults. Lowering the threshold too aggressively can create extra compaction work and discard useful detail earlier than necessary. Tune it only after observing a real long-session problem.

## Profiles

- `pavan-economy`: routine fixes and high-volume work.
- `pavan-balanced`: normal features; recommended default.
- `pavan-deep`: architecture, hard bugs, security, final audits.

The installer places these next to the user `config.toml`. CLI usage: `codex --profile pavan-economy`, `codex --profile pavan-balanced`, or `codex --profile pavan-deep` when your Codex version supports profile selection.
