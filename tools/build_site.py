"""Bouwt de tweetalige wiki-website (NL + EN) in docs/ voor GitHub Pages, inclusief SEO.

Gebruik:  python3 tools/build_site.py        (eerst build_wiki.py en build_en.py draaien)
Vereist:  pip install markdown pillow
"""
import os, re, json, shutil, html, subprocess, datetime
import markdown

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DOCS = os.path.join(ROOT, "docs")
SITE = "https://lrvdlinden.github.io/app.lrvdlinen.claudwiki/"
GH_USER = "https://github.com/LRvdLinden"
MD_EXT = ["tables", "fenced_code", "md_in_html", "sane_lists", "attr_list"]

UI = {
 "nl": dict(tag="onofficiële NL-gids", search="Zoek in de wiki…", searchlab="Zoeken", adv="Skill-adviseur", prev="Vorige", next="Volgende",
            menu="Menu", nav="Navigatie", foot="Onofficiële wiki door LRvdLinden · Claude is een product van Anthropic", src="Bron op GitHub",
            other="English", otherlang="en", ask="Vraag de Skill-adviseur →", asksub="Beschrijf wat je wilt en krijg de beste skill",
            site_desc="Onofficiële Nederlandstalige gids over Claude-skills: uitleg, voorbeelden en installatie per skill.", locale="nl_NL", home="Home",
            og_alt="Claude Wiki – {t}"),
 "en": dict(tag="unofficial guide", search="Search the wiki…", searchlab="Search", adv="Skill adviser", prev="Previous", next="Next",
            menu="Menu", nav="Navigation", foot="Unofficial wiki by LRvdLinden · Claude is a product of Anthropic", src="Source on GitHub",
            other="Nederlands", otherlang="nl", ask="Ask the Skill adviser →", asksub="Describe what you want and get the best skill",
            site_desc="Unofficial guide to Claude skills: explanations, examples and installation for every skill.", locale="en_US", home="Home",
            og_alt="Claude Wiki – {t}"),
}

def git_date(path):
    try:
        d = subprocess.run(["git", "-C", ROOT, "log", "-1", "--format=%cs", "--", path], capture_output=True, text=True).stdout.strip()
        return d or datetime.date.today().isoformat()
    except Exception:
        return datetime.date.today().isoformat()

def out_path(md_path):
    p = md_path[:-3]
    if p.endswith("README"): p = p[:-6] + "index"
    return p + ".html"

def canon_rel(md_path):
    o = out_path(md_path)
    return o[:-10] if o.endswith("index.html") else o   # map/  i.p.v. map/index.html

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
def md(text): return markdown.markdown(text, extensions=MD_EXT, output_format="html")

def fix_links(h, asset_prefix):
    def rep(m):
        attr, url = m.group(1), m.group(2)
        if re.match(r"^(https?:|mailto:|#|data:)", url): return m.group(0)
        if ".gitbook/assets/" in url:
            return f'{attr}="{asset_prefix}assets/{url.split(".gitbook/assets/")[1]}"'
        u, frag = (url.split("#", 1) + [""])[:2]
        if u.endswith(".md"):
            u = u[:-3]
            if u.endswith("README"): u = u[:-6] + "index"
            u += ".html"
        return f'{attr}="{u}{"#" + frag if frag else ""}"'
    return re.sub(r'(href|src)="([^"]+)"', rep, h)

def gb_blocks(t):
    t = re.sub(r'\{% code title="([^"]*)"[^%]*%\}\n(```.*?```)\n\{% endcode %\}',
               lambda m: keep(f'<figure class="code"><figcaption>{html.escape(m.group(1))}</figcaption>{md(m.group(2))}</figure>'), t, flags=re.S)
    t = re.sub(r'\{% embed url="([^"]+)" %\}\n?(.*?)\n?\{% endembed %\}',
               lambda m: keep(f'<a class="embed" href="{m.group(1)}" target="_blank" rel="noopener"><span class="embed-k">↗</span><strong>{html.escape(m.group(2).strip() or m.group(1))}</strong><span class="embed-u">{html.escape(m.group(1))}</span></a>'), t, flags=re.S)
    def stepper(m):
        steps = re.findall(r"\{% step %\}\n?(.*?)\{% endstep %\}", m.group(1), re.S)
        return keep('<ol class="stepper">' + "".join(f"<li>{render(s)}</li>" for s in steps) + "</ol>")
    t = re.sub(r"\{% stepper %\}(.*?)\{% endstepper %\}", stepper, t, flags=re.S)
    def tabs(m):
        items = re.findall(r'\{% tab title="([^"]*)" %\}\n?(.*?)\{% endtab %\}', m.group(1), re.S)
        head = "".join(f'<button role="tab" aria-selected="{"true" if i == 0 else "false"}">{html.escape(ti)}</button>' for i, (ti, _) in enumerate(items))
        panes = "".join(f'<div class="pane" role="tabpanel"{"" if i == 0 else " hidden"}>{render(b)}</div>' for i, (_, b) in enumerate(items))
        return keep(f'<div class="tabs"><div class="tablist" role="tablist">{head}</div>{panes}</div>')
    t = re.sub(r"\{% tabs %\}(.*?)\{% endtabs %\}", tabs, t, flags=re.S)
    ICON = {"info": "i", "success": "✓", "warning": "!", "danger": "★"}
    t = re.sub(r'\{% hint style="(\w+)" %\}\n?(.*?)\{% endhint %\}',
               lambda m: keep(f'<aside class="hint {m.group(1)}"><span class="hint-i" aria-hidden="true">{ICON.get(m.group(1), "i")}</span><div>{render(m.group(2))}</div></aside>'), t, flags=re.S)
    def cards(m):
        rows = re.findall(r"<tr><td><strong>(.*?)</strong></td><td>(.*?)</td><td><a href=\"([^\"]+)\">.*?</a></td><td>(.*?)</td></tr>", m.group(0), re.S)
        out = []
        for ti, tx, href, cov in rows:
            c = re.search(r'href="([^"]+)"', cov)
            img = f'<img src="{c.group(1)}" alt="" width="1990" height="480" loading="lazy" decoding="async">' if c else ""
            out.append(f'<a class="card" href="{href}">{img}<strong>{ti}</strong><span>{tx}</span></a>')
        return keep('<div class="cards">' + "".join(out) + "</div>")
    t = re.sub(r'<table data-view="cards">.*?</table>', cards, t, flags=re.S)
    t = re.sub(r'<a href="([^"]+)" class="button (primary|secondary)" data-icon="[^"]*">(.*?)</a>', r'<a href="\1" class="btn \2">\3</a>', t)
    return t.replace("- [ ] ", "- ☐ ")

def render(t):
    t = gb_blocks(t); h = md(t)
    for _ in range(4):
        for k, v in list(TOK.items()):
            h = h.replace(f"<p>{k}</p>", v).replace(k, v)
    return h

def nav(src_root):
    items = []
    for line in open(os.path.join(src_root, "SUMMARY.md"), encoding="utf-8").read().splitlines():
        g = re.match(r"^## (.+)", line)
        if g: items.append(("group", g.group(1), None, 0)); continue
        m = re.match(r"^(\s*)\* \[(.+?)\]\((.+?)\)", line)
        if m: items.append(("item", m.group(2), m.group(3), len(m.group(1)) // 2))
    return items

def href_for(link, prefix):
    return prefix + ("adviseur/" if link == "adviseur/README.md" else out_path(link))

def nav_html(NAV, current, prefix):
    cur_parent, last_top = None, None
    for kind, title, link, lvl in NAV:
        if kind == "item" and lvl == 0: last_top = link
        if kind == "item" and link == current: cur_parent = last_top if lvl else link
    out, open_sub, last_top = [], False, None
    for kind, title, link, lvl in NAV:
        if kind == "group":
            if open_sub: out.append("</ul>"); open_sub = False
            out.append(f'<p class="nav-g">{html.escape(title)}</p>'); continue
        if lvl == 0:
            if open_sub: out.append("</ul>"); open_sub = False
            last_top = link
        if lvl == 1 and last_top != cur_parent: continue
        if lvl == 1 and not open_sub: out.append('<ul class="sub">'); open_sub = True
        on = link == current
        out.append(f'<a href="{href_for(link, prefix)}"{" class=\"on\" aria-current=\"page\"" if on else ""}>{html.escape(title)}</a>')
    if open_sub: out.append("</ul>")
    return "\n".join(out)

def section(md_path):
    p = md_path.split("/")
    if p[0] == "skills" and len(p) > 2: return p[1]
    return {"basis": "basis", "gespot-op-social": "social", "bronnen": "bronnen", "catalogus": "catalogus", "adviseur": "adviseur"}.get(p[0], "home")

def clip(s, n):
    s = " ".join(s.split())
    if len(s) <= n: return s
    cut = s[:n - 1].rsplit(" ", 1)[0].rstrip(",.;:")
    return cut + "…"

CSS = open(os.path.join(HERE, "site.css"), encoding="utf-8").read()
MARK = open(os.path.join(ROOT, ".gitbook/assets/mark.svg"), encoding="utf-8").read().replace('width="128" height="128"', 'width="34" height="34" aria-hidden="true"')

def lang_script(lang, other_url):
    # NL-pagina's: buiten Nederland (tijdzone én browsertaal) automatisch naar EN; een eigen keuze wint altijd.
    if lang == "nl":
        cond = "c==='en'||(!c&&!nl())"
    else:
        cond = "c==='nl'"
    return ("<script>(function(){var c=null;try{c=localStorage.getItem('cw-lang')}catch(e){}"
            "if(/bot|crawl|spider|slurp|preview|facebookexternalhit|linkedin|whatsapp|telegram|discord|lighthouse/i.test(navigator.userAgent))return;"
            "function nl(){var z='';try{z=Intl.DateTimeFormat().resolvedOptions().timeZone||''}catch(e){}"
            "var l=((navigator.languages||[]).join(',')||navigator.language||'').toLowerCase();"
            "return z==='Europe/Amsterdam'||/(^|,)nl/.test(l)}"
            f"if({cond})location.replace('{other_url}'+location.search+location.hash)}})();</script>")

def head(lang, title, desc, canon, alt_nl, alt_en, og_img, og_alt, ldjson, asset_prefix, extra=""):
    U = UI[lang]
    other = alt_en if lang == "nl" else alt_nl
    return f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="nl" href="{alt_nl}"><link rel="alternate" hreflang="en" href="{alt_en}"><link rel="alternate" hreflang="x-default" href="{alt_en}">
<meta name="theme-color" content="#FAF9F5" media="(prefers-color-scheme: light)"><meta name="theme-color" content="#141413" media="(prefers-color-scheme: dark)">
<link rel="icon" href="{asset_prefix}favicon.ico" sizes="32x32"><link rel="icon" href="{asset_prefix}assets/mark.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{asset_prefix}apple-touch-icon.png"><link rel="manifest" href="{asset_prefix}site.webmanifest">
<meta property="og:type" content="website"><meta property="og:site_name" content="Claude Wiki">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canon}"><meta property="og:locale" content="{U['locale']}"><meta property="og:locale:alternate" content="{UI[U['otherlang']]['locale']}">
<meta property="og:image" content="{og_img}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:type" content="image/png"><meta property="og:image:alt" content="{html.escape(og_alt)}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{html.escape(title)}">
<meta name="twitter:description" content="{html.escape(desc)}"><meta name="twitter:image" content="{og_img}"><meta name="twitter:image:alt" content="{html.escape(og_alt)}">
{lang_script(lang, other)}
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700&family=Lora:ital,wght@0,400;0,600;1,400&family=JetBrains+Mono:wght@500&display=swap">
<script type="application/ld+json">{json.dumps(ldjson, ensure_ascii=False)}</script>
{extra}</head>"""

def build_lang(lang):
    src_root = ROOT if lang == "nl" else os.path.join(ROOT, "en")
    out_root = DOCS if lang == "nl" else os.path.join(DOCS, "en")
    U = UI[lang]
    NAV = nav(src_root)
    ORDER = [i[2] for i in NAV if i[0] == "item"]
    lang_base = SITE + ("" if lang == "nl" else "en/")
    pages, index = [], []
    TITLES = {i[2]: i[1] for i in NAV if i[0] == "item"}
    parents, last = {}, None
    for kind, title, link, lvl in NAV:
        if kind == "item" and lvl == 0: last = link
        elif kind == "item": parents[link] = last
    for md_path in ORDER:
        if md_path == "adviseur/README.md": continue
        TOK.clear()
        src = os.path.join(src_root, md_path)
        meta, body = frontmatter(open(src, encoding="utf-8").read())
        title = (re.search(r"^# (.+)$", body, re.M) or [None, "Claude Wiki"])[1]
        depth = out_path(md_path).count("/")
        prefix = "../" * depth
        asset_prefix = prefix + ("" if lang == "nl" else "../")
        h = fix_links(render(body), asset_prefix)
        desc = clip(meta.get("description") or U["site_desc"], 158)
        full_title = clip(title if md_path == "README.md" else f"{title} | Claude Wiki", 70)
        if md_path == "README.md": full_title = "Claude Wiki – " + ("Claude-skills uitgelegd" if lang == "nl" else "Claude skills explained")
        rel = canon_rel(md_path)
        canon = lang_base + rel
        alt_nl, alt_en = SITE + rel, SITE + "en/" + rel
        sec = section(md_path)
        og_img = f"{SITE}og/{sec}-{lang}.png"
        # JSON-LD
        crumbs = [{"@type": "ListItem", "position": 1, "name": U["home"], "item": lang_base}]
        if md_path in parents and parents[md_path]:
            pp = parents[md_path]; crumbs.append({"@type": "ListItem", "position": 2, "name": TITLES[pp], "item": lang_base + canon_rel(pp)})
        if md_path != "README.md": crumbs.append({"@type": "ListItem", "position": len(crumbs) + 1, "name": title, "item": canon})
        graph = [{"@type": "WebPage", "@id": canon, "url": canon, "name": title, "description": desc, "inLanguage": lang,
                  "isPartOf": {"@id": SITE + "#website"}, "primaryImageOfPage": og_img, "dateModified": git_date(src)}]
        if len(crumbs) > 1: graph.append({"@type": "BreadcrumbList", "itemListElement": crumbs})
        if md_path == "README.md":
            graph.append({"@type": "WebSite", "@id": SITE + "#website", "url": lang_base, "name": "Claude Wiki", "description": U["site_desc"],
                          "inLanguage": lang, "publisher": {"@id": SITE + "#author"},
                          "potentialAction": {"@type": "SearchAction", "target": {"@type": "EntryPoint", "urlTemplate": lang_base + "adviseur/?q={search_term_string}"},
                                              "query-input": "required name=search_term_string"}})
            graph.append({"@type": "Person", "@id": SITE + "#author", "name": "LRvdLinden", "url": GH_USER, "sameAs": [GH_USER],
                          "image": SITE + "assets/mark.png"})
        if md_path == "bronnen/faq.md":
            qa = re.findall(r"<summary>(.*?)</summary>\s*(.*?)</details>", body, re.S)
            graph.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q.strip(),
                          "acceptedAnswer": {"@type": "Answer", "text": " ".join(re.sub(r"[`*]", "", a).split())}} for q, a in qa]})
        ld = {"@context": "https://schema.org", "@graph": graph}
        cover = ""
        if meta.get("cover"):
            cover = f'<img class="cover{" hero" if meta.get("hero") else ""}" src="{asset_prefix}assets/{os.path.basename(meta["cover"])}" alt="" width="1990" height="480" fetchpriority="high">'
        i = ORDER.index(md_path)
        def pl(j, lab):
            if 0 <= j < len(ORDER):
                l = ORDER[j]
                return f'<a href="{href_for(l, prefix)}"><small>{lab}</small>{html.escape(TITLES[l])}</a>'
            return "<span></span>"
        lead = f'<p class="lead">{html.escape(meta["description"])}</p>' if meta.get("description") else ""
        if lead: h = re.sub(r"(</h1>)", lambda m: m.group(1) + lead, h, count=1)
        other_href = ("../" * depth) + ("en/" if lang == "nl" else "../") + out_path(md_path)
        page = head(lang, full_title, desc, canon, alt_nl, alt_en, og_img, U["og_alt"].format(t=title), ld, asset_prefix, f"<style>{CSS}</style>") + f"""<body>
<header class="top"><button class="menu" aria-label="{U['menu']}" aria-expanded="false">☰</button>
<a class="brand" href="{prefix}index.html">{MARK}<span>Claude Wiki<small>{U['tag']}</small></span></a>
<form class="search" role="search"><input id="s" type="search" placeholder="{U['search']}" autocomplete="off" aria-label="{U['searchlab']}"><div class="sres" hidden></div></form>
<a class="lang" href="{other_href}" hreflang="{U['otherlang']}" lang="{U['otherlang']}" data-lang="{U['otherlang']}">{U['otherlang'].upper()}<span> · {U['other']}</span></a>
<a class="adv" href="{prefix}adviseur/">{U['adv']}</a></header>
<div class="layout"><nav class="side" aria-label="{U['nav']}">{nav_html(NAV, md_path, prefix)}</nav>
<main>{cover}<article>{h}</article><nav class="pager">{pl(i - 1, U['prev'])}{pl(i + 1, U['next'])}</nav>
<footer>{U['foot']} · <a href="https://github.com/LRvdLinden/app.lrvdlinen.claudwiki">{U['src']}</a></footer></main></div>
<script>window.PREFIX="{prefix}";window.UI={json.dumps({"ask": U["ask"], "asksub": U["asksub"]}, ensure_ascii=False)};</script><script src="{asset_prefix}site.js" defer></script></body></html>"""
        dest = os.path.join(out_root, out_path(md_path))
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, "w", encoding="utf-8").write(page)
        plain = " ".join(re.sub(r"<[^>]+>", " ", h).split())
        index.append({"t": title, "d": meta.get("description", ""), "u": out_path(md_path), "x": plain[:1500]})
        pages.append((rel, git_date(src)))
    json.dump(index, open(os.path.join(out_root, "search.json"), "w", encoding="utf-8"), ensure_ascii=False)
    build_adviseur(lang, out_root)
    return pages

ADV_EN = [
 ('Vertel in gewone taal wat je wilt doen. De adviseur zoekt in <strong id="total">alle</strong> skills en plugins de beste opties, met waar ze werken en hoe je ze installeert.',
  'Describe in plain language what you want to do. The adviser searches <strong id="total">all</strong> skills and plugins for the best options, with where they work and how to install them.'),
 ('aria-label="Zoeken"', 'aria-label="Search"'), ('>Wat wil je met Claude doen?<', '>What do you want to do with Claude?<'),
 ('placeholder="Bijv. ‘Ik wil van mijn notulen een nette nieuwsbrief maken’"', 'placeholder="E.g. ‘Turn my meeting notes into a tidy newsletter’"'),
 ('aria-label="Waar gebruik je Claude?"', 'aria-label="Where do you use Claude?"'), ('>Overal<', '>Everywhere<'), ('>Claude-app<', '>Claude app<'),
 ('> Ook marketplace-plugins<', '> Include marketplace plugins<'), ('Vraag Claude om persoonlijk advies', 'Ask Claude for personal advice'),
 ('>Claude leest je vraag en de beste kandidaten en legt uit welke je moet nemen.<', '>Claude reads your question and the best candidates and explains which one to pick.<'),
 ('>Advies van Claude<', '>Advice from Claude<'), ('Populair om mee te beginnen', 'Popular to start with'),
 ('>Onofficiële wiki door LRvdLinden · Claude is een product van Anthropic<', '>Unofficial wiki by LRvdLinden · Claude is a product of Anthropic<'),
 ('>Naar de wiki<', '>Back to the wiki<'), ('>Bron op GitHub<', '>Source on GitHub<'), ("'top 12 van '", "'top 12 of '"), ("' gevonden'", "' found'"),
 ('Niets gevonden. Probeer andere woorden, zet de filters op ‘Overal’, of maak je eigen skill met <strong>Skill Creator</strong>.',
  'Nothing found. Try other words, set the filter to ‘Everywhere’, or make your own skill with <strong>Skill Creator</strong>.'),
 ('>Beste keuze<', '>Best pick<'), ('>Officieel<', '>Official<'), ('>Officiële marketplace<', '>Official marketplace<'),
 ('Werkt in: ', 'Works in: '), ('Past bij: ', 'Matches: '), ('>Kopieer<', '>Copy<'), ("'Gekopieerd'", "'Copied'"), ("'Kopieer'", "'Copy'"), ("'Geselecteerd'", "'Selected'"),
 ("'Beste opties voor jou'", "'Best options for you'"), ("'Advies van Claude, daarna overige opties'", "'Claude’s advice, then other options'"),
 ("'Claude denkt na…'", "'Claude is thinking…'"),
 ("'Even te veel vragen achter elkaar. Probeer het over een minuut opnieuw.'", "'Too many questions in a row. Try again in a minute.'"),
 ("'Advies vragen lukte nu niet. De lijst hieronder is wel bijgewerkt.'", "'Asking for advice didn’t work right now. The list below has been updated.'"),
 ("const EX=['Ik wil video’s maken voor Instagram','Mijn teksten klinken te veel als AI','Ik bouw een iPhone-app in SwiftUI','Een presentatie maken voor de vergadering','Facturen ordenen voor de belasting','Claude moet eerlijk tegenspreken','Website die er professioneel uitziet','Claude moet dingen onthouden'];",
  "const EX=['I want to make videos for Instagram','My writing sounds too much like AI','I am building an iPhone app in SwiftUI','Make a presentation for a meeting','Organise invoices for my taxes','Claude should push back honestly','A website that looks professional','Claude should remember things'];"),
 ("'de Claude-app'", "'the Claude app'"), ("'nog onbekend'", "'unknown'"),
 ("Je bent de Skill-adviseur van een Nederlandstalige wiki over Claude-skills.", "You are the Skill adviser of a wiki about Claude skills."),
 ("2-4 zinnen in het Nederlands, direct en concreet", "2-4 sentences in English, direct and concrete"),
 ('Claude Wiki · onofficiële gids', 'Claude Wiki · unofficial guide'), ('>Skill-adviseur</h1>', '>Skill adviser</h1>'),
]

def build_adviseur(lang, out_root):
    tpl = open(os.path.join(HERE, "adviseur_template.html"), encoding="utf-8").read()
    data = json.load(open(os.path.join(HERE, f"adv_{lang}.json"), encoding="utf-8"))
    body = tpl.replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")).replace("__WIKI_BASE__", "../").replace("__HOME__", "../index.html")
    if lang == "en":
        for a, b in ADV_EN:
            if a not in body: print("ADV_EN niet gevonden:", a[:60])
            body = body.replace(a, b)
    # head-onderdelen uit de artifact-template halen
    body = re.sub(r"^<title>.*?</title>\n<meta name=\"claude:viewport-fit-sides\"[^>]*>\n<link rel=\"preconnect\"[^>]*>\n<link rel=\"stylesheet\"[^>]*>\n", "", body, flags=re.S)
    U = UI[lang]
    t = "Skill-adviseur – vind de beste Claude-skill" if lang == "nl" else "Skill adviser – find the best Claude skill"
    d = ("Beschrijf wat je met Claude wilt doen en krijg direct de best passende skill of plugin, met installatiecommando."
         if lang == "nl" else "Describe what you want to do with Claude and instantly get the best-fitting skill or plugin, with its install command.")
    canon = SITE + ("" if lang == "nl" else "en/") + "adviseur/"
    ld = {"@context": "https://schema.org", "@type": "WebApplication", "name": U["adv"], "url": canon, "description": d, "inLanguage": lang,
          "applicationCategory": "UtilitiesApplication", "operatingSystem": "Web", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"},
          "isPartOf": {"@id": SITE + "#website"}}
    ap = "../" if lang == "nl" else "../../"
    page = head(lang, t, d, canon, SITE + "adviseur/", SITE + "en/adviseur/", f"{SITE}og/adviseur-{lang}.png", U["og_alt"].format(t=U["adv"]), ld, ap,
                '<style>[hidden]{display:none!important}</style>') + "<body>" + body + "</body></html>"
    other = "../en/adviseur/" if lang == "nl" else "../../adviseur/"
    ol = U["otherlang"]
    page = page.replace("</footer>", f'<a href="{other}" hreflang="{ol}" lang="{ol}" onclick="try{{localStorage.setItem(\'cw-lang\',\'{ol}\')}}catch(e){{}}">{U["other"]}</a></footer>', 1)
    os.makedirs(os.path.join(out_root, "adviseur"), exist_ok=True)
    open(os.path.join(out_root, "adviseur", "index.html"), "w", encoding="utf-8").write(page)

def icons():
    from PIL import Image
    src = Image.open(os.path.join(ROOT, ".gitbook/assets/mark.png")).convert("RGBA")
    src.resize((180, 180), Image.LANCZOS).save(os.path.join(DOCS, "apple-touch-icon.png"))
    src.resize((192, 192), Image.LANCZOS).save(os.path.join(DOCS, "icon-192.png"))
    src.resize((512, 512), Image.LANCZOS).save(os.path.join(DOCS, "icon-512.png"))
    src.save(os.path.join(DOCS, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
    json.dump({"name": "Claude Wiki", "short_name": "Claude Wiki", "lang": "nl", "start_url": "./", "scope": "./", "display": "standalone",
               "background_color": "#FAF9F5", "theme_color": "#D97757",
               "icons": [{"src": "icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"}]},
              open(os.path.join(DOCS, "site.webmanifest"), "w"), indent=1)

def main():
    for name in os.listdir(DOCS) if os.path.isdir(DOCS) else []:
        p = os.path.join(DOCS, name)
        shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    os.makedirs(os.path.join(DOCS, "assets"), exist_ok=True)
    for f in os.listdir(os.path.join(ROOT, ".gitbook/assets")):
        s = os.path.join(ROOT, ".gitbook/assets", f)
        if os.path.isfile(s): shutil.copy(s, os.path.join(DOCS, "assets", f))
    shutil.copytree(os.path.join(ROOT, ".gitbook/assets/og"), os.path.join(DOCS, "og"))
    shutil.copy(os.path.join(HERE, "site.js"), os.path.join(DOCS, "site.js"))
    open(os.path.join(DOCS, ".nojekyll"), "w").close()
    icons()
    nl = build_lang("nl"); en = dict(build_lang("en"))
    # sitemap met hreflang-alternates
    xs = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    nl.append(("adviseur/", git_date(os.path.join(HERE, "adviseur_template.html"))))
    en["adviseur/"] = nl[-1][1]
    for rel, d in nl:
        for lang, loc in (("nl", SITE + rel), ("en", SITE + "en/" + rel)):
            lm = d if lang == "nl" else en.get(rel, d)
            xs.append(f"<url><loc>{loc}</loc><lastmod>{lm}</lastmod>"
                      f'<xhtml:link rel="alternate" hreflang="nl" href="{SITE + rel}"/>'
                      f'<xhtml:link rel="alternate" hreflang="en" href="{SITE + "en/" + rel}"/>'
                      f'<xhtml:link rel="alternate" hreflang="x-default" href="{SITE + "en/" + rel}"/></url>')
    xs.append("</urlset>")
    open(os.path.join(DOCS, "sitemap.xml"), "w").write("\n".join(xs) + "\n")
    open(os.path.join(DOCS, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n")
    nf = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Page not found | Claude Wiki</title><meta name="robots" content="noindex"><link rel="icon" href="/app.lrvdlinen.claudwiki/favicon.ico">
<style>body{font:18px/1.6 Georgia,serif;background:#FAF9F5;color:#141413;display:grid;place-items:center;min-height:100vh;margin:0;padding:16px;text-align:center}
a{color:#C6613F;font-family:Arial,sans-serif;font-weight:600}h1{font-family:Arial,sans-serif}@media(prefers-color-scheme:dark){body{background:#141413;color:#F4F2EA}}</style></head>
<body><main><h1>404</h1><p>Deze pagina bestaat niet (meer). · This page doesn't exist (anymore).</p>
<p><a href="/app.lrvdlinen.claudwiki/">Naar de wiki</a> · <a href="/app.lrvdlinen.claudwiki/en/">Go to the wiki</a> · <a href="/app.lrvdlinen.claudwiki/adviseur/">Skill-adviseur</a></p></main></body></html>"""
    open(os.path.join(DOCS, "404.html"), "w").write(nf)
    print("NL:", len(nl), "EN:", len(en))

if __name__ == "__main__":
    main()
