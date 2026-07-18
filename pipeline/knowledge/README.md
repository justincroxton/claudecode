# rfp-engine knowledge base

These are the institutional documents the `rfp-engine` drafting stage loads on every run, so the
pipeline remembers them across sessions (they're committed to the repo). List below tracks what's
in place vs. still needed, per **rfp-engine SKILL v4** (`rfp-engine_SKILL_v4.md`, uploaded — newer
than the globally-installed version; the draft stage uses this one).

## Received ✅
| File | Doc |
|---|---|
| `01_questions_checklist.md` | Questions Checklist (Higher-Ed + Government intake questions) |
| `02_section_template_v12.md` | **Section Instruction Template v12** — the "section builder": per-section tone/length/content/win-loss rules |
| `rfp-engine_SKILL_v4.md` | The v4 engine spec (build-time enforcement, full-bleed dividers, Canonical Case Study Library) |

## Still needed ⬜ (Justin uploading next)
| Expected | Doc | Powers |
|---|---|---|
| `03_win_loss_feedback.*` | Win-Loss Feedback | The 7 loss patterns tied to source losses (Empire State, NDSU, CU Boulder, Slate…) |
| `04_sop_lifecycle.*` | SOP | 10-phase lifecycle + red-flag checklist |
| `05_compliance_master.*` | Compliance Master | State-registration pre-check + submission compliance |
| `06_winning_proposals/` | Winning Proposals | **Parkland** (perfect-format ref), **Carlow**, **CU Boulder** (newest/best), Utah State, AB Tech, CCA |
| `07_divider_mapping.txt` + `dividers/` art | Divider Mapping + divider images | Required only for the full **.docx build** (section→divider matching, full-bleed pages) |

## Fidelity
- With #1, #2 and the v4 skill present → drafting produces the **Questions-Answered doc** and
  **section-by-section proposal text** at full fidelity.
- The polished **.docx with full-bleed dividers** additionally needs the **divider art + mapping**
  (#07) and Poppins installed; without them the stage delivers the drafted sections + a note.

## Note
Contents are committed to the private repo so they persist. Update by replacing a file and
committing. The draft stage globs this folder.
