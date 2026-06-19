# Project State Standard

> **Purpose**: Define the standard project lifecycle states and the required fields for state tracking files.
> **Version**: 1.0
> **Maintained in**: `ai-collaboration-playbook/standards/PROJECT_STATE.md`

---

## Lifecycle States

Every project in the AI collaboration system should declare its current state.

| State | Emoji | Meaning | Allowed Actions | Required Artifacts |
|-------|-------|---------|----------------|-------------------|
| **ACTIVE** | 🟢 | Under active development | All normal operations | `CURRENT.md`, `TASKS.md`, recent commits |
| **FROZEN** | 🔴 | Temporarily locked — no changes | Read-only audit only | Reason for freeze, who authorized it |
| **ARCHIVED** | 📦 | Preserved for reference, not maintained | Reference and cite | Archive date, successor project (if any) |
| **EXPERIMENTAL** | 🧪 | Proof-of-concept, early exploration | Free experimentation | "Experimental" declaration |
| **PRODUCTION** | 🏭 | Serving real users with SLA | Changes via staging first | Health checks, monitoring, rollback plan |
| **DEPRECATED** | ⚠️ | Being phased out | Maintenance only, no new features | Sunset date, migration path |
| **BLOCKED** | 🚧 | Cannot proceed due to external constraint | Unblock investigation | Blocking factor, who can resolve |
| **UNKNOWN** | ❓ | Status cannot be determined | Audit required | Last known activity date |

## State Transitions

```
EXPERIMENTAL → ACTIVE (proof validated)
EXPERIMENTAL → ARCHIVED (experiment abandoned)
ACTIVE → PRODUCTION (ready for users)
ACTIVE → FROZEN (risk identified)
ACTIVE → DEPRECATED (superseded)
PRODUCTION → DEPRECATED (sunset planned)
FROZEN → ACTIVE (risk resolved)
FROZEN → ARCHIVED (not worth unfreezing)
BLOCKED → ACTIVE (blocker removed)
BLOCKED → ARCHIVED (blocker unresolvable)
DEPRECATED → ARCHIVED (sunset complete)
```

## Required Fields in State File

Every project's state file (typically `CURRENT.md` or `STATE.md`) must include:

| Field | Required | Description |
|-------|----------|-------------|
| **Status** | Yes | One of the 8 lifecycle states above |
| **Branch** | Yes | Current git branch |
| **Last Commit** | Yes | Hash + message of most recent commit |
| **Phase** | Yes | Current project phase name |
| **Fact Source** | Yes | URL or path to the single source of truth |
| **Active Tasks** | If ACTIVE | Summary of P0 tasks (full list in TASKS.md) |
| **Freeze Reason** | If FROZEN | Why the project is frozen |
| **Archive Date** | If ARCHIVED | When the project was archived |
| **Health Check** | If PRODUCTION | URL and expected response |
| **Blocker** | If BLOCKED | What is blocking progress |
| **Last Audit** | Recommended | Date of last state audit or drift check |

## State Validation Checklist

Run this checklist periodically to verify state accuracy:

- [ ] Status in `CURRENT.md` matches actual project activity
- [ ] Branch exists and is not detached
- [ ] Last commit hash matches `git log -1`
- [ ] No untracked files that should be committed
- [ ] If PRODUCTION: health check passes
- [ ] If FROZEN: no commits since freeze date
- [ ] If DEPRECATED: sunset date is still valid
