#!/usr/bin/env python3
"""Build the 121 Scan help site.

    python build.py            -> site/ (what GitHub Pages publishes)
    python build.py --preview  -> also preview.html: every page in one file,
                                  for trying the site without hosting it

Inputs:
  content/<lang>/<slug>.md   page texts (front matter: title, lead)
  data/pages.yml             page order and fixed addresses
  data/ui.yml                the guide's own wording per language
  data/messages.yml          messages: meaning and what to do, per language
  data/app_text.json         the app's own on-screen text (scripts/sync_app_text.py)
  checked.json               the scandroid commit the guide was checked against
  assets/                    styles, script, icons, screens/<lang>/<shot>.png

Writes screens-needed.md: every screenshot slot not yet filled.
Fails loudly if a page uses app text that doesn't exist.
"""

import base64
import json
import re
import shutil
import sys
from pathlib import Path

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from markupsafe import Markup

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "site"
SUPPORT_EMAIL = "jharrison@redcross.nl"
LANG_NAMES = {"en": "English", "fr": "Français", "ar": "العربية"}
LANG_SHORT = {"en": "EN", "fr": "FR", "ar": "عربي"}


def load_yaml(rel):
    return yaml.safe_load((ROOT / rel).read_text(encoding="utf-8"))


PAGES = load_yaml("data/pages.yml")
UI = load_yaml("data/ui.yml")
MESSAGES = load_yaml("data/messages.yml")
APP = json.loads((ROOT / "data/app_text.json").read_text(encoding="utf-8"))
CHECKED = json.loads((ROOT / "checked.json").read_text(encoding="utf-8"))
LANGS = PAGES["langs"]


class AppText(dict):
    """The app's text in one language, falling back to English."""

    def __init__(self, lang):
        super().__init__(APP.get(lang, {}))
        self.lang = lang

    def __missing__(self, key):
        if key in APP["en"]:
            return APP["en"][key]
        raise KeyError(f"'{key}' is not in the app's text (data/app_text.json)")


def front_matter(text):
    m = re.match(r"\A---\n(.*?)\n---\n?(.*)\Z", text, re.S)
    return (yaml.safe_load(m.group(1)) or {}, m.group(2)) if m else ({}, text)


def md_inline(text):
    html = markdown.markdown(str(text)).strip()
    m = re.fullmatch(r"<p>(.*)</p>", html, re.S)
    return Markup(m.group(1) if m else html)


def fmt_date(ymd, lang):
    y, mo, d = (int(x) for x in ymd.split("-"))
    return f"{d} {UI[lang]['months'][mo - 1]} {y}"


def page_meta(slug, lang):
    path = ROOT / "content" / lang / f"{slug}.md"
    if not path.exists():
        raise SystemExit(f"Missing page: content/{lang}/{slug}.md")
    meta, body = front_matter(path.read_text(encoding="utf-8"))
    return meta, body


# The page being rendered. Jinja caches the macros in templates/macros.html,
# so they reach the current page through this record rather than closures.
CURRENT = {}


def collect_step(html):
    CURRENT["steps"].append(Markup(html))
    return html


def shot_html(shot, desc):
    if not shot:
        return ""
    lang, slug, root, ui = CURRENT["lang"], CURRENT["slug"], CURRENT["root"], CURRENT["ui"]
    rel = f"assets/screens/{lang}/{shot}.png"
    if (ROOT / rel).exists():
        return Markup(f'<figure class="shot"><a href="{root}{rel}" target="_blank" rel="noopener">'
                      f'<img src="{root}{rel}" alt="" loading="lazy"></a></figure>')
    CURRENT["needed"].append((lang, slug, shot, desc))
    return ""  # no picture yet: the step shows without one


def build(preview=False):
    env = Environment(loader=FileSystemLoader(ROOT / "templates"), undefined=StrictUndefined,
                      autoescape=False, trim_blocks=False)
    env.filters["md_inline"] = md_inline
    env.filters["label"] = lambda s: str(s).strip().rstrip(":").strip()
    env.filters["collect_step"] = collect_step
    env.globals["shot_html"] = shot_html
    needed = []
    pages = PAGES["pages"]

    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir()

    for lang in LANGS:
        app = AppText(lang)
        ui = UI[lang]
        titles = {p["slug"]: page_meta(p["slug"], lang)[0] for p in pages}
        steps_by_slug = {}

        for i, p in enumerate(pages):
            slug, kind, role = p["slug"], p["kind"], p.get("role")
            meta, body = page_meta(slug, lang)
            root = "../" * (slug.count("/") + 1)

            def url(target, to_lang=lang, root=root):
                target, _, frag = target.partition("#")
                return f"{root}{to_lang}/{target}.html" + (f"#{frag}" if frag else "")

            def links(text, url=url):
                text = re.sub(r"\]\(@([a-z0-9/#_-]+)\)", lambda m: f"]({url(m.group(1))})", text)
                text = re.sub(r'href="@([a-z0-9/#_-]+)"', lambda m: f'href="{url(m.group(1))}"', text)
                return re.sub(r"\(@([a-z0-9/_-]+)\)",
                              lambda m: f"([{titles[m.group(1)]['title']}]({url(m.group(1))}))", text)

            steps = []
            CURRENT.update(lang=lang, slug=slug, root=root, ui=ui, steps=steps, needed=needed)
            ctx = dict(app=app, facts=APP.get("facts", {}))
            rendered = env.from_string('{% from "macros.html" import step, note %}' + body).render(**ctx)
            body_html = Markup(markdown.markdown(links(rendered)))
            steps_by_slug[slug] = steps

            group_pages = [q for q in pages if q.get("role") == role and q["kind"] in ("task", "card")] if role else []
            nxt = None
            if kind in ("task", "card"):
                idx = [q["slug"] for q in group_pages].index(slug)
                if idx + 1 < len(group_pages):
                    nxt = {"slug": group_pages[idx + 1]["slug"], "title": titles[group_pages[idx + 1]["slug"]]["title"]}
            parent = None
            if kind in ("task", "card") and role:
                parent = {"slug": f"{role}/index", "title": titles[f"{role}/index"]["title"]}
            children = [{"slug": q["slug"], **titles[q["slug"]]} for q in group_pages] if kind == "role" else []

            # Messages, in this language
            def message(m):
                if "key" in m:
                    own = m["key"] in APP.get(lang, {})
                    text = app[m["key"]]
                    english_only = not own and lang != "en"
                else:
                    text, english_only = m["text"], lang != "en"
                text = text.replace("{n}", "…")
                words = m.get(lang) or m["en"]
                means = md_inline(links(env.from_string(words["means"]).render(**ctx)))
                do = md_inline(links(env.from_string(words["do"]).render(**ctx)))
                en_text = (APP["en"].get(m["key"]) if "key" in m else m["text"]) or ""
                search = " ".join([m["id"], text, en_text, re.sub("<[^>]+>", "", means), re.sub("<[^>]+>", "", do)])
                return dict(id=m["id"], group=m["group"], text=text, english_only=english_only,
                            means=means, do=do, search=search.replace('"', "&quot;"), card=m.get("card", False))

            msgs = [message(m) for m in MESSAGES]
            groups = []
            for m in msgs:
                if not groups or groups[-1]["name"] != m["group"]:
                    groups.append({"name": m["group"], "msgs": []})
                groups[-1]["msgs"].append(m)

            card_tasks = [{"title": titles[q["slug"]]["title"], "steps": steps_by_slug.get(q["slug"], [])}
                          for q in group_pages if q["kind"] == "task"] if kind == "card" else []

            html = env.get_template("page.html").render(
                lang=lang, langs=LANGS, lang_names=LANG_NAMES, lang_short=LANG_SHORT, ui=ui, app=app, slug=slug, kind=kind, role=role,
                page=meta, body=body_html, root=root, url=url, parent=parent, next=nxt, children=children,
                message_groups=groups, card_tasks=card_tasks, card_messages=[m for m in msgs if m["card"]],
                checked_date=fmt_date(CHECKED["checked"], lang), support_email=SUPPORT_EMAIL)
            if lang == "ar":  # keep "121 Scan" in left-to-right order inside Arabic text
                html = html.replace("121 Scan", "\u2066121 Scan\u2069")
            out = SITE / lang / f"{slug}.html"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(html, encoding="utf-8")

    # Assets, language chooser, marker
    shutil.copytree(ROOT / "assets", SITE / "assets")
    (SITE / "checked.json").write_text(json.dumps(CHECKED) + "\n", encoding="utf-8")
    (SITE / ".nojekyll").write_text("")
    (SITE / "index.html").write_text(f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>121 Scan help</title><link rel="icon" type="image/png" href="assets/favicon.png">
<script>
(function () {{
  var langs = {json.dumps(LANGS)}, pick = null;
  try {{ pick = localStorage.getItem("guide-lang"); }} catch (e) {{}}
  if (langs.indexOf(pick) < 0) {{
    pick = (navigator.languages || [navigator.language || "en"]).map(function (l) {{ return l.slice(0, 2); }})
      .filter(function (l) {{ return langs.indexOf(l) >= 0; }})[0] || "en";
  }}
  location.replace(pick + "/index.html" + location.hash);
}})();
</script></head>
<body>{"".join(f'<p><a href="{l}/index.html">{LANG_NAMES[l]}</a></p>' for l in LANGS)}</body></html>
""", encoding="utf-8")

    lines = ["# Screenshots to take", "",
             "Take each on the demo instance with the app in the language shown. Crop to the part of",
             "the screen that matters (roughly 16:10, at least 600 px wide) and mark the button to tap.",
             "Save as `assets/screens/<language>/<name>.png`. Slots already filled are not listed.", ""]
    for lang, slug, shot, desc in sorted(set(needed)):
        lines.append(f"- `{lang}/{shot}.png` ({slug}): {desc}")
    (ROOT / "screens-needed.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    n = sum(1 for _ in SITE.rglob("*.html")) - 1
    print(f"Built {n} pages in {len(LANGS)} languages; {len(set(needed))} screenshot slots to fill.")
    if preview:
        build_preview()


def build_preview():
    """All pages in one self-contained file, with links handled in the page."""
    css = (ROOT / "assets/site.css").read_text(encoding="utf-8")
    js = (ROOT / "assets/site.js").read_text(encoding="utf-8")
    icon = "data:image/png;base64," + base64.b64encode((ROOT / "assets/icon-96.png").read_bytes()).decode()
    templates = []
    for lang in LANGS:
        for p in PAGES["pages"]:
            path = f"{lang}/{p['slug']}.html"
            html = (SITE / path).read_text(encoding="utf-8")
            title = re.search(r"<title>(.*?)</title>", html, re.S).group(1)
            cls = re.search(r'<body class="([^"]*)"', html).group(1)
            body = re.search(r"<body[^>]*>(.*)</body>", html, re.S).group(1)
            body = re.sub(r'<script src="[^"]*site\.js"></script>', "", body)
            body = re.sub(r'src="[./]*assets/icon-96\.png"', f'src="{icon}"', body)
            # The preview is one file, so screenshots go inside it too.
            body = re.sub(r'<a href="[./]*assets/screens/[^"]+\.png" target="_blank" rel="noopener">(.*?)</a>', r"\1", body)
            body = re.sub(r'src="[./]*(assets/screens/[^"]+\.png)"',
                          lambda m: 'src="data:image/png;base64,'
                          + base64.b64encode((ROOT / m.group(1)).read_bytes()).decode() + '"', body)
            templates.append(f'<template data-path="{path}" data-lang="{lang}" data-dir="{"rtl" if lang == "ar" else "ltr"}" '
                             f'data-class="{cls}" data-title="{title}">{body}</template>')
    router = """
(function () {
  var T = {}, BY_ID = {}, current = null;
  Array.prototype.forEach.call(document.querySelectorAll("template[data-path]"), function (t) {
    T[t.dataset.path] = t; BY_ID[id(t.dataset.path)] = t.dataset.path;
  });
  function id(p) { return p.replace(/\\.html$/, "").replace(/[^a-z0-9]+/gi, "-"); }
  function show(path, frag, query) {
    if (!T[path]) path = "en/index.html";
    var t = T[path], app = document.getElementById("app");
    document.documentElement.lang = t.dataset.lang;
    document.documentElement.dir = t.dataset.dir;
    document.title = t.dataset.title;
    document.body.className = t.dataset.class;
    app.replaceChildren(t.content.cloneNode(true));
    current = path;
    window.Guide.init(app, query || "");
    if (location.hash.slice(1) !== id(path)) location.hash = id(path);
    var target = frag && document.getElementById(frag);
    if (target) { target.scrollIntoView(); target.classList.add("is-target"); } else window.scrollTo(0, 0);
  }
  function resolve(href) { var u = new URL(href, "https://guide.local/" + current); return [u.pathname.slice(1), u.hash.slice(1)]; }
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a[href]");
    if (!a) return;
    var href = a.getAttribute("href");
    if (/^(https?:|mailto:|#)/.test(href)) return;
    e.preventDefault();
    var r = resolve(href); show(r[0], r[1]);
  });
  document.addEventListener("submit", function (e) {
    var f = e.target; if (!f.getAttribute("action")) return;
    e.preventDefault();
    var q = f.querySelector("input[name=q]");
    show(resolve(f.getAttribute("action"))[0], "", q ? q.value : "");
  });
  window.addEventListener("hashchange", function () {
    var p = BY_ID[location.hash.slice(1)]; if (p && p !== current) show(p);
  });
  var start = BY_ID[location.hash.slice(1)];
  if (!start) {
    var pick = null; try { pick = localStorage.getItem("guide-lang"); } catch (e) {}
    if (!T[pick + "/index.html"]) pick = (navigator.language || "en").slice(0, 2);
    start = T[pick + "/index.html"] ? pick + "/index.html" : "en/index.html";
  }
  show(start);
})();
"""
    page = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>121 Scan help</title>
<style>{css}
.msg.is-target {{ border-color: var(--accent); box-shadow: 0 0 0 2px var(--accent); }}</style>
</head><body>
<div id="app"></div>
{"".join(templates)}
<script>window.GUIDE_PREVIEW = true;</script>
<script>{js}</script>
<script>{router}</script>
</body></html>
"""
    out = ROOT / "preview.html"
    out.write_text(page, encoding="utf-8")
    print(f"Preview: {out.name} ({out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    build(preview="--preview" in sys.argv)
