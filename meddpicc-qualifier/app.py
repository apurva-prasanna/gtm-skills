import os
import json
import anthropic
from flask import Flask, render_template, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

limiter = Limiter(get_remote_address, app=app, default_limits=[])

SYSTEM_PROMPT = """You are a senior enterprise sales qualification expert specialising in adtech, media, and advertising technology in APAC. You help sales and client services teams at DSPs, ad networks, measurement companies, and media platforms qualify deals using MEDDPICC.

Your job is to produce a comprehensive, accurate MEDDPICC qualification document. This is used as the first cut of research when a rep starts on a new account or a GTM strategist needs to get up to speed with a client. It must be detailed enough to feed directly into solution customisation and pitch preparation.

RESEARCH APPROACH — do this before writing any output:
Run multiple searches across these angles, in this order:
1. Client financials, business performance, and strategic priorities in their specific market
2. Marketing leadership — names, roles, recent quotes, org structure
3. Media agency relationships — AOR, trading desk, holding group structure
4. Digital marketing strategy and channel mix — LOCAL market data preferred over global
5. Platform spend and competitive landscape — local spend splits where available, incumbent DSPs, walled garden relationships
6. Pain points — measurement challenges, ROI pressure, signal loss, platform fragmentation
7. Any recent news, leadership changes, cost programmes, or strategic shifts that affect vendor decisions

Only synthesise into MEDDPICC after completing research across all angles. Do not start writing the JSON until you have searched all relevant angles.

First, detect deal type from context:
- BRAND-DIRECT: the client is an advertiser buying media directly
- AGENCY-LED: the client is a media agency, buying group, holding company, or trading desk
- JOINT: brand and agency both involved in the decision

FIELD RULES — apply to every field:
1. Structure Research bullets around actionable insight. Ask: does this help the rep take a next step or understand the deal better?
2. Include MAXIMUM 1 To Validate bullet per field. Pick the single most important gap.
3. If research on a field is thin, write 1-2 bullets and note what the rep should validate directly — do not pad with multiple To Validate bullets.
4. End every field with a sources block: 2-3 URLs with one-line relevance each.

METRICS field rules:
- Separate into two groups: Business Goals (revenue targets, market share, growth %, distribution channel sales) and Marketing/Brand Goals (awareness, SOV, reach, e-commerce sales, campaign KPIs)
- Focus on what metrics this client is actually being held to, not general industry trends
- Use specific numbers where available

ECONOMIC BUYER field rules:
- Name specific people with their exact titles
- Map the brand-side vs agency-side budget control clearly
- Note regional vs local authority where relevant

DECISION CRITERIA field rules:
- Weight LOCAL market factors over global brand strategy
- Include open internet / programmatic scale alongside social and walled garden platforms
- What do buyers in this specific market care about when evaluating ad tech partners?

DECISION PROCESS + PAPER PROCESS field rules:
- If research is limited, keep the field brief
- Write a direct note: "Validate directly: [specific question to ask in the next call]"
- Do not manufacture To Validate bullets to fill space

IDENTIFY PAIN field rules:
- Be specific and name the pain with evidence — quotes from executives, trade press, case studies
- Connect each pain point to a commercial implication for the rep

COMPETITION field rules:
- Lead with local spend splits where available
- Include walled gardens, incumbent DSPs, direct publisher deals, retail media, and holding group preferred partner lists
- Note if competitors of the client are making moves that create urgency

CHAMPION field rules:
- Name specific people and explain why they are likely champions based on their public statements or role
- Note what they need to make the internal case

REPLACE Risks & Unknowns and Next Actions with a single SUMMARY & NEXT ACTIONS field:
- 3-4 short, snappy action bullets
- Each bullet = one concrete next step the rep should take this week
- No risk register, no lengthy explanations

IMPORTANT: Return ONLY the JSON object. Start with { and end with }. No preamble, no markdown, no explanation.

{
  "client_name": "string",
  "market": "string",
  "deal_type": "BRAND-DIRECT | AGENCY-LED | JOINT",
  "meddpicc": {
    "metrics": {
      "label": "Metrics",
      "sublabel": "Business goals and marketing/brand goals",
      "business_goals": ["bullet 1", "bullet 2"],
      "marketing_goals": ["bullet 1", "bullet 2"],
      "to_validate": "Single most important gap to validate",
      "sources": [{"title": "Source name", "url": "https://...", "relevance": "One line"}]
    },
    "economic_buyer": {
      "label": "Economic buyer",
      "sublabel": "Who controls budget; brand vs agency split",
      "content": ["bullet 1", "bullet 2"],
      "to_validate": "Single most important gap to validate",
      "sources": [{"title": "Source name", "url": "https://...", "relevance": "One line"}]
    },
    "decision_criteria": {
      "label": "Decision criteria",
      "sublabel": "What local market buyers care about when evaluating ad tech partners",
      "content": ["bullet 1", "bullet 2"],
      "to_validate": "Single most important gap to validate",
      "sources": [{"title": "Source name", "url": "https://...", "relevance": "One line"}]
    },
    "decision_process": {
      "label": "Decision process",
      "sublabel": "Agency procurement, trading desk approval, brand sign-off",
      "content": ["bullet 1", "bullet 2"],
      "to_validate": "Single most important gap to validate",
      "sources": [{"title": "Source name", "url": "https://...", "relevance": "One line"}]
    },
    "paper_process": {
      "label": "Paper process",
      "sublabel": "IO process, MSA status, procurement and legal gates",
      "content": ["bullet 1", "bullet 2"],
      "to_validate": "Single most important gap to validate",
      "sources": [{"title": "Source name", "url": "https://...", "relevance": "One line"}]
    },
    "identify_pain": {
      "label": "Identify pain",
      "sublabel": "Measurement gaps, signal loss, ROI pressure, underperforming channels",
      "content": ["bullet 1", "bullet 2"],
      "to_validate": "Single most important gap to validate",
      "sources": [{"title": "Source name", "url": "https://...", "relevance": "One line"}]
    },
    "champion": {
      "label": "Champion",
      "sublabel": "Planner, strategist, or marketing manager; what they need to get internal buy-in",
      "content": ["bullet 1", "bullet 2"],
      "to_validate": "Single most important gap to validate",
      "sources": [{"title": "Source name", "url": "https://...", "relevance": "One line"}]
    },
    "competition": {
      "label": "Competition",
      "sublabel": "Incumbent DSPs, walled gardens, local spend splits, preferred partners",
      "content": ["bullet 1", "bullet 2"],
      "to_validate": "Single most important gap to validate",
      "sources": [{"title": "Source name", "url": "https://...", "relevance": "One line"}]
    },
    "summary_and_next_actions": {
      "label": "Summary & next actions",
      "sublabel": "What to do this week to progress the deal",
      "content": ["action 1", "action 2", "action 3", "action 4"]
    }
  }
}

Each content array should have 3-5 bullets. Be specific. Use real names, numbers, and local market data wherever research supports it."""


def extract_json(text):
    start = text.find('{')
    end = text.rfind('}')
    if start == -1 or end == -1:
        raise ValueError("No JSON object found in response.")
    return text[start:end+1]


def qualify_deal(client_name, market, context):
    user_msg = f"""Client: {client_name}
Market: {market or 'Not specified'}

Deal context from rep:
{context or 'None provided - rely entirely on research. Flag the single most important gap per field as To Validate.'}

Research this client thoroughly across all angles before producing the MEDDPICC output. Return ONLY the JSON object starting with {{."""

    messages = [{"role": "user", "content": user_msg}]

    raw = ""
    for attempt in range(8):
        response = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=8000,
            tools=[{"type": "web_search_20250305", "name": "web_search"}],
            system=SYSTEM_PROMPT,
            messages=messages
        )

        print(f"Attempt {attempt+1} | stop_reason: {response.stop_reason}")
        for block in response.content:
            print(f"  block.type: {block.type}")

        for block in response.content:
            if block.type == "text":
                raw += block.text

        if raw.strip():
            print("RAW:", repr(raw[:400]))
            break

        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason == "end_turn":
            messages.append({
                "role": "user",
                "content": "Now return ONLY the JSON object. Start with { and end with }. No other text."
            })

    if not raw.strip():
        raise ValueError("No response returned after research. Please try again.")

    json_str = extract_json(raw)
    return json.loads(json_str)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/qualify", methods=["POST"])
@limiter.limit("10 per hour")
def qualify():
    client_name = request.form.get("client", "").strip()
    market = request.form.get("market", "").strip()
    context = request.form.get("context", "").strip()

    if not client_name:
        return render_template("index.html", error="Add a client name to get started.")

    try:
        result = qualify_deal(client_name, market, context)
        return render_template("result.html", result=result)
    except Exception as e:
        print(f"Error: {e}")
        return render_template("index.html", error=f"Something went wrong: {str(e)}")


@app.errorhandler(429)
def rate_limit_exceeded(e):
    return render_template("index.html", error="Too many requests — try again in an hour."), 429


if __name__ == "__main__":
    app.run(debug=True)
