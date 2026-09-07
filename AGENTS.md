# PAVAN CODEX OS — Engineering Defaults

## Mission
Produce production-quality software with evidence, not optimistic claims.

## Before Editing
- Inspect the repository and relevant files first.
- Understand architecture, data flow, build system, and existing conventions.
- Reuse working components and interfaces before inventing replacements.
- Identify root cause before fixing defects.

## Planning
For multi-file, risky, architectural, or ambiguous work, form a short plan before editing. Keep simple changes simple.

## Implementation
- Preserve working behavior unless the task explicitly changes it.
- Prefer minimal, reversible changes over broad rewrites.
- Avoid unnecessary dependencies.
- Never hard-code secrets, credentials, tokens, or private endpoints.
- Validate inputs and handle errors deliberately.
- Keep public APIs compatible unless a breaking change is required and documented.

## Frontend
- Design before coding major UI: hierarchy, typography, spacing, layout, states, responsiveness, and interaction.
- Avoid generic AI-dashboard aesthetics, excessive cards, unnecessary gradients, and decorative clutter.
- Reuse design tokens and components.
- Support keyboard/focus behavior and accessible semantics.
- Cover loading, empty, error, success, disabled, hover, active, and focus states when relevant.
- Verify on mobile and desktop when visual tooling is available.

## Backend
- Keep domain logic separated from transport and persistence where practical.
- Validate request boundaries.
- Return useful errors without leaking secrets.
- Add tests for edge cases and failure paths, not only happy paths.

## Debugging
1. Reproduce or establish the failure.
2. Locate the root cause.
3. Make the smallest correct fix.
4. Check adjacent behavior for regressions.
5. Validate the fix with executable evidence.
Never silence errors merely to make a test green.

## Verification
After meaningful changes, run the narrowest relevant checks, then broader validation as needed:
- typecheck / compile
- lint
- unit tests
- integration tests
- production build
- visual inspection for UI
Do not claim PASS when required validation did not run or failed.

## Subagents
Use subagents for independent architecture review, code review, testing, repository exploration, security review, or visual QA. Keep the main agent responsible for integration and final decisions.

## Completion Report
Summarize:
- what changed
- important files
- validation actually run
- PASS/FAIL/PARTIAL
- remaining risks or limitations

## External Actions
Deployments, publishing, destructive data changes, credential changes, purchases, and irreversible external mutations require explicit user intent.