#!/usr/bin/env bash
source "$(dirname "$0")/lib/common.sh"
shopt -s nullglob; files=("$PIPELINE"/reviewed/*.json)
if (( ${#files[@]} == 0 )); then log "digest: reviewed empty, nothing to post"; exit 0; fi
run_claude "$PROMPTS/digest.md"
