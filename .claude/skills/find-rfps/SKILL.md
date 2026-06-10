---
name: find-rfps
description: Search the web for open marketing/advertising RFP opportunities for Propellant Media across six verticals (higher education, tourism, airports, government, public health, healthcare). Use when the user runs /find-rfps or asks to find RFPs, bids, or proposal opportunities. Compiles results into a CSV and posts a summary to Slack.
---

# Find Marketing RFPs for Propellant Media

This is the "one button" RFP finder for **Propellant Media** (https://propellant.media),
a digital marketing agency. When invoked, run a fresh live web search for **open**
Request-for-Proposal / Request-for-Qualifications / bid opportunities where an
organization is hiring a **marketing, advertising, media, creative, branding,
PR, or digital agency**, across six target verticals.

The user is non-technical and just wants to "hit a button." Do the work end to
end without asking unnecessary questions. Only ask if genuinely blocked.

## Arguments (all optional)

`/find-rfps [verticals] [#channel]`

- **verticals** — comma-separated subset to limit the search, e.g. `healthcare,tourism`.
  If omitted, search **all six**.
- **#channel** — Slack channel/DM to post to. Default: **direct message to Justin
  Croxton** (`U57HCS3K8`). Accepts a channel like `#propellantmediasales`
  (`C56P28H4J`) if the user wants it posted to a channel instead.
- `--no-slack` — skip the Slack post (still writes the CSV).
- `--no-email` — skip the Gmail inbox scan (web search only).
- `--no-web` — skip the web search (inbox sources only).

## The six verticals + what counts as a hit

For every vertical the opportunity must be about hiring outside **marketing /
advertising / media buying / digital / creative / branding / communications /
public relations / SEO / web / social** services. Ignore RFPs for unrelated
goods/services (construction, IT hardware, legal, etc.).

**Always exclude (even if marketing-adjacent):**
- **Event-specific RFPs** — event production, coordination, management, or
  promotion of a single named event (e.g., "fly-buy event," festival/expo
  production, one-off event services). Ongoing destination/brand marketing is
  fine even if it references an event calendar.
- **Airport advertising-concession / ad-space-lease RFPs** — these hire a
  concessionaire to sell/operate ad space, not a marketing agency. (Keep true
  airport *marketing / advertising / air-service-development* RFPs.)

| Vertical | Typical issuers | Vertical-specific signals |
|----------|-----------------|---------------------------|
| **Higher education** | universities, colleges, community colleges, university systems, foundations | enrollment marketing, student recruitment, brand campaign, lead generation |
| **Tourism** | DMOs, CVBs, tourism boards, state/city tourism offices, chambers, "Visit ___" orgs | destination marketing, tourism advertising, brand/awareness campaign, media buying |
| **Airports** | airport authorities, regional airports, port authorities, aviation departments | air service development marketing, passenger/destination advertising, brand campaign |
| **Government** | cities, counties, states, agencies, transit/utility authorities, economic development | public information/awareness campaign, marketing & communications, advertising services |
| **Public health** | state/county health departments, public health districts, coalitions | health awareness/education campaign, anti-vaping/vaccine/mental-health media buy |
| **Healthcare** | hospitals, health systems, clinics, payers, senior living, behavioral health | service-line marketing, patient acquisition, brand campaign, digital advertising |

## Search procedure

Use the `WebSearch` tool. For **each vertical in scope**, run several focused
queries. Vary the wording; aim for recent (current/next quarter) **open** notices.
Use the current date to bias toward fresh postings and future deadlines.

Effective query patterns (substitute the vertical and rotate phrasing):

- `"request for proposal" marketing agency <vertical> 2026`
- `"RFP" "digital marketing" OR "advertising services" <issuer type> deadline 2026`
- `<vertical> "marketing and communications" RFP "due" 2026`
- `"request for qualifications" advertising agency <vertical>`
- `media buying RFP <vertical> "proposals due"`

Also sweep the common bid aggregators / portals (search within them):

- `site:bidnetdirect.com marketing advertising RFP`
- `site:rfpdb.com marketing OR advertising`
- `site:governmentbids.com marketing agency`
- `site:findrfp.com advertising marketing`
- `site:demandstar.com marketing`
- `site:thebidbanana.com marketing OR advertising OR "media buying"` (BidBanana)
- `site:planetbids.com marketing OR advertising OR branding RFP` (PlanetBids — many city/county/college portals)
- `site:bonfirehub.com marketing OR advertising OR "media buying" RFP` (Bonfire)
- `bidnet / BidNet Direct, DemandStar, Periscope S2G / BidSync, OpenGov procurement`
- State procurement portals (e.g. eVA Virginia, Cal eProcure, Texas SmartBuy, Florida MyFloridaMarketPlace) when a query points to one.

Higher-education sweep — also run explicit `.edu` queries so we catch RFPs hosted
directly on university procurement pages, e.g.:
- `site:edu "request for proposal" marketing OR advertising OR "enrollment marketing" 2026`
- `site:edu RFP "media buying" OR "creative services" OR "agency of record" 2026`

Note on BidBanana / PlanetBids / Bonfire: search their public/indexed listing
pages only. Do NOT attempt to log in or use any stored credentials. If a
listing requires authentication to view detail, capture what is public and note
"login required" in the summary.

Run **3–5 queries per vertical**. When a promising result lacks a deadline or
issuer, use `WebFetch` on the listing to confirm it is a real, open marketing RFP
and to pull the due date, issuing organization, and a one-line scope.

## Email sources (Gmail inbox scan)

Unless `--no-email`, also scan Justin's Gmail for two paid RFP-alert
subscriptions he receives. These are high-signal — RFPMart even has a dedicated
marketing category — so treat them as first-class sources alongside web search.
Use `search_threads` to find recent alerts, then `get_thread` with
`messageFormat: FULL_CONTENT` to read the listings out of each email body.

**RFPMart** — search `from:rfpmart.com newer_than:30d`. Two senders:
- `alerts@rfpmart.com` — category digest emails. **Prioritize** subjects
  containing *Marketing, Branding, Social Media, Digital Marketing, Public
  Relations* (the `MRB-` series) and *Social Media, Internet and Digital
  Marketing, SEO, SEM* (the `SEO-` series). **Skip** off-topic categories
  (Auditing/Finance, etc.). Each email body lists multiple RFPs with title,
  issuing org/state, and a link.
- `rfp-alerts@rfpmart.com` — "Daily RFP Notification" digests with a link to each
  matched RFP at the bottom of the body.

**RFP School Watch** — search `from:rfpschoolwatch-bids.com newer_than:30d`
(sender `bids@rfpschoolwatch-bids.com`, subject "RFPSchoolwatch Daily Bid Alert").
Bid data is in the email body; the full detail (including due dates) is in an
attached PDF. Read the body first; if a due date or scope is missing, read the
PDF attachment via `get_thread` FULL_CONTENT. (Ignore marketing/newsletter mail
from `content@rfpschoolwatch.com` — those are not bid alerts.)

For every RFP pulled from these emails: classify it into one of the six verticals
(drop anything that fits none), apply the same marketing-scope and open-deadline
filters below, capture the source link from the email, and set the CSV `source`
column to `RFPMart` or `RFPSchoolWatch`. Scan the last ~30 days of alerts and
de-duplicate across emails and against the web results.

## Filtering rules

Keep a result only if **all** hold:
1. It is an actual procurement notice (RFP/RFQ/RFI/ITB/bid), not a news article,
   blog, or vendor sales page. (A reputable aggregator listing is fine.)
2. The scope is marketing/advertising/media/creative/branding/PR/digital.
3. The submission deadline is **today or later** (drop expired ones). If the
   deadline is unknown after a fetch, keep it but mark `due_date` as `unknown`.
4. De-duplicate by organization + title (and by URL). Prefer the primary source
   over an aggregator mirror.

Be honest: if a vertical yields nothing credible this run, report zero for it
rather than padding with weak matches.

## Output 1 — CSV

Write/overwrite `output/rfps_<YYYY-MM-DD>.csv` (create `output/` if needed) with
this exact header and one row per kept opportunity, sorted by `due_date` ascending
(unknown dates last):

```
vertical,title,organization,location,due_date,estimated_value,source,source_url,posted_date,summary
```

- `due_date` / `posted_date`: ISO `YYYY-MM-DD` when known, else `unknown`.
- `estimated_value`: contract value/budget if stated, else blank.
- `source`: where it came from — `RFPMart`, `RFPSchoolWatch`, or `Web`.
- `summary`: one sentence on the scope of work.
- Quote/escape fields properly (use Python's `csv` module via a quick Bash
  `python3` script, not hand-rolled string joining, so commas/quotes are safe).

After writing, surface the file to the user with `SendUserFile` so they can open
it on web/mobile.

## Output 2 — Slack summary

Unless `--no-slack`, post one message to the target destination (default is a
**direct message to Justin Croxton** / `U57HCS3K8`) using `slack_send_message`.
Send DMs by passing the user ID `U57HCS3K8` as the channel. **Always begin the
message with the Slack mention token `<@U57HCS3K8>`** (literal angle brackets,
not markdown) so it pushes a real notification to Justin. Format:

```
<@U57HCS3K8> :mag: *RFP scan — <Mon DD, YYYY>* — <N> open marketing opportunities

*Higher education (<n>)*
• <Title (hyperlinked)> — <Organization> — due <date>
*Tourism (<n>)*
• ...
(repeat for each vertical that has hits; omit verticals with 0)

_Generated by /find-rfps. Full spreadsheet attached in Claude Code._
```

**Make every item clickable** — never leave a bare RFP number as dead text.
Hyperlink the **title** (Slack standard markdown `[Title](url)`) using this priority:
1. A real document/listing URL if the source provides one (e.g. a
   `files.rfpmart.com/...` doc link, a portal listing URL, or a `.edu` page).
2. Otherwise build a one-click lookup link so the number still resolves:
   `https://www.google.com/search?q=RFPMart+<RFP#>+<state>` (URL-encode spaces
   as `+`). For RFP School Watch refs, link a search of the title + organization.
This way Justin can click straight from Slack to the listing.

Keep it scannable: list up to ~5 per vertical in Slack (the CSV has the full set);
if a vertical has more, add `…and <x> more in the CSV`. Confirm the destination
before posting only if the user passed a channel that doesn't resolve.

## Wrap-up

End your turn with a short chat summary: total count, per-vertical breakdown, the
CSV path, and confirmation the Slack message posted. Note any verticals that came
back empty and suggest re-running later (postings refresh constantly).
