# Claude Code Coordination Standard V1

> **Standard ID**: `CLAUDE_CODE_COORDINATION_V1`
> **Status**: Historical stable baseline from `PLAYBOOK_OPERATIONAL_BASELINE_V1.1`
> **Current V2 note**: historical coordination standard. V2 still requires Codex to coordinate Claude Code, but daily tasks default to Drive task packages.
> **Maintained in**: `ai-collaboration-playbook/standards/CLAUDE_CODE_COORDINATION_V1.md`

---

## Purpose

Define how Codex coordinates Claude Code without turning Claude Code into an independent default execution lane.

Claude Code is useful for local engineering depth. It is not the final integrator.

## Stable Role

Claude Code is appropriate for:

- deep code reading;
- call-chain and dependency analysis;
- test failure localization;
- local fix drafts;
- read-only diff review;
- second-opinion risk review.

Claude Code is not responsible for:

- replacing Codex as final integrator;
- merging PRs;
- deploying;
- changing production systems;
- changing databases;
- handling credentials or secrets;
- deciding final project status by itself.

## Coordination Rule

Codex may coordinate Claude Code during an active Codex task when it materially improves the result.

Stable coordination flow:

```text
1. Codex verifies the active task and allowed scope.
2. Codex creates or reads a bounded Claude Code task when needed.
3. Claude Code performs only the requested analysis, draft, or review.
4. Claude Code writes or returns evidence.
5. Codex verifies the evidence against the repository fact source.
6. Codex decides what enters the final diff and report.
7. ChatGPT validates from GitHub facts after Codex reports.
```

## User Experience Rule

The user should not manually relay long Claude Code task packages when Codex can coordinate the local workflow.

Current V2 preferred user-facing instruction:

```text
任务已写入 Drive：tasks/codex/YYYYMMDD/<task-name>.md；请读取该任务包执行，完成后写 Drive 报告。
```

The detailed Claude Code coordination belongs in the active task package and report. Use GitHub task files only when a project explicitly enables the GitHub-backed compatibility registry.

## Evidence Rule

Claude Code output is evidence, not authority.

Required handling:

- keep the Claude Code scope explicit;
- preserve the report path or summarized evidence;
- distinguish facts, inference, and suggestions;
- record whether Codex accepted, rejected, or modified the recommendation;
- clear `tasks/claude/latest.md` after the bounded subtask is complete.

## Boundary Rule

Claude Code does not replace Codex as final integrator.

Hermes, Qwen, MCP, heartbeat, automation, and subagents are not default stable execution members. They may enter only when a project fact source or explicit user authorization requires them.
