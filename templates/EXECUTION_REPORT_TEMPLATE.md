# Execution Report Template

> **Purpose**: Standard format for reporting the results of any AI agent task execution.
> **Applies to**: Claude Code audits, Codex deliveries, ChatGPT acceptance checks.
> **Place at**: `reports/` directory or project root.

> **Template Authority**: This file is an upstream template from `ai-collaboration-playbook`. When copied into a project repository, remove the `_TEMPLATE` suffix and use the format as-is or adapt field names. The project-local copy becomes the execution authority for that project, while this template remains the upstream baseline.

## How to use

- Fill all fields. If a field is not applicable, write "N/A" with reason.
- Use PASS / PARTIAL PASS / FAIL / BLOCKED for status.
- Be specific in file lists and test results.

---

## Execution Report — [Task Name]

| Field | Value |
|-------|-------|
| **Status** | PASS / PARTIAL PASS / FAIL / BLOCKED |
| **Executed by** | [Claude Code / Codex / ChatGPT / Human] |
| **Date** | YYYY-MM-DD |
| **Branch** | [branch name] |
| **Commit** | `[hash] [message]` |
| **Pushed** | Yes / No / N/A |

## Execution Scope

> What was attempted. Be specific about the boundaries of the work.

## Files Modified

> List all files that were created, modified, or deleted.

| Action | File Path | Description |
|--------|-----------|-------------|
| Created | `path/to/file.md` | [What and why] |
| Modified | `path/to/file.py` | [What changed] |
| Deleted | `path/to/old.md` | [Reason] |

## Test Results

| Test Suite | Result | Notes |
|-----------|--------|-------|
| [Suite name] | PASS / FAIL | [Brief note] |
| [Suite name] | PASS / FAIL | [Brief note] |

## Safety Confirmation

- [ ] No secrets committed (no `.env`, `auth.json`, token files)
- [ ] No databases committed (no `*.db`, `*.sqlite`)
- [ ] No logs committed (no `logs/`, `backups/`)
- [ ] No `node_modules/` committed
- [ ] No backup files committed (no `*.tar.gz`, `*.zip`)
- [ ] No business source code modified outside task scope

## Unresolved Items

| Item | Severity | Reason | Next Step |
|------|----------|--------|-----------|
| [What wasn't resolved] | High / Medium / Low | [Why] | [What to do next] |

## Next Steps

1. [Recommended action, who should do it]
2. [Recommended action, who should do it]

## Acceptance Notes

> Any additional context, observations, or warnings for the reviewer.
