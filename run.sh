#!/usr/bin/env bash
# RFP pipeline orchestrator.
#
#   ./run.sh                 # nightly: scan -> score -> review -> digest
#   ./run.sh nightly         # same as above
#   ./run.sh scan            # run a single stage (scan|score|review|digest|draft)
#   ./run.sh score review    # run several stages in the given order
#   ./run.sh draft           # separate stage: rfp-engine drafting on approved/
#   ./run.sh approve <id>    # human gate: move a reviewed opportunity into approved/
#
# The scan + digest stages need the Gmail and Slack MCP connectors available to the
# `claude` CLI. The score/review/draft stages need the `rfp-engine` skill installed.
# For unattended runs, set CLAUDE_FLAGS (see pipeline/stages/lib/common.sh).
set -euo pipefail
cd "$(dirname "$0")"
S="pipeline/stages"

run_stage() {
  case "$1" in
    scan)    "$S/01_scan.sh" ;;
    score)   "$S/02_score.sh" ;;
    review)  "$S/03_review.sh" ;;
    digest)  "$S/04_digest.sh" ;;
    draft)   "$S/05_draft.sh" ;;
    *) echo "unknown stage: $1" >&2; exit 2 ;;
  esac
}

cmd="${1:-nightly}"; shift || true
case "$cmd" in
  nightly|all) for s in scan score review digest; do
                 echo "===== $s ====="; run_stage "$s"; done ;;
  approve)     "$S/approve.sh" "$@" ;;
  scan|score|review|digest|draft)
               echo "===== $cmd ====="; run_stage "$cmd"
               for s in "$@"; do echo "===== $s ====="; run_stage "$s"; done ;;
  *) echo "usage: ./run.sh [nightly|scan|score|review|digest|draft|approve <id>]" >&2; exit 2 ;;
esac
