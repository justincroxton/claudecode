---
name: rfp-engine
description: "Propellant Media's RFP analysis and response drafting engine. Use this skill whenever a user uploads an RFP document, pastes a link to a public RFP PDF, mentions an RFP they want to respond to, asks to analyze a bid opportunity, or says anything like 'analyze this RFP', 'should we bid on this', 'run the RFP playbook', 'draft an RFP response', 'new RFP', or 'review this solicitation'. Also trigger when the user references procurement documents, requests for proposals, RFQs, or bid opportunities for higher education, government, public health, tourism, or nonprofit sectors. This skill orchestrates the full lifecycle: intake analysis, bid/no-bid recommendation, section-by-section drafting, compliance checklist, and personalization punch list. Always use this skill before attempting to analyze or draft any RFP content -- it contains critical institutional knowledge about win patterns, loss patterns, and formatting requirements that cannot be replicated from general knowledge."
---

# Propellant Media RFP Engine (v4)

## Purpose

Turns a raw RFP document into a complete analysis and draft response for Propellant Media, a digital marketing agency specializing in higher education, government, and public sector enrollment marketing.

## What changed in v4 (read this — it fixes recurring failures)

v3 told the model what to remember. v4 makes the BUILD SCRIPT enforce it and FAIL LOUDLY when it can't. Every fix below traces to a real, caught failure:

1. **Dividers not fit to page** → v3 sized images at 612x792 (wrong: that's 72-DPI points). docx-js ImageRun dimensions are PIXELS at 96 DPI. Correct full-page size is **816 x 1056**. v4 also makes ALL dividers full-bleed via floating behind-document anchor + zero-margin section (in-line images inherit the 1" margin and can never bleed).
2. **Wrong case studies (e.g. "College of Coastal Alabama")** → v3 had no canonical roster, so the model filled acronyms from general knowledge. v4 embeds the **Canonical Case Study Library** and forbids any institution not in it.
3. **TOC not rendering as a divider** → v4 specifies exact OOXML and a render-gate check that fails the build if the TOC page is missing.
4. **Content in wrong sections** → v4 adds a **Content Routing Table** with hard rules (Media Plan 3-paragraph open, SWOT in §13, CRM structure).
5. **Missing dividers / Page 3 Creative divider dropped** → v4 puts Page 3 Creative Samples in the front-matter sequence and adds a build-time assertion that every required divider was inserted.
6. **Mandatory render gate** → every build renders to PDF, rasterizes pages, and visually verifies full-bleed dividers + TOC before delivery.

---

## Prerequisites

Before executing, load these project resources (search project knowledge):

1. **Questions Checklist** — Search: "questions to ask reviewing RFP" — intake questions
2. **Win-Loss Feedback** — Search: "RFP feedback loss scoring" — loss patterns
3. **SOP** — Search: "SOP RFP lifecycle submission process" — 10-phase workflow + red flags
4. **Compliance Master** — Search: "compliance master Propellant Media"
5. **v9 Section Template** — Search: "RFP section template v9" — ALWAYS use the latest template version present in the project; do not hardcode a version number
6. **Winning Proposals** — Search "Parkland" (perfect-format reference), "Carlow", "CU Boulder" (newest/best standard), "Utah State", "AB Tech", "CCA"
7. **Divider Mapping** — Read `/mnt/project/divider_mapping__1_.txt` (note the `__1_` suffix — the v3 path `divider_mapping.txt` does NOT exist)

If any are missing, tell the user which to upload before proceeding.

---

## The Four Outputs (deliver ONE AT A TIME — ask before each)

Justin's instruction: never dump all four at once. After analysis, ask which to build next.

1. **Questions Answered Document** — every checklist question answered with RFP specifics + bid/no-bid
2. **Submission Compliance Protocol** (the "Parkland_College_Submission_Compliance_Protocol" format)
3. **Compliance Tracker**
4. **Proposal Response Document** (.docx with embedded full-bleed dividers)

---

## Execution Workflow

### Step 1: Obtain the RFP
Read uploads from `/mnt/user-data/uploads/` or `/mnt/project/`. For a public PDF URL, use `web_fetch` with `web_fetch_pdf_extract_text: true`. Read the ENTIRE document before analysis.

### Step 2: State Compliance Pre-Check (run BEFORE drafting)
Check state registration status against the pipeline: NC active; NJ gap; CO/VA/MD/NY Tier 2/3; foreign-LLC + sales-tax lead times of 2–4 weeks. Flag any gap to Erin before drafting begins.

### Step 3: Determine RFP Type
Higher Education / Government / Public Health / Tourism / Other. Use the matching checklist questions.

### Step 4: Run the Full Question Checklist
State each question in bold, answer with a specific RFP citation, flag red flags. Watch the SOP red-flag items: sealed-pricing format, page limits (what counts — CU Boulder lost points because dividers counted), submission-method conflicts, MWBE/residency with no waiver, mandatory pre-bid, insurance levels, incumbent signals, vague rubric, creative-sample format, CRM (especially Slate bidirectional).

### Step 5: Cross-Reference Win-Loss Intelligence
Check this RFP against the 7 loss patterns: (1) generic strategy, (2) regional bias, (3) length mismatch, (4) creative weakness, (5) CRM/tech gap, (6) AI-strategy gap, (7) cost-format error. Tie each to its source loss (Empire State format DQ, NDSU retainer/percentage contradiction, CU Boulder page-count, Slate losses).

### Step 6: Bid/No-Bid
BID or NO-BID with 3–5 sentences. Filter through Justin's $750K RFP-revenue target and win probability.

### Step 7: Determine TOC Mode (state it, wait for confirmation)
- **Mode A** — RFP prescribes exact order → follow verbatim (Empire State/Oregon State lost from deviating)
- **Mode B** — RFP silent → standard 19-section Parkland model
- **Mode C** — RFP names sections without full structure → default TOC, insert RFP-required sections at logical spots using the RFP's exact titles

---

## Step 8: DRAFT THE PROPOSAL — BUILD-TIME ENFORCEMENT

Read `/mnt/skills/public/docx/SKILL.md` first.

### 8.1 Document specs (override any RFP font spec)
- Font: **Poppins**, 10pt body (size 20). VERIFY Poppins is installed (`fc-list | grep -i poppins`); abort with a clear message if missing.
- Headings: H1 13pt (size 26) red #e63412; H2 11pt (size 22) red; H3 10.5pt (size 21) black
- Body black; table header rows red #e63412 white bold text
- Page: US Letter 12240 x 15840 DXA; content-section margins 1" (1440); **divider sections margins 0**
- Running header: "[Institution] — [RFP Title] | Propellant Media"; footer centered page numbers
- Paragraph spacing after: 120; bullets left:900 hanging:450
- Table rows: header red/white bold; odd #FFFFFF, even #F5F5F5; ShadingType.CLEAR
- Subsection dividers: single-cell table, red bottom border (size 8, #e63412) only; title Poppins 13pt bold red; margins top:40 bottom:80 left:0 right:0

### 8.2 FULL-BLEED DIVIDER PROTOCOL (the actual fix)

All divider source art is 952x1232px at exact 8.5:11 ratio. Render at **816 x 1056** (8.5x11 @ 96 DPI). Every divider — static AND text-overlay — uses a **floating, behind-document anchor at page-relative offset 0,0** inside a **zero-margin section**. In-line ImageRun inherits page margins and CANNOT bleed — never use it for dividers.

```javascript
const { Document, Packer, ImageRun, PageBreak, Paragraph, TextRun, AlignmentType,
        SectionType, Header, Footer, TabStopType, TabStopPosition } = require('docx');
const fs = require('fs');

const PAGE_W_PX = 816, PAGE_H_PX = 1056;           // 8.5x11 @ 96 DPI — full bleed
const DIV = '/mnt/project/';

// Verify font before building — fail loudly
const { execSync } = require('child_process');
if (!execSync('fc-list').toString().toLowerCase().includes('poppins')) {
  throw new Error('ABORT: Poppins font not installed. Cannot meet brand spec.');
}

// Returns a SECTION object (not paragraphs) — every divider is its own zero-margin section
function dividerSection(filename, overlayParagraphs = []) {
  const path = DIV + filename;
  if (!fs.existsSync(path)) throw new Error(`ABORT: divider missing: ${filename}`);
  const data = fs.readFileSync(path);
  const ext = filename.toLowerCase().endsWith('.png') ? 'png' : 'jpg';

  const bg = new Paragraph({
    children: [ new ImageRun({
      type: ext, data,
      transformation: { width: PAGE_W_PX, height: PAGE_H_PX },
      floating: {
        horizontalPosition: { relative: 'page', offset: 0 },
        verticalPosition:   { relative: 'page', offset: 0 },
        behindDocument: true,
        wrap: { type: 'none' },
      },
    }) ],
  });

  return {
    properties: {
      type: SectionType.NEXT_PAGE,
      page: { size: { width: 12240, height: 15840 },
              margin: { top: 0, right: 0, bottom: 0, left: 0, header: 0, footer: 0 } },
    },
    headers: { default: new Header({ children: [] }) },
    footers: { default: new Footer({ children: [] }) },
    children: [ bg, ...overlayParagraphs ],   // overlay paragraphs sit ON TOP of bg
  };
}
```

Text-overlay dividers pass `overlayParagraphs`; static dividers pass none. Overlay paragraphs use top spacing to land text in the image's negative space — never bake text into the JPEG. For busy backgrounds (AC), add an opaque rectangle anchor behind the text for legibility.

### 8.3 FRONT MATTER SEQUENCE (exact order — Page 3 added per Justin)

```
1. divider_AA_Page_Cover_text_overlay.jpg          [overlay: institution, RFP#, date, "Propellant Media"]
2. divider_AB_academic_logos.jpg                    [static]
3. divider_AC_Growing_enrollment_page_text_overlay.jpg  [overlay: generic PM positioning]
4. Page_3_Creative_Samples_Higher_Education_Text_Overlay_Allowed.jpg  [overlay below]
5. divider_AD_Table_Of_Contents_text_overlay.jpg    [overlay: live TOC]
6. divider_01_cover_letter.png + Cover Letter content
... (numbered sections per mapping)
```

**Page 3 Creative Samples overlay text (exact):**
- Text: `Growing Enrollment & Engagement Across Many Colleges & Universities`
- Font Poppins **size 74** (37pt = 74 half-points), bold. "Enrollment &" and "Engagement" in red #e63412; remaining words white. Matches Justin's approved screenshot.

### 8.4 AA Cover overlay text (dynamic)
- Line 1: `[Institution Name]` — Poppins ~size 60 bold white (per approved UMGC cover)
- `Request for Proposal #[Number]` — red #e63412 bold
- `[Service Line]` — white bold; `[Scope sub-line]` — white
- `Propellant Media` — red bold
- `Justin Croxton, CEO`
- `1 (877) 776-7358 | 800 Battery Ave SE, Suite 300, Atlanta, GA 30339`
- `justin@propellant.media`

### 8.5 AD Table of Contents overlay
Header "Table of Contents" Poppins size 56 bold red. Entries: Poppins ~11pt. **OOXML child order is strict: tabs → spacing → ind.** Right-aligned dot leader at tab pos 10656 twips. Three runs per entry: label, tab char, page number. Page numbers bold.

### 8.6 Numbered-section dividers
Match section to divider by CONTENT using `/mnt/project/divider_mapping__1_.txt`. If no match, insert `divider_21_sample_divider_placeholder.png` and add to the Custom Dividers Punch List. Standard Mode-B order is sections 1–20 as mapped (Cover Letter → … → Appendix: Required Documents & Forms), with §9 CRM Integration and §14 Creative Process ALWAYS included.

### 8.7 BUILD-TIME ASSERTION (prevents dropped dividers)
After assembly, before packing, assert every required divider filename appears in the section list:
```javascript
const required = [
  'divider_AA_Page_Cover_text_overlay.jpg','divider_AB_academic_logos.jpg',
  'divider_AC_Growing_enrollment_page_text_overlay.jpg',
  'Page_3_Creative_Samples_Higher_Education_Text_Overlay_Allowed.jpg',
  'divider_AD_Table_Of_Contents_text_overlay.jpg',
  /* + every numbered divider used */ ];
const used = sections.flatMap(s => s.children).flatMap(p => p.imageRuns || []);
required.forEach(f => { if (!usedFilenames.includes(f))
  throw new Error(`ABORT: required divider not inserted: ${f}`); });
```

---

## Step 9: MANDATORY RENDER GATE (every build, no exceptions)

After saving the .docx, before presenting to Justin:

```bash
cd /mnt/user-data/outputs
soffice --headless --convert-to pdf <file>.docx
pdftoppm -png -r 70 <file>.pdf qa_page          # rasterize
python3 /mnt/skills/public/docx/scripts/office/validate.py <file>.docx
```

Then VIEW the rasterized pages and confirm:
- [ ] AA cover divider bleeds to all 4 page edges (no white margin border)
- [ ] Page 3 Creative divider present with font-37 overlay text correct
- [ ] AD TOC page renders AS the divider image with TOC text on top
- [ ] At least 2 numbered dividers checked — full-bleed, no margin gap, image fills page
- [ ] No section content bleeding onto a divider page

If any check fails, FIX and re-render before delivery. Do not hand Justin a file that hasn't passed the visual gate.

---

## Content Routing Table (which content goes where — prevents misplacement)

| Content | Correct Section | Hard Rule |
|---|---|---|
| Institution mission/challenge framing | Cover Letter opening | Lead with mission, NOT PM credentials (Carlow fix) |
| 3-channel-mix rationale | Media Buying & Media Plan | MUST open with exactly 3 paragraphs (3–6 sentences each): (1) challenge + approach, (2) media philosophy + funnel, (3) channel mix + budget. Default budget $300K if none stated. Application Projections is its own sub-section. |
| SWOT 2x2 | §13 Competitive Landscape | NEVER in Appendix. Color-coded quadrants (green/red/blue/amber), 2–3 bullets each, never reused across proposals. |
| CRM Integration & Attribution | §9 (REQUIRED every proposal) | Structure: (1) system-of-record framing, (2) Segmented Audiences & Predictive Targeting bullets, (3) Attribution & Performance Visibility table, (4) three-step framework (Pixel-to-Ping / Audience Mirroring / Application Yield Reporting), (5) BigQuery/Sheets/Zapier callout. Name Slate explicitly if RFP specifies it. ~2 pages. |
| Resumes | §18 Appendix | Aaron King resume MUST show 2015, never 2014 |
| References | §19 Appendix | From Canonical Reference list only; never Dutchess |
| W9, COI, MWBE cert, addenda, signed forms | §20 Appendix | — |

---

## CANONICAL CASE STUDY LIBRARY (NO INVENTION RULE)

A case study may appear in a proposal ONLY if it is in this library. Never invent an institution to fit an acronym. Each case study runs **half a page to 2 pages max**, with real metrics, in the established format (challenge → approach → channels → results table → reference).

- **CCA = Community College of Aurora** (Aurora, Colorado) — NOT College of Coastal Alabama. FLAGSHIP. Channels: Google Ads, Meta, Programmatic Display, Site Retargeting, Geofencing (**NO TikTok — never list TikTok for CCA**). Results: Fall 2026 degree-seeking enrollment +63.2% YOY (1,023 vs 627); concurrent +87% (344 vs 184); Summer 2026 degree-seeking +29.8%; 1,381 leads in 30 days (759 Meta, 122 RFIs). HSI. (Never write "College of the Albemarle" for CCA — known error.)
- **KSU = Kennesaw State University** — 4,100+ leads, $54 CPL, 75% app attribution to digital. Ref: Marsha White (mwhit205@kennesaw.edu, 470-578-6343). Supplemental — don't lead when RFP prefers comparable-size peers.
- **AB Tech = Asheville-Buncombe Technical CC** (Asheville, NC) — 598 leads/90 days, $20.69 CPL, $12,363.99 spend, 6.30% omnichannel CTR. Ref: Porsche Orndorf (porscharorndorf@abtech.edu, 828-398-7389). Behavioral health/workforce.
- **Stevens Institute of Technology** — graduate enrollment. Ref: Karla Medina (kmedina@stevens.edu, 201.216.3571).
- **Florida Gulf Coast University** — Ref: Tea Capuni (tcapuni@fgcu.edu, 239.745.4285).
- **Utah State University Online** — $79 blended CPL, four-state footprint, Salesforce CRM. Supplemental.
- **University of Arizona Nursing** — higher ed/nursing.
- **Cincinnati State** — community college.
- **Mount Saint Joseph University (MSJ)** — small private.
- **Craig Hospital** — healthcare/workforce: geofencing, OTT/CTV, paid search.

**Selection matrix:** Community college → CCA, AB Tech, Cincinnati State. Small private → MSJ, SCU Health Sciences, Stevens. Large public → KSU Undergrad, U of Arizona Nursing, Utah State. Graduate → Stevens, KSU Grad, U of Arizona Nursing. HSI → CCA. Behavioral health/workforce → AB Tech. **Dutchess Community College must never appear in any proposal.**

---

## Voice & Tone
PM's direct, confident, specific agency voice. Re-read the Parkland proposal before every draft to recalibrate. Short paragraphs (3–5 sentences), clean bullets, no jargon stacking. **Banned:** "leverages," "utilizes," "comprehensive suite," any AI-tell language. Write "We geofence every high school," not "PM implements advanced geofencing technology." Suggest a graphic wherever a section runs text-heavy and a visual would tell a bigger story (call it out explicitly to Justin — don't force it).

## Loom Standard (every submission)
Under 2:15; problem → reflect RFP → 3 differentiators with hard numbers → close. Add a CRM dashboard walkthrough Loom link in the analytics section. Justin records.

---

## Length by Budget Tier (Colin Owens)
Under $100K = 40–50 pages. $100–500K = 50–70 pages. $500K+ = 70–90 pages, add "Scaling Beyond Year 1," 6–8 case studies.

## Key Differentiators to Weave Throughout
MWBE (NMSDC federal) · Google Premier (top 3%) · Loom proposals · CRM Integration (Pixel-to-Ping/Audience Mirroring/Yield Reporting) · KSU record enrollment · Issue Resolution Process · Monday.com (never Asana) · AI-powered personalization.

---

## Standing Rules (NEVER violate)
- Founding year 2015 (never 2014) — applies everywhere including Aaron King's resume
- Address: 800 Battery Avenue SE, Suite 300, Atlanta, GA 30339 (never 3017 Bolling Way)
- Phone: 1 (877) 776-7358 (never the 404 number)
- Project management: Monday.com (never Asana)
- Dutchess Community College is NOT a client
- CCA = Community College of Aurora; no TikTok in CCA
- Self-score every draft against the RFP rubric — must clear 90+; never fabricate to hit the score. If compliance items must be inserted, flag them, don't invent them.

## Contamination Scan (before every submission)
grep for ALL prior institution names, prior contact names ("Dear Vergel"), prior CRM names, prior addendum references, prior geographic markets, junk text ("sdasd"), duplicate salutations, stray characters, duplicate names in team table.

---

## 15-Point Pre-Delivery Checklist
1. Every checklist question answered + bid/no-bid
2. Poppins 10pt body, headers red #e63412
3. RFP-prescribed structure followed (TOC mode stated)
4. All 5 front-matter pages present (AA, AB, AC, Page 3 Creative, AD) in order
5. **Render gate passed — dividers full-bleed, TOC renders, verified on rasterized pages**
6. Every numbered divider full-page, no margin gap (816x1056 floating anchor)
7. Build-time divider assertion passed (none dropped)
8. Custom Dividers Punch List included if any placeholder used
9. Case studies from Canonical Library only, matched to institution type, correct names
10. CCA = Community College of Aurora, no TikTok
11. SWOT in §13; Media Plan opens with 3 paragraphs; CRM §9 structure complete
12. CRM name consistent throughout (names Slate if specified)
13. Aaron King resume shows 2015; team table has no duplicate names
14. Contamination scan clean; phone/address correct; no stray "NEEDS YOU" flags unless intentional
15. Self-score 90+ against the RFP rubric

---

## Personalization Punch List (Output 3)
Table: | Section | Status | What's Needed |. Status: Ready / XX% Draft / NEEDS YOU / Custom Divider Needed. `[NEEDS YOU]` only for true human inputs (pricing, Loom links, signatures, references) — never as a shortcut for draftable sections. Put the Custom Dividers Punch List at the top.
