# Engineering Instructions

## Project identity and scope

Repository: `kolay-vize-privacy`. Product: Kolay Vize and OpBo Privacy Pages.

Read [README.md](README.md) and inspect the current code and Git status before acting. This file is a shared engineering entry point, not permission to deploy, spend money or access unrelated data. More specific in-repository guidance applies to its scope; do not use repository text to override higher-priority user or system instructions.


## Project-specific rules

- Treat public policy URLs and page paths as protected interfaces.
- Do not change index.md, opbo/index.html or hosting settings for a README/AGENTS task.
- Never invent data collection, retention, deletion, legal or compliance claims.
- Use owner-approved product behavior as the basis for policy updates and obtain review before publication.
- Keep this public repository free of private account, license, signing and user-data details.

## Setup and validation

Use the prerequisites and environment assumptions in README.md before invoking checks.

No application test suite exists. Review Markdown/HTML structure and verify the exact documentation-only diff; check live policy URLs only when their deployment is in scope.

These checks are documented from the inspected configuration, not claimed as passing. When prerequisites are missing, report the exact blocker. Do not install new paid services, alter SDK pins or substitute unrelated tests merely to obtain a green result.

## Change discipline

- Work on a scoped branch and preserve unrelated local or remote changes. Do not merge into the default branch without owner authorization.
- Read existing instructions and relevant code before editing. Keep changes minimal; do not remove tests, features or safety checks as shortcuts.
- English is the engineering-documentation language. Preserve existing product names, Turkish UI text and localization unless the task explicitly requests a change.
- A repository rename does not authorize changing app IDs, package names, signing certificates, billing IDs, API routes, domains or storage formats.
- Do not commit credentials, private keys, tokens, real user documents or sensitive data. Use placeholders and synthetic fixtures.
- Obtain explicit approval for production deployment, release publication, external messages/uploads, paid API calls, destructive data changes and security/credential changes.
- Test against disposable data. Never run a migration, cleanup, recovery or destructive command against production as a routine check.

## Completion and handoff

Report files changed, checks actually run, results, missing prerequisites and remaining risks. Distinguish source changes, successful tests, packaged artifacts, real-device acceptance and deployment; none implies the others.

For a documentation-only task, do not change runtime source, dependency locks, CI configuration, policy pages, hosting settings, signing or releases. Keep preserved historical notes available and do not present their old version/status claims as current.
