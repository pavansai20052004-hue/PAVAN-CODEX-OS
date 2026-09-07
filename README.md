# PAVAN CODEX OS

PAVAN CODEX OS is a personal engineering layer for Codex: durable instructions, reusable skills, specialized subagents, design intelligence, project overlays, validation, and a local plugin package.

## Goals

- Improve consistency without stuffing every prompt with repeated rules.
- Separate permanent behavior (`AGENTS.md`) from task workflows (skills) and parallel specialists (subagents).
- Make UI work design-first and visually verified.
- Make debugging root-cause-first rather than patch-first.
- Require evidence before claiming a task is complete.
- Keep configuration modular so one weak skill can be replaced without destabilizing the rest.

## Repository map

```text
AGENTS.md                         Global engineering defaults
.codex/config.toml               Recommended Codex runtime defaults
.codex/agents/*.toml             Custom subagents
plugins/pavan-codex-os/          Installable local Codex plugin
  .codex-plugin/plugin.json      Plugin manifest
  skills/*/SKILL.md              Reusable workflows
  skills/*/references/           On-demand detail
project-overlays/                Stack-specific AGENTS.md overlays
docs/                            Architecture and operating guidance
scripts/install-windows.ps1      Windows installer / updater
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

The installer backs up conflicting Codex files before replacing them, installs custom agents separately, installs the local plugin under your user profile, and registers it in the personal marketplace.

After installation, restart Codex so the new instructions, agents, and plugin are discovered.

## Validate

```powershell
.\scripts\validate.ps1
```

or directly:

```bash
python scripts/validate_repo.py
```

## Recommended workflow

For substantial work, use the system in this order:

1. Root `AGENTS.md` supplies durable engineering behavior.
2. The smallest matching skill supplies the workflow.
3. Specialized subagents handle independent exploration, architecture, review, or visual QA.
4. Project overlays add stack-specific rules only when relevant.
5. Validation and visual inspection decide PASS/FAIL.

## Safety

No skill is allowed to claim success from code inspection alone when executable validation is available. Destructive actions, deployments, publishing, credential changes, and irreversible external mutations remain explicit user-controlled operations.

## Status

Version 1 is intentionally opinionated but modular. It is designed to evolve as Codex capabilities and the user's engineering workflow evolve.
