# Propellant Portfolio Engine

Turns a case study PDF into a portfolio item on propellant.media — anonymized,
brand-styled, with the charts rebuilt as HTML and an FAQ accordion on the end.

`SKILL.md` is written for Claude. This file is written for you.

---

## Installing (claude.ai — works in Projects and regular chats)

1. **Settings → Capabilities** — turn on "Code execution and file creation."
   Without it the Skills menu is greyed out.
2. **Customize → Skills → +** — upload `pm-portfolio-engine.zip` whole. Do not unzip it.
3. **Toggle it on.** Uploaded is not the same as enabled.
4. **Settings → Connectors** — make sure the **Zapier** connector is connected, and that
   its **WordPress** actions are enabled. This is the piece that actually writes to the
   site. Manage the enabled actions here:
   https://mcp.zapier.com/mcp/servers/452edbf3-cceb-4b89-83a6-f2e871d5a54e/config

   Required WordPress actions: **Create Post**, **Update Post**, **Find Post**,
   **Upload Media**, **API Request (GET)**, **API Request (Mutating)**.

Then in any chat or Project: upload the PDF and say *"Post this to the Propellant
portfolio."* You don't have to name the skill.

In Claude Code this repo's copy loads automatically — nothing to install.

---

## What each file does

| File | Plain English |
|---|---|
| `SKILL.md` | The instructions Claude reads. Site structure, rules, styling spec, category map. |
| `PROMPT.md` | The same thing as a paste-able prompt, for anywhere the skill isn't loaded. |
| `README.md` | This file. |

---

## Using it in a Claude Project

A Project works well for this because the standing instructions never have to be
re-pasted. Two ways to set it up:

- **With the skill installed** (recommended) — nothing else needed. The skill triggers
  on its own when you upload a case study.
- **Without it** — paste `PROMPT.md`'s long version into the Project's custom
  instructions, or drop `Propellant-Portfolio-Prompt.txt` into Project knowledge.

Either way the Zapier connector still has to be on. The skill is the knowledge; the
connector is the hands.

---

## What to expect

- **Drafts by default.** It never publishes unless you say so.
- **The client is always anonymized.** Real metrics, blurred identity.
- **You supply the grid thumbnail.** It won't pick one for you.
- **Timeouts are normal.** A large page write often exceeds Zapier's 30-second task
  limit while still saving fine. The skill knows to verify rather than re-send — if
  Claude tells you it timed out and then confirms the content landed, believe it.
- **Approve the tool call.** Writing to a live site prompts for permission each run.
