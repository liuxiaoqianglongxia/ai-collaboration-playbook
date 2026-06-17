# V2.1 Absorption Acceptance Checklist

checklist_id: V2_1_ABSORPTION_ACCEPTANCE_CHECKLIST
base_stable: PLAYBOOK_OPERATIONAL_BASELINE_V2 / PASS
patch: DRIVE_NATIVE_V2_1_ABSORPTION_PATCH_CANDIDATE
status: candidate

## Compatibility

- [ ] Stable baseline still says `PLAYBOOK_OPERATIONAL_BASELINE_V2 / PASS`.
- [ ] Patch level is additive, not a competing baseline.
- [ ] Existing V2 projects can continue without full rewrite.
- [ ] Minimal Level 1 absorption is documented.

## Drive Write Boundary

- [ ] ChatGPT cannot claim unverified Drive writes.
- [ ] Parent-folder verification rule exists.
- [ ] Codex local Drive sync fallback exists.
- [ ] Root-level duplicate handling exists.

## Routing

- [ ] Claude Code is first-pass only.
- [ ] Interactive Claude Code usage is encouraged for high-token analysis.
- [ ] Codex remains final integrator.
- [ ] Codex report captures Claude evidence.

## Registry

- [ ] GitHub-backed registry remains compatibility only.
- [ ] No instruction restores repository-backed latest pointers as the daily dispatch surface.

## Safety

- [ ] No business project code changed.
- [ ] No deployment.
- [ ] No database change.
- [ ] No secrets change.
- [ ] No force push.
- [ ] No tag deletion.
- [ ] No main rewrite.

## Verdict

```text
Conclusion: PASS / PARTIAL PASS / FAIL / BLOCKED
```
