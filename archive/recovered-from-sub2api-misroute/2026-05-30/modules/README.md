# modules｜稳定模块目录

定位：存放已经验证、可以进入项目默认流程的稳定协作模块。

---

## 当前稳定模块

```text
CORE_FOUR_PIECE_V4
CORE_EXECUTION_HANDOFF_V1
CLAUDE_CODE_HARDENING_V1
ENV_COMMAND_SAFETY_V1
WSL_SERVER_PROD_GUARD_V1
```

---

## 稳定模块准入标准

一个能力从 `lab/` 升级到 `modules/`，必须满足：

```text
1. 有明确输入。
2. 有明确输出。
3. 有适用场景。
4. 有禁止事项。
5. 有停止条件。
6. 有报告格式。
7. 能连续稳定通过测试。
8. 不破坏 V4 四件套主链路。
9. 不增加多个 agent 抢改同一批文件的风险。
10. 不绕过 GitHub 事实源、Codex 收口和 ChatGPT 验收。
```

---

## 当前原则

```text
V4 主链路保持稳定。
新能力先进入 lab/。
实验有效后，再拆成稳定模块。
```
