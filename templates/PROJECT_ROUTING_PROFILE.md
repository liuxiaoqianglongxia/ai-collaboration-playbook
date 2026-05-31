# Project Routing Profile Template

> Copy into a project repository only after adapting it to that project.

## Project

```text
repository_full_name: <owner/name>
default_branch: <branch>
primary_fact_source: <CHATGPT_START_HERE.md or equivalent>
```

## Universal Baseline

```text
playbook_baseline: PLAYBOOK_OPERATIONAL_BASELINE_V1.1
one_active_execution_lane: yes
github_is_fact_source: yes
codex_final_integrator: yes
claude_code_final_integrator: no
```

## Project Layer

Project-specific fact files:

```text
CHATGPT_START_HERE.md
AGENTS.md
CLAUDE.md
CURRENT.md
TASKS.md
DECISIONS.md
reports/latest.md
tasks/codex/latest.md
tasks/claude/latest.md
reports/codex/latest.md
reports/claude/latest.md
```

## Routing

| Lane | Allowed In This Project | Owner | Notes |
|---|---|---|---|
| ChatGPT direct docs/task/report work | yes/no | ChatGPT | Only when safe and GitHub write access exists |
| Codex local execution | yes/no | Codex | Final integration and report owner |
| Claude Code deep review | yes/no | Codex coordinates | Evidence only |
| Qwen or cheap model batch work | yes/no | <owner> | Bounded summarization only |
| Hermes / historical tooling | yes/no | <owner> | Optional project-specific tool |
| MCP / official docs lookup | yes/no | <owner> | Must not override project fact source |
| Automation | yes/no | <owner> | Requires explicit authorization |
| Production / deploy / database / secrets | yes/no | <owner> | Separate safety task required |

## Hard No

```text
no force push unless explicitly authorized
no database changes unless explicitly authorized
no deployment unless explicitly authorized
no credential or secret edits unless explicitly authorized
no cross-project state copying
no second active Codex task in the same stage
```

## Current Task Pointers

```text
tasks/codex/latest.md: <none-or-task-path> / <status>
tasks/claude/latest.md: <none-or-task-path> / <status>
```

## Review Cadence

```text
update_when: project phase changes, new high-risk lane is authorized, optional tool becomes allowed/forbidden
review_by: ChatGPT controller and Codex executor
```
