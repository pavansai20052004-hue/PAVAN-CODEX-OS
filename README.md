# PAVAN CODEX OS v2

A modular personal engineering and design system for Codex: durable instructions, adaptive reasoning profiles, specialist subagents, reusable plugins/skills, Figma workflows, project overlays, starter templates, and evidence-based QA.

## What v2 optimizes

**Capability:** better architecture, UI art direction, Figma roundtrips, accessibility, responsive design, database design, performance, observability, AI-agent workflows, security, and production QA.

**Efficiency:** low/medium reasoning by default, specialist-only deeper reasoning, capped subagent concurrency, concise outputs, progressive-disclosure skills, optional plugin packs, and no forced early compaction.

## Packages

### `pavan-codex-os`
Core engineering workflows. Recommended for almost every project.

### `pavan-design-studio`
Design Director, Figma Roundtrip, Responsive System, Accessibility Design, Motion Design, and Design Critique.

### `pavan-backend-lab`
Database Architect, Performance Optimizer, Observability Readiness, AI Agent Builder, Refactor Planner, and Dependency Auditor.

The optional packages are separated so specialist capabilities do not have to crowd every task.

## Adaptive profiles

- `pavan-economy` — routine fixes, CRUD, CSS, small refactors, high-volume work.
- `pavan-balanced` — normal development; recommended default.
- `pavan-deep` — architecture, difficult debugging, security, or final audits.

Profiles are stored under `.codex/profiles/` and copied next to your user config by the installer.

## Windows install

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\scripts\install-windows.ps1
```

This installs the core system only.

Add Design Studio:

```powershell
.\scripts\install-windows.ps1 -InstallDesignStudio
```

Add Backend Lab:

```powershell
.\scripts\install-windows.ps1 -InstallBackendLab
```

Install all local plugin folders:

```powershell
.\scripts\install-windows.ps1 -InstallAllPlugins
```

The installer backs up conflicting PAVAN files, preserves an existing `config.toml`, installs profiles, copies custom agents, and places selected local plugin packages under the Codex user directory. Depending on the current Codex build, local plugins may still need to be imported/enabled from the plugin UI.

Restart Codex after installation.

## Figma

Figma authentication is intentionally separate from this repository. See `docs/FIGMA-WORKFLOW.md`. Connect the Figma MCP integration in Codex Desktop, then the `figma-roundtrip` skill can use real design context when the tools are available.

## Maximize usable Codex time

Read `docs/TOKEN-EFFICIENCY.md`. The short version:

- use Standard mode when duration matters more than speed
- use lighter/high-usage models for routine work when available
- keep normal reasoning low/medium
- use deep reasoning only for hard tasks
- do not spawn agents for trivial work
- narrow tests first, broad validation once
- keep optional plugins/tools scoped to projects that need them

## Repository map

```text
AGENTS.md                         Adaptive global engineering rules
.codex/config.toml               Balanced default config
.codex/profiles/                 Economy / balanced / deep profiles
.codex/agents/                   Specialist subagents
plugins/pavan-codex-os/          Core plugin
plugins/pavan-design-studio/     Design + Figma plugin
plugins/pavan-backend-lab/       Deep backend plugin
project-overlays/                Stack-specific rules
templates/                       Starter blueprints
docs/                            Operating and setup guides
scripts/install-windows.ps1      Installer / updater
scripts/doctor.ps1               Local environment check
scripts/validate_repo.py         Deterministic repository validation
.github/workflows/validate.yml   CI validation
```

## Validate

```powershell
.\scripts\validate.ps1
```

or:

```bash
python scripts/validate_repo.py
```

## Operating principle

More prompt text is not more intelligence. Give Codex the smallest relevant instruction set, the right tools, an appropriate reasoning budget, and a verification loop.
