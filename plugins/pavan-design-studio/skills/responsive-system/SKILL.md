---
name: responsive-system
description: Design responsive UI behavior across mobile, tablet, laptop, and wide screens without fragile breakpoint-by-breakpoint patching.
---

# Responsive System

1. Identify layout invariants and what is allowed to reflow, stack, collapse, scroll, or disappear.
2. Use intrinsic layout, min/max constraints, grids/flex, fluid type/spacing, and container-aware behavior before adding breakpoints.
3. Define navigation, tables, charts, dialogs, forms, and dense controls separately; each has different mobile behavior.
4. Protect touch targets, reading order, focus order, and content priority.
5. Test narrow mobile, common mobile, tablet, laptop, and one wide viewport.
6. Fix overflow/root layout causes instead of hiding them with clipping.
