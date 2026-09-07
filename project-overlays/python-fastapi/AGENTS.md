# Python / FastAPI Project Overlay

- Keep request schemas separate from persistence/domain models where useful.
- Validate external input with typed schemas.
- Keep blocking work out of async request paths unless explicitly isolated.
- Centralize configuration and never commit secrets.
- Test status codes, validation failures, auth boundaries, and failure paths.
- Run formatting/linting/type checks used by the repository plus pytest.
