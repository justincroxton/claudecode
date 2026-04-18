from typing import Iterable
from urllib.parse import urljoin
from bs4 import BeautifulSoup

from .base import RFP, Source, http, get, clean, matches_keywords, looks_like_institution, parse_date

BASE = "https://www.rfpalooza.com"


class RfpaloozaSource(Source):
    name = "rfpalooza"

    def fetch(self) -> Iterable[RFP]:
        session = http()
        results = []
        for path in ("/?s=marketing+higher+education", "/?s=enrollment+marketing"):
            r = get(session, urljoin(BASE, path))
            if not r:
                continue
            soup = BeautifulSoup(r.text, "lxml")
            for art in soup.select("article, .post, .search-result"):
                link = art.find("a", href=True)
                if not link:
                    continue
                title = clean(link.get_text(" "))
                href = urljoin(BASE, link["href"])
                desc = clean(art.get_text(" "), max_len=600)
                if not matches_keywords(title, desc):
                    continue
                if not looks_like_institution(title, desc):
                    continue
                due = ""
                for label in art.find_all(string=lambda s: s and ("due" in s.lower() or "deadline" in s.lower())):
                    due = parse_date(label)
                    if due:
                        break
                results.append(RFP(
                    title=title,
                    url=href,
                    description=desc,
                    school_name="",
                    due_date=due,
                    source=self.name,
                ))
        return results
