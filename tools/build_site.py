"""Bouwt de wiki als statische website in docs/ (GitHub Pages).

Gebruik:  python3 tools/build_site.py
Vereist:  pip install markdown
Zet GitBook-blokken ({% hint %}, {% tabs %}, {% stepper %}, kaarten, ...) om naar HTML.
"""
import os, re, json, shutil, html
import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs")
SITE = "https://lrvdlinden.github.io/app.lrvdlinen.claudwiki/"
MD_EXT = ["tables", "fenced_code", "md_in_html", "sane_lists", "attr_list"]

# ───────── helpers ─────────
def read(p): return open(os.path.join(ROOT, p), encoding="utf-8").read()

def out_path(md_path):
    p = md_path[:-3]
    if p.endswith("README"): p = p[:-6] + "index"
    return p + ".html"

def frontmatter(t):
    m = re.match(r"---\n(.*?)\n---\n", t, re.S)
    if not m: return {}, t
    fm, body = m.group(1), t[m.end():]
    meta = {}
    d = re.search(r"description: >-\n\s+(.*?)\n(?=\w)", fm + "\nx", re.S)
    if d: meta["description"] = " ".join(d.group(1).split())
    for k in ("icon", "cover"):
        mm = re.search(rf"^{k}: (.*)$", fm, re.M)
        if mm: meta[k] = mm.group(1).strip()
    meta["hero"] = "size: hero" in fm
    return meta, body

TOK = {}
def keep(h):
    k = f"@@TOK{len(TOK)}@@"; TOK[k] = h; return f"\n\n{k}\n\n"

def md(text):
    return markdown.markdown(text, extensions=MD_EXT, output_format="html")

def fix_links(h, src_dir):
    def rep(m):
        attr, url = m.group(1), m.group(2)
        if re.match(r"^(https?:|mailto:|#|data:)", url): return m.group(0)
        u, frag = (url.split("#", 1) + [""])[:2]
        if u.endswith(".md"):
            u = u[:-3]
            if u.endswith("README"): u = u[:-6] + "index"
            u += ".html"
        elif u.endswith("/") or u == "":
            pass
        u = u.replace(".gitbook/assets/", "assets/")
        return f'{attr}="{u}{"#" + frag if frag else ""}"'
    return re.sub(r'(href|src)="([^"]+)"', rep, h)

def gb_blocks(t):
    # code-titel
    t = re.sub(r'\{% code title="([^"]*)"[^%]*%\}\n(```.*?```)\n\{% endcode %\}',
               lambda m: keep(f'<figure class="code"><figcaption>{html.escape(m.group(1))}</figcaption>{md(m.group(2))}</figure>'), t, flags=re.S)
    # embed
    t = re.sub(r'\{% embed url="([^"]+)" %\}\n?(.*?)\n?\{% endembed %\}',
               lambda m: keep(f'<a class="embed" href="{m.group(1)}" target="_blank" rel="noopener"><span class="embed-k">Bekijk</span><strong>{html.escape(m.group(2).strip() or m.group(1))}</strong><span class="embed-u">{html.escape(m.group(1))}</span></a>'), t, flags=re.S)
    # stepper
    def stepper(m):
        steps = re.findall(r"\{% step %\}\n?(.*?)\{% endstep %\}", m.group(1), re.S)
        return keep('<ol class="stepper">' + "".join(f"<li>{render(s)}</li>" for s in steps) + "</ol>")
    t = re.sub(r"\{% stepper %\}(.*?)\{% endstepper %\}", stepper, t, flags=re.S)
    # tabs
    def tabs(m):
        items = re.findall(r'\{% tab title="([^"]*)" %\}\n?(.*?)\{% endtab %\}', m.group(1), re.S)
        n = len(TOK)
        head = "".join(f'<button role="tab" aria-selected="{"true" if i == 0 else "false"}" data-i="{i}">{html.escape(ti)}</button>' for i, (ti, _) in enumerate(items))
        panes = "".join(f'<div class="pane" role="tabpanel"{"" if i == 0 else " hidden"}>{render(b)}</div>' for i, (_, b) in enumerate(items))
        return keep(f'<div class="tabs" id="t{n}"><div class="tablist" role="tablist">{head}</div>{panes}</div>')
    t = re.sub(r"\{% tabs %\}(.*?)\{% endtabs %\}", tabs, t, flags=re.S)
    # hints
    ICON = {"info": "i", "success": "✓", "warning": "!", "danger": "★"}
    t = re.sub(r'\{% hint style="(\w+)" %\}\n?(.*?)\{% endhint %\}',
               lambda m: keep(f'<aside class="hint {m.group(1)}"><span class="hint-i" aria-hidden="true">{ICON.get(m.group(1), "i")}</span><div>{render(m.group(2))}</div></aside>'), t, flags=re.S)
    # kaarten
    def cards(m):
        rows = re.findall(r"<tr><td><strong>(.*?)</strong></td><td>(.*?)</td><td><a href=\"([^\"]+)\">.*?</a></td><td>(.*?)</td></tr>", m.group(0), re.S)
        out = []
        for ti, tx, href, cov in rows:
            c = re.search(r'href="([^"]+)"', cov)
            img = f'<img src="{c.group(1)}" alt="" loading="lazy">' if c else ""
            out.append(f'<a class="card" href="{href}">{img}<strong>{ti}</strong><span>{tx}</span></a>')
        return keep('<div class="cards">' + "".join(out) + "</div>")
    t = re.sub(r'<table data-view="cards">.*?</table>', cards, t, flags=re.S)
    # knoppen
    t = re.sub(r'<a href="([^"]+)" class="button (primary|secondary)" data-icon="[^"]*">(.*?)</a>',
               r'<a href="\1" class="btn \2">\3</a>', t)
    t = t.replace("- [ ] ", "- ☐ ")
    return t

def render(t):
    t = gb_blocks(t)
    h = md(t)
    for _ in range(4):
        for k, v in list(TOK.items()):
            h = h.replace(f"<p>{k}</p>", v).replace(k, v)
    return h

# ───────── navigatie uit SUMMARY.md ─────────
def nav():
    items, group = [], None
    for line in read("SUMMARY.md").splitlines():
        g = re.match(r"^## (.+)", line)
        if g: group = g.group(1); items.append(("group", group, None, 0)); continue
        m = re.match(r"^(\s*)\* \[(.+?)\]\((.+?)\)", line)
        if m: items.append(("item", m.group(2), m.group(3), len(m.group(1)) // 2))
    return items

NAV = nav()
ORDER = [i[2] for i in NAV if i[0] == "item"]

def nav_html(current, prefix):
    out, open_sub, parent_active = [], False, False
    # bepaal ouder van huidige pagina
    cur_parent = None
    last_top = None
    for kind, title, link, lvl in NAV:
        if kind == "item" and lvl == 0: last_top = link
        if kind == "item" and link == current: cur_parent = last_top if lvl else link
    last_top = None
    for kind, title, link, lvl in NAV:
        if kind == "group":
            if open_sub: out.append("</ul>"); open_sub = False
            out.append(f'<p class="nav-g">{html.escape(title)}</p>')
            continue
        if lvl == 0:
            if open_sub: out.append("</ul>"); open_sub = False
            last_top = link
        if lvl == 1 and last_top != cur_parent: continue
        if lvl == 1 and not open_sub: out.append('<ul class="sub">'); open_sub = True
        cls = ' class="on"' if link == current else ""
        cur = ' aria-current="page"' if link == current else ""
        href = prefix + (out_path(link) if link != "adviseur/README.md" else "adviseur/")
        out.append(f'<a href="{href}"{cls}{cur}>{html.escape(title)}</a>')
    if open_sub: out.append("</ul>")
    return "\n".join(out)

CSS = open(os.path.join(ROOT, "tools", "site.css"), encoding="utf-8").read()
MARK = open(os.path.join(ROOT, ".gitbook/assets/mark.svg"), encoding="utf-8").read().replace('width="128" height="128"', 'width="34" height="34" aria-hidden="true"')

def page(md_path, title, meta, body_html, prefix):
    cover = ""
    if meta.get("cover"):
        src = prefix + "assets/" + os.path.basename(meta["cover"])
        cover = f'<img class="cover{" hero" if meta.get("hero") else ""}" src="{src}" alt="">'
    i = ORDER.index(md_path) if md_path in ORDER else -1
    def pl(j, lab):
        if 0 <= j < len(ORDER):
            l = ORDER[j]; t = next(x[1] for x in NAV if x[2] == l)
            href = prefix + (out_path(l) if l != "adviseur/README.md" else "adviseur/")
            return f'<a href="{href}"><small>{lab}</small>{html.escape(t)}</a>'
        return "<span></span>"
    pager = f'<nav class="pager">{pl(i - 1, "Vorige")}{pl(i + 1, "Volgende")}</nav>' if i >= 0 else ""
    desc = html.escape(meta.get("description", "Onofficiële Nederlandstalige gids over Claude-skills."))
    lead = f'<p class="lead">{desc}</p>' if meta.get("description") else ""
    return f"""<!doctype html><html lang="nl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{html.escape(title)} · Claude Wiki</title><meta name="description" content="{desc}">
<meta property="og:title" content="{html.escape(title)} · Claude Wiki"><meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}assets/{os.path.basename(meta.get('cover', 'cover-home.png'))}">
<link rel="icon" href="{prefix}assets/mark.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700&family=Lora:ital,wght@0,400;0,600;1,400&family=JetBrains+Mono:wght@500&display=swap">
<style>{CSS}</style></head><body>
<header class="top"><button class="menu" aria-label="Menu" aria-expanded="false">☰</button>
<a class="brand" href="{prefix}index.html">{MARK}<span>Claude Wiki<small>onofficiële NL-gids</small></span></a>
<form class="search" role="search"><input id="s" type="search" placeholder="Zoek in de wiki…" autocomplete="off" aria-label="Zoeken"><div class="sres" hidden></div></form>
<a class="adv" href="{prefix}adviseur/">Skill-adviseur</a></header>
<div class="layout"><nav class="side" aria-label="Navigatie">{nav_html(md_path, prefix)}</nav>
<main>{cover}<article>{lead_fix(body_html, lead)}</article>{pager}
<footer>Onofficiële wiki door LRvdLinden · Claude is een product van Anthropic · <a href="https://github.com/LRvdLinden/app.lrvdlinen.claudwiki">Bron op GitHub</a></footer></main></div>
<script>window.PREFIX="{prefix}";</script><script src="{prefix}site.js" defer></script></body></html>"""

def lead_fix(body, lead):
    # beschrijving direct onder de eerste h1
    return re.sub(r"(</h1>)", r"\1" + lead.replace("\\", "\\\\"), body, count=1) if lead else body

# ───────── bouwen ─────────
def main():
    keep_dirs = {"adviseur"}
    for name in os.listdir(OUT) if os.path.isdir(OUT) else []:
        p = os.path.join(OUT, name)
        if name in keep_dirs or name in (".nojekyll",): continue
        shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    for f in os.listdir(os.path.join(ROOT, ".gitbook/assets")):
        shutil.copy(os.path.join(ROOT, ".gitbook/assets", f), os.path.join(OUT, "assets", f))
    shutil.copy(os.path.join(ROOT, "tools", "site.js"), os.path.join(OUT, "site.js"))
    open(os.path.join(OUT, ".nojekyll"), "w").close()
    index = []
    for md_path in ORDER:
        if md_path == "adviseur/README.md": continue
        TOK.clear()
        meta, body = frontmatter(read(md_path))
        title = (re.search(r"^# (.+)$", body, re.M) or [None, "Claude Wiki"])[1]
        depth = out_path(md_path).count("/")
        prefix = "../" * depth
        h = fix_links(render(body), os.path.dirname(md_path))
        dest = os.path.join(OUT, out_path(md_path))
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, "w", encoding="utf-8").write(page(md_path, title, meta, h, prefix))
        plain = re.sub(r"<[^>]+>", " ", h)
        index.append({"t": title, "d": meta.get("description", ""), "u": out_path(md_path), "x": " ".join(plain.split())[:1500]})
    json.dump(index, open(os.path.join(OUT, "search.json"), "w", encoding="utf-8"), ensure_ascii=False)
    print("pagina's:", len(index))

if __name__ == "__main__":
    main()
