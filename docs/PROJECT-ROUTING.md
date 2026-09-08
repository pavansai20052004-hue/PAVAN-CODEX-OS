# Automatic Project Routing

The adaptive orchestrator identifies the project before selecting specialist context.

## Cheap signals
- Web: `package.json`, Next/Vite/React configs.
- Mobile: Expo/React Native dependencies and app configs.
- Java backend: `pom.xml`, Gradle, Spring Boot markers.
- Python backend: `pyproject.toml`/requirements with FastAPI, Flask, or Django.
- AI/agent: OpenAI/Agents SDK, LangChain/LlamaIndex, vector DB, model-serving dependencies.
- Data/ML: pandas, scikit-learn, PyTorch/TensorFlow, notebooks.
- DevOps: Docker, Kubernetes, Terraform, Ansible, CI-heavy repositories.
- Mixed/full-stack: multiple strong frontend/backend signals.

## Routing examples
- React/Vite redesign → Core + Design Studio; design-director/responsive-system/UI reviewer.
- Figma implementation → Design Studio `figma-roundtrip`, then visual QA.
- Spring Boot API → Core + Backend Lab; api-builder/database-architect as needed.
- AI agent app → Core + Backend Lab `ai-agent-builder`; add UI skills only if the task touches UI.
- Intermittent production bug → root-cause-debugger + systems-thinker; deep-deliberation if C2/C3.
- Hackathon final → hackathon-judge-ready + production-qa, with design or backend skills only where they support the demo.

Routing should be revised only when new repository evidence contradicts the initial classification.
