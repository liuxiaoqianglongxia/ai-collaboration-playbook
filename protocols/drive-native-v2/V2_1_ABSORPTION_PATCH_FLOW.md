# V2.1 Absorption Patch Flow

protocol_id: V2_1_ABSORPTION_PATCH_FLOW
base_stable: PLAYBOOK_OPERATIONAL_BASELINE_V2 / PASS
patch: DRIVE_NATIVE_V2_1_ABSORPTION_PATCH_CANDIDATE
status: candidate

## Flow

1. Keep current stable baseline as V2.
2. Add V2.1 as patch-level candidate.
3. Implement standards, guides, templates, and checklists additively.
4. Update public entrypoints with a short patch note only.
5. Test against at least one active V2 project and one small-project path.
6. Run private-path, GitHub registry residue, candidate/stable conflict, and registry-default scans.
7. Promote patch to PASS only after ChatGPT acceptance.

## Entrypoint Update Rule

Update only these public entrypoints initially:

```text
README.md
CHATGPT_START_HERE.md
AI_AGENT_ONBOARDING.md
reports/latest.md
guides/DRIVE_NATIVE_V2_USER_GUIDE.md
```

Do not rewrite all historical documents.

## Old-project Absorption Rule

Existing projects should use Level 1 absorption unless there is a specific maintenance task.

```text
Add patch-level lines. Do not rewrite everything.
```

## Codex / Claude Flow

```text
ChatGPT creates task package.
Codex opens branch.
Codex asks Claude Code for interactive first-pass review.
Claude produces first-pass report.
Codex applies final patch and validates.
Codex opens PR or leaves branch ready.
ChatGPT reviews and accepts.
```

## Stop Conditions

Stop and report `BLOCKED` if:

```text
- the change would alter production or business project code
- Drive parent folder cannot be verified and Codex fallback is unavailable
- patch creates two competing stable baselines
- public docs contain private local Drive paths
- default daily dispatch returns to GitHub registry
```
