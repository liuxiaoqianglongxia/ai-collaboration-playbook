# Incident Report Template

> **Purpose**: Document production incidents, root causes, fixes, and prevention measures.
> **Applies to**: Any service disruption, data loss, security event, or deployment failure.
> **Place at**: `reports/incident/` directory.

## How to use

- File one report per incident.
- Name the file with date and short description: `YYYY-MM-DD-short-name.md`.
- Write the report as soon as possible after the incident is resolved.

---

# Incident Report — [Short Title]

| Field | Value |
|-------|-------|
| **Incident Date** | YYYY-MM-DD HH:MM |
| **Resolved Date** | YYYY-MM-DD HH:MM |
| **Duration** | [X hours / minutes] |
| **Severity** | Critical / High / Medium / Low |
| **Reported by** | [Agent / Human] |
| **Service(s) Affected** | [Service names] |

## Timeline

| Time | Event |
|------|-------|
| HH:MM | [Incident began — what happened] |
| HH:MM | [Detection — how it was discovered] |
| HH:MM | [Initial response — first action taken] |
| HH:MM | [Investigation — what was learned] |
| HH:MM | [Fix applied — what was done] |
| HH:MM | [Verification — how we confirmed fix] |
| HH:MM | [Incident resolved] |

## Impact

| Dimension | Details |
|-----------|---------|
| **Users affected** | [Who was impacted] |
| **Data affected** | [Was data lost, corrupted, or exposed?] |
| **Service downtime** | [How long was the service unavailable?] |
| **Business impact** | [Revenue, reputation, operational] |

## Root Cause

> What specifically caused this incident? Be precise — not "something broke."

## Fix Process

> What was done to fix it, step by step? Include commands, config changes, or code fixes.

## Acceptance / Verification

> How did we confirm the fix worked? Include health checks, test results, or monitoring data.

## Unresolved Risks

| Risk | Severity | Mitigation Plan |
|------|----------|-----------------|
| [Risk that remains] | High / Medium / Low | [What to do about it] |

## Prevention Measures

| Measure | Priority | Assignee | Target Date |
|---------|----------|----------|-------------|
| [What to add/change] | P0 / P1 / P2 | [Who] | YYYY-MM-DD |

## Rollback Plan

> If the fix itself causes problems, how do we roll back?

## Lessons Learned

> What did we learn from this incident? What would we do differently next time?
