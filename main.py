import csv
import os
import sys
from datetime import date

from config import OUTPUT_DIR, OUTPUT_CSV
from sources.base import RFP, is_future
from sources.sam_gov import SamGovSource
from sources.bonfire import BonfireSource
from sources.rfpschoolwatch import RfpSchoolWatchSource
from sources.commbuys import CommBuysSource
from sources.rfpalooza import RfpaloozaSource
from sources.google_cse import GoogleCseSource

SOURCES = [
    SamGovSource(),
    BonfireSource(),
    RfpSchoolWatchSource(),
    CommBuysSource(),
    RfpaloozaSource(),
    GoogleCseSource(),
]

FIELDS = ["title", "url", "school_name", "contact_title", "due_date", "description", "source"]


def collect() -> list[RFP]:
    seen_urls: set[str] = set()
    out: list[RFP] = []
    for src in SOURCES:
        try:
            rows = list(src.fetch())
        except Exception as e:
            print(f"[{src.name}] error: {e}", file=sys.stderr)
            continue
        kept = 0
        for r in rows:
            if not r.url or r.url in seen_urls:
                continue
            if not is_future(r.due_date):
                continue
            seen_urls.add(r.url)
            out.append(r)
            kept += 1
        print(f"[{src.name}] {kept} kept (of {len(rows)})")
    return out


def write_csv(rows: list[RFP], path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.to_row().get(k, "") for k in FIELDS})


def main() -> int:
    rows = collect()
    rows.sort(key=lambda r: (r.due_date or "9999-12-31", r.source))
    out_path = os.path.join(OUTPUT_DIR, OUTPUT_CSV)
    write_csv(rows, out_path)
    print(f"\nWrote {len(rows)} RFPs to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
