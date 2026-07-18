# RFP Pipeline — Propellant Media

A file-based, staged pipeline. The scanner **finds** opportunities; every later stage reads
and writes JSON files on disk, so each stage is independent and re-runnable. Reasoning stages
(score / review / draft) call the `rfp-engine` skill via headless `claude`; plumbing (dedup,
file moves) is plain Python/shell.

## Folder structure

```
pipeline/
├── inbox/        scanner output — NEW opportunities (deduped vs archive/)   [01 scan]
├── archive/      dedup ledger (seen.jsonl) — every opportunity ever seen
├── scored/       opportunity + bid/no-bid score block                        [02 score]
├── reviewed/     + adversarial red-flag review block                         [03 review]
├── approved/     YOU move winners here (human gate)                          → feeds 05
├── drafts/       <id>/response.md · compliance.md · punch-list.md · brief.json [05 draft]
├── logs/         per-run claude logs
├── tmp/          scratch (candidates.jsonl)
├── schema/opportunity.schema.json   the record every stage honors
├── prompts/      scan · score · review · digest · draft  (the stage instructions)
└── stages/
    ├── 01_scan.sh 02_score.sh 03_review.sh 04_digest.sh 05_draft.sh approve.sh
    └── lib/ingest.py (dedup engine)   lib/common.sh
../run.sh          orchestrator (at repo root)
```

## Flow

```
                 ┌─────────── nightly (./run.sh) ───────────┐
 emails ─▶ 01 scan ─▶ inbox/ ─▶ 02 score ─▶ scored/ ─▶ 03 review ─▶ reviewed/ ─▶ 04 digest ─▶ Slack
                                                                         │
                                              you triage: ./run.sh approve <id>
                                                                         ▼
                                                     approved/ ─▶ 05 draft ─▶ drafts/<id>/
```

Move-forward semantics: each stage consumes its input dir and writes the next. `archive/` is
permanent dedup memory (never cleared); `inbox/` etc. hold only what's awaiting the next stage.

## Run it

```bash
./run.sh                    # nightly: scan → score → review → digest
./run.sh scan               # a single stage (scan|score|review|digest|draft)
./run.sh score review       # several, in order
./run.sh approve 2026-06-25-a1b2c3d4   # move a reviewed opp into approved/
./run.sh draft              # rfp-engine drafting on everything in approved/
```

## Dedup (the scanner's output contract)

`stages/lib/ingest.py` reads candidate opportunities (JSONL) and writes only the NEW ones to
`inbox/`. It dedups on **the source ref OR normalized title+due+location** (buyer-independent,
stopword-stripped) — so the RFPMart (anonymized) and RFP School Watch (named) copies of the
same RFP collapse to one. Idempotent: re-running the same candidates yields zero new files.
Test it directly:

```bash
python3 stages/lib/ingest.py --input tmp/candidates.jsonl [--today YYYY-MM-DD]
```

## Requirements

- **`claude` CLI** on PATH (reasoning stages run headless). For unattended/cron runs set
  `CLAUDE_FLAGS` (see `stages/lib/common.sh`) so tools run without interactive prompts.
- **Gmail + Slack MCP connectors** available to `claude` for the `scan` and `digest` stages.
- **`rfp-engine` skill** installed for `score` and `draft` (holds the real bid/no-bid + drafting
  methodology). `digest` posts to Slack channel **#rfp_opportunities** (`C0BDV86M5FF`).
```
