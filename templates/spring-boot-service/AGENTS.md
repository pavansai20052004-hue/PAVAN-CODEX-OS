# Spring Boot Service Template

Suggested shape:

```text
src/main/java/.../
  controller/
  service/
  repository/
  domain/
  dto/
  config/
src/test/java/.../
```

Use constructor injection, request validation, explicit API error handling, environment-driven configuration, and tests appropriate to controller/service/repository boundaries. Keep migrations/versioned schema changes explicit.
