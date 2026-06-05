# Serenity Invest Skills

[![Research only](https://img.shields.io/badge/boundary-research%20only-111111.svg)](#research-boundary)
[![License: MIT](https://img.shields.io/badge/license-MIT-black.svg)](LICENSE)

**Serenity Invest Skills** is an open-source agent skill pack for AI supply-chain
bottleneck research. It helps Codex, Claude Code, Cursor, and other coding
agents turn public market data, supply-chain evidence, community diffusion, and
price-volume signals into structured diligence.

English | [中文](README.zh-CN.md)

## What It Is

This project packages a repeatable research workflow:

- map AI demand into second-order supply-chain bottlenecks
- identify upstream anchors and downstream mapped companies
- separate early scout ideas from confirmed core candidates
- check freshness, crowding, provenance and missing primary evidence
- use the Bottleneck Research CLI as the public data/context interface

The skill is designed for questions such as:

> Is MRVL a standalone idea, or an upstream anchor for optical/network names?

> Is 00894.HK a scout candidate, pilot candidate, core candidate, or no-chase?

The answer should be a research checklist, not a personalized trade instruction.

## Install

Install the CLI first:

```bash
pipx install git+https://github.com/chatjesus/bottleneck-research-cli.git
```

Install the skill locally:

```bash
mkdir -p ~/.codex/skills
cp -R skills/serenity-invest ~/.codex/skills/
```

Then ask your agent:

```text
Use Serenity Invest Skills to decision-check MRVL.
Use Serenity Invest Skills to review optical chain candidates.
Use Serenity Invest Skills to classify 00894.HK as scout, pilot, core, or no-chase.
```

## Public Data Interface

The skill calls the Bottleneck Research CLI:

```bash
br --base-url https://bottleneckresearch.com agent-context --format markdown
br --base-url https://bottleneckresearch.com decision-check MRVL --format markdown
br --base-url https://bottleneckresearch.com candidates --chain optical --limit 20 --format markdown
br --base-url https://bottleneckresearch.com freshness --format markdown
```

The public endpoint currently requires no API key:

```bash
https://bottleneckresearch.com/data.json
```

## Research Framework

Serenity Invest Skills uses this default structure:

1. **Demand source**: AI capex, GPU/ASIC, data centers, robotics, storage, power.
2. **Second-order bottleneck**: optical, PCB/CCL, MLCC/passives, power/cooling,
   storage peripherals, advanced packaging, test, interconnect.
3. **Upstream anchor**: NVDA, MRVL, AVGO, LITE, COHR, hyperscalers or other
   primary chain-confirmation sources.
4. **Mapped candidates**: listed companies by market with provenance and next
   evidence requirements.
5. **Research state**: scout, pilot, core, no-chase, anchor-monitor.
6. **Risk control**: freshness, crowding, missing primary evidence, valuation
   context, counter-evidence and kill criteria.

## Research Boundary

This is a research skill pack. It is not investment advice, and it is not:

- investment advice
- a buy/sell recommendation engine
- a portfolio or position-sizing tool
- an automated trading system
- a substitute for independent diligence

Outputs should preserve provenance, timestamps, confidence, missing evidence,
freshness status and counter-evidence. Agents should never remove uncertainty to
make an idea sound cleaner than the underlying evidence.

## Development

```bash
python3 -m unittest discover -s tests
```

## License

MIT License. See [LICENSE](LICENSE).
