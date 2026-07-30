---
name: Feature request
about: Create a new feature request
title: "[Feature] "
labels:
  - type::feature
assignees: []
---

> [!IMPORTANT]
> Issues are public. Do not include confidential or sensitive information.

# <Feature Title>

## Problem to solve

Describe the business problem this feature addresses.

Consider answering:

- Why is this feature needed?
- What pain point does it solve?
- What is the origin of the problem?
- How does solving this problem benefit the business or its users?

## Solution

Provide a concise summary (2–4 sentences) of the proposed solution.

Describe **what** will be delivered and **how** it addresses the problem.
Leave implementation details for the **Proposal** section.

## User Stories / Requirements

### User Stories

List every relevant user story.

Format:

- As a **<role>**, I want **<capability>**, so that **<benefit>**.

### Requirements

List all functional requirements that define the feature scope.

Format:

- The system shall...

## Acceptance Criteria

List all verifiable conditions that must be satisfied before this issue can be considered complete.

Acceptance criteria should validate observable system behavior.

Format:

- [ ] ...

## Intended Users

Describe who will use this feature and how it benefits them.

Example:

- User Role: Benefit.

## Proposal

Describe the implementation in detail.

Include, where applicable:

- Domain model.
- CRUD operations.
- Business rules.
- Validation rules.
- API endpoints.
- Database/schema changes.
- Authorization considerations.
- Integration points with existing or future modules.
- Any other relevant implementation details.

## Implementation Checklist

- [ ] Review authorization changes.
- [ ] Add unit tests.
- [ ] Add integration / functional / E2E tests.
- [ ] Review or implement audit logs (tracks).
- [ ] Update documentation.
- [ ] Analyze data migration/backward compatibility.
- [ ] Review whether new credentials or secrets are required.
- [ ] Verify the code contributions checklist has been followed.

## Success Metrics

Describe how success will be measured.

Examples:

- Feature adoption.
- Successful completion of the intended workflows.
- Error reduction.
- Performance improvements.
- User satisfaction.

## Out of Scope

Explicitly list everything that is **not** included in this issue.

This section should clearly define the implementation boundaries and prevent scope creep.

## Further Notes

Include any additional context that may help implementation.

Examples:

- Design decisions.
- Assumptions.
- Dependencies.
- Risks.
- Future considerations.

## Links / References
