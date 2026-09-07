# Spring Boot Project Overlay

- Preserve controller/service/repository responsibilities unless architecture requires otherwise.
- Prefer constructor injection.
- Validate request DTOs at the boundary.
- Use explicit exception mapping for API errors.
- Keep secrets and environment-specific settings outside source control.
- Add tests at service/controller boundaries appropriate to the change.
- Run the repository's Maven/Gradle test and package/build commands.
