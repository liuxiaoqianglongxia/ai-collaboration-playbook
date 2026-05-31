# PLAYBOOK-V1.1-FINAL-USER-GUIDE-ROUTING-PRO-REVIEW-V1 Codex Report

## 1. Conclusion

PASS

## 2. Repository

- Repo: `liuxiaoqianglongxia/ai-collaboration-playbook`
- Branch: `docs/playbook-v1-1-final-user-guide-routing-pro-review-v1`
- HEAD: `a7988512b89e1472042f003b4931f161036d015a` before this task branch commit
- PR: pending branch push / controller review

## 3. User-Facing Result

The playbook now has a daily user guide:

```text
guides/USER_OPERATING_GUIDE_V1.md
```

The guide explains what the user should say, what ChatGPT/Codex/Claude Code do, how to read task status, what a task announcement looks like, and what not to do.

## 4. Files Read

```text
CHATGPT_START_HERE.md
README.md
AI_AGENT_ONBOARDING.md
AI_COLLABORATION_MODE_V4.md
reports/latest.md
reports/codex/latest.md
reports/claude/latest.md
tasks/codex/latest.md
tasks/claude/latest.md
standards/TASK_PACKAGE_REGISTRY_V1_1.md
standards/EXECUTION_LANE_MANAGEMENT_V1.md
standards/CLAUDE_CODE_COORDINATION_V1.md
protocols/GITHUB_AI_COLLABORATION.md
templates/USER_FACING_TASK_ANNOUNCEMENT.md
templates/CODEX_TASK_PACKAGE.md
templates/CLAUDE_CODE_READONLY_ANALYSIS_TASK.md
templates/tasks/codex/_template.md
templates/tasks/claude/_template.md
checklists/TASK_PACKAGE_REGISTRY_REVIEW.md
checklists/CODEX_BEFORE_EXECUTION_CHECK.md
checklists/CLAUDE_CODE_HARDENING.md
lab/
archive/
whitepapers/
reports/codex/
reports/claude/
Anthropic Claude Code CLI docs
Local `claude --help` and `claude --version`
```

Preflight note: `tasks/codex/latest.md` pointed to this active task while `reports/latest.md` still described the previous no-active state. Because the named task existed on `origin/main`, the branch was created from `origin/main`, and the task explicitly allowed updating `reports/latest.md` and clearing the latest pointer, this was treated as assignment-pointer lag and reconciled in this closeout.

## 5. Files Changed

```text
README.md
CHATGPT_START_HERE.md
guides/USER_OPERATING_GUIDE_V1.md
docs/README.md
standards/ROUTING_AND_EXTENSIBILITY_V1.md
templates/PROJECT_ROUTING_PROFILE.md
reports/chatgpt/pro-review/PRO_REVIEW_START_HERE.md
reports/chatgpt/personalization/PERSONALIZATION_CANDIDATE_V1.md
reports/latest.md
reports/codex/latest.md
reports/codex/playbook-v1-1-final-user-guide-routing-pro-review-v1.md
tasks/codex/latest.md
```

## 6. User Guide

Added `guides/USER_OPERATING_GUIDE_V1.md`.

It is Chinese-first, user-facing, and keeps daily operation short:

```text
用户给目标
ChatGPT 读取 GitHub 事实源
Codex 执行 active task
Claude Code only supports when Codex coordinates it
Codex writes reports/codex/latest.md
ChatGPT validates from GitHub
```

## 7. Routing And Extensibility

Added `standards/ROUTING_AND_EXTENSIBILITY_V1.md` and `templates/PROJECT_ROUTING_PROFILE.md`.

The standard separates:

```text
Universal layer
Project layer
Execution lane
Tool lane
Research lane
High-risk lane
```

It keeps Hermes, Qwen, MCP, heartbeat, automation, and subagents optional and project-specific.

## 8. Codex / Claude Code Research

Local evidence:

```text
command -v claude -> /Users/liuxiaoqiang/.local/bin/claude
claude --version -> 2.1.158 (Claude Code)
claude --help -> confirms interactive default and -p/--print non-interactive output
claude -p --tools "" --max-turns 1 "Reply with exactly OK." -> OK
git status --short after Claude checks -> clean
```

One attempted Linux-style timeout wrapper failed because macOS lacks `timeout` by default:

```text
timeout 30 claude ... -> /bin/bash: timeout: command not found
```

Practical conclusion:

- Codex can call Claude Code from local shell when `claude` is installed and authenticated.
- Non-interactive mode is available through `-p/--print`.
- `--tools ""` is a safe pattern for no-tool smoke checks.
- Interactive Claude Code can require TTY and human permission handling, so it should stay outside stable automation unless separately tested.
- File-based handoff through `tasks/claude/latest.md` and `reports/claude/latest.md` remains the stable standard.

Official docs consulted:

```text
https://docs.anthropic.com/en/docs/claude-code/cli-reference
https://docs.anthropic.com/en/docs/claude-code/sdk
https://docs.anthropic.com/en/docs/claude-code/settings
```

## 9. Pro Review Entry

Added:

```text
reports/chatgpt/pro-review/PRO_REVIEW_START_HERE.md
```

It includes current stable status, read order, solved items, Pro reasoning questions, known uncertainties, and freeze judgment criteria.

## 10. Personalization Candidate

Added:

```text
reports/chatgpt/personalization/PERSONALIZATION_CANDIDATE_V1.md
```

It contains candidate Personal Details and Custom Instructions only. It is not final until ChatGPT accepts or revises it.

## 11. Validation Commands

```text
git status -sb
git branch --show-current
git remote -v
git fetch origin --prune
git rev-parse origin/main
git log --oneline -12 origin/main
command -v claude
claude --version
claude --help
claude -p --tools "" --max-turns 1 "Reply with exactly OK."
git diff --name-only origin/main...HEAD
git diff --stat origin/main...HEAD
git diff --check origin/main...HEAD
grep -R "USER_OPERATING_GUIDE\|使用说明\|用户使用" -n README.md CHATGPT_START_HERE.md guides docs reports/chatgpt || true
grep -R "ROUTING_AND_EXTENSIBILITY\|routing\|路由\|扩展" -n README.md CHATGPT_START_HERE.md standards protocols templates reports/chatgpt || true
grep -R "PRO_REVIEW\|Pro review\|Pro 深度" -n reports/chatgpt README.md CHATGPT_START_HERE.md || true
grep -R "Personal Details Candidate\|Custom Instructions Candidate\|个人详情\|自定义指令" -n reports/chatgpt || true
grep -R "one active\|active execution lane\|NO_ACTIVE_CODEX_TASK" -n README.md CHATGPT_START_HERE.md standards protocols templates tasks reports/latest.md || true
grep -R "Claude Code.*final integrator\|Claude Code.*replace Codex\|Hermes.*default\|五件套" -n README.md CHATGPT_START_HERE.md standards protocols templates reports/chatgpt || true
git diff --name-only origin/main...HEAD | grep -E '^(AI_COLLABORATION_MODE_V4.md|lab/|archive/|whitepapers/|modules/)' && exit 1 || true
```

## 12. Forbidden Scope Confirmation

```text
No AI_COLLABORATION_MODE_V4.md change.
No lab/ archive/ whitepapers/ modules/ writes.
No business repository touched.
No production system touched.
No database touched.
No credentials or secrets touched.
No automation publish chain touched.
No force push.
No self-merged PR.
No V0.3 redesign.
No Hermes / Qwen / MCP / heartbeat / automation / subagent default-member promotion.
Claude Code did not write repository files.
```

## 13. Remaining Issues

None for this task.

The personalization file remains a candidate and should be accepted or revised by ChatGPT before being copied into actual Personal Details or Custom Instructions fields.

## 14. Next Step

Open a PR from `docs/playbook-v1-1-final-user-guide-routing-pro-review-v1` to `main` for ChatGPT/controller review. Do not merge without explicit authorization.
