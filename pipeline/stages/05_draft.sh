#!/usr/bin/env bash
source "$(dirname "$0")/lib/common.sh"
shopt -s nullglob; files=("$PIPELINE"/approved/*.json)
if (( ${#files[@]} == 0 )); then log "draft: approved empty, nothing to draft"; exit 0; fi
run_claude "$PROMPTS/draft.md"
