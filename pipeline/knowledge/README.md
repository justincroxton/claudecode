# rfp-engine knowledge base

These are the institutional documents the `rfp-engine` drafting stage loads on every run, so the
pipeline remembers them across sessions (they're committed to the repo). List below tracks what's
in place vs. still needed, per **rfp-engine SKILL v4** (`rfp-engine_SKILL_v4.md`, uploaded — newer
than the globally-installed version; the draft stage uses this one).

## Received ✅
| File | Doc |
|---|---|
| `01_questions_checklist.md` | Questions Checklist (Higher-Ed + Government intake questions) |
| `02_section_template_v12.md` | **Section Instruction Template v12** — the "section builder" |
| `04a_velocity_methodology_guide.md` | SOP — RFP pipeline velocity methodology |
| `04b_process_improvements_standards.md` | SOP — process improvements & standards |
| `04c_policy_adoption_memo.md` | SOP — team policy adoption memo |
| `05_compliance_obligation_extraction.md` | Compliance Master — obligation-extraction protocol |
| `06_winning_proposals/` (5) | **Winning/Pitch Proposals** — Colorado School of Mines (WIN), NECC26MKT01 (WIN), Univ. of Wyoming MBA (PITCH), WorWic (PITCH), STCC (PITCH) |
| `07_divider_mapping.txt` | Divider Mapping (21 dividers + AA–AD front matter) |
| `rfp-engine_SKILL_v4.md` | The v4 engine spec (build enforcement, full-bleed dividers, Canonical Case Study Library) |

## Still needed ⬜ (optional / .docx-only)
| Expected | Doc | Powers |
|---|---|---|
| `dividers/` art (PNG/JPG, ~25 files) | Divider images referenced by `07_divider_mapping.txt` | Needed ONLY for the polished **.docx** full-bleed build (binary art). Questions-Answered + section-text drafting work without them. |
| `03_win_loss_feedback.*` | Win-Loss Feedback (optional) | Full loss corpus. The 7 loss patterns already live in `rfp-engine_SKILL_v4.md`, so this is enrichment, not a blocker. |

**Status: drafting knowledge base COMPLETE.** The engine can now produce full-fidelity
Questions-Answered docs and section-by-section proposal text. Only the divider art images remain,
and only for the final Word/PDF render.

## Fidelity
- With #1, #2 and the v4 skill present → drafting produces the **Questions-Answered doc** and
  **section-by-section proposal text** at full fidelity.
- The polished **.docx with full-bleed dividers** additionally needs the **divider art + mapping**
  (#07) and Poppins installed; without them the stage delivers the drafted sections + a note.

## Note
Contents are committed to the private repo so they persist. Update by replacing a file and
committing. The draft stage globs this folder.
