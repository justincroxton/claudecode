from typing import Iterable

from config import GOOGLE_CSE_API_KEY, GOOGLE_CSE_ID
from .base import RFP, Source, http, clean, matches_keywords, parse_date

API_URL = "https://www.googleapis.com/customsearch/v1"

QUERIES = [
    '"request for proposal" "marketing" (university OR college) 2026',
    '"RFP" "enrollment marketing" site:edu 2026',
    '"request for proposal" "digital advertising" "higher education" 2026',
    '"RFP" "media buying" (college OR university) 2026',
]


class GoogleCseSource(Source):
    name = "google_cse"

    def fetch(self) -> Iterable[RFP]:
        if not (GOOGLE_CSE_API_KEY and GOOGLE_CSE_ID):
            return []

        session = http()
        results = []
        seen = set()
        for q in QUERIES:
            params = {"key": GOOGLE_CSE_API_KEY, "cx": GOOGLE_CSE_ID, "q": q, "num": 10}
            r = session.get(API_URL, params=params, timeout=30)
            if r.status_code != 200:
                continue
            for item in r.json().get("items", []) or []:
                url = item.get("link", "")
                if not url or url in seen:
                    continue
                seen.add(url)
                title = clean(item.get("title", ""))
                desc = clean(item.get("snippet", ""))
                if not matches_keywords(title, desc):
                    continue
                results.append(RFP(
                    title=title,
                    url=url,
                    description=desc,
                    school_name=clean(item.get("displayLink", "")),
                    due_date=parse_date(desc),
                    source=self.name,
                ))
        return results
