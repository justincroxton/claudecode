---
name: daily-rfps
description: Daily RFP operations run for Propellant Media. Scans Justin's RFPMart + RFP School Watch email alerts for new marketing/advertising opportunities, DMs a digest to Justin AND Erin on Slack, stages an opportunity brief for each into the Google Drive "RFPs - To Review" folder (the Claude Project scores them there), and lists the gated ones with where-to-find pointers. Use when the user runs /daily-rfps or asks for the daily RFP update. Intended to be run on a daily schedule.
---

# Daily RFP Run — Propellant Media

The daily operator. It does NOT score bids — scoring happens in Justin & Erin's
Claude Project. This run's job is to **find new opportunities, notify both of
them, and stage material in Drive** so the Project can score it.

Designed to run unattended on a daily schedule, so be efficient and idempotent
(never re-post or re-stage an opportunity already handled on a previous day).

## People & places (hard-coded)

- **Slack — Justin Croxton**: `U57HCS3K8`
- **Slack — Erin Brantley**: `U0AL4CU2PL5`
- **Drive — "RFPs - To Review"** (Project's source folder): `17aK5UpXFGnWUW5rF6bXgRQXKwAuXRou7`

## Arguments (optional)

`/daily-rfps [--web]`
- Default: **email sources only** (RFPMart + RFP School Watch) — fast, for daily use.
- `--web`: also run the `/find-rfps` web sweep (better for a weekly deeper run).

## Step 1 — Scan today's alerts

Follow the **email-source procedure in `/find-rfps`** (`.claude/skills/find-rfps/SKILL.md`):
scan `from:rfpmart.com` and `from:rfpschoolwatch-bids.com` for `newer_than:2d`,
read the digests, and extract opportunities. Apply the same **filtering rules and
exclusions** from `/find-rfps` (six verticals; marketing/advertising/media scope;
open deadline ≥ today; drop event-specific and airport ad-concession RFPs;
de-dupe across emails).

## Step 2 — Keep only what's NEW since yesterday

Read the most recent daily digest doc already in the Drive folder (titles start
with `RFP Opportunities — `) and drop any opportunity whose RFP#/title already
appears there. Only brand-new opportunities go forward. If nothing is new, still
send a short "no new RFPs today" Slack note and skip the Drive write.

## Step 3 — Stage in Drive for the Project to score

Write ONE daily digest Google Doc into the "RFPs - To Review" folder
(`create_file`, `parentId = '17aK5UpXFGnWUW5rF6bXgRQXKwAuXRou7'`,
`contentMimeType: text/plain`), titled `RFP Opportunities — <YYYY-MM-DD>`. One
clearly delimited section per opportunity, pre-structured to Justin's scoring
template so the Project only has to judge it:

```
=== <Organization or best descriptor> — <Title> ===
Vertical:            Location:
Deadline:            Posted:            Est. value:
Source:  <RFPMart MRB-##### / RFP School Watch ref / link>
Document status:  <Accessible link | NEEDS MANUAL DOWNLOAD — get it at: ...>
Scope (from the alert):  <1–3 lines>
--- TEMPLATE (for the Project to fill) ---
<Justin's qualifying questions go here once provided; until then leave the
scope above for the Project to score against.>
```

(When Justin provides his template of questions + agency context, embed it under
the TEMPLATE divider so each opportunity arrives pre-formatted for scoring. Store
the template at the top of this file or in `.claude/skills/daily-rfps/template.md`.)

Keep it to one doc per day. Do not create 100 separate files.

## Step 4 — Slack DM the digest to BOTH Justin and Erin

Send the SAME message to `U57HCS3K8` and to `U0AL4CU2PL5` (two `slack_send_message`
calls). Begin each with both mentions so it notifies them:
`<@U57HCS3K8> <@U0AL4CU2PL5>`. Format (hyperlink every title per the `/find-rfps`
clickable-link rule — real URL if available, else a one-click lookup link):

```
<@U57HCS3K8> <@U0AL4CU2PL5> :sunrise: *Daily RFP update — <Mon DD>* — <N> new opportunities

*<Vertical> (<n>)*
• [<Title>](<link>) — <Org> — due <date> — <est value>
... (group by vertical; the six verticals; omit empty)

:page_facing_up: *Needs manual download* (<k>) — grab the doc + drop it in "RFPs - To Review":
• <Title> — <Org> — get it: <where-to-find link>

_Briefs staged in your *RFPs - To Review* Drive folder for scoring in the Bid Decisions project._
```

If `--web` was used, note the extra web finds in the digest.

## Step 5 — Where-to-find for gated docs

For any opportunity whose document is behind RFPMart/agency login (most RFPMart
items), don't fail — give a precise pointer in the "Needs manual download"
section: the RFPMart RFP# to search, or a `https://www.google.com/search?q=...`
lookup of the title + organization, so Justin or Erin can fetch it and drop the
real file into the Drive folder.

## Wrap-up

End with a short chat summary: # new opportunities, # staged to Drive, # needing
manual download, and confirmation both Slack DMs sent. Note that scoring happens
in the **Bid Decisions** Claude Project, which reads the "RFPs - To Review" folder.
