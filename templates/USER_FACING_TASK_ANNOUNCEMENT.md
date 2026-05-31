# User-Facing Task Announcement Template

> Use this when ChatGPT assigns a GitHub-backed Codex task. Keep chat short; keep the full task package in GitHub.

```text
任务：<TASK-ID>
能实现：
- <one concrete outcome>
- <one concrete outcome>
- <one concrete outcome>
不做：<key boundary>
你发给 Codex：执行 tasks/codex/latest.md，完成后更新 reports/codex/latest.md。
详情：任务包已在 GitHub。
```

## Rules

- Do not paste the full task package in chat by default.
- Do not hide what the task is for.
- Do not overload the user with implementation steps.
- Do not claim the task package is in GitHub unless it actually exists in the repository.
- If ChatGPT cannot write GitHub in the current session, say so and provide the smallest safe fallback.
- If an active Codex task already exists, do not announce a second active task for the same stage.
