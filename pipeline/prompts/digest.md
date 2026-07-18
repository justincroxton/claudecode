# Stage 04 — DIGEST (post qualified opportunities to Slack #rfp_opportunities)

Post the qualified opportunities to the team Slack channel. Read-only over the pipeline —
do NOT move or delete files; opportunities stay in `pipeline/reviewed/` until a human triages
them into `pipeline/approved/`.

## Qualified = worth the team's attention
From `pipeline/reviewed/*.json`, include an opportunity if:
- `score.recommendation` is BID or MAYBE, AND
- `review.verdict` is not one that kills it (exclude verdict DOWNGRADE when it drops to PASS).
Always surface `review.verdict == NEEDS_HUMAN` items in a separate "needs a human look" group.

## Post to Slack channel #rfp_opportunities (channel_id C0BDV86M5FF)
Group by bucket in this order: Higher Education · K-12 · Public Health & Healthcare ·
Government & Tourism · Other. Omit empty buckets. Header:
`:mag: *RFP digest — <Mon DD>* — <N> qualified (rolling 5 days)`
One line per opportunity, sorted by due date (soonest first):
`• [<Title>](<url>) — <Buyer> (<ST>) — due <M/D> — *<BID|MAYBE>* <fit_score>/100`
Then a `:warning: Needs a human look` group for NEEDS_HUMAN items (with the reviewer's flag).
Footer: per-bucket counts. Split into multiple messages (all to C0BDV86M5FF) if over 5000 chars,
preserving bucket order. Never leave a bare RFP number as dead text — every line has a link.
End by confirming the message(s) posted with their links.
