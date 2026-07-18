#!/usr/bin/env bash
# Usage: ./stages/approve.sh <id-or-substring> [...]
source "$(dirname "$0")/lib/common.sh"
[ $# -ge 1 ] || { echo "usage: approve.sh <id-or-substring> [...]"; exit 1; }
for q in "$@"; do
  shopt -s nullglob; hits=("$PIPELINE"/reviewed/*"$q"*.json)
  if (( ${#hits[@]} == 0 )); then echo "no reviewed match for '$q'"; continue; fi
  for f in "${hits[@]}"; do mv "$f" "$PIPELINE/approved/"; echo "approved: $(basename "$f")"; done
done
