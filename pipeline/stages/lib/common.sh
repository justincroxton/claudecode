#!/usr/bin/env bash
# Shared helpers for pipeline stages.
set -euo pipefail

# Resolve pipeline root (…/pipeline) regardless of where a stage is invoked from.
# This file lives in pipeline/stages/lib/, so the root is two levels up.
PIPELINE="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
export PIPELINE
export PROMPTS="$PIPELINE/prompts"
export LOGS="$PIPELINE/logs"
export TMP="$PIPELINE/tmp"
mkdir -p "$LOGS" "$TMP"

CLAUDE="${CLAUDE_BIN:-claude}"
# Flags for headless runs. For fully unattended (cron) execution you likely need the
# reasoning stages to use tools without prompts — set e.g.
#   export CLAUDE_FLAGS="--dangerously-skip-permissions"
# (only on a machine/automation you trust). Default keeps edits auto-approved.
CLAUDE_FLAGS="${CLAUDE_FLAGS:---permission-mode acceptEdits}"

log() { printf '[%s] %s\n' "$(date '+%H:%M:%S')" "$*"; }

# run_claude <prompt-file>  — runs Claude headless with the prompt, tee'd to a log.
run_claude() {
  local prompt="$1" name ts logf
  name="$(basename "$prompt" .md)"
  ts="$(date '+%Y%m%d-%H%M%S')"
  logf="$LOGS/${ts}-${name}.log"
  log "claude -p $name (log: $logf)"
  "$CLAUDE" -p "$(cat "$prompt")" $CLAUDE_FLAGS 2>&1 | tee "$logf"
}
