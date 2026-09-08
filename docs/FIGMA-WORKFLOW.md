# Figma + Codex Roundtrip

Figma is an optional tool connection, not a requirement for every project.

## Setup

In Codex/ChatGPT desktop, open Settings → MCP servers, add/install the Figma MCP integration available to your account, authenticate it, and restart when requested. Use `/mcp` where supported to confirm the connection.

PAVAN CODEX OS never stores Figma credentials in this repository.

## Workflow A — idea → Figma → code

1. Product brief and user journey.
2. FigJam: flow, edge cases, information architecture, component inventory.
3. Figma: three meaningfully different visual directions.
4. Select one direction and establish tokens/components/variants.
5. Use `figma-roundtrip` to inspect real design context and implement it.
6. Render code at representative widths and compare to Figma.
7. Fix layout/state/accessibility drift.

## Workflow B — code → Figma → improved code

1. Start from a working implementation.
2. Send stable screens/states into Figma using the connected integration when supported.
3. Explore visual alternatives in separate frames.
4. Keep the baseline and annotate design decisions.
5. Bring the selected version back into code.
6. Run visual QA and production validation.

## Useful Figma artifacts

- user-flow FigJam board
- design-direction board
- token/style page
- component + variant inventory
- desktop/mobile frames
- empty/loading/error/success states
- interaction prototype
- accessibility annotations
- implementation handoff frame

Do not use Figma as a substitute for real browser/device validation.
