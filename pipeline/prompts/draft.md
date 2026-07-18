# Stage 05 — DRAFT (full rfp-engine drafting on approved/)

For every opportunity a human has moved into `pipeline/approved/`, run the FULL `rfp-engine`
skill drafting lifecycle. This is the heavy stage and runs only on human-approved winners.

## Engine version + knowledge base check FIRST
Use the engine spec at **`pipeline/knowledge/rfp-engine_SKILL_v4.md`** if present — it is newer
than any globally-installed rfp-engine and governs the build (Canonical Case Study Library,
full-bleed divider protocol, content routing, standing rules). Then load the knowledge docs in
`pipeline/knowledge/` (Questions Checklist, Section Template v12, Win-Loss, SOP, Compliance Master,
Winning Proposals, Divider Mapping). Check what's present:
- **If present** — load them and draft at FULL fidelity: complete Questions-Checklist answers,
  the templated Poppins `.docx` per the Section Instruction Template, and winning-proposal
  structures/pricing models.
- **If absent** (only README/.gitkeep) — draft at PARTIAL fidelity (outline + bid analysis +
  loss-pattern flags), and clearly stamp each output "PARTIAL — pending knowledge docs" with a
  pointer to `pipeline/knowledge/README.md`. Do NOT fabricate the checklist answers or winning
  structures you don't have.

## Procedure
1. List `pipeline/approved/*.json` (skip `.gitkeep`). For each:
2. **Invoke the `rfp-engine` skill** to run its full lifecycle on this opportunity: intake
   analysis, bid/no-bid confirmation, section-by-section response drafting, compliance
   checklist, and personalization punch list. If the actual RFP document is available (a real
   URL or a file the human dropped alongside), use it; otherwise draft from the record + note
   what must be pulled from the source document (gated portals need a human download).
3. Write the output package to `pipeline/drafts/<id>/`:
   - `response.md` — the drafted response sections
   - `compliance.md` — the compliance/checklist + mandatory forms
   - `punch-list.md` — personalization to-dos before submission
   - `brief.json` — the opportunity record with `stage` = "drafted"
4. Move `pipeline/approved/<id>.json` into `pipeline/drafts/<id>/brief.json` (consume approved).

Do not fabricate RFP requirements — if the source document is gated/unavailable, draft what you
can and clearly flag the sections that require the real document. End by listing the draft
packages created and any that need the source document pulled first.
