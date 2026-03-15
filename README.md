# GTM Skills for Claude

A collection of Claude Skills built for enterprise B2B sales and GTM teams.

Each skill is a working tool, not a prompt template. They encode specific workflows for complex sales contexts — relationship-driven deals, multi-stakeholder buying committees, long cycles — the environments that most AI GTM content ignores.

Built and shared as part of [Narratives and Nodes](https://apurvap.substack.com) — a Substack about AI-era GTM in complex enterprise markets.

---

## Skills

### gtm-narrative-partner

A senior GTM and narrative co-creation partner for B2B sales and client services teams.

Works in two modes, detected automatically from context:

- **Proactive** — you have a market signal or category trend and want to shape it into an upstream client story
- **Reactive** — you have a specific client, meeting, or brief and need to build the right narrative for that room

Runs MEDDIC discovery conversationally, uses web search to fill research gaps, and produces story outlines, talk tracks, concept notes, and slide-by-slide structures. If you end up with a slide outline, you can ask Claude to generate it as a downloadable PowerPoint.

**Who it's for:** Sales reps, account managers, GTM leads, and client services teams preparing for senior client meetings, pitches, partnership reviews, or campaign proposals.

→ [View SKILL.md](./gtm-narrative-partner/SKILL.md)

---

## How to Use These Skills

### Claude Code (recommended)

Copy the skill folder into your personal skills directory:

```bash
cp -r gtm-narrative-partner ~/.claude/skills/
```

Claude Code will pick it up automatically. You can also invoke it directly with `/gtm-narrative-partner`.

### Claude.ai (Project instructions)

If you use claude.ai without Claude Code, each skill has a companion Project instructions file — same workflow, formatted for pasting into a Claude Project's custom instructions field.

→ [GTM Narrative Partner — Project instructions](./gtm-narrative-partner/project-instructions.txt)

To set it up: create a new Project in claude.ai, open Project instructions, and paste the contents of the file.

---

## What's Coming

Skills I'm building and documenting on the Substack:

| Skill | Description | Status |
|---|---|---|
| `gtm-narrative-partner` | Upstream and client-specific narrative development | ✅ Available |
| `meddic-builder` | Conversational deal qualification with research | Coming soon |
| `opportunity-signal-surface` | Proactive account engagement signals | Planned |
| `pitch-localiser` | Adapt master narratives for APAC markets | Planned |

---

## Context

Most AI GTM tools are built for self-serve SaaS — short cycles, digital-first buyers, direct API access. These skills are built for the other kind: enterprise deals where the rep is in the room, the buying committee has six people, and the agency sits between you and the brand.

That's the environment these workflows are stress-tested against. If that's your context too, they should be useful out of the box. If it's not, they're still worth reading for the underlying approach.

---

## Follow Along

I document what I build, what works, and what doesn't on [Narratives and Nodes](https://apurvap.substack.com).

If you use one of these skills and have feedback — what worked, what didn't, what you changed — I'd genuinely like to hear it.
