from dataclasses import dataclass, asdict, field
from typing import Iterable, List, Optional
import re
import requests
from datetime import datetime, date
from dateutil import parser as dateparser

from config import KEYWORDS, INSTITUTION_HINTS, REQUEST_TIMEOUT, USER_AGENT


@dataclass
class RFP:
    title: str
    url: str
    description: str = ""
    school_name: str = ""
    contact_title: str = ""
    due_date: str = ""
    source: str = ""

    def to_row(self) -> dict:
        return asdict(self)


class Source:
    name: str = "base"

    def fetch(self) -> Iterable[RFP]:
        raise NotImplementedError


def http() -> requests.Session:
    s = requests.Session()
    s.headers.update({"User-Agent": USER_AGENT, "Accept-Language": "en-US,en;q=0.9"})
    return s


def get(session: requests.Session, url: str, **kw) -> Optional[requests.Response]:
    try:
        r = session.get(url, timeout=REQUEST_TIMEOUT, **kw)
        if r.status_code >= 400:
            return None
        return r
    except requests.RequestException:
        return None


def matches_keywords(*texts: str) -> bool:
    blob = " ".join(t for t in texts if t).lower()
    return any(k in blob for k in KEYWORDS)


def looks_like_institution(*texts: str) -> bool:
    blob = " ".join(t for t in texts if t).lower()
    return any(h in blob for h in INSTITUTION_HINTS)


def parse_date(text: str) -> str:
    if not text:
        return ""
    try:
        d = dateparser.parse(text, fuzzy=True, default=datetime(2026, 1, 1))
        return d.date().isoformat()
    except (ValueError, TypeError, OverflowError):
        return ""


def is_future(iso_date: str, today: Optional[date] = None) -> bool:
    if not iso_date:
        return True
    try:
        d = date.fromisoformat(iso_date)
    except ValueError:
        return True
    return d >= (today or date.today())


def clean(text: str, max_len: int = 500) -> str:
    if not text:
        return ""
    t = re.sub(r"\s+", " ", text).strip()
    return t[:max_len]
