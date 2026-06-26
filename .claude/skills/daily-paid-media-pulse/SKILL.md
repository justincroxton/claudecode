---
name: daily-paid-media-pulse
description: Daily Paid Media Pulse for Propellant Media. Pulls every connected Google Ads account from Windsor.ai, compares the last 14 days vs. the prior 14 days on conversions/CPL/spend, and DMs a short, scannable big-picture read (not a full audit) to Justin Croxton on Slack. Use when the user runs /daily-paid-media-pulse or asks for the daily paid media pulse. Intended to run unattended on a daily schedule at 8:00 AM ET.
---

# Daily Paid Media Pulse — Propellant Media

Store this as a daily routine set to run at 8:00 AM ET. Everything under
**PROMPT** is what gets run each morning. No client list to maintain — it pulls
every Google Ads account connected in Windsor.ai automatically.

This is the SHORT big-picture version of the paid-media-analyzer methodology —
NOT a full audit. Do not produce the long report format.

## Hard-coded facts (verified)

- **Data source:** Windsor.ai MCP, connector `google_ads`. 12 Google Ads
  accounts are connected as of this writing; the routine enumerates them live
  each run rather than relying on a fixed list.
- **Slack recipient:** Justin Croxton — email `justin@propellant.media`,
  Slack user ID `U57HCS3K8`. NOTE: the bare handle "justincroxton" does NOT
  resolve in Slack search. Always resolve the user by full name or email first,
  then DM their user ID. (This DM lands in Justin's own DM space.)
- **Windsor field IDs (confirmed valid):** `account_name`, `account_id`,
  `date`, `spend`, `conversions`, `cost_per_conversion`, `clicks`.
- **CPL:** compute as total window spend ÷ total window conversions. Do NOT
  average the daily `cost_per_conversion` field — it skews on low-volume days.
- **Florida Gulf Coast University (watched account):** always give FGCU a full
  account block, even when it falls under the ~30-conversion low-data
  threshold. Do NOT relegate it to the low-data footnote. FGCU runs thin volume
  with frequent zero-conversion days, so when data is sparse, frame it as a
  likely conversion-tracking issue to verify — not a performance read.

---

## PROMPT

You are running my Daily Paid Media Pulse. Use the paid-media-analyzer
methodology, but this is the SHORT big-picture version — not a full audit. Do
not produce the long report format.

**Step 1 — Data source (required):** Pull all numbers from the connected
Windsor.ai data (connector `google_ads`). Include EVERY Google Ads account
connected in Windsor.ai — do not limit to a subset, and do not ask me which
accounts. Enumerate all available Google Ads accounts first (get_connectors),
then run the pulse across all of them. Do not estimate, guess, or use any other
source. If Windsor.ai can't be reached, or a specific account returns no data,
say so plainly in the Slack rather than filling gaps.

Scope: All Google Ads accounts in Windsor.ai. (Meta is out of scope for this
routine.)

Comparison window: Last 14 days vs. the prior 14 days (the 14 days before
that). Confirm today's date first so the windows are correct. Pull each window
pre-aggregated per account (request `account_name`, `spend`, `conversions`
without the `date` field, with `date_from`/`date_to` set per window) — that
returns one total row per account and avoids summing daily rows by hand. Do all
numeric work in code, never by eye.

Lead metrics, in this order of importance:

1. **Conversions / Leads** — volume trend, this is the headline
2. **CPL** — cost per lead, always weighted against volume, never in isolation.
   Calculate CPL as total window spend ÷ total window conversions, not an
   average of daily CPL.
3. **Spend** — pacing, is the change driven by budget or by efficiency?

Guardrails (keep this honest):

- If conversion tracking looks broken, or a campaign went from conversions to
  zero, flag it FIRST. Assume tracking broke before assuming performance
  tanked.
- Never call a CPL move good or bad without the volume behind it. A lower CPL
  on collapsing volume is not a win.
- If an account has too little data to read (under ~30 conversions in the
  window), say so instead of over-reading noise. EXCEPTION: Florida Gulf Coast
  University is a watched account — always give it a full block regardless of
  volume, and when its data is thin or shows zero-conversion days, flag it as a
  likely conversion-tracking issue to verify rather than calling performance.

**Step 2 — Deliver to Slack (required):** Post the finished pulse as a Slack
direct message to Justin Croxton (email `justin@propellant.media`). First look
up the user to get their Slack user ID (`U57HCS3K8`), then send the DM to that
ID — the bare handle "justincroxton" does not resolve, so do not pass it as the
target. If the lookup or send fails, say so in chat rather than dropping the
message. The Slack DM is the deliverable — don't just leave it in chat.
Scannable, no emojis, Propellant voice (direct, no fluff). Structure:

**Top line (3-5 sentences):** Across all accounts, what moved most this period —
biggest movers up and down, total spend direction, and the 2-3 accounts I should
actually pay attention to today. With a full book of accounts, lead me to the
ones that matter; don't make me read every block to find the fires.

**Then one block per account:**

- Account name
- Conversions: prior 14d → last 14d (with % change, up/down)
- CPL: prior 14d → last 14d (with % change, up/down)
- Spend: prior 14d → last 14d (with % change)
- One-line read: what the numbers are telling me
- 3 recommendations to look into — specific, not generic, each one handable to
  the ad ops team. Examples: "Check zero-conversion spend on [campaign],"
  "Brand vs. non-brand may be masking weak non-brand — split it apart,"
  "Quality Score looks low on [ad group] — review."

To keep this readable with a full account list, order the blocks by attention
needed: accounts with the biggest negative swings or flagged issues first,
steady/healthy accounts last (those can be a one-line "stable" note rather than
a full block).

Close with a one-line priority: the single account or action worth my time
first this morning.

Keep the whole thing skimmable. These are flags for me to investigate, not
final calls — make that clear. Do not apply any changes to accounts.
