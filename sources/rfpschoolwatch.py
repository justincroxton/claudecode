from typing import Iterable
from urllib.parse import urljoin
from bs4 import BeautifulSoup

from .base import RFP, Source, http, get, clean, matches_keywords, parse_date

BASE = "https://www.rfpschoolwatch.com"


class RfpSchoolWatchSource(Source):
    name = "rfpschoolwatch"

    def fetch(self) -> Iterable[RFP]:
        session = http()
        r = get(session, f"{BASE}/rfps")
        if not r:
            return []
        soup = BeautifulSoup(r.text, "lxml")
        results = []
        for card in soup.select("article, .rfp-listing, li.rfp, .post"):
            link = card.find("a", href=True)
            if not link:
                continue
            title = clean(link.get_text(" "))
            href = urljoin(BASE, link["href"])
            text = clean(card.get_text(" "), max_len=600)
            if not matches_keywords(title, text):
                continue
            due = ""
            for label in card.find_all(string=lambda s: s and "due" in s.lower()):
                due = parse_date(label)
                if due:
                    break
            school = ""
            sn = card.select_one(".school, .institution, h3")
            if sn:
                school = clean(sn.get_text(" "))
            results.append(RFP(
                title=title,
                url=href,
                description=text,
                school_name=school,
                due_date=due,
                source=self.name,
            ))
        return results
