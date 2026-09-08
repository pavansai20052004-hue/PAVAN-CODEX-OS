# Plugin Strategy

More installed capabilities are useful only when they remain discoverable and relevant.

## Packages

### pavan-codex-os
Core engineering. Install for most projects.

### pavan-design-studio
Install/enable for UI-heavy work, Figma roundtrips, responsive design, accessibility, motion, and visual critique.

### pavan-backend-lab
Install/enable for database, performance, observability, AI-agent, refactor, and dependency-heavy work.

## Why split plugins

Skills use progressive disclosure, but the initial skill catalog still occupies model context. Separate packages let you keep the routine toolset small and enable specialist capabilities only when a project benefits from them.

## External integrations worth considering

- Figma MCP for design/code roundtrips.
- GitHub for repository, PR, issue, and review workflows.
- Browser/Developer mode for console/network/layout validation.
- Documentation MCP such as the official OpenAI developer docs when building against OpenAI APIs.
- Project-management/deployment plugins only when the project actually uses those services.

Third-party connections require their own authorization. This repository never attempts to bypass OAuth, workspace permissions, or provider controls.
