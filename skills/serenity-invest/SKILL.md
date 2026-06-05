---
name: serenity-invest
description: Use when a user wants an agent to apply Serenity Invest Skills for AI supply-chain bottleneck research, including second-order bottleneck discovery, upstream anchor mapping, scout/pilot/core candidate classification, market regime checks, social diffusion, price-volume validation, and Bottleneck Research CLI context. Research-only: never provide personalized investment advice, buy/sell instructions, position sizing, or return promises.
---

# Serenity Invest Skills

Use this skill to run a disciplined AI supply-chain bottleneck research workflow.
The default data/context interface is the Bottleneck Research CLI.

## Hard Boundary

- This is research context, not investment advice.
- Never give personalized buy/sell instructions, position sizing, return
  promises, or automated trading actions.
- Convert "can I buy/sell?" into diligence: evidence, valuation, freshness,
  crowding, counter-evidence and next verification.
- Preserve provenance, source timestamp, confidence, missing evidence and
  freshness status.
- If primary evidence is missing, say so even when the narrative is attractive.

## CLI First

Prefer `br` if installed:

```bash
br --base-url https://bottleneckresearch.com agent-context --format markdown
```

Useful commands:

```bash
br --base-url https://bottleneckresearch.com decision-check MRVL --format markdown
br --base-url https://bottleneckresearch.com candidates --chain optical --limit 20 --format markdown
br --base-url https://bottleneckresearch.com candidates --chain storage --limit 20 --format markdown
br --base-url https://bottleneckresearch.com freshness --format markdown
```

If `br` is unavailable, tell the user to install:

```bash
pipx install git+https://github.com/chatjesus/bottleneck-research-cli.git
```

## Research Loop

1. Identify the object: ticker, chain, event, theme, market regime, or user
   watchlist question.
2. Pull the narrowest CLI context first:
   - ticker: `decision-check`
   - chain: `candidates --chain`
   - broad market: `agent-context`
   - data quality: `freshness`
3. Classify the signal:
   - `upstream_anchor`: chain-confirmation source, not an early setup by itself.
   - `scout_candidate`: early diffusion and plausible bottleneck logic, primary
     evidence incomplete.
   - `pilot_candidate`: scout plus price-volume or relative-strength
     confirmation, still small and evidence-controlled.
   - `core_candidate`: orders, capacity, ASP, EPS/revenue expectation, customer
     validation or management disclosure exists.
   - `no_chase`: late, crowded, single-day spike, stale, or missing primary proof.
4. Explain:
   - what the signal may indicate
   - why the chain matters
   - what is already priced or crowded
   - what evidence is missing
   - what would prove or kill the thesis
   - what to monitor next

## Second-Order Bottleneck Map

Track these chains before defaulting to obvious first-order AI winners:

- optical/CPO/silicon photonics/DSP/EML/CW laser/InP
- PCB/CCL/high-speed substrate/glass fiber/copper foil/resin
- MLCC/passive components/capacitors/power modules
- HBM/enterprise SSD/QLC NAND/nearline HDD/storage peripherals
- power/cooling/UPS/transformers/substations/data-center engineering
- advanced packaging/test/metrology/probe cards
- connectors/cables/liquid-cooling interfaces/high-speed interconnect
- Physical AI/robotics/edge modules/sensors/machine vision/automation

## Upstream Anchor Logic

Treat NVDA, MRVL, AVGO, LITE, COHR, hyperscalers and similar leaders as
confirmation sources. A strong anchor move should trigger downstream mapping,
not automatic trade conclusions.

Always ask:

- Which downstream chain is being confirmed?
- Which mapped names are still early versus crowded?
- What primary evidence is required for each mapped name?
- Is the move price-volume confirmed or only narrative diffusion?
- Is the data fresh enough to act as research context?

## Response Template

Use this concise structure:

```text
Research state:
Signal:
Why it matters:
What is priced/crowded:
Missing primary evidence:
Counter-evidence / kill criteria:
Next verification:
Boundary: research context only, not personalized investment advice.
```
