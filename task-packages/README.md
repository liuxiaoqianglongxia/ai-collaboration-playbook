# Task Packages

This directory stores executable task packages for Claude Code, Codex, and other project agents.

The goal is to avoid long copy-paste prompts in chat. ChatGPT writes task packages into GitHub; execution agents read the relevant Markdown file from the repository and execute it exactly within the stated boundaries.

## How to use

For any task package, give the execution agent a short instruction:

```text
Read `<task-package-path>` from `liuxiaoqianglongxia/ai-collaboration-playbook` and execute it strictly. Do not rely on chat history. Stop if the package conflicts with current repo facts.
```

## Authority model

- `ai-collaboration-playbook/task-packages/` is the upstream task package source.
- A project-local execution report is the actual evidence of what was done.
- Business repositories remain their own execution authority after a task starts.
- ChatGPT remains the controller for architecture decisions, task routing, and acceptance.

## Parallel execution rule

Parallel Claude Code sessions are allowed only when they do **not** write the same branch, the same repository path, or the same output files.

Safe pattern:

```text
Main Executor   -> writes target feature branch
Review Agent    -> writes read-only review report branch
Security Agent  -> writes safety scan report branch
Closeout Agent  -> writes closeout report after main task completes
```

Unsafe pattern:

```text
Two agents writing the same feature branch
Two agents copying files into the same target directory
One agent cleaning while another agent audits
Any agent touching production without explicit authorization
```

## Result values

Use only:

- `PASS`
- `PARTIAL PASS`
- `FAIL`
- `BLOCKED`

## Standard final report fields

Every task package must require:

1. Status
2. Branch
3. Commit hash
4. Push status
5. PR link, if any
6. File list
7. `git status -sb`
8. `git diff --cached --name-only`
9. Safety confirmation
10. Next recommended phase
