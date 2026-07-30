---
name: Feature Request
about: Propose a new feature or enhancement
title: "[Feature]: "
labels:
  - type::feature
assignees: []
---

> [!IMPORTANT]
> Issues are public. Do not include confidential or sensitive information.
>
> Complete every applicable section before submitting the issue.

### Problem to solve

> Describe why this feature is needed.
>
> Include:
> - The business problem.
> - The pain point it solves.
> - Who is affected.
> - The origin of the problem.

### Solution

> Provide a concise summary (2–4 sentences) of the proposed solution.
>
> Explain the solution from the user's perspective.
> Save implementation details for the Proposal section.

### User Stories

> List all relevant user stories.
>
> Format:
>
> 1. As a **<actor>**, I want **<feature>**, so that **<benefit>**.
>
> Include every relevant actor impacted by this feature.

### Acceptance criteria

> List all verifiable conditions that must be satisfied before this issue can be considered complete.
>
> Write requirements as observable end-to-end behavior.
>
> Format:
>
> - [ ] The system shall...

### Intended users

> Describe who will use this feature.
>
> Include:
> - Primary users.
> - Secondary users (if applicable).
> - How each user benefits from the feature.

### Permissions and Security

> Describe any permission, authentication, authorization, or security considerations.
>
> Examples:
> - RBAC changes.
> - Authentication requirements.
> - Sensitive data.
> - Audit logs.
> - Security implications.

### Proposal

> Describe the implementation in detail.
>
> Include, where applicable:
>
> - Architecture changes.
> - Module structure.
> - API contracts.
> - Database/schema changes.
> - UI/UX changes.
> - Edge cases.
> - Rollout strategy.
> - Technical decisions.

### Test plan

> Describe how this feature will be validated.
>
> Include:
>
> - Business scenarios.
> - Edge cases.
> - Modules affected.
> - Existing tests to reference.

### Steps

- [ ] Review if authorization changes are needed.
- [ ] Build unit tests.
- [ ] Build other automated tests (functional/E2E).
- [ ] Review/implement audit logs (tracks).
- [ ] Update documentation.
- [ ] Analyze impact on data (e.g., ensure old records are not broken by new fields).
- [ ] Review changes involving new credentials (e.g., ensure new secrets are added to the secret rotation process).
- [ ] Make sure that the [code contributions checklist](https://docs.fluidattacks.com/internal/engineering/contributing) has been followed.

### What does success look like, and how can we measure that?

> Define measurable outcomes.
>
> Examples:
> - Feature adoption.
> - Performance improvements.
> - Error reduction.
> - User satisfaction.
> - Business KPIs.

### ETC model

> **Required**
>
> https://dev.fluidattacks.com/components/common/commit-msg/#eta
>
> Explain how the ETC model applies.
> If it does not apply, explain why.
>
> Include:
> - Entry.
> - Task.
> - Completion.

### Out of Scope

> Explicitly list what is **not** included in this feature.
>
> This section helps prevent scope creep.

### Further Notes

> Include any additional context that may help implementation.
>
> Examples:
> - Design decisions.
> - Assumptions.
> - Risks.
> - Dependencies.
> - Open questions.

### Links / references

> Documentation:
>
> Design:
>
> Related Issues:
>
> Pull Requests:
