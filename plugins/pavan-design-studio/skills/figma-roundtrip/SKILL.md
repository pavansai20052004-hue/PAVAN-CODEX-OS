---
name: figma-roundtrip
description: Move product UI between Figma and code while preserving editable structure, assets, tokens, responsiveness, and visual fidelity.
---

# Figma Roundtrip

Use Figma/MCP tools when connected; never invent access.

## Figma → code
1. Inspect frames, components, variants, tokens/styles, assets, constraints, and responsive intent.
2. Build a component/token map before writing UI code.
3. Implement layout hierarchy first, then states, then visual polish.
4. Reuse provided assets instead of random substitutes.
5. Render representative widths and compare against the source design.
6. Fix material drift before completion.

## Code → Figma
1. Identify stable product states worth exploring visually.
2. Send the actual implementation/state to Figma when the available integration supports it.
3. Keep generated design layers editable and semantically grouped.
4. Explore alternatives in separate frames, not by destroying the baseline.
5. Bring the selected direction back to code and verify parity.

For idea exploration, use FigJam/Figma as a workspace for user flow, component inventory, three design directions, and decision annotations before implementation.
