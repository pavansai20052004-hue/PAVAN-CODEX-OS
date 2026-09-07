from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

required = [
    ROOT / "AGENTS.md",
    ROOT / ".codex" / "config.toml",
    ROOT / "plugins" / "pavan-codex-os" / ".codex-plugin" / "plugin.json",
]
for path in required:
    if not path.exists():
        errors.append(f"missing required file: {path.relative_to(ROOT)}")

manifest = ROOT / "plugins" / "pavan-codex-os" / ".codex-plugin" / "plugin.json"
if manifest.exists():
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
        for key in ("name", "version", "description"):
            if not data.get(key):
                errors.append(f"plugin manifest missing {key}")
    except Exception as exc:
        errors.append(f"invalid plugin manifest: {exc}")

skills = list((ROOT / "plugins" / "pavan-codex-os" / "skills").glob("*/SKILL.md"))
if not skills:
    errors.append("no skills found")
for skill in skills:
    text = skill.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{skill.relative_to(ROOT)} missing YAML frontmatter")
    if not re.search(r"^name:\s*\S+", text, re.M):
        errors.append(f"{skill.relative_to(ROOT)} missing name")
    if not re.search(r"^description:\s*.+", text, re.M):
        errors.append(f"{skill.relative_to(ROOT)} missing description")

agents = list((ROOT / ".codex" / "agents").glob("*.toml"))
if not agents:
    errors.append("no custom agents found")

if errors:
    print("PAVAN CODEX OS validation: FAIL")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print(f"PAVAN CODEX OS validation: PASS ({len(skills)} skills, {len(agents)} agents)")
