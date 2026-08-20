---
name: pm-portfolio-engine
description: Propellant Media's portfolio case study publisher. Turns a case study PDF (or campaign results doc) into a draft portfolio-item on propellant.media -- extracting the narrative, metrics, charts, tables, and quotes, anonymizing the client, and pushing it to WordPress as a draft. Use whenever Justin uploads a case study PDF and asks to post it to the portfolio, says "add this to the portfolio", "post this case study to the site", "make this a portfolio item", "run the portfolio engine", or asks to check what is already on the portfolio page. Also trigger when he references the portfolio page, portfolio items, or wants a finished case study turned into a web page. Always use this skill before attempting to create any portfolio content -- it carries the verified WordPress structure, the anonymization rules, the category map, and the media-upload constraints that cannot be reconstructed from general knowledge.
---

# Propellant Media Portfolio Engine

Turns a case study PDF into a **draft** `portfolio-item` on propellant.media, with its
graphics uploaded to the media library and embedded in the page.

Companion to `pm-case-study-engine` (which *produces* the PDF) and `pm-blog-engine`
(same site, different post type). This skill *publishes* to the web.

## Hard Rules

1. **NEVER publish.** Always `status: draft` on create -- Justin reviews and publishes
   by hand. On **update**, always pass `status` explicitly too: never leave it unset and
   trust the default, or an edit can silently flip a draft live (or knock a published
   item back to draft). Check the item's current status first and pass that same value.
2. **NEVER name the client.** Anonymize every case study. See Anonymization below.
3. **Publish the real metrics.** Do not band, round, or soften numbers -- if the PDF
   says $4,318 spend and a $37 CPL, the page says $4,318 and $37. (Justin, 2026-08-20.)
4. **NEVER invent a number, quote, or result** that is not in the source document.
   If the PDF contradicts itself (e.g. a flight window in the fact box that disagrees
   with the date range in a verification footnote), use the primary field, and tell
   Justin about the conflict rather than silently picking.
5. **Always dedup** against the existing portfolio items before creating anything.
6. **The featured image is Justin's.** Never auto-assign a grid thumbnail; ask for it.

## Verified Site Facts

Confirmed against the live install on 2026-08-20 -- do not re-derive.

| Fact | Value |
|---|---|
| Post type | `portfolio-item` (a CPT, *not* a page) |
| REST base | `https://propellant.media/wp-json/wp/v2/portfolio-item` |
| Public URL | `https://propellant.media/portfolio-item/<slug>/` |
| Taxonomy | The **same** `categories` taxonomy the blog uses |
| Existing items | ~100 |

### How to reach the site

Direct HTTPS to `propellant.media` and to `hooks.zapier.com` is **blocked** from Claude
Code sessions by the environment network policy. `curl` will fail. Every read and write
goes through the **Zapier MCP WordPress connection**, which runs server-side and is
unaffected.

Do **not** reuse the blog engine's Zapier catch hook
(`hooks.zapier.com/hooks/catch/2849243/uj0zl7h/`) -- that Zap is wired to post type
`Posts` and will file a portfolio item in the wrong place.

| Need | Call |
|---|---|
| Read anything | `execute_zapier_read_action` -> `wordpress_make_api_get_request` |
| Create the item | `execute_zapier_write_action` -> `wordpress_create_post`, `post_type: "portfolio-item"` |
| Update an item | `execute_zapier_write_action` -> `wordpress_update_post` |
| Upload a graphic/PDF | `execute_zapier_write_action` -> `wordpress_upload_media` |
| Delete a mistake | `wordpress_make_api_mutating_request`, `DELETE`, `?force=true` |

Always `inspect_zapier_actions` first to resolve the current schema.

## Content Structure

The body is **plain HTML inside a single WPBakery text block** -- no page-builder
layout to reproduce. Same wrapper the blog engine emits:

```
[vc_row][vc_column][vc_column_text css=""]
  ...HTML...
[/vc_column_text][/vc_column][/vc_row]
```

### Section template

Follow the house structure. Headings are `<h3>` wrapping `<strong>`:

1. **Opening paragraph** -- what the client is and what they do (anonymized).
2. **The challenge** -- the competitive or market problem before engagement.
3. `<h3><strong>What Our Team Was Tasked With</strong></h3>` -- objective, goals, budget.
4. `<h3><strong>Media Plan We Developed</strong></h3>` -- a `<ul>` with one `<li>` per
   channel, each opening with `<strong>Channel:</strong>`.
5. **Creative + landing page alignment** -- messaging strategy, conversion path.
6. `<h3><strong>Campaign Results</strong></h3>` -- results graphic, then metric bullets
   as `<p>` lines using `•` and `<strong>Label:</strong> value`.
7. **Closing outcome paragraph** -- what it proved, plus forward-looking note.

Add sections when the source supports them (a `<h3><strong>Client Feedback</strong></h3>`
pull quote, an extra results table). Never pad with sections the PDF cannot support.

### Brand palette

| Token | Hex |
|---|---|
| Propellant red | `#E63412` |
| Charcoal | `#2B2B2B` |
| Grid / rule | `#dcdcdc` |
| Zebra fill | `#f7f7f7` |
| Muted label | `#8a8a8a` |

There is no way to add theme CSS from here, so every style is an inline `style`
attribute. Inline styles beat the theme stylesheet, so they hold.

### Lists — use real `<ul>`, never bullet characters

Some older portfolio items fake bullets with `•` and `<br />` inside a `<p>`. **Do not
copy that.** It renders as a grey wall of text. A real `<ul><li>` picks up the theme's
branded red circled-check bullets, which is the look Justin wants. Match the WordPress
editor's own list formatting (a space and a tab before each `<li>`):

```html
<ul>
 	<li><strong>Label:</strong> value</li>
</ul>
```

Numbered takeaways stay an `<ol>`.

### Tables — always style them

An unstyled `<table>` renders borderless and unreadable on this theme. Every data table
gets: a Propellant-red header row with white text, a 1px `#dcdcdc` grid on every cell,
`#f7f7f7` zebra striping on alternating rows, right-aligned numeric columns, and a
charcoal total row with white bold text.

```html
<table style="width:100%;border-collapse:collapse;margin:28px 0;font-size:16px;">
<thead><tr style="background-color:#E63412;">
<th style="padding:14px 16px;text-align:left;color:#ffffff;font-weight:600;border:1px solid #E63412;font-size:15px;letter-spacing:0.3px;">Channel</th>
...
</tr></thead>
<tbody>
<tr><td style="padding:12px 16px;border:1px solid #dcdcdc;text-align:left;">...</td>...</tr>
<tr style="background-color:#f7f7f7;">...</tr>
<tr style="background-color:#2B2B2B;"><td style="...;color:#ffffff;font-weight:700;">Total</td>...</tr>
</tbody></table>
```

### Rebuild the PDF's charts as HTML, don't lift them as bitmaps

The designed panels in a Propellant case study -- the share-of-delivery stacked bar, the
completion-rate bars, the stat tiles -- are vector. Rebuild them as inline-styled HTML
rather than cropping them to PNG. It is crisp at every resolution, reflows on mobile,
needs no media staging, and stays editable.

Two patterns that work:

- **Stacked share bar:** a wrapper `div` at `width:100%;font-size:0;line-height:0;
  border-radius:3px;overflow:hidden;` holding one `<span style="display:inline-block;
  width:<pct>%;height:32px;background:<hex>;">` per segment. `font-size:0` on the parent
  kills the whitespace gaps between inline-blocks. Put the largest segment in charcoal
  `#1A1A1A` and the hero segment in Propellant red, then step down through greys.
- **Horizontal bar chart:** a borderless `<table>`, one row per bar -- label cell, a
  track cell (`<span style="display:block;background:#EDEDED;height:22px;">` wrapping a
  `<span>` at `width:<pct>%` in red or `#C9C9C9`), and a right-aligned value cell.
  Bar widths are the real percentages, never rescaled to exaggerate a gap.

Wrap each in `border:1px solid #e5e5e5;border-radius:10px;padding:24px;` to echo the
card treatment in the PDF.

**Emit each graphic as one single line of HTML with no internal newlines.** WordPress
runs `wpautop` on the content and will inject `<br />` and `<p>` tags at line breaks
inside your markup, which shatters the layout.

### Graphics, tables, icons, quotes

All of it makes the cut -- charts, data tables, performance screenshots, icons, and
client quotes. Handling:

- **Charts / screenshots / icons** -> upload to the media library, embed as `<img>`.
- **Tables** -> rebuild as real HTML `<table>` markup, not a flat image, whenever the
  PDF's table is machine-readable. Screenshot only if the layout can't be reproduced.
- **Quotes** -> `<blockquote>`, attributed by *role and org type only*
  ("Director of Marketing, regional health system"), never by name.

Strip any client logo, client name, or identifying URL from a graphic before upload.
If a chart is legible only because it carries the client's name, re-render or crop it.

## Anonymization

The client is never identified. Live examples of the house voice:

- "A University's summer program", then "the program" / "the university" thereafter
- "local hospital system", "west coast university", "government army based entity",
  "regional airport", "national accounting firm"

Rules:

- Replace the client name with a `<size/region> + <category>` descriptor. Region granularity
  stays broad -- "Midwest", "West Coast", "regional", "national". Never a city that
  makes the client obvious in a small market.
- Keep the *vertical* specific (it is the value of the case study); blur the *identity*.
- Strip named products, campaign names, and staff names.
- Watch the closing paragraphs -- a program's brand name slipping into the last line is
  the most common leak. Re-read the finished HTML for stray proper nouns before posting.
- The slug carries the same treatment:
  `local-hospital-system-utilize-omnichannel-advertising-geofencing-to-drive-disease-awareness`

## Categories

Assign the **vertical** (required, inferred from the case study) plus every **service**
the media plan actually used. Recent items carry 3-12 categories.

**Verticals:** Higher Education `5789` · Healthcare/Medical `5790` · Government `6102` ·
Travel & Hospitality `5797` · Real Estate `5798` · Retail `5775` · Auto Industry `5776` ·
Food/Restaurant `5796` · Home Care Services `5791` · Non Profit `4451` ·
Cannabis/CBD/Hemp `5898` · Furniture `4` · B2B Marketing `4486`

**Services:** Geofencing Advertising `181` · Addressable Geofencing `5793` ·
Digital Out Of Home `6756` ·
Programmatic Display `182` · Programmatic Video `5799` · OTT Advertising `4271` ·
Pre-Roll Video `5829` · YouTube Advertising `5827` · Google Ads `5823` ·
Paid Search `119` · Facebook/IG Advertising `5800` · Keyword Contextual/Search `5792` ·
Native Advertising `5826` · Retargeting `5373` · Video Marketing `5845` ·
Political Advertising `4133` · Recruitment `5802` · Inbound Marketing `4479` ·
White Label Marketing `5814` · Digital Advertising Strategy `5910` ·
Dashboard Analytics `5839`

Never assign `Uncategorized` (`1`). If no vertical fits, ask Justin.

Verify an ID before use, and find any not listed here:

```
wordpress_make_api_get_request
  url: https://propellant.media/wp-json/wp/v2/categories
  querystring: {search: "<term>", _fields: "id,name", per_page: "100"}
```

## Media Upload — read this before touching graphics

`wordpress_upload_media`'s `file` parameter accepts a **fetchable URL only**.

Verified 2026-08-20: a `data:image/png;base64,...` value fails with
`500: Sorry, you are not allowed to upload this file type` -- Zapier does not decode it,
it writes the string as a text file and WordPress rejects the type. A plain `https://`
URL works and WordPress generates every image size correctly.

**Consequence:** images extracted from the PDF live in the session sandbox, which has no
public URL. They must be staged somewhere Zapier can fetch before upload. Confirm the
staging route with Justin at the start of a run -- do not guess, and do not upload client
campaign data to a third-party paste or file-drop host.

Once each asset has a URL:

```
wordpress_upload_media
  file:      <public URL>
  filename:  descriptive-kebab-case.png
  title:     Human readable title
  alt_text:  Describes the data shown, no client name
```

Capture the returned `id` and `source_url`, then embed inline exactly as the house
markup does:

```html
<img class="alignnone size-full wp-image-<ID>" src="<source_url>" alt="" width="<W>" height="<H>" />
```

The **featured image** (portfolio grid thumbnail) is a separate attachment from any
inline graphic. Justin supplies it. Set `featured_media: <attachment id>`.

Attaching the source PDF is supported the same way -- upload it as media and link it
from the page. Ask first; not every case study should ship its PDF publicly.

## Workflow

1. **Read the PDF.** The sandbox has no poppler (`pdftotext`/`pdfimages` are absent)
   and the system `cryptography` build is broken, so `pypdf` and `pdfplumber` fail on
   import. `pip install pymupdf` works and handles text, images and page rendering.

   **Check what is actually raster before planning any upload.** A Propellant-designed
   case study is mostly vector text and shapes -- its charts, stat tiles and tables are
   drawn, not embedded, so `get_images()` may return nothing but the logo. Use
   `page.get_image_rects(xref)` to check placement: a ~74x22pt box at the top-left is
   the letterhead logo, not content. Rebuild vector charts and tables as HTML; only
   upload rasters that are genuinely images (dashboard screenshots, photos).
2. **Confirm setup with Justin:** the image staging route, the featured image, and
   whether to attach the source PDF.
3. **Dedup.** Pull existing slugs and titles; abort on a match.
   ```
   url: https://propellant.media/wp-json/wp/v2/portfolio-item
   querystring: {per_page: "100", _fields: "id,slug,title", orderby: "date", order: "desc"}
   ```
4. **Draft the HTML** against the section template.
5. **Anonymize** and re-read for leaked proper nouns.
6. **Assign categories** -- vertical plus services.
7. **Upload media**, capture IDs and URLs, embed.
8. **Create the draft.** `post_type` goes at the top level; everything else nests
   under `dynamic_properties`:
   ```
   wordpress_create_post
     post_type: "portfolio-item"
     dynamic_properties: {title, content, status: "draft", categories: ["4133", ...]}
   ```
   Category IDs are passed as an array of **strings**.
9. **Set the slug.** `slug` is not in the create action's schema, and WordPress leaves
   it empty on drafts (`generated_slug` only previews it). Set it explicitly after:
   ```
   wordpress_make_api_mutating_request
     url: https://propellant.media/wp-json/wp/v2/portfolio-item/<id>
     method: POST
     headers: {Content-Type: application/json}
     body: "{\"slug\":\"...\"}"
   ```
9. **Verify** by reading the created item back (`context=edit`) -- confirm the shortcode
   wrapper survived, images resolve, and status is `draft`.
11. **Report** the preview link, the categories assigned, and anything the PDF did not
    supply.

## QA Checklist

- [ ] Status is `draft`
- [ ] No client name, product name, staff name, or identifying URL anywhere
- [ ] Every metric traces to the source document
- [ ] Content wrapped in the `[vc_row]...[/vc_row]` shortcode
- [ ] Headings are `<h3><strong>`
- [ ] Every image resolves and carries a `wp-image-<ID>` class
- [ ] Tables are real HTML where the source allowed it, and styled (red header, grid,
      zebra, charcoal total row)
- [ ] Bullets are real `<ul><li>`, not `•` characters with `<br />`
- [ ] Charts rebuilt as inline-styled HTML, each emitted on a single line
- [ ] Quotes attributed by role and org type only
- [ ] A vertical category is set; services match the media plan; not `Uncategorized`
- [ ] Featured image set from Justin's upload
- [ ] Slug is descriptive and anonymized (set explicitly -- drafts have none)
- [ ] Flag to Justin: Yoast writes no meta description for portfolio items, so the
      page ships without one unless he wants it set
