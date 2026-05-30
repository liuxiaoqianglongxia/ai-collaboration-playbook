# Experiment 004｜Memory Distillation

状态：实验设计  
类型：记忆蒸馏实验  
是否进入稳定主链路：否

---

## 1. 目标

验证能否从执行报告、失败记录和项目复盘中提取可复用经验，形成 memory candidates。

记忆蒸馏不是自动写正式记忆。

第一阶段只做：

```text
从报告中提取候选经验
标注适用场景
标注风险和证据
等待 ChatGPT / 人工验收
```

---

## 2. 输入

```text
reports/latest.md
reports/codex/latest.md
reports/claude/latest.md
reports/deploy/latest.md
reports/runs/*.md
```

可选输入：

```text
TASKS.md
DECISIONS.md
failure logs
PR review comments
```

---

## 3. 输出

建议输出目录：

```text
memories/candidates/
```

输出文件命名：

```text
memories/candidates/YYYY-MM-DD-<topic>.md
```

候选记忆格式：

```markdown
# Memory Candidate｜<topic>

## Source

- reports/codex/latest.md
- commit / PR / task file

## Observation

发生了什么？

## Reusable Lesson

可复用经验是什么？

## Applies When

什么场景适用？

## Does Not Apply When

什么场景不适用？

## Evidence

证据路径 / 报告 / diff / 测试结果。

## Risk

错误使用会有什么风险？

## Recommended Destination

- project-memory.md
- engineering-memory.md
- ops-memory.md
- role failure-log
- role experience-log
```

---

## 4. 禁止事项

禁止：

```text
自动写正式 memory
把 memory 当当前事实源
从失败日志直接生成强制规则
写入未经验证的经验
写入密钥、个人隐私、生产配置
覆盖 CURRENT.md / TASKS.md / reports/latest.md
```

---

## 5. 核心原则

```text
Memory 是经验，不是事实。
CURRENT.md 才是当前事实。
reports/latest.md 才是最新报告。
任务文件才是执行依据。
```

---

## 6. 验收标准

PASS：

```text
只生成候选记忆
候选记忆有来源证据
候选记忆标注适用场景
没有写入正式记忆
没有泄露敏感信息
```

FAIL：

```text
自动把候选写成正式规则
把 memory 当事实源
提取无证据结论
包含密钥 / 隐私 / 生产配置
```

---

## 7. 升级条件

连续通过后，可考虑升级为：

```text
modules/REPO_MEMORY_V1.md
modules/EXPERIENCE_FAILURE_LOG_V1.md
```

但正式 memory 写入仍需 ChatGPT / 人工验收。
