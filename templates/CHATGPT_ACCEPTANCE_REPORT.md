# ChatGPT 验收报告模板

> 用途：ChatGPT 在读取 GitHub 事实源、任务文件、执行报告和必要 diff 后，给出验收结论。

## 验收对象

```text
仓库：<owner/repo>
分支：<branch>
任务文件：<path>
执行报告：<path>
commit / PR：<hash-or-url>
```

## 结论

选择一个：

- PASS
- PARTIAL PASS
- FAIL
- BLOCKED

## 已读取事实源

列出本次验收实际读取的文件或提交：

```text
<path-or-commit>
<path-or-report>
```

## 任务目标复述

用自己的话简要复述本轮原始目标，避免验收偏题。

## 验收结果

### 已完成

- `<item>`：依据 `<path/line/commit>`。

### 未完成

- `<item>`：原因与影响。

### 风险

- `<risk>`：建议处理方式。

## 禁止范围检查

- 是否改业务代码：否 / 是，说明。
- 是否改 V4 主链路：否 / 是，说明。
- 是否做 Claude Code 能力测试：否 / 是，说明。
- 是否接入自动化：否 / 是，说明。
- 是否处理业务项目：否 / 是，说明。
- 是否跨项目写入：否 / 是，说明。

## 证据摘要

列出最关键证据，不凭聊天承诺验收。

```text
<evidence>
<evidence>
```

## 下一步建议

- 如果 PASS：建议是否可以进入下一阶段。
- 如果 PARTIAL PASS：给出下一轮任务包方向。
- 如果 FAIL：说明应回滚、修复或重做。
- 如果 BLOCKED：说明需要用户提供什么。
