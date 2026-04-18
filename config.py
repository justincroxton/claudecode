import os
from dotenv import load_dotenv

load_dotenv()

SAM_GOV_API_KEY = os.getenv("SAM_GOV_API_KEY", "")
GOOGLE_CSE_API_KEY = os.getenv("GOOGLE_CSE_API_KEY", "")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID", "")
BONFIRE_INSTITUTIONS = [
    s.strip() for s in os.getenv("BONFIRE_INSTITUTIONS", "").split(",") if s.strip()
]

KEYWORDS = [
    "marketing",
    "advertising",
    "media buying",
    "digital media",
    "enrollment",
    "student recruitment",
    "programmatic",
    "creative services",
    "branding",
    "communications",
    "public relations",
    "ott",
    "geofencing",
    "paid search",
    "seo",
]

INSTITUTION_HINTS = [
    "university",
    "college",
    "community college",
    "school district",
    "higher education",
    "academy",
    "institute",
]

REQUEST_TIMEOUT = 30
USER_AGENT = "PropellantRFPScout/0.1 (+https://propellant.media)"
OUTPUT_DIR = "output"
OUTPUT_CSV = "rfps.csv"
