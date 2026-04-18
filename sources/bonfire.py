from typing import Iterable
from urllib.parse import urljoin
from bs4 import BeautifulSoup

from config import BONFIRE_INSTITUTIONS
from .base import RFP, Source, http, get, clean, matches_keywords, parse_date


class BonfireSource(Source):
    name = "bonfire"

    def fetch(self) -> Iterable[RFP]:
        if not BONFIRE_INSTITUTIONS:
            return []

        session = http()
        results = []
        for sub in BONFIRE_INSTITUTIONS:
            base = f"https://{sub}.bonfirehub.com"
            opps_url = f"{base}/portal/?tab=openOpportunities"
            r = get(session, opps_url)
            if not r:
                continue
            soup = BeautifulSoup(r.text, "lxml")
            for row in soup.select("a.opportunity, .opportunity-row a, table a"):
                title = clean(row.get_text(" "))
                href = row.get("href", "")
                if not (title and href):
                    continue
                if not matches_keywords(title):
                    continue
                detail_url = urljoin(base, href)
                desc, due = "", ""
                d = get(session, detail_url)
                if d:
                    dsoup = BeautifulSoup(d.text, "lxml")
                    desc = clean(dsoup.get_text(" "), max_len=600)
                    for label in dsoup.find_all(string=lambda s: s and "close" in s.lower()):
                        due = parse_date(label.parent.get_text(" "))
                        if due:
                            break
                results.append(RFP(
                    title=title,
                    url=detail_url,
                    description=desc,
                    school_name=sub.upper(),
                    due_date=due,
                    source=self.name,
                ))
        return results
