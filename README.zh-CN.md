# Serenity Invest Skills

[![Research only](https://img.shields.io/badge/boundary-research%20only-111111.svg)](#研究边界)
[![License: MIT](https://img.shields.io/badge/license-MIT-black.svg)](LICENSE)

**Serenity Invest Skills** 是一个开源 Agent 投研技能包，用来把 AI 供应链
瓶颈研究沉淀成 Codex、Claude Code、Cursor 等 Agent 可以直接执行的工作流。

[English](README.md) | 中文

## 它是什么

这个项目封装的是一套可复用的研究流程：

- 从 AI 需求映射到二阶供应链瓶颈
- 识别上游锚点和下游映射公司
- 区分早期 Scout、试仓 Pilot 和基本面验证后的 Core
- 检查数据新鲜度、拥挤度、来源和缺失的一手证据
- 通过 Bottleneck Research CLI 读取公开数据和上下文

它适合处理这类问题：

> MRVL 是单独标的，还是光链/网络链的上游确认器？

> 00894.HK 是 scout、pilot、core，还是 no-chase？

Agent 应该输出研究清单，而不是个性化交易指令。

## 安装

先安装 CLI：

```bash
pipx install git+https://github.com/chatjesus/bottleneck-research-cli.git
```

安装 skill：

```bash
mkdir -p ~/.codex/skills
cp -R skills/serenity-invest ~/.codex/skills/
```

然后在 Agent 里这样使用：

```text
使用 Serenity Invest Skills 检查 MRVL 的决策上下文。
使用 Serenity Invest Skills 查看光链候选。
使用 Serenity Invest Skills 判断 00894.HK 是 scout、pilot、core 还是 no-chase。
```

## 公开数据接口

这个 skill 调用 Bottleneck Research CLI：

```bash
br --base-url https://bottleneckresearch.com agent-context --format markdown
br --base-url https://bottleneckresearch.com decision-check MRVL --format markdown
br --base-url https://bottleneckresearch.com candidates --chain optical --limit 20 --format markdown
br --base-url https://bottleneckresearch.com freshness --format markdown
```

当前公开端点不需要 API key：

```bash
https://bottleneckresearch.com/data.json
```

## 研究框架

Serenity Invest Skills 默认使用这套结构：

1. **需求源**：AI capex、GPU/ASIC、数据中心、机器人、存储、电力。
2. **二阶瓶颈**：光链、PCB/CCL、MLCC/被动元件、电力冷却、存储周边、
   先进封装、测试、高速互连。
3. **上游锚点**：NVDA、MRVL、AVGO、LITE、COHR、云厂商或其他一手链条
   确认源。
4. **映射候选**：按市场映射上市公司，并保留来源和下一步验证要求。
5. **研究状态**：scout、pilot、core、no-chase、anchor-monitor。
6. **风险控制**：新鲜度、拥挤度、缺失一手证据、估值语境、反证和失效条件。

## 研究边界

这是研究技能包。它不是：

- 投资建议
- 买入/卖出推荐工具
- 组合配置或仓位管理工具
- 自动交易系统
- 独立尽调的替代品

输出必须保留来源、时间戳、置信度、缺失证据、数据新鲜度和反证。Agent 不能
为了让观点更好看而抹掉不确定性。

## 开发

```bash
python3 -m unittest discover -s tests
```

## 许可证

MIT License。详见 [LICENSE](LICENSE)。
