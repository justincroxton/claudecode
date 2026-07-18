#!/usr/bin/env bash
source "$(dirname "$0")/lib/common.sh"
shopt -s nullglob; files=("$PIPELINE"/scored/*.json)
if (( ${#files[@]} == 0 )); then log "review: scored empty, nothing to do"; exit 0; fi
run_claude "$PROMPTS/review.md"
