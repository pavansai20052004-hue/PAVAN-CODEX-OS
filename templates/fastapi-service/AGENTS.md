# FastAPI Service Template

Suggested shape:

```text
app/
  api/
  core/
  models/
  schemas/
  services/
  repositories/
tests/
```

Use typed settings, Pydantic schemas at boundaries, explicit error mapping, dependency injection where it improves testability, and pytest coverage for service/API behavior. Keep secrets in environment configuration and provide `.env.example` with names only.
