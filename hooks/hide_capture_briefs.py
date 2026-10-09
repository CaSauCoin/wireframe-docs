"""MkDocs hook: turn capture slots into reader-facing figures.

Every "### Image — …" / "### Short video — …" / "### Diagram — …" section
carries a `!!! note "… brief"` block and, once captured, a `<!-- wf:shot … -->`
slot with the steps WireFrame's doc_builder replays. Those stay in the Markdown
(they are how the media is reproduced: `python3 -m doc_builder docs-fill`);
readers should see a figure, not the production notes.

At build time this hook:
  * drops every brief admonition and every `wf:` comment from the page HTML;
  * turns a captured section — heading + screenshot or video — into
    `<figure class="wf-figure">` whose caption is the heading's text, keeping
    the heading's id so existing links still land on it;
  * drops the section altogether while it has no media yet;
  * removes all of these headings from the table of contents.
"""
from __future__ import annotations

import re

_BRIEF = re.compile(
    r'<div class="admonition note">\s*<p class="admonition-title">'
    r"(?:Image capture|Video production|Diagram production) brief</p>.*?</div>\s*",
    re.S,
)
_WF_COMMENT = re.compile(r"<!--\s*/?wf:(?:shot|video|out)\b.*?-->\s*", re.S)
_SLOT_HEADING = re.compile(
    r'<h3 id="(?P<id>[^"]+)">(?P<kind>Image|Short video|Diagram) — (?P<title>.*?)'
    r'<a class="headerlink"[^>]*>.*?</a></h3>\s*', re.S)
_NEXT_SECTION = re.compile(r"<h[1-3][ >]")
# The media right under the heading: a paragraph holding the (lightbox-wrapped)
# image, or a <video> element, bare or in a paragraph.
_MEDIA = re.compile(
    r'\s*(?:<p>\s*(?P<p>(?:<a class="glightbox".*?</a>|<img\b[^>]*>))\s*</p>'
    r'|(?:<p>\s*)?(?P<v><video\b.*?</video>)(?:\s*</p>)?)\s*', re.S)


def _drop_toc(items, ids: set[str]) -> None:
    items[:] = [i for i in items if i.id not in ids]
    for i in items:
        _drop_toc(i.children, ids)


def on_page_content(html: str, page, config, files):
    html = _BRIEF.sub("", html)
    html = _WF_COMMENT.sub("", html)
    slot_ids: set[str] = set()
    out, pos = [], 0
    for m in _SLOT_HEADING.finditer(html):
        slot_ids.add(m.group("id"))
        out.append(html[pos:m.start()])
        nxt = _NEXT_SECTION.search(html, m.end())
        end = nxt.start() if nxt else len(html)
        media = _MEDIA.match(html, m.end(), end)
        if not media:
            pos = m.end()          # nothing captured yet: no empty heading
            continue
        kind = "Video" if media.group("v") else ("Diagram" if m.group("kind") == "Diagram" else "Screenshot")
        body = media.group("v") or media.group("p")
        # The caption written at capture time (img alt / video title) says
        # what the frame shows; the brief heading is a slot key and can still
        # carry a feature name the app has since retired.
        cap = re.search(r'(?:alt|title)="([^"]+)"', body)
        title = cap.group(1) if cap else re.sub(r"<[^>]+>", "", m.group("title")).strip()
        out.append(f'<figure class="wf-figure" id="{m.group("id")}">{body}'
                   f'<figcaption data-kind="{kind}">{title}</figcaption></figure>\n')
        pos = media.end()
    out.append(html[pos:])
    if slot_ids and page.toc:
        _drop_toc(page.toc.items, slot_ids)
    return "".join(out)
