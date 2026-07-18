#!/usr/bin/env bash
source "$(dirname "$0")/lib/common.sh"
: > "$TMP/candidates.jsonl"                      # scanner overwrites this each run
run_claude "$PROMPTS/scan.md" || true            # Claude writes candidates.jsonl
log "ingesting candidates -> inbox/ (dedup vs archive/)"
python3 "$PIPELINE/stages/lib/ingest.py" --input "$TMP/candidates.jsonl"
