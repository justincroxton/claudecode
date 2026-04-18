from datetime import date, timedelta
from typing import Iterable

from config import SAM_GOV_API_KEY
from .base import RFP, Source, http, clean, matches_keywords, looks_like_institution

API_URL = "https://api.sam.gov/opportunities/v2/search"


class SamGovSource(Source):
    name = "sam.gov"

    def __init__(self, lookback_days: int = 30, page_size: int = 100):
        self.lookback_days = lookback_days
        self.page_size = page_size

    def fetch(self) -> Iterable[RFP]:
        if not SAM_GOV_API_KEY:
            return []

        session = http()
        results = []
        posted_to = date.today()
        posted_from = posted_to - timedelta(days=self.lookback_days)

        for keyword in ("marketing higher education", "enrollment marketing", "advertising university"):
            params = {
                "api_key": SAM_GOV_API_KEY,
                "limit": self.page_size,
                "offset": 0,
                "postedFrom": posted_from.strftime("%m/%d/%Y"),
                "postedTo": posted_to.strftime("%m/%d/%Y"),
                "ptype": "o,k,p",
                "q": keyword,
            }
            r = session.get(API_URL, params=params, timeout=30)
            if r.status_code != 200:
                continue
            data = r.json().get("opportunitiesData", []) or []
            for opp in data:
                title = clean(opp.get("title", ""))
                desc = clean(opp.get("description", ""))
                org = clean(opp.get("fullParentPathName", "") or opp.get("organizationType", ""))
                if not (matches_keywords(title, desc) and looks_like_institution(title, desc, org)):
                    continue
                results.append(RFP(
                    title=title,
                    url=opp.get("uiLink", "") or f"https://sam.gov/opp/{opp.get('noticeId', '')}/view",
                    description=desc,
                    school_name=org,
                    contact_title=clean((opp.get("pointOfContact") or [{}])[0].get("title", "")),
                    due_date=(opp.get("responseDeadLine") or "")[:10],
                    source=self.name,
                ))
        return results
