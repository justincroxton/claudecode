---
name: qualify-rfps
description: Read RFP documents Justin dropped in his Google Drive "RFPs - To Review" folder, qualify each against Propellant Media's services, and produce a bid brief + bid/no-bid recommendation. Use when the user runs /qualify-rfps or asks to qualify, score, review, or assess RFP documents in their Drive review folder. Writes a brief to Drive and can DM a summary to Slack.
---

# Qualify RFPs for Propellant Media (bid / no-bid)

This is the partner to `/find-rfps`. Where that one *finds* opportunities, this
one *qualifies* the documents Justin has decided to look at: it reads each RFP,
scores it against Propellant Media's capabilities, and writes a clean **bid
brief** so he can decide whether to pursue it (and hand the brief to a Claude
Project for the deeper go/no-go and proposal drafting).

Justin is non-technical. Do the work end to end; only ask if genuinely blocked.

## Where things live (Google Drive)

- **Inbox folder — "RFPs - To Review"**: `17aK5UpXFGnWUW5rF6bXgRQXKwAuXRou7`
  (Justin drops RFP PDFs/Docs/zips here.)
- **Output folder — "RFPs - Qualified"**: `1cQddItRtI53LwkuBEF8tAk0bOOIrbwcE`
  (Write each finished brief here.)

## Arguments (all optional)

`/qualify-rfps [filename or "all"] [--slack]`

- **filename** — qualify only a matching file. Default: qualify **all new** files
  in the inbox folder (those without an existing brief in the Qualified folder).
- `--slack` — also DM a short bid/no-bid summary to Justin (`U57HCS3K8`).
- `--all` — re-qualify everything, even files already done.

## Propellant Media profile (score against this)

Propellant Media — digital marketing/advertising agency. Core services:
**programmatic display & video, OTT/CTV, geofencing/location-based, paid search
(SEM), paid social, SEO, retargeting, media planning & buying, creative, web
design/dev, analytics/attribution.** Strong in mid-market and public-sector work.
Target verticals: **higher education, tourism, airports, government, public
health, healthcare.**

Treat as **strong fit**: media buying/planning, digital advertising, programmatic/
OTT/geofencing, paid search/social, SEO, integrated marketing campaigns, agency
of record, awareness/enrollment/destination campaigns in the six verticals.
Treat as **weak/▼**: pure print/graphic-design-only, standalone website builds
with no marketing, PR-only with no paid media, pure strategy/research with no
execution, or work requiring capabilities Propellant doesn't offer (e.g. TV
production studios, call centers).
(If Justin corrects the profile, update this section.)

## Procedure

1. **List the inbox.** Use Drive `search_files` with `parentId = '17aK5UpXFGnWUW5rF6bXgRQXKwAuXRou7'`.
   Skip the "START HERE" doc and any folders.
2. **Skip already-qualified files** unless `--all`: a file is done if the
   Qualified folder already has a brief whose title contains the source
   filename (search `parentId = '1cQddItRtI53LwkuBEF8tAk0bOOIrbwcE'`).
3. **Read each RFP.** Use `read_file_content` for the natural-language text
   (works for Google Docs/PDF/Word). For zips or files that don't read cleanly,
   note what couldn't be parsed rather than guessing. Never invent RFP details —
   only state what's in the document.
4. **Extract the facts** for each RFP (mark anything not found as "not stated"):
   issuing organization (real buyer), title, location, submission deadline,
   pre-bid/Q&A dates, contract term, estimated budget/value, scope of work,
   mandatory requirements (registration, certifications, insurance/bonding,
   set-asides such as minority/woman/veteran-owned, mandatory pre-bid meetings,
   local presence), submission format, and incumbent agency if named.
5. **Score it** with the rubric below into an overall **Bid-Fit score (0–100)**
   and a recommendation: **BID / MAYBE / PASS**.

### Bid-fit rubric (weight)
- **Service fit (30)** — does the scope map to Propellant's services?
- **Vertical fit (15)** — one of the six target verticals?
- **Budget viability (15)** — is there real budget, sized to be worth pursuing
  and winnable (neither trivial nor enterprise-only)?
- **Timeline (10)** — enough runway before the deadline to produce a strong response?
- **Competitive position (15)** — incumbent advantage? open field? AOR up for grabs?
- **Barriers to entry (15)** — heavy bonding, in-state-only, certifications, or
  set-asides Propellant can't meet → lower. Few barriers → higher.

Map score → reco: **70+ = BID**, **45–69 = MAYBE**, **<45 = PASS**. Always give
the top 2–3 reasons driving the call, and any disqualifier to verify.

## Output 1 — a bid brief per RFP (Google Doc in the Qualified folder)

Use Drive `create_file` with `parentId = '1cQddItRtI53LwkuBEF8tAk0bOOIrbwcE'`,
`contentMimeType: text/plain` (it converts to a Google Doc), title:
`RFP Brief — <Organization> — due <YYYY-MM-DD> — <BID|MAYBE|PASS> [src: <filename>]`.
Body (keep it tight and Project-ready):

```
RFP BID BRIEF — <Organization>
Recommendation: <BID | MAYBE | PASS>   Bid-Fit Score: <NN>/100
Why: <2–3 sentence rationale>

THE OPPORTUNITY
- Title / Solicitation #:
- Issuing organization & location:
- Vertical:
- Submission deadline:        Pre-bid / Q&A dates:
- Contract term:              Estimated value:

SCOPE OF WORK
- <bullet the work; map each to a Propellant service>

PROPELLANT FIT
- Services we'd lead with:
- Strengths for this bid:
- Gaps / things we'd need a partner or subcontractor for:

REQUIREMENTS & FLAGS
- Mandatory: <registration, certs, insurance/bonding, set-asides, pre-bid mtg, local presence>
- Submission format:
- Incumbent (if named):
- Disqualifiers to verify:

SCORE BREAKDOWN
- Service fit, Vertical, Budget, Timeline, Competition, Barriers (1 line each)
```

Including the source filename in the title is what lets the next run skip files
already done.

## Output 2 — running scorecard

Maintain a single Google Sheet titled **"RFP Bid Scorecard"** in the Qualified
folder (create it if missing; otherwise append). One row per RFP:
`date_qualified, organization, title, vertical, deadline, est_value, bid_fit_score, recommendation, source_file, brief_link`.
Sort/keep newest on top isn't required — just append.

## Output 3 — Slack (only with --slack)

DM `U57HCS3K8`, beginning with `<@U57HCS3K8>`. One scannable block:
```
<@U57HCS3K8> :clipboard: *RFP qualification — <N> reviewed*
:large_green_circle: BID — [<Org> — <Title>](<brief_link>) — <score>/100 — due <date>
:large_yellow_circle: MAYBE — [<Org> — <Title>](<brief_link>) — <score>/100 — due <date>
:red_circle: PASS — <Org> — <Title> — <score>/100 (<one-line reason>)
```
Hyperlink each BID/MAYBE to its brief in Drive so Justin can tap straight in.

## Wrap-up & hand-off

End with a short chat summary: how many qualified, the BID/MAYBE/PASS counts, and
links to the briefs. Then remind Justin of the hand-off:

> The finished briefs live in your **"RFPs - Qualified"** Drive folder. Add that
> folder to a **Claude Project** (e.g. "Bid Decisions") and you can chat to go
> deeper on any BID/MAYBE — pressure-test the go/no-go, then draft the proposal —
> with every brief already in the Project's knowledge.

This keeps the division clean: **Code finds & qualifies; the Project decides & writes.**
