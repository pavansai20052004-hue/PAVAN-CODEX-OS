# PAVAN CODEX OS — Engineering Defaults

## Mission
Produce production-quality software with evidence while using context, tools, tests, and subagents deliberately.

## Work Budget
Treat intelligence as an adaptive budget, not a fixed maximum.

- **Small/reversible change:** inspect the directly relevant files, edit, run one focused check. No subagent unless risk is hidden.
- **Normal feature:** inspect the affected flow, make a short plan, implement a vertical slice, use at most one specialist when it materially helps, then validate.
- **Complex/risky work:** map contracts and risks, parallelize only independent investigations, use at most three useful specialists by default, integrate findings, then run broader verification.
- Do not invoke every installed skill. Use only skills whose trigger matches the task.
- Do not read the entire repository when targeted search/navigation can establish the behavior.
- Do not repeatedly restate plans, requirements, or already-proven facts.
- Keep inter-agent reports and final reports concise; return decisions and evidence, not transcripts.

## Before Editing
- Inspect relevant repository files and local instructions first.
- Understand the affected architecture, data flow, build system, and conventions.
- Reuse working components and interfaces before inventing replacements.
- Identify root cause before fixing defects.

## Planning
For multi-file, risky, architectural, or ambiguous work, form a short executable plan before editing. Keep simple changes simple and continue to implementation instead of over-planning.

## Implementation
- Preserve working behavior unless the task explicitly changes it.
- Prefer minimal, reversible changes over broad rewrites.
- Avoid unnecessary dependencies.
- Never hard-code secrets, credentials, tokens, or private endpoints.
- Validate inputs and handle errors deliberately.
- Keep public APIs compatible unless a breaking change is required and documented.
- Prefer deterministic code for deterministic problems; use AI/model calls only where they add value.

## Frontend and Product Design
- For major UI, establish product goal, hierarchy, visual direction, typography, spacing, layout, states, responsiveness, and interaction before coding.
- Avoid generic AI-dashboard aesthetics, excessive cards, unnecessary gradients, and decorative clutter.
- Reuse design tokens and components; preserve real reference assets.
- Support keyboard/focus behavior and accessible semantics.
- Cover loading, empty, error, success, disabled, hover, active, and focus states when relevant.
- Verify actual rendered UI on representative mobile and desktop widths when visual/browser tooling is available.
- When Figma is connected, use it for real design context and roundtrip iteration; never invent Figma access or assets.

## Backend and Data
- Keep domain logic separated from transport and persistence where practical.
- Validate trust boundaries and enforce authorization server-side.
- Return useful errors without leaking secrets.
- Treat schemas, migrations, indexes, transactions, retries, idempotency, and observability as first-class when the problem needs them.

## Debugging
1. Reproduce or establish the failure.
2. Trace the smallest relevant path.
3. Prove or strongly establish the root cause.
4. Make the smallest correct fix.
5. Check adjacent behavior for regressions.
6. Validate with executable evidence.
Never silence errors merely to make a test green.

## Verification
Use the cheapest check that proves the change, then broaden once when risk requires it:
- targeted test or reproduction
- typecheck / compile
- lint when relevant
- integration test for boundaries
- production build near completion
- visual inspection for UI
Do not rerun a passing broad suite unless code affecting it changed or new evidence warrants it. Do not claim PASS when required validation did not run or failed.

## Subagents
Use specialists for genuinely independent architecture, code review, security, data, performance, product, testing, or visual QA work. The main agent owns integration and final decisions. Prefer a few targeted agents over a crowd of redundant agents.

## Context Efficiency
- Prefer concise skill descriptions and on-demand references.
- Keep large examples, design catalogs, and playbooks outside always-loaded instructions.
- Start a fresh thread after a completed milestone when old conversation state no longer helps.
- Keep unrelated MCP servers/plugins out of a task when practical.
- Do not force early compaction by default; let the active Codex/model defaults manage long context unless measured workflow needs justify tuning.

## Completion Report
Return only:
- what changed
- important files
- validation actually run
- PASS / FAIL / PARTIAL
- remaining material risks or limitations

## External Actions
Deployments, publishing, destructive data changes, credential changes, purchases, and irreversible external mutations require explicit user intent.
