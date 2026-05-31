# Pro Review Start Here

> Purpose: first source file for a future ChatGPT Pro deep review of `PLAYBOOK_OPERATIONAL_BASELINE_V1.1`.

## Current Stable Status

```text
repository_full_name: liuxiaoqianglongxia/ai-collaboration-playbook
baseline: PLAYBOOK_OPERATIONAL_BASELINE_V1.1
reports/latest.md: PASS
current task pointers after Codex closeout: none / NO_ACTIVE_CODEX_TASK, none / NO_ACTIVE_CLAUDE_TASK
```

## Read Order

```text
reports/latest.md
guides/USER_OPERATING_GUIDE_V1.md
README.md
CHATGPT_START_HERE.md
AI_AGENT_ONBOARDING.md
AI_COLLABORATION_MODE_V4.md
standards/TASK_PACKAGE_REGISTRY_V1_1.md
standards/EXECUTION_LANE_MANAGEMENT_V1.md
standards/CLAUDE_CODE_COORDINATION_V1.md
standards/ROUTING_AND_EXTENSIBILITY_V1.md
protocols/GITHUB_AI_COLLABORATION.md
templates/USER_FACING_TASK_ANNOUNCEMENT.md
templates/PROJECT_ROUTING_PROFILE.md
reports/chatgpt/personalization/PERSONALIZATION_CANDIDATE_V1.md
reports/codex/latest.md
reports/claude/latest.md
```

## What Has Been Solved

- V4 four-piece role model remains stable.
- GitHub is the fact source.
- V1.1 task-package registry reduces long chat copy-paste.
- One-active-execution-lane rule is documented.
- Claude Code is coordinated by Codex and does not replace Codex.
- User-facing task announcement format is short.
- Routing/extensibility guidance now separates universal rules from project facts and optional tools.
- User operating guide exists.
- Personalization content is prepared as a candidate, not final.

## User Concern To Review Carefully

The user believes Claude Code is still underused.

Current V1.1 correctly keeps Claude Code out of the default final-integrator role, but the Pro review should check whether the playbook is too conservative in practice.

The important correction is:

```text
Claude Code is not only a reviewer.
Claude Code can also perform bounded coding work, local edits, draft fixes, debugging, refactors, and implementation subtasks.
Codex should not waste quota doing every task if Claude Code can safely do the first-pass work.
Codex should be reserved for final integration, hard failures, full validation, PR ownership, and tasks Claude Code cannot safely complete.
```

The target is not to make Claude Code a fifth default member. The target is to make Claude Code a real execution-support worker inside the active execution lane, while still keeping:

```text
ChatGPT: controller and acceptance
Codex: final integrator, verifier, PR/report owner, hard-problem executor
Claude Code: deep engineering assistant, bounded implementation worker, local draft generator, reviewer
GitHub: fact source
```

## Claude Code Value-Maximization Question

Pro should not only ask whether Claude Code is safe. Pro should ask how to maximize Claude Code value without losing control.

Core question:

```text
How should the system route work so Claude Code handles as much safe engineering work as possible, while Codex only handles final integration, validation, PR/report ownership, and tasks Claude Code cannot do well?
```

Potential routing idea to evaluate:

```text
Claude Code first-pass worker:
- bounded local code edits;
- small bugfix drafts;
- isolated file changes;
- test failure analysis and patch proposal;
- refactor draft inside an explicit file list;
- implementation alternatives for Codex to choose from.

Codex final integrator:
- verify repository state;
- review Claude-generated diff;
- reject or normalize unsafe changes;
- run tests;
- commit / push / PR;
- write reports/codex/latest.md;
- escalate to ChatGPT when blocked.
```

## Specific Claude Code Review Questions

Pro should answer these directly:

```text
1. Is Claude Code coordination in V1.1 too passive?
2. Should medium-risk tasks default to a Claude Code first-pass implementation or analysis before Codex spends heavy effort?
3. Which work should be Claude-first, Codex-final?
4. Should complex bugfixes, multi-file refactors, failed tests, or architecture-risk tasks default to Codex-coordinated Claude Code work?
5. What exact task package fields should trigger Claude Code as reviewer vs implementer?
6. Should tasks/claude/latest.md be used more often, or should Codex invoke Claude Code directly and only summarize evidence?
7. What is the safest stable pattern for non-interactive Claude Code invocation from Codex?
8. When is Claude Code allowed to write files, and how must Codex verify those writes?
9. What remains experimental because it needs TTY, human confirmation, auth setup, broad permissions, or unsafe tools?
10. How should Claude Code output be recorded so ChatGPT can verify it without reading huge local logs?
11. How can the system use Claude Code more without making the user copy long Claude prompts?
12. What minimum examples should be added to templates so future projects actually use Claude Code as a worker, not only a reviewer?
```

## Sources Pro Should Research

Pro should research and compare at least these sources:

```text
1. Official Claude Code CLI reference.
2. Official Claude Code settings / permissions docs.
3. Official Claude Code hooks / skills / plugins / SDK docs, if available.
4. OpenClaw skill design and SKILL.md-style routing patterns.
5. Hermes or project-local skill/task patterns that call or coordinate Claude Code.
6. Existing files in this playbook repository related to Claude Code:
   - standards/CLAUDE_CODE_COORDINATION_V1.md
   - templates/CLAUDE_CODE_READONLY_ANALYSIS_TASK.md
   - templates/tasks/claude/_template.md
   - checklists/CLAUDE_CODE_HARDENING.md
   - reports/claude/latest.md
```

If OpenClaw or Hermes repositories / docs are not accessible in the current session, Pro should say so and request the repo links or file paths instead of guessing.

## Claude Code Research Hints From Current Validation

Previous Codex validation found:

```text
command -v claude -> installed locally in that environment
claude --version -> Claude Code available
claude -p --tools "" --max-turns 1 "Reply with exactly OK." -> OK
```

Stable inference from that task:

```text
- Non-interactive Claude Code invocation is possible when Claude Code is installed and authenticated.
- `-p/--print` is the likely stable mode for Codex-driven checks.
- `--tools ""` or restricted tool lists are safer for smoke tests and read-only analysis.
- Interactive Claude Code may require TTY and human permission handling, so it should not be treated as stable automation without a separate experiment.
- File-based handoff through tasks/claude/latest.md and reports/claude/latest.md remains the safest stable pattern.
```

Pro should verify whether this is sufficient or too weak.

## Design Patterns Pro Should Consider

### Pattern A: File-based Claude Code handoff

```text
ChatGPT/Codex writes tasks/claude/<TASK-ID>.md
Codex or user runs Claude Code against that file
Claude Code writes reports/claude/<REPORT-ID>.md
Codex reads the report
Codex decides what enters final diff/report
ChatGPT validates from GitHub
```

Best for:

```text
read-only review
architecture review
complex bug analysis
high-risk diff review
bounded implementation drafts when a durable task/report is required
```

Weakness:

```text
More files and pointer hygiene.
Can feel heavy if overused.
```

### Pattern B: Codex invokes Claude Code non-interactively

```text
Codex runs a bounded command such as:
claude -p --tools "" --max-turns 1 <prompt-or-file>
Codex captures output into reports/codex or reports/claude evidence
Codex remains final integrator
```

Best for:

```text
quick second opinion
read-only diff review
summarizing a failure trace
checking assumptions before editing
```

Weakness:

```text
Requires Claude Code installed/authenticated locally.
Must avoid broad tools, unsafe permissions, or hidden writes.
```

### Pattern C: Codex invokes Claude Code with restricted read tools

```text
claude -p --tools "Read,Grep,Glob" --max-turns <small-number> <bounded-review-prompt>
```

Best for:

```text
deep repository reading without write authority
call-chain analysis
multi-file context gathering
```

Weakness:

```text
Needs reliable permission/tool syntax across environments.
Should be validated before stabilizing.
```

### Pattern D: Claude Code bounded implementation worker

```text
Codex verifies active task and allowed scope.
Codex creates a bounded Claude Code implementation prompt with explicit file list, forbidden paths, stop conditions, and expected diff/report.
Claude Code performs a first-pass implementation or patch draft.
Codex reviews the working tree diff.
Codex runs tests and validation.
Codex either accepts, modifies, rejects, or escalates the Claude Code work.
Codex owns the final commit, PR, and reports/codex/latest.md.
```

Best for:

```text
small bug fixes
localized frontend/backend changes
copy/paste mechanical edits
low-risk refactor drafts
writing tests suggested by Codex
fixing obvious lint/type/test failures
preparing alternate implementations for Codex to choose from
```

Required boundaries:

```text
Claude Code must receive explicit allowed files or directories.
Claude Code must not modify secrets, deployment, production, database, or unrelated files.
Claude Code should not push, merge, or own PR status.
Codex must inspect the diff before commit.
Codex must run validation appropriate to the task.
ChatGPT accepts only from GitHub facts and Codex report.
```

### Pattern E: Claude Code patch-file worker

```text
Claude Code writes a patch file or implementation notes instead of editing the repository directly.
Codex applies, edits, or rejects the patch.
```

Best for:

```text
when write permissions are risky
when Claude Code is useful but should not touch the working tree
when comparing multiple approaches
when preserving a clear review boundary
```

Weakness:

```text
More manual integration for Codex.
Less efficient than direct local edits for simple tasks.
```

### Pattern F: Interactive Claude Code session

```text
Codex starts or coordinates an interactive Claude Code session.
Human may approve or guide permission prompts.
```

Best for:

```text
long manual analysis sessions
exploratory refactoring
when the user explicitly wants interactive local Claude Code
```

Weakness:

```text
TTY/human-permission dependence.
Harder to standardize as hidden automation.
Not suitable as default unless separately proven.
```

## Draft Routing Matrix For Pro To Evaluate

```text
Task type                              Preferred first worker            Final owner
Safe doc/task/report update             ChatGPT if GitHub write exists     ChatGPT
Small localized code change              Claude Code or Codex               Codex
Mechanical multi-file edit               Claude Code first-pass              Codex
Test failure investigation               Claude Code analysis                Codex
Complex bugfix                           Claude Code analysis + draft         Codex
Architecture-risk refactor               Claude Code review/draft             Codex
Full integration / PR                    Codex                               Codex
Production / deployment / DB / secrets   Separate high-risk task              Codex + ChatGPT acceptance
```

Pro should decide whether this routing is correct, too aggressive, or still too conservative.

## OpenClaw / Hermes Comparison Questions

Pro should specifically investigate whether OpenClaw / Hermes skill design suggests useful improvements, for example:

```text
1. Skill files with clear name / purpose / trigger / allowed tools / stop conditions.
2. Workspace-scoped skills that are only loaded for a project.
3. Explicit routing rules that decide when a capability is available.
4. Local script wrappers that make tool calls repeatable.
5. Capability manifests that prevent every prompt from restating the same boundary.
6. Security checks for third-party or community skills.
7. Skill-level allowed write paths for Claude Code implementation subtasks.
8. Standard skill templates for implementation, review, debugging, and report writing.
```

Important boundary:

```text
Do not copy OpenClaw / Hermes architecture wholesale.
Extract only stable patterns that improve V1.1.
Keep V4 four-piece model unchanged.
Do not turn Hermes / OpenClaw / skills into default members.
Do not let skill routing bypass GitHub facts, one-active-lane discipline, or Codex final integration.
```

## Questions For Pro Reasoning

1. Is the user-facing guide short enough for daily use?
2. Are the Personal Details and Custom Instructions candidates concise enough for ChatGPT personalization fields?
3. Does `ROUTING_AND_EXTENSIBILITY_V1` keep the playbook flexible instead of rigid?
4. Are optional tools clearly useful without becoming default members?
5. Is the one-active-execution-lane rule too strict for any legitimate parallel read-only review scenario?
6. Are there contradictions between `reports/latest.md`, latest pointers, and the standards?
7. What should be removed before freezing Personal Details and Custom Instructions?
8. Is Claude Code underused in the current stable workflow?
9. What exact, safe default triggers should route suitable tasks into Claude Code support?
10. Should Claude Code be allowed to perform bounded implementation work by default for low/medium-risk tasks?
11. How should Codex verify Claude Code edits before owning the final commit/PR?
12. Should the playbook add a stable `CLAUDE_CODE_INVOCATION_PATTERNS_V1` doc, or keep invocation examples in templates only?

## Known Uncertainties

- Future project rollout may reveal project-specific exceptions.
- Claude Code interactive coordination can require TTY and human permission handling; only non-interactive no-tools smoke was verified in the last task.
- Claude Code write-capable workflows need stronger validation than read-only review workflows.
- Claude Code CLI and settings features can change, so Pro should verify current official docs before recommending a stable invocation pattern.
- Qwen, Hermes, MCP, heartbeat, automation, and subagents remain optional or experimental unless a project fact source authorizes them.
- Pro should check whether the candidate personalization is too project-management-heavy for everyday ChatGPT use.
- OpenClaw / Hermes references should be treated as design references, not sources of authority, unless the actual repo/docs are read.

## Do Not Change Casually

- Do not rewrite `AI_COLLABORATION_MODE_V4.md` without explicit authorization.
- Do not add a fifth default member.
- Do not make Claude Code final integrator.
- Do not turn optional tools into defaults.
- Do not mix business project facts into this generic playbook.
- Do not weaken GitHub fact-source discipline.
- Do not authorize production, database, secrets, deployment, automation, or force push by default.

## Freeze Judgment

The playbook is stable enough to freeze Personal Details and Custom Instructions only if:

```text
1. reports/latest.md remains PLAYBOOK_OPERATIONAL_BASELINE_V1.1 / PASS.
2. latest task pointers are clear after the active task closes.
3. candidate personalization is short, general, and not tied to one PR.
4. V4 role boundaries remain intact.
5. optional tools remain project-specific, not default.
6. user daily workflow remains short: goal -> GitHub-backed task -> Codex report -> ChatGPT acceptance.
7. Claude Code has a practical route to be used often enough on suitable tasks without burdening the user.
8. Claude Code can perform bounded implementation work where safe, not just review.
9. Codex remains final integrator and verifier for Claude Code work.
10. OpenClaw / Hermes / skill-style patterns are considered for routing and repeatability, but only stable, safe patterns are promoted.
```

## Expected Output From Pro

```text
1. Final verdict: PASS / PARTIAL PASS / FAIL / BLOCKED.
2. Whether Personal Details and Custom Instructions should be frozen now.
3. Claude Code utilization verdict: sufficient / underused / overcomplicated / unsafe.
4. Recommended stable Claude Code triggers.
5. Recommended Codex -> Claude Code invocation patterns.
6. Recommended Claude Code implementation-worker boundaries.
7. Which tasks should be Claude-first and which must remain Codex-first.
8. Which OpenClaw / Hermes / skill-style ideas should be adopted, deferred, or rejected.
9. Minimal required edits before freeze, if any.
10. Final copyable Personal Details and Custom Instructions.
```