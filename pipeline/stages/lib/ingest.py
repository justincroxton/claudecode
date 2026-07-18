#!/usr/bin/env python3
"""
ingest.py — the scanner's output stage (dedup engine).

The scanner (01_scan) FINDS candidate opportunities and writes them to a JSONL
file (one JSON object per line). This script decides what is NEW: it computes a
stable dedup key for each candidate, checks it against the archive ledger, and
for anything unseen it writes a schema-shaped record to inbox/ and records the
key in archive/seen.jsonl so it is never re-ingested.

Deterministic and idempotent: re-running the same candidates produces zero new
files. This is intentionally separate from the LLM so dedup is testable.

Usage:
    python3 ingest.py --input pipeline/tmp/candidates.jsonl
    cat candidates.jsonl | python3 ingest.py           # stdin also works
Exit code 0 always (a scan finding nothing new is not an error).
"""
import argparse, hashlib, json, re, sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]          # .../pipeline
INBOX = ROOT / "inbox"
ARCHIVE = ROOT / "archive"
SEEN = ARCHIVE / "seen.jsonl"
BUCKETS = {"higher_education", "k12", "public_health_healthcare", "government_tourism", "other"}


STOP = r"\b(services?|solutions?|inc|llc|the|and|or|for|of|a|an|to)\b"


def norm(s: str) -> str:
    s = (s or "").lower().replace("&", " and ")
    s = re.sub(STOP, " ", s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def _h(basis: str) -> str:
    return hashlib.sha1(basis.encode()).hexdigest()


def keys(o: dict):
    """Return (primary_key, content_key, ref_key). We dedup if EITHER the source
    ref OR the content key (title+due+location, buyer-independent) has been seen —
    so the RFPMart (anonymized) and RFP School Watch (named) copies of the same
    RFP collapse even when buyer naming and title suffixes differ."""
    ref = norm(o.get("source_ref", ""))
    ref_key = _h(f"ref:{ref}") if ref else ""
    content_key = _h(f"c:{norm(o.get('title',''))}|{o.get('due_date','unknown')}|{norm(o.get('location',''))}")
    return (ref_key or content_key), content_key, ref_key


def load_seen() -> set:
    """Every ref_key and content_key ever recorded — a hit on either = duplicate."""
    keys_seen = set()
    if SEEN.exists():
        for line in SEEN.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            for k in ("dedup_key", "content_key", "ref_key"):
                if rec.get(k):
                    keys_seen.add(rec[k])
    return keys_seen


def read_candidates(path):
    raw = (Path(path).read_text(encoding="utf-8") if path else sys.stdin.read()).strip()
    if not raw:
        return []
    # Accept either a JSON array or JSONL
    if raw[0] == "[":
        return json.loads(raw)
    out = []
    for line in raw.splitlines():
        line = line.strip()
        if line:
            out.append(json.loads(line))
    return out


def coerce(o: dict) -> dict:
    b = o.get("bucket", "other")
    if b not in BUCKETS:
        b = "other"
    return {
        "source":      o.get("source", "Other"),
        "source_ref":  o.get("source_ref", ""),
        "buyer":       o.get("buyer", "").strip(),
        "title":       o.get("title", "").strip(),
        "bucket":      b,
        "location":    o.get("location", ""),
        "due_date":    o.get("due_date", "unknown"),
        "posted_date": o.get("posted_date", "unknown"),
        "est_value":   o.get("est_value", ""),
        "url":         o.get("url", "").strip(),
        "summary":     o.get("summary", ""),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", help="JSONL/JSON file of candidate opportunities; omit to read stdin")
    ap.add_argument("--today", default=date.today().isoformat(), help="override ingest date (YYYY-MM-DD)")
    args = ap.parse_args()

    INBOX.mkdir(parents=True, exist_ok=True)
    ARCHIVE.mkdir(parents=True, exist_ok=True)

    candidates = read_candidates(args.input)
    seen = load_seen()
    new, dupes, skipped, seen_this_run = 0, 0, 0, set()

    with SEEN.open("a", encoding="utf-8") as ledger:
        for raw in candidates:
            o = coerce(raw)
            if not o["title"] or not o["url"]:
                skipped += 1  # scanner contract: every opportunity needs a title and a link
                continue
            key, content_key, ref_key = keys(o)
            hit = {key, content_key, ref_key} - {""}
            if hit & (seen | seen_this_run):
                dupes += 1
                continue
            seen_this_run |= hit
            oid = f"{args.today}-{key[:8]}"
            rec = {"id": oid, "dedup_key": key, "first_seen": args.today, "stage": "inbox", **o}
            (INBOX / f"{oid}.json").write_text(json.dumps(rec, indent=2), encoding="utf-8")
            ledger.write(json.dumps({"dedup_key": key, "content_key": content_key, "ref_key": ref_key,
                                     "id": oid, "first_seen": args.today, "source_ref": o["source_ref"],
                                     "buyer": o["buyer"], "title": o["title"]}) + "\n")
            new += 1

    print(json.dumps({"new": new, "duplicates": dupes, "skipped_no_title_or_url": skipped,
                      "candidates": len(candidates), "inbox": str(INBOX)}))


if __name__ == "__main__":
    main()
