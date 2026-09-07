# PAVAN CODEX OS

PAVAN CODEX OS is a personal engineering layer for Codex: durable instructions, reusable skills, specialized subagents, design intelligence, project overlays, starter templates, validation, and a local plugin package.

## Goals

- Improve consistency without stuffing every prompt with repeated rules.
- Separate permanent behavior (`AGENTS.md`) from task workflows (skills) and parallel specialists (subagents).
- Make UI work design-first and visually verified.
- Make debugging root-cause-first rather than patch-first.
- Require evidence before claiming a task is complete.
- Keep configuration modular so individual parts can evolve safely.

## Repository map

```text
AGENTS.md                         Global engineering defaults
.codex/config.toml               Recommended Codex runtime defaults
.codex/agents/*.toml             Custom subagents
plugins/pavan-codex-os/          Local Codex plugin package
  .codex-plugin/plugin.json      Plugin manifest
  skills/*/SKILL.md              Reusable workflows
  skills/*/references/           On-demand detail
project-overlays/                Stack-specific AGENTS.md overlays
templates/                       Project starter blueprints
docs/                            Architecture and operating guidance
scripts/install-windows.ps1      Windows installer / updater
scripts/setup-project.ps1        Apply a stack overlay to a project
scripts/validate.ps1             Local validation entrypoint
scripts/validate_repo.py         Deterministic repository checks
.github/workflows/validate.yml   CI validation
```

## Install on Windows

Clone the repository, then from PowerShell run:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\scripts\install-windows.ps1
```

The installer backs up conflicting global instructions and agent files, preserves an existing `config.toml` instead of overwriting it, and copies the plugin package into your Codex user directory for local use.

After installation, restart Codex so configuration can be rediscovered. If your Codex build manages plugins through its UI/marketplace, point it at or import the local plugin package rather than assuming manual discovery.

## Apply project rules

Example:

```powershell
.\scripts\setup-project.ps1 -Type react -ProjectPath C:\code\my-app
```

Supported types: `react`, `python-fastapi`, `spring-boot`.

## Validate

```powershell
.\scripts\validate.ps1
```

or:

```bash
python scripts/validate_repo.py
```

## Recommended workflow

1. Root `AGENTS.md` supplies durable engineering behavior.
2. The smallest matching skill supplies the workflow.
3. Specialized subagents handle independent architecture, review, QA, or visual inspection.
4. Project overlays add stack-specific rules only where relevant.
5. Templates accelerate project starts without replacing engineering judgment.
6. Validation and visual inspection decide PASS/FAIL.

## Safety

No skill is allowed to claim success from code inspection alone when executable validation is available. Destructive actions, deployments, publishing, credential changes, and irreversible external mutations remain explicit user-controlled operations.

## Status

Version 1 is intentionally opinionated but modular. It is designed to evolve as Codex capabilities and the user's engineering workflow evolve.
