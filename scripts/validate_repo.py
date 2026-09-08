from pathlib import Path
import json
import re
import sys
import tomllib

ROOT = Path(__file__).resolve().parents[1]
errors = []
warnings = []

required = [
    ROOT / "AGENTS.md",
    ROOT / ".codex" / "config.toml",
    ROOT / "docs" / "TOKEN-EFFICIENCY.md",
    ROOT / "docs" / "FIGMA-WORKFLOW.md",
]
for path in required:
    if not path.exists():
        errors.append(f"missing required file: {path.relative_to(ROOT)}")

config_path = ROOT / ".codex" / "config.toml"
if config_path.exists():
    try:
        config = tomllib.loads(config_path.read_text(encoding="utf-8"))
        effort = config.get("model_reasoning_effort")
        if effort not in {"minimal", "low", "medium", "high", "xhigh"}:
            errors.append(f"unsupported model_reasoning_effort: {effort}")
        threads = config.get("agents", {}).get("max_concurrent_threads_per_session")
        if threads and threads > 4:
            warnings.append("default agent concurrency > 4 may consume usage quickly")
    except Exception as exc:
        errors.append(f"invalid .codex/config.toml: {exc}")

plugin_roots = sorted((ROOT / "plugins").glob("*/.codex-plugin/plugin.json"))
if not plugin_roots:
    errors.append("no plugin manifests found")

skill_count = 0
names = set()
for manifest in plugin_roots:
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
        for key in ("name", "version", "description", "skills"):
            if not data.get(key):
                errors.append(f"{manifest.relative_to(ROOT)} missing {key}")
    except Exception as exc:
        errors.append(f"invalid plugin manifest {manifest.relative_to(ROOT)}: {exc}")
        continue

    plugin_dir = manifest.parents[1]
    skills = list((plugin_dir / "skills").glob("*/SKILL.md"))
    if not skills:
        errors.append(f"{plugin_dir.relative_to(ROOT)} has no skills")
    for skill in skills:
        skill_count += 1
        text = skill.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append(f"{skill.relative_to(ROOT)} missing YAML frontmatter")
        name = re.search(r"^name:\s*(\S+)", text, re.M)
        desc = re.search(r"^description:\s*(.+)", text, re.M)
        if not name:
            errors.append(f"{skill.relative_to(ROOT)} missing name")
        elif name.group(1) in names:
            errors.append(f"duplicate skill name: {name.group(1)}")
        else:
            names.add(name.group(1))
        if not desc:
            errors.append(f"{skill.relative_to(ROOT)} missing description")
        elif len(desc.group(1)) > 240:
            warnings.append(f"long skill description may waste discovery context: {skill.relative_to(ROOT)}")

agents = list((ROOT / ".codex" / "agents").glob("*.toml"))
if not agents:
    errors.append("no custom agents found")
for agent in agents:
    try:
        data = tomllib.loads(agent.read_text(encoding="utf-8"))
        for key in ("name", "description", "developer_instructions"):
            if not data.get(key):
                errors.append(f"{agent.relative_to(ROOT)} missing {key}")
    except Exception as exc:
        errors.append(f"invalid agent {agent.relative_to(ROOT)}: {exc}")

if skill_count > 30:
    warnings.append("more than 30 installed skills: consider splitting/enabling plugins on demand")

for warning in warnings:
    print(f"WARNING: {warning}")

if errors:
    print("PAVAN CODEX OS validation: FAIL")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print(f"PAVAN CODEX OS validation: PASS ({len(plugin_roots)} plugins, {skill_count} skills, {len(agents)} agents)")
