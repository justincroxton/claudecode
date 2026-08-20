# Propellant Media — RFP Finder & Qualifier

A two-command pipeline for [Propellant Media](https://propellant.media):

1. **`/find-rfps`** — finds open marketing/advertising RFP opportunities across six
   target verticals and delivers a CSV + Slack summary.
2. **`/qualify-rfps`** — reads RFP documents you drop in a Google Drive folder,
   scores each against Propellant's services, and writes a **bid brief** with a
   **BID / MAYBE / PASS** recommendation.

```
/find-rfps   →   you pick promising ones, drop the docs in Drive   →   /qualify-rfps   →   hand the briefs to a Claude Project to decide & draft
```

Six target verticals:

- Higher education
- Tourism
- Airports
- Government
- Public health
- Healthcare

## 1. Find — `/find-rfps`

In Claude Code (web, desktop, or CLI), just run:

```
/find-rfps
```

Claude then pulls opportunities from three places — a fresh live **web search**
across all six verticals (including bid portals like BidBanana, PlanetBids,
Bonfire, BidNet, DemandStar, and direct `.edu` university procurement pages),
plus your two paid email subscriptions, **RFPMart** (`alerts@rfpmart.com` /
`rfp-alerts@rfpmart.com`) and **RFP School Watch** (`bids@rfpschoolwatch-bids.com`)
scanned straight from your Gmail — filters for real **open**
marketing/advertising/media RFPs (dropping expired ones, news articles, and
off-topic bids), and delivers:

1. **A CSV spreadsheet** — `output/rfps_<date>.csv`, sorted by deadline, with the
   organization, due date, estimated value, source link, and a one-line scope.
   The file is sent to you so you can open it on web or mobile.
2. **A Slack summary** — sent as a **direct message to you (Justin Croxton)**,
   grouped by vertical with the top opportunities and links. Pass a channel name
   if you'd rather post it to a channel.

### Options

```
/find-rfps healthcare,tourism        # only search specific verticals
/find-rfps #propellantmediasales     # post to a channel instead of DMing you
/find-rfps --no-slack                # just produce the CSV, skip Slack
/find-rfps --no-email                # web search only, skip the inbox scan
/find-rfps --no-web                  # inbox sources only (RFPMart + RFP School Watch)
```

No API keys or setup required — Claude performs the searches and reads the alert
emails each time you run it.

The command itself lives in [`.claude/skills/find-rfps/SKILL.md`](.claude/skills/find-rfps/SKILL.md);
edit that file to tune the verticals, search queries, filtering rules, or output.

---

## 2. Qualify — `/qualify-rfps`

Drop any RFP document (PDF/Doc/Word) into your Google Drive folder
**"RFPs - To Review"**, then run:

```
/qualify-rfps           # qualify all new docs in the folder
/qualify-rfps --slack   # also DM you a BID/MAYBE/PASS summary
```

Claude reads each RFP, scores it against Propellant's services with a weighted
bid-fit rubric, and writes a **bid brief** (BID / MAYBE / PASS + score + rationale,
scope mapped to your services, requirements, flags) into your **"RFPs - Qualified"**
Drive folder, plus a running **"RFP Bid Scorecard"** sheet.

**The hand-off:** add the "RFPs - Qualified" Drive folder to a **Claude Project**
(e.g. "Bid Decisions") to go deeper on any BID/MAYBE and draft the proposal — the
briefs are already there as the Project's knowledge. *Code finds & qualifies; the
Project decides & writes.*

The command lives in [`.claude/skills/qualify-rfps/SKILL.md`](.claude/skills/qualify-rfps/SKILL.md).

---

## 3. Publish a case study — `pm-portfolio-engine`

Upload a case study PDF and ask Claude to post it to the portfolio. It extracts the
narrative, metrics, charts, tables, and quotes, anonymizes the client, and creates a
**draft** `portfolio-item` on propellant.media with the graphics uploaded to the media
library.

Drafts only — Justin reviews and publishes by hand. The skill lives in
[`.claude/skills/pm-portfolio-engine/SKILL.md`](.claude/skills/pm-portfolio-engine/SKILL.md)
and carries the verified WordPress structure, anonymization rules, and category map.

In Claude Code the skill triggers on its own, so all you need is:

```
Post this case study to the Propellant portfolio. Draft only, anonymize the client,
keep the real metrics.
```

For anywhere the skill isn't loaded — a Claude Project, a scheduled routine, a fresh
chat — [`PROMPT.md`](.claude/skills/pm-portfolio-engine/PROMPT.md) holds a portable,
paste-whole version of the same instructions.

---

## Optional: standalone automated backend (advanced)

This repo also contains a self-contained Python scraper (`main.py` + `sources/`)
that pulls RFPs from structured sources (SAM.gov, Bonfire, Google Programmable
Search, etc.) without Claude in the loop. It is **optional** and currently tuned
mainly for higher education. It requires free API keys.

```bash
pip install -r requirements.txt
cp .env.example .env   # then fill in keys
python main.py         # writes output/rfps.csv
```

Most users should just use the `/find-rfps` command above; the Python backend is
here if you later want a scheduled/headless run.
