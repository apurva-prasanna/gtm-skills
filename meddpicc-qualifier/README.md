# MEDDIC Deal Qualifier

A Flask app that researches a client using web search and produces a MEDDIC qualification document — flagging what's confirmed, what came from research, and what still needs to be validated.

Built as part of [Narratives & Nodes](https://apurvap.substack.com) — a build-in-public series on AI in enterprise GTM.

---

## What it does

Enter a client name, market, and whatever context you have about the deal. The app:

1. Searches the web for recent news, financial performance, org structure, and strategic priorities
2. Maps findings to each MEDDIC element
3. Tags every bullet as **Confirmed** (from your input), **Research** (from web search), or **To Validate** (gaps you still need to close)

The less context you provide, the more it flags as To Validate — which is usually the point.

---

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/apurva-prasanna/gtm-skills.git
cd gtm-skills/meddic-qualifier
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
python3 app.py
```

Open [http://localhost:5000](http://localhost:5000) in your browser.

---

## MEDDIC fields

| Letter | Element | What it captures |
|--------|---------|-----------------|
| M | Metrics | Business, marketing, and campaign KPIs |
| E | Economic Buyer | Who approves spend; brand vs agency split |
| D | Decision Criteria | What matters when evaluating partners |
| D | Decision Process | Timeline, stakeholders, procurement gates |
| I | Identify Pain | Core problem and cost of inaction |
| C | Champion | Internal advocate and what they need to succeed |

---

## Part of the GTM Skills repo

This tool is one of several builds documenting AI leverage points in complex enterprise GTM. See the full repo at [github.com/apurva-prasanna/gtm-skills](https://github.com/apurva-prasanna/gtm-skills).
