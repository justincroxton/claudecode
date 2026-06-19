# White-Label Geofencing Landing Page — Agency Setup Guide

A complete, single-file geofencing / location-based advertising landing page that any
marketing agency can rebrand in **under 30 minutes** — no build tools, no frameworks,
no dependencies. Just one `index.html` file you can open in any browser or drop onto any host.

---

## 1. What's in this folder

| File | Purpose |
|------|---------|
| `index.html` | The entire landing page (HTML + CSS + a tiny bit of JS, all self-contained). |
| `WHITE-LABEL-GUIDE.md` | This guide. |
| `assets/` | Drop your logo, favicon, and any client logos here. |

Because everything is inline, you can email the single HTML file, host it on Webflow/
WordPress/Netlify/S3, or paste it into a landing-page builder. No `npm install` required.

---

## 2. The 5-minute rebrand (colors, fonts, logo)

Open `index.html` and find the block labeled **`EDIT ME #2 — BRAND CONTROL PANEL`**
near the top (inside `<style>`). This `:root` block re-skins the **entire page**:

```css
:root {
  --brand:      #2563eb;   /* Primary brand color — buttons, links, accents */
  --brand-dark: #1e3a8a;   /* Darker shade for gradients & hovers */
  --brand-soft: #dbeafe;   /* Light tint for badges & icon backgrounds */
  --accent:     #f59e0b;   /* Secondary highlight (stars, etc.) */
  ...
  --font: "Inter", ...;    /* Swap for your brand typeface */
}
```

**To rebrand the look:** change `--brand`, `--brand-dark`, and `--brand-soft` to your
client's palette. Tip: pick your main color for `--brand`, a noticeably darker version
for `--brand-dark`, and a very light tint for `--brand-soft`. Everything — buttons,
the hero gradient, icons, the map illustration accents — updates automatically.

**To change the font:** edit `--font`. To use a Google Font, add its `<link>` in the
`<head>` and reference the family name here.

---

## 3. Swap the logo & name

There are 14 clearly-marked `EDIT ME #N` comments throughout the file. The brand ones:

- **`EDIT ME #1`** — Browser tab title + SEO description.
- **`EDIT ME #3`** — Header logo. Replace `[AGENCY NAME]` and the `◎` mark, **or**
  replace the whole `<a class="logo">…</a>` with an image:
  ```html
  <a href="#" class="logo"><img src="assets/logo.svg" alt="Your Agency" style="height:34px"></a>
  ```
- **`EDIT ME #14`** — Footer logo, tagline, address, phone, and email.

Then do a global find-and-replace of **`[AGENCY NAME]`** with your client's name
(appears in the header, footer, and copyright line).

---

## 4. Edit the copy (find each `EDIT ME #N`)

| Marker | Section | What to change |
|--------|---------|----------------|
| `#4`  | Hero | Main headline + subheadline. Lead with the client's value proposition. |
| `#5`  | Trust strip | Replace category words with real client logos (`<img>`). |
| `#6`  | Stats band | Swap in **your own** proof numbers. *Don't keep placeholder stats live.* |
| `#7`  | Solutions | Your service cards — rename, add, or remove. |
| `#8`  | How It Works | The 4-step process. |
| `#9`  | Benefits | Benefit bullet points. |
| `#10` | Industries | The industries you serve. |
| `#11` | Testimonials | **Real** client quotes only — get written permission. |
| `#12` | FAQ | Questions and answers. |
| `#13` | Contact / CTA | Final headline + connect the form (see §5). |

---

## 5. Make the contact form actually work

The form is a **demo** — it pops an alert on submit. Connect it to your stack:

- **Easiest (no backend):** point it at a form service —
  ```html
  <form action="https://formspree.io/f/yourid" method="POST">
  ```
  (Formspree, Getform, Basin, or Netlify Forms all work this way.)
- **Scheduling:** replace the form with a Calendly/HubSpot embed.
- **CRM:** paste your HubSpot / Mailchimp / GoHighLevel embed code in place of the form.

Then update the phone number and email in `EDIT ME #13` and `#14`.

---

## 6. Legal & compliance checklist (important for resale)

Before putting a client's name on this page:

- [ ] Replace **all** placeholder statistics and testimonials with real, defensible data.
- [ ] Add a real **Privacy Policy** and **Terms** (links are in the footer).
- [ ] Confirm geofencing privacy claims match your actual data practices and local law.
- [ ] Add the client's business address, phone, and a working contact method.
- [ ] Add analytics (Google Analytics / GTM) before the closing `</body>` tag.
- [ ] Set up a favicon: drop `favicon.ico` in `assets/` and add
      `<link rel="icon" href="assets/favicon.ico">` in the `<head>`.

---

## 7. Going live

1. Test locally — just double-click `index.html`.
2. Host it: drag the folder into **Netlify Drop**, a **Cloudflare Pages** project, an
   **S3** bucket, or upload via WordPress/Webflow.
3. Point your domain at it and you're live.

---

## 8. Notes on design

- **Fully responsive** — collapses cleanly to tablet and mobile.
- **Zero external image dependencies** — the hero "map" is hand-drawn SVG, so the page
  always looks complete even before you add real photography.
- **Accessible-friendly** — semantic headings, labeled SVG, keyboard-focusable controls.
- Want photography? Replace the `.map-card` SVG in the hero with an `<img>` of a real
  map/dashboard screenshot for a more literal look.

---

*Built as a reusable template. Each agency is responsible for the accuracy of the
claims, stats, and testimonials they publish under their own brand.*
