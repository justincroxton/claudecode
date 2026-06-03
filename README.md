# Propellant Media — RFP Finder

A "one button" tool that searches the web for **open marketing/advertising RFP
opportunities** for [Propellant Media](https://propellant.media) across six
target verticals:

- Higher education
- Tourism
- Airports
- Government
- Public health
- Healthcare

## How to use it (the button)

In Claude Code (web, desktop, or CLI), just run:

```
/find-rfps
```

Claude then does a fresh live web search across all six verticals, filters for
real **open** marketing/advertising/media RFPs (dropping expired ones, news
articles, and off-topic bids), and delivers:

1. **A CSV spreadsheet** — `output/rfps_<date>.csv`, sorted by deadline, with the
   organization, due date, estimated value, source link, and a one-line scope.
   The file is sent to you so you can open it on web or mobile.
2. **A Slack summary** — posted to **#propellantmediasales**, grouped by vertical
   with the top opportunities and links.

### Options

```
/find-rfps healthcare,tourism        # only search specific verticals
/find-rfps #my-channel               # post the summary to a different channel
/find-rfps --no-slack                # just produce the CSV, skip Slack
```

No API keys or setup required — Claude performs the searches each time you run it.

The command itself lives in [`.claude/skills/find-rfps/SKILL.md`](.claude/skills/find-rfps/SKILL.md);
edit that file to tune the verticals, search queries, filtering rules, or output.

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
