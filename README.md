# PAVAN CODEX OS v3

A modular personal engineering and design system for Codex with automatic project routing, adaptive reasoning depth, specialist subagents, Figma workflows, reusable skills, and evidence-based QA.

## What v3 adds

### Automatic project classification
Before substantial work, the core `adaptive-orchestrator` classifies the repository and task using cheap signals first. A deterministic helper (`scripts/classify_project.py`) recognizes common React/Next/Expo, Spring Boot, Python API, AI/agent, data/ML, Docker/Terraform, and mixed full-stack signals.

### Adaptive thinking depth
Tasks are routed into C0-C3 complexity levels:
- C0: direct edit + narrow check
- C1: short plan + focused validation
- C2: evidence + alternatives + specialist + independent verification
- C3: deep deliberation + failure/recovery analysis + adversarial verification

Normal execution stays efficient, while Codex Plan mode gets a higher reasoning budget.

### Stronger hard-task reasoning
v3 adds:
- `deep-deliberation` skill
- `adversarial-verification` skill
- `reasoning-critic` agent
- `systems-thinker` agent
- architect upgraded to high reasoning
- explicit falsification/counterexample checks before important decisions

This does not change the model's underlying intelligence; it improves effective problem-solving by allocating more reasoning and independent verification to the tasks that benefit from it.

## Reasoning profiles

- `pavan-economy` — routine fixes and high-volume work.
- `pavan-balanced` — recommended default: medium execution reasoning + high Plan-mode reasoning.
- `pavan-deep` — high execution reasoning + xhigh Plan mode where supported.
- `pavan-maximum` — xhigh execution/Plan reasoning where the selected model supports it; intentionally expensive.

`xhigh` availability is model-dependent. Keep balanced as the normal profile and use maximum only for genuinely hard tasks.

## Plugin packs

### `pavan-codex-os`
Core orchestration, full-stack development, debugging, testing, security, hackathon, production QA, and adaptive reasoning workflows.

### `pavan-design-studio`
Design Director, Figma Roundtrip, Responsive System, Accessibility Design, Motion Design, and Design Critique.

### `pavan-backend-lab`
Database Architect, Performance Optimizer, Observability Readiness, AI Agent Builder, Refactor Planner, and Dependency Auditor.

Optional packs stay separate so unrelated specialist context does not crowd every task.

## Windows install / upgrade

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\scripts\install-windows.ps1
```

If your existing `config.toml` was installed by PAVAN CODEX OS, v3 backs it up and upgrades it automatically. A custom non-PAVAN config is preserved.

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

Restart Codex after installation.

## Figma

Connect the Figma MCP integration in Codex Desktop separately from this repository. See `docs/FIGMA-WORKFLOW.md`. When Figma/design context exists and UI fidelity matters, the automatic router should prefer the Figma/design workflow instead of inventing the design from scratch.

## Usage efficiency

See `docs/TOKEN-EFFICIENCY.md`. v3 deliberately separates **reasoning quality** from **reasoning everywhere**:
- normal execution: low/medium where sufficient
- Plan mode: higher reasoning
- hard specialists: high reasoning
- maximum/xhigh: only when the decision is difficult enough to justify the usage
- no unnecessary subagents for tiny tasks
- narrow falsifying tests before broad suites
- optional plugins enabled only when relevant

## Repository map

```text
AGENTS.md                         Adaptive C0-C3 engineering rules
.codex/config.toml               Balanced execution + deeper Plan mode
.codex/profiles/                 Economy / balanced / deep / maximum
.codex/agents/                   Specialist and reasoning agents
plugins/pavan-codex-os/          Core + adaptive orchestration
plugins/pavan-design-studio/     Design + Figma
plugins/pavan-backend-lab/       Backend + AI + performance
scripts/classify_project.py      Deterministic project classifier
project-overlays/                Stack-specific rules
templates/                       Starter blueprints
docs/ADAPTIVE-INTELLIGENCE.md    Reasoning architecture
docs/PROJECT-ROUTING.md          Automatic routing map
scripts/install-windows.ps1      Installer / updater
scripts/doctor.ps1               Local environment check
scripts/validate_repo.py         Repository validation
.github/workflows/validate.yml   CI validation
```

## Validate

```powershell
.\scripts\validate.ps1
```

or:

```bash
python scripts/validate_repo.py
python scripts/classify_project.py . --json
```

## Operating principle

Use the strongest reasoning that materially improves the decision, not the strongest reasoning available for every keystroke. Intelligence comes from the combination of model capability, relevant context, deliberate decomposition, tools, counterexamples, specialists, and verification.
