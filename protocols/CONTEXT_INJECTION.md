# Context Injection Protocol

> **Purpose**: Define how the primary agent injects project state and expert role context into sub-agents.
> **Version**: 1.0
> **Maintained in**: `ai-collaboration-playbook/protocols/CONTEXT_INJECTION.md`

---

## What Is Context Injection?

Context injection is the protocol for giving sub-agents the information they need to perform their tasks effectively — without bloating the parent agent's context window or relying on chat history.

Instead of embedding all project knowledge in a single system prompt, context injection:
1. **Separates** role profiles from project state
2. **Assembles** a targeted "fact packet" for each sub-agent
3. **Delivers** only the context relevant to the specific task
4. **Prevents** context pollution from irrelevant project details

## Why Chat History Is Not Enough

| Problem | Chat History | Context Injection |
|---------|-------------|-------------------|
| Persistence | Lost when session ends | Stored in GitHub files |
| Accuracy | Drifts over time | Updated via `CURRENT.md` |
| Specificity | Generic, conversational | Targeted to task |
| Reproducibility | Different each session | Deterministic from files |
| Auditability | Untraceable | File-based, versioned |

## Project Fact Source Files

The following files form the fact packet for context injection:

| File | Content | When to Include |
|------|---------|----------------|
| `CURRENT.md` | Project state, phase, risks | Always — the entry point |
| `TASKS.md` | Task list with acceptance criteria | When delegating tasks |
| `AGENTS.md` | Role definitions and boundaries | When multi-agent collaboration |
| `CLAUDE.md` | Claude Code rules | When Claude Code is active |
| `DECISIONS.md` | Decision history | When task relates to past decisions |
| Project-specific docs | Architecture, API, SOPs | When task requires domain knowledge |

## New Session Relay

When a new agent session starts:

1. **Read `CHATGPT_START_HERE.md`** — understand the entry protocol.
2. **Read `CURRENT.md`** — get current state.
3. **Read `TASKS.md`** — get pending work.
4. **Assemble fact packet** — only the files relevant to the first task.
5. **Delegate** with clear task package including fact packet reference.

## How Claude Code / Codex Task Packages Reference Fact Sources

A task package must include:

```
Task Package: [ID] [Description]
- Goal: [What needs to be achieved]
- Fact Sources:
  - CURRENT.md (project state)
  - TASKS.md (task context)
  - [specific file paths relevant to task]
- Constraints: [What must NOT be done]
- Acceptance: [How we know it's done]
- Stop Conditions: [When to stop and report]
```

The agent receiving the task reads only the listed fact sources — not the entire project.

## How to Control Context Pollution

| Technique | How | When |
|-----------|-----|------|
| **Fact packet minimization** | Only include files the sub-agent actually needs | Every delegation |
| **Role profile separation** | Keep role definitions in separate files, injected on demand | Multi-agent setup |
| **Project state snapshot** | Use `CURRENT.md` as the state entry, not full history | New sessions |
| **Context boundaries** | Explicitly tell sub-agent what NOT to read | Security-sensitive tasks |
| **Reference over content** | Say "read X.md" instead of pasting X.md content | Large files |
| **Progressive disclosure** | Start with minimal context, add more only if needed | Exploration tasks |
