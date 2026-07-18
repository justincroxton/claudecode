# Stage 02 — SCORE (apply rfp-engine bid/no-bid to each inbox file)

Score every opportunity awaiting scoring. **Invoke the `rfp-engine` skill** and apply its
bid/no-bid criteria and institutional win/loss patterns — do NOT improvise scoring; the skill
holds the real methodology.

## Procedure
1. List `pipeline/inbox/*.json`. For each file (skip `.gitkeep`):
2. Read the opportunity record. Apply the rfp-engine bid/no-bid criteria for its `bucket`
   (higher_education, k12, public_health_healthcare, government_tourism, other), considering
   Propellant's services, the vertical fit, budget, timeline, competition, and barriers.
3. Add a `score` block to the record:
   {"recommendation":"BID|MAYBE|PASS","fit_score":<0-100>,"rationale":"<2-3 sentences>",
    "disqualifiers":["<any hard blockers to verify>"],"scored_at":"<ISO datetime>"}
   Set `stage` = "scored".
4. Write the enriched record to `pipeline/scored/<id>.json`, then DELETE the original
   `pipeline/inbox/<id>.json` (move-forward — each dir means "awaiting the next stage").

Only state what the record and rfp-engine support; never invent RFP facts. If a record lacks
enough detail to score confidently, set recommendation "MAYBE" and note it in the rationale.
End by printing how many files were scored and the BID/MAYBE/PASS counts.
