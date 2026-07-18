# rfp-engine knowledge base (drop the 5 docs here)

The `rfp-engine` skill needs five project-knowledge documents to draft at **full fidelity**
(the Questions-Checklist answers + the templated Poppins `.docx` + winning-proposal structures).
The skill folder only ships `SKILL.md`; these live in Justin's **Claude Project / chat**. Until
they're here, the `draft` stage produces a **partial** package (outline + bid analysis + flags).

## Add them (export from the Claude Project, drop the files in this folder)

| Expected file (any readable format: .md / .txt / .pdf / .docx) | Contents |
|---|---|
| `01_questions_checklist.*`      | 30+ intake questions (Higher Ed + Government sets) |
| `02_section_instruction_template.*` | Section-by-section drafting specs (Poppins, tone/length/always-include/never-include, win-loss warnings) |
| `03_win_loss_feedback.*`        | Loss patterns from 8+ institutions (the full corpus, not just the 7-pattern summary) |
| `04_sop_lifecycle.*`           | 10-phase RFP lifecycle + red-flag checklist |
| `05_winning_proposals/`        | Winning/recent submissions (Utah State, AB Tech, CCA, Dutchess, Montana) for structure & pricing |

Exact names aren't critical — the `draft` stage globs this folder and loads whatever is here.

## Once added
Re-run drafting on anything approved:  `./run.sh draft`
The stage will detect the knowledge base and produce the full templated response instead of the
partial outline.

## Note on sensitivity
These are proprietary win/loss + client materials, so `.gitignore` keeps their **contents out of
git** by default (only this README + `.gitkeep` are tracked). Commit them yourself only if you want
them versioned in the repo. Alternatively, put them in a Google Drive folder and point the draft
stage there.
