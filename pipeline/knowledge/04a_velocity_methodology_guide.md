RFP Pipeline Velocity — Methodology Guide  |  Propellant Media

**RFP Pipeline Velocity — Methodology ****&**** Reporting Guide**

How Propellant Media measures RFP submission-to-pitch-to-award velocity

Owner: Justin Croxton  ·  For: Erin Brantley, Diana Woodruff  ·  Version 1.0

# **1. Purpose**

This document is the standard method for measuring the health and velocity of Propellant Media's RFP pipeline. It exists so that anyone on the team — not just Justin — can rerun this analysis each month against fresh numbers and get a defensible, apples-to-apples read.

Use it when you want to answer questions like: *Are we converting more submissions into pitch rounds? Is our win rate improving? Is a new hire or process change actually moving the funnel?*

The worked example throughout is Erin's first quarter (Mar 15 – Jun 2026). Treat that as the reference implementation: when you rerun this, your output should look like Section 6.

# **2. The Two Concepts That Make This Honest**

Most pipeline reporting lies by accident. It divides wins by every bid ever sent, including bids that haven't been answered yet, and produces a rate that looks worse than reality. Two concepts prevent that.

## **2.1 The Status Taxonomy**

Every bid on the tracker is one of four states, coded by cell color. This is the single source of truth — do not invent new categories.

| **Color** | **Status** | **What it means** |
| --- | --- | --- |
| Red | Immediate No | Submitted a proposal and received a no — never reached a pitch. |
| Purple | Pitch Round | Advanced to the pitch / interview / finalist round. |
| Yellow | Win (Awarded) | Won the contract. |
| Green | Outstanding | Submitted, but the procurement team has not responded yet. |

## **2.2 Decided vs. Pending — the key split**

A green bid has no verdict yet. Counting it against your win or pitch rate is like scoring a batting average mid-swing — the ball is still in the air. So we split every cohort into two groups:

- **Decided bids** — reds (immediate no) + purples (reached pitch) + yellows (won). These got an answer.

- **Pending bids** — greens (still outstanding). No verdict. Excluded from decided-bid rates.

**Rule: **Report rates two ways — against total submissions (the conservative floor) and against decided bids only (the true skill signal). The decided-bid rate is the number that predicts forward performance, because the pending greens will keep converting after the report is written.

# **3. Every Metric and Its Formula**

Compute each of these. When you rerun the analysis, fill the same rows so month-over-month comparisons stay clean.

| **Metric** | **Formula** |
| --- | --- |
| Submissions | Count of all bids submitted in the window |
| Submissions / month | Submissions ÷ months in window |
| Pitch Rounds Reached | Count of purple (+ yellow, since wins passed pitch) |
| Pitch Rounds / month | Pitch rounds ÷ months in window |
| Pitch rate (of total submissions) | Pitch rounds ÷ total submissions |
| Pitch rate (of decided bids) | Pitch rounds ÷ decided bids |
| Immediate-no rate (of decided) | Reds ÷ decided bids |
| RFP Win (Awarded) | Count of yellow |
| Pitch Round / Award Rate | Wins ÷ pitch rounds reached |
| Win / Award Rate (of total submissions) | Wins ÷ total submissions |

**Note on the two pitch rates: **the 'of total submissions' version is dragged down by unanswered greens and understates performance. The 'of decided bids' version is the truer read. Always show both.

# **4. Forecasting Live Finalists — Expected Value (EV)**

When bids are still live at the pitch stage, don't guess a whole number of wins. Use Expected Value: the probability-weighted forecast.

### **The method**

- Assign each live finalist a realistic close probability (Justin owns this call).

- Multiply the number of live bids by their probability to get expected wins.

- Report EV as the planning number, and the all-win scenario as best case.

### **Worked example**

3 live finalists × 80% close odds = **2.4 expected wins**.

- **Plan on ~2. Celebrate 3. **You will never literally win 2.4 — that is the average, not the outcome.

- **Discipline: **forecast Q3 revenue on EV, not on best case. If you plan on 3 and land 2, you have manufactured a miss that didn't need to exist.

**One honest caveat to always state: **EV rides on the close-probability gut call. If the 80% is optimistic, the EV drops. Treat it as optimistic-case unless the odds are independently validated.

# **5. How to Rerun This Analysis**

Follow these steps against the current bid sheet (the 'All Bids' tab). This is the self-serve procedure for Erin or Diana.

- Set the window. Pick a start and end date. For a person's impact, anchor on their start date (Erin = March 15, 2026) and compare the window before vs. after.

- Anchor on Submission Due Date. That is the date field that marks when the bid shipped. Do not use issue date or award date.

- Classify every row by color into the four statuses from Section 2.1. Exclude future-dated rows that haven't actually been submitted yet.

- Split into decided vs. pending (Section 2.2).

- Compute every metric in Section 3, for both the current window and the comparison window.

- For any live finalists, run the EV forecast (Section 4).

- Report both pitch rates. Lead with the numbers that are already banked (submissions/month, pitch rounds/month) and clearly label anything that is a forecast.

**Contamination check: **before sharing, confirm the denominator. If someone says '29 submissions' but the sheet shows 38 rows, the gap is almost always future-dated bids not yet submitted. Reconcile before reporting a rate — a wrong denominator changes every percentage.

# **6. Worked Example — Erin****'****s First Quarter**

**Window: **Mar 15 – Jun 2026 (3 months), Erin's first quarter, vs. Pre-Erin Nov '24 – Mar 13 '26 (~15.8 months). Denominator: 29 submitted bids.

### **The funnel, pre vs. post**

| **Metric** | **Pre-Erin** | **Post-Erin** |
| --- | --- | --- |
| Submissions | 124 | 29 |
| Submissions / month | 7.9 | 9.7 |
| Decided bids | — | 15 |
| Still outstanding | — | 14 |
| Pitch Rounds Reached | 20 | 6 |
| Pitch Rounds / month | 1.3 | 2.0 |
| Pitch rate (of total submissions) | 16% | 21% |
| Pitch rate (of decided bids) | 18% | 40% |
| Immediate-no rate (of decided) | — | 60% |
| RFP Win (Awarded) | 5 | 0 today → EV 2.4 / best 3 |
| Pitch Round / Award Rate | 25% | 0% → ~40% EV / 50% best |
| Win / Award Rate (of total subs) | 4.0% | 0% → ~8% EV / 10% best |

### **What the example shows**

- **Volume went up, not down. **9.7 submissions/month vs. 7.9 pre-Erin. She raised throughput and quality at once.

- **Pitch rounds/month nearly doubled: 1.3 → 2.0. **This is already banked, not a forecast — the cleanest number to lead with.

- **Pitch rate of decided bids more than doubled: 18% → 40%. **When Erin's bids get answered, they reach the pitch round far more often.

- **The real problem is upstream. **9 of 15 decided bids (60%) were immediate nos — on names we consider strong builds (Carlow, CU Boulder, Parkland). Losing before the pitch is an earlier, bigger leak than losing at the pitch. That is the priority fix.

**The defensible one-liner today: ***"**Erin lifted submissions to 9.7/month and pitch rounds to 2.0/month in her first quarter, with three finalists live. Win rate gets written once they close.**"*

# **7. Reporting Guardrails**

Rules for keeping these numbers credible in front of the team, Brent, or a board:

- **Never present a forecast as banked. **Wins are 0 until awarded. EV is a plan, not a result.

- **Small samples are signals, not track records. **A 40% close rate on 5 finalists is a leading indicator. Watch whether it holds across the next 10–15.

- **Lead with banked numbers. **Submissions/month and pitch rounds/month are real today. Rates involving future wins are forecasts — label them.

- **State the denominator. **Every percentage is only as honest as what it divides by. Say whether it's of total submissions or of decided bids.

Propellant Media  ·  Internal RFP Operations  ·  Save this document to the project knowledge base so it is referenceable in future analyses.

Page