#!/usr/bin/env bash
source "$(dirname "$0")/lib/common.sh"
shopt -s nullglob; files=("$PIPELINE"/inbox/*.json)
if (( ${#files[@]} == 0 )); then log "score: inbox empty, nothing to do"; exit 0; fi
run_claude "$PROMPTS/score.md"
