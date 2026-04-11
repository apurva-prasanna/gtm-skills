# MEDDPICC Deal Qualifier

A Flask app built for adtech and media sales. Enter a client name and market — it researches the account across multiple angles and produces a structured MEDDPICC qualification document, flagging what came from research and what still needs to be validated directly.

Built as part of [Narratives & Nodes](https://apurvap.substack.com) — a build-in-public series on AI in enterprise GTM.

---

## What it does

Enter a client, market, and whatever context you have. The app:

1. Searches across multiple angles — financials, marketing leadership, agency relationships, digital strategy, competitive landscape, pain points, and recent news
2. Maps findings to each MEDDPICC element with adtech/media specificity
3. Detects whether the deal is brand-direct, agency-led, or joint
4. Tags every bullet as **Research** (from web search) or **To Validate** (the single most important gap per field)
5. Surfaces sources at the bottom of each field so you can dig deeper

The less context you provide, the more it flags as To Validate — which is usually the point. This tool is designed as the first cut of research when a rep starts on a new account, feeding directly into solution customisation and pitch preparation.

---

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/apurva-prasanna/gtm-skills.git
cd gtm-skills/meddpicc-qualifier
```

**2. Install dependencies**
```bash
pip3 install -r requirements.txt
```

**3. Set your Anthropic API key**
```bash
export ANTHROPIC_API_KEY=your_key_here
```
Get a key at [console.anthropic.com](https://console.anthropic.com).

**4. Run the app**
```bash
FLASK_RUN_PORT=5001 python3 -m flask run
```

Open [http://localhost:5001](http://localhost:5001) in your browser.

---

## MEDDPICC fields

| Letter | Element | What it captures |
|--------|---------|-----------------|
| M | Metrics | Business goals and marketing/brand goals — separated |
| E | Economic Buyer | Who controls budget; brand vs agency split; regional vs local authority |
| D | Decision Criteria | What local market buyers care about when evaluating ad tech partners |
| D | Decision Process | Agency procurement, trading desk approval, brand sign-off layers |
| P | Paper Process | IO process, MSA status, procurement and legal gates |
| I | Identify Pain | Measurement gaps, signal loss, ROI pressure, underperforming channels |
| C | Champion | Named advocates with evidence; what they need to make the internal case |
| C | Competition | Incumbent DSPs, walled gardens, local spend splits, holding group preferred partners |

---

## Part of Palm Tree

This tool is one of several builds under Palm Tree — a suite of AI tools for enterprise GTM in APAC. See the full repo at [github.com/apurva-prasanna/gtm-skills](https://github.com/apurva-prasanna/gtm-skills).
