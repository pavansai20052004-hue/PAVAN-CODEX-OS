from __future__ import annotations

import argparse
import json
from pathlib import Path


def read_lower(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore").lower()
    except OSError:
        return ""


def classify(root: Path) -> dict:
    scores: dict[str, int] = {}
    signals: list[str] = []

    def add(name: str, points: int, signal: str) -> None:
        scores[name] = scores.get(name, 0) + points
        signals.append(signal)

    package = read_lower(root / "package.json")
    if package:
        if '"expo"' in package or '"react-native"' in package:
            add("mobile", 6, "package.json: expo/react-native")
        if '"next"' in package:
            add("full-stack-web", 5, "package.json: next")
        if '"react"' in package or '"vue"' in package or '"svelte"' in package:
            add("frontend-web", 4, "package.json: frontend framework")
        if '"express"' in package or '"fastify"' in package or '"nestjs' in package:
            add("backend-api", 4, "package.json: Node backend")

    py = "\n".join(read_lower(root / p) for p in ("pyproject.toml", "requirements.txt", "requirements-dev.txt"))
    if py:
        if any(x in py for x in ("fastapi", "flask", "django")):
            add("backend-api", 5, "python: web backend framework")
        if any(x in py for x in ("openai", "langchain", "llama-index", "llamaindex", "agents-sdk")):
            add("ai-agent", 5, "python: AI/agent dependency")
        if any(x in py for x in ("scikit-learn", "sklearn", "torch", "tensorflow", "pandas")):
            add("data-ml", 4, "python: data/ML dependency")

    pom = read_lower(root / "pom.xml") + read_lower(root / "build.gradle") + read_lower(root / "build.gradle.kts")
    if "spring-boot" in pom or "org.springframework.boot" in pom:
        add("backend-api", 6, "JVM: Spring Boot")

    if (root / "Dockerfile").exists() or any(root.glob("docker-compose*.yml")) or any(root.glob("docker-compose*.yaml")):
        add("devops", 2, "Docker configuration")
    if any(root.rglob("*.tf")):
        add("devops", 5, "Terraform")
    if (root / "k8s").exists() or (root / "kubernetes").exists():
        add("devops", 4, "Kubernetes directory")

    strong_front = scores.get("frontend-web", 0) >= 4
    strong_back = scores.get("backend-api", 0) >= 4
    if strong_front and strong_back:
        scores["full-stack-web"] = max(scores.get("full-stack-web", 0), 8)
        signals.append("combined frontend + backend signals")

    ranked = sorted(scores.items(), key=lambda x: (-x[1], x[0]))
    family = ranked[0][0] if ranked else "unknown"
    top = ranked[0][1] if ranked else 0
    confidence = "high" if top >= 6 else "medium" if top >= 4 else "low"

    routing = {
        "frontend-web": ["premium-ui-designer", "responsive-system"],
        "full-stack-web": ["fullstack-builder"],
        "backend-api": ["api-builder"],
        "mobile": ["responsive-system"],
        "ai-agent": ["ai-agent-builder"],
        "data-ml": ["production-qa"],
        "devops": ["deployment-readiness"],
        "unknown": ["adaptive-orchestrator"],
    }

    return {
        "family": family,
        "confidence": confidence,
        "ranked_families": ranked[:4],
        "signals": signals[:20],
        "recommended_skills": routing.get(family, ["adaptive-orchestrator"]),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Classify a repository using cheap deterministic signals.")
    parser.add_argument("path", nargs="?", default=".")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = classify(Path(args.path).resolve())
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"family={result['family']} confidence={result['confidence']}")
        for signal in result["signals"]:
            print(f"- {signal}")


if __name__ == "__main__":
    main()
