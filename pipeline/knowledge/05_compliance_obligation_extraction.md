**PROPELLANT MEDIA**

RFP Compliance Obligation
Extraction Protocol

For Claude AI & RFP Team Reference

Version 1.0  |  March 2026

**1. Purpose**

This document defines the protocol for extracting every mandatory obligation from an RFP document and presenting them in a categorized, actionable compliance tracker. The goal is simple: never get disqualified for missing a submission requirement.

When Claude analyzes an RFP, this extraction runs automatically as part of the workflow. The output is a standalone Compliance Obligations Tracker that your team uses as the submission checklist before final delivery.

**2. Trigger Words by Risk Tier**

Not all obligation language carries the same weight. We scan for three tiers of keywords, each with different implications for your response.

**Tier 1: Disqualification Risk**

If the RFP uses any of these words to describe a requirement, missing it can result in automatic disqualification. These are non-negotiable.

| **Keyword** | **What It Means** | **Default Risk** |
| --- | --- | --- |
| MUST | Absolute obligation. No flexibility. | PASS/FAIL |
| SHALL | Legal/contractual obligation. Treated identically to MUST in procurement. | PASS/FAIL |
| REQUIRED | Explicitly stated as a condition of submission. | PASS/FAIL |
| MANDATORY | Often used for pre-bid conferences, forms, and certifications. | PASS/FAIL |
| CRITICAL | Signals highest-priority items the evaluation committee will check first. | PASS/FAIL |

**Tier 2: Scoring Risk**

These words indicate strong expectations. Missing them won't always disqualify you, but they will cost points on the scoring rubric.

| **Keyword** | **What It Means** | **Default Risk** |
| --- | --- | --- |
| EXPECTED | The committee assumes you will do this. Absence is noticed. | SCORED |
| WILL (as obligation) | E.g., 'Vendor will provide monthly reports.' Treated as a commitment. | SCORED |
| NECESSARY | Implies the item is needed for a compliant response. | SCORED |
| ESSENTIAL | Core to the scope. Skipping it signals you didn't read the RFP. | SCORED |
| IS REQUIRED TO | Phrase-level trigger. Same weight as REQUIRED. | PASS/FAIL |

**Tier 3: Bonus Scoring Opportunities**

These are not mandatory, but addressing them shows thoroughness and can differentiate your response. Think of these as 'easy points on the table.'

| **Keyword** | **What It Means** | **Default Risk** |
| --- | --- | --- |
| SHOULD | Recommended but not required. | BONUS |
| PREFERRED | The committee has a preference. Meeting it scores higher. | BONUS |
| RECOMMENDED | Suggested approach. Including it shows you're aligned. | BONUS |
| STRONGLY ENCOURAGED | One step below mandatory. Treat it as near-required. | BONUS |
| DESIRABLE | Nice-to-have. Include if it doesn't add significant effort. | BONUS |

**3. Obligation Categories**

Every extracted obligation gets assigned to one of these categories. This is how your team divides and conquers -- each category maps to a different person or workflow step.

| **Category** | **What Gets Captured** |
| --- | --- |
| Submission Format | How to submit: portal vs. email vs. hard copy, number of copies, file format, page limits, font/binding requirements, naming conventions |
| Required Forms & Documents | Addendums, exhibits, certifications, notarizations, vendor registration forms, W-9, conflict of interest disclosures, references |
| Content Requirements | Specific narrative sections the RFP says MUST be included -- executive summary structure, case study requirements, question-response format |
| Certifications & Legal | MWBE certs, state vendor registrations, bonding requirements, NDA execution, non-collusion affidavits, debarment certifications |
| Personnel Requirements | Named staff requirements, resumes, org charts, professional certifications, key personnel substitution restrictions |
| Technical/Scope Compliance | Specific platforms, integrations (especially CRM like Slate), deliverables, reporting cadences, or capabilities that MUST be demonstrated |
| Financial/Pricing | Sealed bid requirements, pricing template format, budget breakdowns by channel, rate cards, fee structures, payment terms |
| Deadlines & Timeline | Submission deadline, pre-bid conference date, Q&A submission window, intent-to-bid deadline, contract start date, campaign launch date |
| Insurance & Bonding | General liability minimums, professional liability, workers comp, auto insurance, cyber liability, performance bonds |

**4. Compliance Obligations Tracker Template**

This is the output format Claude produces for every RFP. Each row represents one mandatory obligation extracted from the document.

| **#** | **Obligation** | **Category** | **Trigger** | **RFP Ref** | **Risk** | **Status** | **Owner** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Submit 3 hard copies + 1 USB drive | Submission Format | MUST | Sec 2.1, p.4 | PASS/FAIL | NOT STARTED |  |
| 2 | Include signed Non-Collusion Affidavit (Exhibit B) | Required Forms | SHALL | Sec 3.2, p.8 | PASS/FAIL | NOT STARTED |  |
| 3 | Provide 3 higher education case studies within last 5 years | Content Req. | REQUIRED | Sec 5.1, p.12 | PASS/FAIL | NOT STARTED |  |
| 4 | Demonstrate Slate CRM integration capability | Technical | MUST | Sec 6.3, p.18 | PASS/FAIL | NOT STARTED |  |
| 5 | Include resumes for all key personnel | Personnel | REQUIRED | Sec 4.2, p.10 | SCORED | NOT STARTED |  |
| 6 | Use provided pricing template (Attachment C) | Financial | SHALL | Sec 8.1, p.22 | PASS/FAIL | NOT STARTED |  |
| 7 | Attend mandatory pre-bid conference March 15 | Deadlines | MANDATORY | Sec 1.4, p.3 | PASS/FAIL | NOT STARTED |  |
| 8 | Carry $2M general liability insurance | Insurance | REQUIRED | Sec 9.2, p.25 | PASS/FAIL | NOT STARTED |  |

**Status Definitions**

| **Status** | **Definition** |
| --- | --- |
| NOT STARTED | Obligation identified but no action taken yet |
| IN PROGRESS | Someone is working on this item |
| COMPLETE | Item is done and ready for submission |
| N/A | Does not apply to Propellant Media (must include justification) |
| CLARIFICATION NEEDED | Ambiguous language -- submit question during Q&A period |

**5. Where This Fits in the RFP Engine Workflow**

The compliance extraction is not a standalone step. It integrates directly into the existing RFP Engine workflow and feeds three downstream outputs.

**Workflow Position**

| **Step** | **Name** | **Compliance Connection** |
| --- | --- | --- |
| Step 1 | Obtain the RFP Document |  |
| Step 2 | Determine RFP Type |  |
| Step 3 | Run Full Question Checklist |  |
| Step 3.5 | COMPLIANCE OBLIGATION EXTRACTION | NEW -- This protocol |
| Step 4 | Cross-Reference Win-Loss Intelligence | Uses compliance items to flag risk patterns |
| Step 5 | Bid/No-Bid Recommendation | Compliance burden factors into recommendation |
| Step 6 | Draft the RFP Response | Every content requirement maps to a response section |
| Step 7 | Generate Personalization Punch List | Every PASS/FAIL item appears as NEEDS YOU |
| Step 8 | Deliver Outputs | Compliance Tracker delivered as Output 1.5 |

**What the Compliance Tracker Feeds Into**

**Output 1 (Question Answers): **The final compliance checklist question in the Questions Checklist gets auto-populated from this tracker instead of being answered from memory.

**Output 2 (Draft Response): **Every content requirement from the tracker gets a corresponding section in the draft. If the RFP says MUST include 3 case studies, the draft has a placeholder for exactly 3.

**Output 3 (Punch List): **Every PASS/FAIL item that Claude can't auto-complete is flagged as NEEDS YOU with specific instructions on what the team must provide.

**6. Extraction Rules ****&**** Edge Cases**

These rules govern how Claude identifies and classifies obligations. They handle the gray areas that cause missed requirements.

**Core Rules**

Scan the ENTIRE document before extracting. Some obligations appear in appendices, exhibits, or boilerplate terms and conditions that are easy to skip.

Extract the full sentence, not just the keyword. 'Proposals must be received by 5:00 PM EST' is the obligation -- not just 'must.'

When the same obligation appears multiple times (common in RFPs), consolidate into one row and note all page references.

If an obligation contradicts another part of the RFP (e.g., Section 2 says email submission, Section 8 says portal only), flag it as CLARIFICATION NEEDED and recommend submitting a question during the Q&A period.

Distinguish between obligations on the VENDOR vs. obligations on the INSTITUTION. Only extract vendor obligations.

When the RFP references an external document (e.g., 'per State Code 123.45'), note the reference but flag that the team needs to verify the external requirement.

**Common Gotchas in Higher Ed ****&**** Government RFPs**

**Buried vendor registration requirements: **Some states require you to register as a vendor BEFORE submitting. This often appears in the terms and conditions section, not the submission instructions. Lead time can be 2-4 weeks.

**Insurance minimums in the contract (not the RFP): **The RFP may not mention insurance, but the attached sample contract might require $2M+ in coverage. Always read attached contracts and terms.

**Sealed pricing envelopes: **Government RFPs frequently require the cost proposal in a SEPARATE sealed envelope or separate uploaded file. Putting pricing in the technical proposal = disqualification. Reference: Empire State loss.

**Page limits that exclude appendices: **Some RFPs say '50 page limit' but exclude appendices, cover page, and TOC from the count. Others include everything. If unclear, ask during Q&A.

**Notarization requirements: **Some forms require notarized signatures. This takes time to schedule. Flag any notarization requirement as a deadline-sensitive item.

**Intent to Bid deadlines: **Missing an intent-to-bid deadline doesn't always disqualify you, but it can. Treat it as PASS/FAIL unless the RFP explicitly says otherwise.

**7. How to Use This Protocol (Team Instructions)**

When Claude produces a Compliance Obligations Tracker for a new RFP, here's what your team does with it.

**Review the PASS/FAIL items first. **These are your non-negotiables. If any PASS/FAIL item can't be met (e.g., state residency requirement, insurance minimum you don't carry), that's a strong signal toward NO-BID.

**Assign an Owner to every row. **Don't leave the Owner column blank. Every obligation needs a name next to it. For Propellant Media, this is typically Justin, the new hire, or the ad ops team.

**Work the deadlines backward. **If pre-bid conference is March 15 and submission is April 1, you have a 17-day window. Map every obligation to a completion date, not just the final deadline.

**Use Q****&****A aggressively. **Every CLARIFICATION NEEDED item should become a formal question submitted during the Q&A period. Don't guess -- ask.

**Final compliance check before submission. **Walk through the tracker row by row. Every Status must be COMPLETE or N/A (with justification). Any NOT STARTED or IN PROGRESS item means you're not ready to submit.

**Cross-Reference with Scoring Rubric**

When the RFP includes a scoring rubric, map each obligation to its corresponding scoring category and point value. This tells you where to invest the most effort. A PASS/FAIL item worth 0 points on the rubric still matters (it's table stakes), but a SCORED item worth 30 points deserves more attention than one worth 5.