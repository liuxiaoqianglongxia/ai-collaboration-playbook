# Task Package Registry Review Checklist

> Use this checklist to review a project-level V1.1 task-package registry and its latest pointers.

## 1. Routing Check

- [ ] `repository_full_name` matches the intended project.
- [ ] Current branch matches the task package.
- [ ] Root README title matches the intended project.
- [ ] Allowed write scope is explicit.

## 2. Project Fact Source Entry Check

- [ ] `CURRENT.md` exists or the task explains why it does not.
- [ ] `TASKS.md` exists or the task explains why it does not.
- [ ] `reports/latest.md` exists or the task explains why it does not.
- [ ] These files do not contradict the registry state.

## 3. tasks/README.md Check

- [ ] Explains ChatGPT task-package ownership.
- [ ] Explains Codex latest pointer.
- [ ] Explains Claude Code latest pointer.
- [ ] Says chat history is not execution authority.

## 4. tasks/codex/latest.md Check

- [ ] Points to one active Codex task or declares no active Codex task.
- [ ] Uses a stable status.
- [ ] Does not contain long task history.
- [ ] Does not conflict with `CURRENT.md`, `TASKS.md`, or `reports/latest.md`.

## 5. tasks/codex/<task-id>.md Check

- [ ] Contains task name, goal, repository, state, allowed scope, forbidden scope, work, validation, report format, stop conditions, and next step.
- [ ] Gives Codex enough information to execute without guessing from chat.
- [ ] Does not authorize deployment, database, credential, or production changes unless a separate safety package exists.

## 6. tasks/claude/latest.md Check

- [ ] Points to one active Claude Code task or declares no active Claude Code task.
- [ ] Does not replace Codex as final integrator.
- [ ] Does not conflict with project status files.

## 7. reports/chatgpt/task-packages/ Check

- [ ] Contains a README.
- [ ] Stores task-package or acceptance snapshots as named files.
- [ ] Does not replace `reports/latest.md`.

## 8. Codex Report Check

- [ ] Codex report records changed files.
- [ ] Validation commands are listed.
- [ ] Forbidden scope confirmation is explicit.
- [ ] Remaining issues and next action are clear.

## 9. Status Consistency Check

- [ ] `reports/latest.md` agrees with the task result.
- [ ] `CURRENT.md` agrees with the task result.
- [ ] `TASKS.md` agrees with the task result.
- [ ] latest pointers do not drift from named task files.

## 10. Forbidden Scope Check

- [ ] No business code changed outside allowed scope.
- [ ] No deployment performed.
- [ ] No database touched.
- [ ] No secrets, credentials, cookies, or tokens touched.
- [ ] No automation added without explicit authorization.

## 11. latest Pointer Drift Check

- [ ] latest pointer target exists.
- [ ] latest pointer status matches the named task state.
- [ ] completed task packages remain in named history files.

## 12. Stable Promotion Judgment

- [ ] At least one real project has run the registry flow.
- [ ] Codex report exists.
- [ ] ChatGPT read-only acceptance exists.
- [ ] Closeout fix or final acceptance evidence exists.
- [ ] Generic templates contain no project-specific business content.
- [ ] V4 four-piece model remains unchanged.

## Conclusion

```text
PASS / PARTIAL PASS / FAIL / BLOCKED
```
