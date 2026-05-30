# Codex 执行报告模板

> 用途：Codex 执行任务后写回项目仓库。报告必须基于实际文件、命令、测试和 diff，不得只写口头承诺。

## 任务名

`<task-name>`

## 结论

选择一个：

- PASS
- PARTIAL PASS
- FAIL
- BLOCKED

## 执行范围

```text
仓库：<owner/repo>
分支：<branch>
任务文件：<path>
执行环境：<local/dev/server/readonly>
```

## 实际修改文件

```text
<path>
<path>
```

若无修改，写：`无文件修改`。

## 实际执行命令或检查

```text
<command-or-check>
<command-or-check>
```

如果没有运行命令，说明原因。

## 测试结果

- `<test-or-check>`：PASS / FAIL / NOT RUN
- `<test-or-check>`：PASS / FAIL / NOT RUN

## diff 摘要

按模块说明修改了什么，不粘贴大段无关 diff。

## 禁止范围确认

逐项确认：

- 是否改密钥：否 / 是，说明。
- 是否改数据库：否 / 是，说明。
- 是否部署：否 / 是，说明。
- 是否改生产配置：否 / 是，说明。
- 是否跨项目写入：否 / 是，说明。
- 是否触碰任务禁止范围：否 / 是，说明。

## 未完成项

- `<item>`：原因与建议。

如果无，写：`无`。

## 风险与回滚

说明当前风险、可回滚文件、是否需要用户人工复核。

## 下一步建议

给 ChatGPT 验收或下一轮任务包的建议。
