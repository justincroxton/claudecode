from typing import Iterable
from urllib.parse import urljoin
from bs4 import BeautifulSoup

from .base import RFP, Source, http, get, clean, matches_keywords, looks_like_institution, parse_date

BASE = "https://www.commbuys.com"
SEARCH_PATH = "/bso/external/publicBids.sdo"


class CommBuysSource(Source):
    name = "commbuys"

    def fetch(self) -> Iterable[RFP]:
        session = http()
        r = get(session, urljoin(BASE, SEARCH_PATH))
        if not r:
            return []
        soup = BeautifulSoup(r.text, "lxml")
        results = []
        for row in soup.select("table tr"):
            cells = row.find_all("td")
            if len(cells) < 4:
                continue
            link = cells[0].find("a", href=True)
            if not link:
                continue
            title = clean(link.get_text(" "))
            href = urljoin(BASE, link["href"])
            org = clean(cells[1].get_text(" ")) if len(cells) > 1 else ""
            due = parse_date(cells[-1].get_text(" "))
            if not matches_keywords(title):
                continue
            if not looks_like_institution(title, org):
                continue
            results.append(RFP(
                title=title,
                url=href,
                description="",
                school_name=org,
                due_date=due,
                source=self.name,
            ))
        return results
