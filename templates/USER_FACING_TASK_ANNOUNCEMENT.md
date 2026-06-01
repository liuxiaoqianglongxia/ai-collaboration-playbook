# User-Facing Task Announcement Template

> V2 default: use this when ChatGPT assigns a Drive task package. Keep chat short; keep the full task package in Drive. Use GitHub-backed registry wording only when a project explicitly enables that compatibility layer.

```text
任务：<TASK-ID>
能实现：
- <one concrete outcome>
- <one concrete outcome>
- <one concrete outcome>
不做：<key boundary>
你发给 Codex：任务已写入 Drive：tasks/codex/YYYYMMDD/<task-name>.md；请读取该任务包执行，完成后写 Drive 报告。
详情：任务包已在 Drive。
```

## Rules

- Do not paste the full task package in chat by default.
- Do not hide what the task is for.
- Do not overload the user with implementation steps.
- Do not claim the task package is in Drive or GitHub unless it actually exists there.
- If ChatGPT cannot write GitHub in the current session, say so and provide the smallest safe fallback.
- If an active Codex task already exists, do not announce a second active task for the same stage.
