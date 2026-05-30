# Experiment 002｜Skill Start Here Audit

状态：实验设计  
类型：Skill / workflow 复用实验  
是否进入稳定主链路：否

---

## 1. 目标

验证是否能把“进入项目先读事实源”封装成可复用 skill / workflow。

该实验目标不是写代码，而是让 Codex / Claude Code 在任何项目启动前，都能稳定完成：

```text
读取事实源
识别当前状态
识别任务边界
识别禁止事项
判断是否允许进入执行
```

---

## 2. 输入

```text
CHATGPT_START_HERE.md
AGENTS.md
CLAUDE.md
CURRENT.md
TASKS.md
DECISIONS.md
reports/latest.md
reports/codex/latest.md
reports/claude/latest.md
```

---

## 3. 预期 skill 名称

```text
start-here-audit
```

描述建议：

```text
Use when an AI agent starts work in a repository and must read project facts before making changes. Do not use for direct coding without state review.
```

---

## 4. 输出

必须输出：

```text
当前项目
当前分支
当前阶段
当前任务
启用模块
允许修改范围
禁止修改范围
风险 flags
是否允许 coding
建议下一步
```

---

## 5. 禁止事项

该 skill 默认只读。

禁止：

```text
修改文件
运行迁移
访问 .env
部署
提交代码
创建 PR
自动更改任务状态
```

---

## 6. Stop Conditions

遇到以下情况必须停止：

```text
CURRENT.md 与 TASKS.md 冲突
reports/latest.md 缺失
任务边界不清
涉及部署 / secrets / 数据库 / 生产配置
当前仓库状态不明
```

---

## 7. 验收标准

PASS：

```text
能稳定读事实源
能输出当前状态
能发现缺失文件
能判断是否允许执行
没有修改文件
```

FAIL：

```text
未读事实源就给建议
直接进入代码修改
忽略禁止事项
输出没有证据路径
```

---

## 8. 升级条件

如果实验稳定，未来可升级为：

```text
modules/START_HERE_AUDIT_V1.md
```

并成为新项目接入和 Codex 执行前的默认门禁。
