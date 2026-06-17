# ChatGPT Drive Tool Capability Boundary V2.1

standard_id: CHATGPT_DRIVE_TOOL_CAPABILITY_BOUNDARY_V2_1
base_stable: PLAYBOOK_OPERATIONAL_BASELINE_V2 / PASS
status: candidate
scope: ChatGPT controller, Drive workbench writes, Codex fallback

## Purpose

Define what counts as a successful ChatGPT Drive write in Drive-native V2 and what must happen when ChatGPT cannot reliably write to the intended project Drive workbench.

## Core Rule

ChatGPT may say a file was written to Drive only when all of these are true:

```text
1. The target project Drive workbench is known.
2. The file title/path is known.
3. The parent folder is the intended project folder or subfolder.
4. The created or updated file is not only a Drive root or unknown-location artifact.
5. The result can be referenced by a Drive path, file id, or verified folder listing.
```

If any condition is false, ChatGPT must not claim the Drive write succeeded.

## Capability Levels

### Level A: Verified direct Drive write

Use when ChatGPT can create or update a file in the intended Drive workbench and verify the parent folder.

Allowed claim:

```text
Written to project Drive workbench:
<verified path or file reference>
```

### Level B: Unverified Drive creation

Use when ChatGPT can create a document, but cannot verify it is inside the intended project folder.

Required claim:

```text
Created a Drive document, but parent folder is not verified. Treat this as not yet written to the project workbench.
```

Required next action:

```text
Fallback to Codex local Google Drive sync directory or ask user to move the file manually before treating it as a project fact.
```

### Level C: No Drive write capability

Use when ChatGPT cannot write to Drive from the current session.

Required claim:

```text
Current ChatGPT session cannot write to the target Drive workbench. I will produce a Codex task package to create/update the file in the local Google Drive sync directory.
```

## Fallback Rule

When direct Drive write is unverified or unavailable, ChatGPT must create a Codex task package that instructs Codex to write the file through the local Google Drive sync directory.

Codex must report:

```text
- project Drive workbench relative path
- local sync path used, if safe to record in private Drive report
- file names created or updated
- parent folder verified: yes/no
- root-level duplicate found: yes/no
- if duplicate exists: cleanup recommendation
```

## Root-level Duplicate Rule

A Drive file created in root or unknown location is not a project workbench fact.

It must be treated as one of:

```text
- draft artifact pending relocation
- duplicate to delete manually
- source material, not stable fact
```

## Public Documentation Rule

Public GitHub docs must not depend on private local Drive paths as the only access route.

Private local sync paths may appear in private Drive reports when operationally necessary, but public docs should use project-relative Drive paths or generic placeholders.

## Anti-long-task-package Rule

ChatGPT must not paste full daily task packages into user chat by default.

Default user-facing handoff:

```text
任务：<TASK-ID>
入口：Drive task package
执行者：Codex
完成后：写回 Drive report
```

Full task package text may be pasted only when:

```text
1. no shared Drive or GitHub task surface is available, or
2. the user explicitly asks for the full text, or
3. it is needed as a fallback artifact and clearly marked as copy-paste fallback.
```

## Acceptance Checklist

- [ ] ChatGPT did not claim an unverified Drive write.
- [ ] Parent folder was verified or fallback was triggered.
- [ ] Root-level residue was checked.
- [ ] User received a short handoff, not a long task package by default.
- [ ] Codex fallback report contains enough evidence for ChatGPT acceptance.
