# Team Boss Routing Protocol

> **Purpose**: Define how the total control (ChatGPT) routes tasks to the right agent.
> **Version**: 1.0
> **Maintained in**: `ai-collaboration-playbook/protocols/TEAM_BOSS_ROUTING.md`

---

## How the Boss Routes Tasks

The total control (ChatGPT) is the router. It receives a goal, decomposes it into tasks, and assigns each task to the most appropriate agent based on capability, access, and risk.

### Routing Decision Matrix

| Task Type | Route To | Why |
|-----------|----------|-----|
| Architecture judgment | ChatGPT (self) | Requires high-level understanding |
| Task package creation | ChatGPT (self) | Requires decomposition skill |
| Acceptance review | ChatGPT (self) | Requires judgment against criteria |
| Code exploration | Claude Code | Deep local file analysis |
| Bug investigation | Claude Code | Local root cause analysis |
| Draft fix proposal | Claude Code | Local engineering, clearly marked as draft |
| Audit report | Claude Code | Read-only analysis with findings |
| Code review | Claude Code | Correctness and safety check |
| Test execution | Codex | Run tests, report pass/fail |
| Fix application | Codex | Apply approved drafts, verify |
| PR creation | Codex | Integration and delivery |
| Delivery report | Codex | Summarize results of task execution |
| File creation/edit (Markdown) | Claude Code or Codex | Depends on complexity |
| Production deployment | Codex (with human confirmation) | Requires integration and rollback |
| Security audit | Claude Code | Deep analysis, no modifications |
| Emergency hotfix | Codex (fast track) | Speed-critical, minimal scope |

## Tasks That Require Human Confirmation

| Task | Why Human |
|------|-----------|
| Production deployment | Risk to real users |
| Database migration | Data loss risk |
| Credential rotation | Security impact |
| Repository force push | History rewrite |
| Deleting files/directories | Irreversible action |
| Merging to main branch | Integration risk |
| Changing infrastructure | System-level impact |
| Exposing secrets or sensitive data | Security and compliance |

## Result Classification

After any task execution, the boss classifies the result:

| Result | Criteria | Boss Action |
|--------|----------|-------------|
| **PASS** | All acceptance criteria met, no risks | Mark task done, proceed to next |
| **PARTIAL PASS** | Core done but follow-up needed | Create follow-up task, note in TASKS.md |
| **FAIL** | Criteria not met or regression | Create fix task, assign to appropriate agent |
| **BLOCKED** | Cannot proceed due to external constraint | Create unblock task or escalate to human |

## Routing Examples

### Example 1: "Fix the auth bug"

1. ChatGPT reads `CURRENT.md` to understand project state.
2. ChatGPT reads bug description from `TASKS.md` or issue.
3. ChatGPT routes to **Claude Code**: "Investigate the auth bug in `src/auth.py`. Read the file, trace the login flow, identify the root cause. Report findings with line numbers."
4. Claude Code reports: "Root cause: token expiry check at line 87 uses wrong comparison operator."
5. ChatGPT routes to **Codex**: "Apply the fix from Claude Code report at `reports/claude/latest.md`. Run all tests. Create PR if tests pass."
6. Codex applies fix, tests pass, creates PR, writes delivery report.
7. ChatGPT reviews PR, accepts, marks task done.

### Example 2: "Audit the project for security issues"

1. ChatGPT routes to **Claude Code**: "Read `CLAUDE.md` for safety rules. Scan all Python files for common security patterns: hardcoded secrets, SQL injection, path traversal, insecure deserialization. Report findings with file paths and severity."
2. Claude Code produces audit report.
3. ChatGPT classifies findings by priority, creates tasks for each high-severity issue.
4. Tasks are routed to appropriate agents for fixing.

## How to Handle Agent Failure

When an agent reports FAIL or BLOCKED:

1. Read the agent's report to understand what went wrong.
2. Determine if the failure is due to:
   - **Insufficient context** → Provide additional fact sources, retry.
   - **Task ambiguity** → Clarify the task, break into smaller pieces, retry.
   - **Technical blocker** → Create a separate unblock task.
   - **Safety concern** → Respect the stop condition, do not override.
3. Route the retry or unblock task to the appropriate agent.
