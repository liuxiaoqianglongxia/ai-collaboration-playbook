# GitHub connector 路由核验清单

> 用途：任何写入 GitHub 前，先确认 connector 没有路由到错误仓库。

## 必查项

- [ ] 已读取目标仓库 metadata。
- [ ] 返回的 `repository_full_name` 与用户指定仓库完全一致。
- [ ] 默认分支符合预期。
- [ ] 仓库 visibility、owner、repo name 符合预期。
- [ ] 已读取一个目标仓库中的已知文件，或确认空仓库返回空仓库状态。
- [ ] 文件内容没有显示成其他项目内容。

## 停止条件

只要出现以下任一情况，必须停止：

- `repository_full_name` 不匹配。
- README 或已知文件内容来自其他项目。
- connector 工具命名空间与目标仓库不一致。
- 用户给出的 URL 与 connector 返回仓库不一致。
- 无法确认当前写入目标。

## 写入前确认句式

```text
确认目标仓库为：<owner/repo>
确认当前分支为：<branch>
确认没有路由到：<wrong-repo-if-any>
本轮只允许写入：<allowed-paths>
```

## 验收标准

- 写入前已有明确仓库核验证据。
- 写入工具只调用目标仓库命名空间。
- 最终报告列出实际写入仓库 full name、分支和 commit。
