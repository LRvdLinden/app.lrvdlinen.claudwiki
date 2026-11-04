import os, sys, textwrap
from data import CATS, S
from install import tabs, tab, code

ROOT = sys.argv[1]
A = ".gitbook/assets"


def w(path, body):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(textwrap.dedent(body).lstrip() if body.startswith("\n") else body)


def rel(depth):
    return "../" * depth


def fm(icon, desc, cover=None, depth=0, hero=False):
    lines = ["---", f"description: >-\n  {desc}", f"icon: {icon}"]
    if cover:
        lines += [f"cover: {rel(depth)}{A}/cover-{cover}.png", "coverY: 0"]
        lines += ["layout:", "  cover:", "    visible: true", f"    size: {'hero' if hero else 'full'}",
                  "  title:", "    visible: true", "  description:", "    visible: true",
                  "  tableOfContents:", "    visible: true", "  outline:", "    visible: true",
                  "  pagination:", "    visible: true"]
    lines.append("---\n")
    return "\n".join(lines)


def cards(rows, depth):
    """rows: (titel, tekst, link, cover-slug|None)"""
    out = ['<table data-view="cards"><thead><tr><th></th><th></th>'
           '<th data-hidden data-card-target data-type="content-ref"></th>'
           '<th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody>']
    for t, txt, link, cov in rows:
        c = f'<a href="{rel(depth)}{A}/cover-{cov}.png">cover-{cov}.png</a>' if cov else ""
        out.append(f'<tr><td><strong>{t}</strong></td><td>{txt}</td><td><a href="{link}">{link}</a></td><td>{c}</td></tr>')
    out.append("</tbody></table>")
    return "\n".join(out)


CAT = {c[0]: c for c in CATS}

# ───────── skill pages ─────────
for s in S:
    p = f"skills/{s['cat']}/{s['slug']}.md"
    b = [fm(s["icon"], s["tagline"], s["cat"], 2), f"# {s['name']}\n"]
    if s.get("social"):
        b.append(f'{{% hint style="danger" %}}\n**Gespot op social.** {s["social"]}\n{{% endhint %}}\n')
    b.append(f"""| | |
| --- | --- |
| **Maker** | {s['maker']} |
| **Werkt in** | {s['werkt']} |
| **Kosten** | {s['prijs']} |
| **Bron** | [{s['bron'].replace('https://', '')}]({s['bron']}) |
""")
    b.append(f"## Wat doet het?\n\n{s['wat']}\n")
    b.append("## Wanneer gebruik je het?\n\n" + "\n".join(f"* {x}" for x in s["wanneer"]) + "\n")
    b.append("## Voorbeelden\n")
    for i, (prompt, res) in enumerate(s["voorbeelden"], 1):
        b.append(f'{{% code title="Voorbeeld {i}: wat je typt" overflow="wrap" %}}\n```\n{prompt}\n```\n{{% endcode %}}\n\n**Wat je krijgt:** {res}\n')
    b.append(f"## Installeren\n\n{s['install']}\n")
    if s["tips"]:
        b.append('{% hint style="success" %}\n**Tips**\n\n' + "\n".join(f"* {t}" for t in s["tips"]) + "\n{% endhint %}\n")
    b.append('{% hint style="warning" %}\nCommunity-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).\n{% endhint %}\n' if "Anthropic" not in s["maker"] else "")
    b.append(f'<a href="{s["bron"]}" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar {CAT[s["cat"]][1]}</a>\n')
    w(p, "\n".join(b))

# ───────── category index pages ─────────
for slug, title, icon, intro in CATS:
    items = [s for s in S if s["cat"] == slug]
    body = fm(icon, intro, slug, 2) + f"# {title}\n\n{intro}\n\n"
    body += cards([(s["name"], s["tagline"], f"{s['slug']}.md", None) for s in items], 2) + "\n\n"
    body += "## Snel overzicht\n\n| Skill | Werkt in | Maker |\n| --- | --- | --- |\n"
    body += "\n".join(f"| [{s['name']}]({s['slug']}.md) | {s['werkt']} | {s['maker']} |" for s in items) + "\n"
    w(f"skills/{slug}/README.md", body)

# ───────── skills overview ─────────
w("skills/README.md", fm("grid-2", "Alle skills in deze wiki, ingedeeld in categorieën.", "home", 1) + f"""# Alle skills

Hier vind je {len(S)} skills en skillpakketten, verdeeld over {len(CATS)} categorieën. Elke pagina legt uit **wat** de skill doet, **wanneer** je hem gebruikt, geeft **voorbeelden** en laat zien **hoe je hem installeert**.

{cards([(t, i, f"{s}/README.md", s) for s, t, ic, i in CATS], 1)}

{{% hint style="info" %}}
**Officieel of community?** Skills van Anthropic staan in [anthropics/skills](https://github.com/anthropics/skills) en de officiële marketplace. Al het andere komt uit de community: vaak geweldig, maar lees altijd even wat je installeert.
{{% endhint %}}
""")

# ───────── home ─────────
w("README.md", fm("house", "De Nederlandstalige gids voor Claude-skills: uitleg, voorbeelden en installatie per skill.", "home", 0, hero=True) + f"""# Welkom bij de Claude Wiki

**Skills maken Claude slimmer in precies het werk dat jij doet.** In deze wiki vind je {len(S)} uitgewerkte skills in {len(CATS)} categorieën plus een catalogus van alle plugins uit de officiële marketplace. We leggen in gewoon Nederlands uit wat skills zijn, hoe je ze installeert en welke skills de moeite waard zijn: van de officiële skills van Anthropic tot de toppers die influencers op Instagram en TikTok delen.

<a href="adviseur/README.md" class="button primary" data-icon="wand-magic-sparkles">Vind jouw skill</a> <a href="basis/wat-zijn-skills.md" class="button secondary" data-icon="rocket">Begin hier</a> <a href="skills/README.md" class="button secondary" data-icon="grid-2">Bekijk alle skills</a>

## Waar wil je beginnen?

{cards([
    ("Skill-adviseur", "Vertel wat je wilt doen en krijg direct de beste skill met installatiecommando.", "adviseur/README.md", "adviseur"),
    ("Wat zijn skills?", "In 5 minuten snappen hoe skills werken en waarom ze zo handig zijn.", "basis/wat-zijn-skills.md", "basis"),
    ("Installeren", "Stap voor stap: in de Claude-app, in Claude Code en via npx.", "basis/skills-installeren.md", "basis"),
    ("Gespot op social", "De skills die Bart Boonstra en andere creators aanraden.", "gespot-op-social/README.md", "social"),
    ("Plugin-catalogus", "Alle plugins uit de officiële Claude Code-marketplace op een rij.", "catalogus/README.md", "catalogus"),
    ("Zelf een skill maken", "Van idee tot werkende SKILL.md in een kwartier.", "basis/eigen-skill-maken.md", "bouwen"),
], 0)}

## Categorieën

{cards([(t, i, f"skills/{s}/README.md", s) for s, t, ic, i in CATS], 0)}

## Top 5 om mee te beginnen

| # | Skill | Waarom |
| --- | --- | --- |
| 1 | [Skill Creator](skills/bouwen/skill-creator.md) | Maak van je vaste werkwijze een eigen skill. |
| 2 | [Superpowers](skills/denken/superpowers.md) | Claude denkt en plant eerst, dan pas bouwen. |
| 3 | [UI UX Pro Max](skills/design/ui-ux-pro-max.md) | Alles wat Claude ontwerpt ziet er direct professioneel uit. |
| 4 | [Humanizer](skills/content/humanizer.md) | Teksten die niet meer naar AI klinken. |
| 5 | [Remotion](skills/creatief/remotion.md) | Video's en animaties maken met code. |

{{% hint style="info" %}}
**Onofficiële wiki.** Deze wiki is gemaakt door LRvdLinden en is niet verbonden aan Anthropic. Claude is een product van Anthropic. Informatie bijgewerkt in november 2026; skills veranderen snel, dus check bij twijfel de bron.
{{% endhint %}}
""")

# ───────── basis ─────────
w("basis/README.md", fm("graduation-cap", CAT and "Alles wat je moet weten voordat je je eerste skill installeert.", "basis", 1) + """# De basis

Nieuw met skills? Lees deze pagina's in volgorde.

{% stepper %}
{% step %}
### [Wat zijn skills?](wat-zijn-skills.md)
Het idee achter skills, en het verschil met plugins, MCP, projecten en CLAUDE.md.
{% endstep %}
{% step %}
### [Skills installeren](skills-installeren.md)
In de Claude-app, in Claude Code, via `npx skills` of handmatig.
{% endstep %}
{% step %}
### [Skills gebruiken](skills-gebruiken.md)
Automatisch laten afgaan of zelf aanroepen met een slash-commando.
{% endstep %}
{% step %}
### [Je eigen skill maken](eigen-skill-maken.md)
Een SKILL.md schrijven, testen en delen.
{% endstep %}
{% step %}
### [Veilig installeren](veiligheid.md)
Waar je op let bij skills van anderen.
{% endstep %}
{% endstepper %}
""")

w("basis/wat-zijn-skills.md", fm("lightbulb", "Skills zijn mappen met instructies, scripts en bestanden die Claude laadt wanneer ze nodig zijn.", "basis", 1) + """# Wat zijn skills?

Een **skill** is een map met instructies (en soms scripts en voorbeeldbestanden) die Claude leert hoe hij een bepaalde taak goed en steeds op dezelfde manier uitvoert. Denk aan een werkinstructie die je een nieuwe collega geeft: *zo maken wij een nieuwsbrief*, *zo ziet onze huisstijl eruit*, *zo test je deze app*.

Het slimme eraan: Claude laadt een skill **alleen als hij hem nodig heeft**. Van elke skill ziet Claude eerst alleen de naam en een korte beschrijving. Pas als je vraag erbij past, leest hij de volledige instructies. Daardoor kun je tientallen skills installeren zonder dat Claude trager of verwarder wordt.

## Hoe ziet een skill eruit?

```
mijn-skill/
├── SKILL.md          ← verplicht: beschrijving + instructies
├── voorbeelden/      ← optioneel: voorbeeldbestanden
└── scripts/          ← optioneel: scripts die Claude mag draaien
```

{% code title="SKILL.md" %}
```markdown
---
name: nieuwsbrief-wijkraad
description: Schrijft de maandelijkse nieuwsbrief van de wijkraad in onze vaste opbouw. Gebruik bij elke vraag om een nieuwsbrief, buurtupdate of mededeling aan bewoners.
---

# Nieuwsbrief wijkraad

1. Begin met een korte persoonlijke opening (max. 3 zinnen).
2. Daarna de vaste rubrieken: Nieuws, Agenda, Oproep, Contact.
3. Schrijf op B1-niveau, spreek de lezer aan met 'je'.
```
{% endcode %}

De **beschrijving** is het belangrijkste: daarop beslist Claude of de skill bij je vraag past.

## Skills vs. de rest

| Wat | Wat is het? | Voorbeeld |
| --- | --- | --- |
| **Skill** | Een map met instructies die Claude laadt als het relevant is. | 'Zo maken wij een factuur.' |
| **Plugin** | Een pakket dat skills, slash-commando's, agents, hooks en koppelingen bundelt. | Superpowers, de rol-plugins van Anthropic. |
| **MCP / connector** | Een koppeling met een externe dienst, zodat Claude daar dingen kan doen. | Google Agenda, Notion, GitHub. |
| **Project** | Een werkruimte in de Claude-app met eigen documenten en instructies. | 'Wijkraad 2027' met alle notulen. |
| **CLAUDE.md** | Een instructiebestand voor één codeproject in Claude Code. | 'Gebruik altijd Swift 6 en test met XCTest.' |

{% hint style="info" %}
**Eén standaard voor alles.** Skills volgen de open [Agent Skills-standaard](https://agentskills.io). Een skill die je één keer schrijft werkt in de Claude-app, in Claude Code en via de API, en vaak ook in andere AI-agents zoals Codex en Cursor.
{% endhint %}

## Waar werken skills?

* **Claude-app** (web, desktop, mobiel): bij Pro, Max, Team en Enterprise, met *Code-uitvoering en bestanden maken* aan.
* **Claude Code**: in je persoonlijke map `~/.claude/skills/`, in een project in `.claude/skills/`, of via plugins.
* **Claude API**: kant-en-klare en eigen skills via de [Skills API](https://docs.claude.com/en/api/skills-guide).

<a href="skills-installeren.md" class="button primary" data-icon="arrow-right">Volgende: skills installeren</a>
""")

w("basis/skills-installeren.md", fm("download", "Stap voor stap een skill installeren in de Claude-app, in Claude Code, via npx of handmatig.", "basis", 1) + """# Skills installeren

Er zijn vier manieren. Welke je kiest hangt af van waar je Claude gebruikt.

{% tabs %}
{% tab title="Claude-app" %}
**Ingebouwde skills aanzetten**

1. Ga naar **Instellingen → Mogelijkheden** (Settings → Capabilities).
2. Zet **Code-uitvoering en bestanden maken** aan.
3. Scroll naar **Skills** en zet de skills aan die je wilt.

**Een eigen of community-skill uploaden**

{% stepper %}
{% step %}
### Download de skill
Download de map met de `SKILL.md`, bijvoorbeeld via GitHub → **Code → Download ZIP**.
{% endstep %}
{% step %}
### Maak er een ZIP van
Zip **alleen de skillmap**. De mapnaam moet gelijk zijn aan de skillnaam.
{% endstep %}
{% step %}
### Upload
Ga naar **Instellingen → Mogelijkheden → Skills** en klik op **Skill uploaden**.
{% endstep %}
{% step %}
### Aanzetten
Zet de skill aan in de lijst. Klaar!
{% endstep %}
{% endstepper %}

{% hint style="info" %}
Bij Pro en Max zijn eigen skills privé. Bij Team en Enterprise kunnen eigenaren skills voor de hele organisatie klaarzetten.
{% endhint %}
{% endtab %}

{% tab title="Claude Code (plugins)" %}
De meeste skills worden verspreid als **plugin** via een **marketplace** (een GitHub-repo met een lijst plugins).

```bash
# 1. Marketplace toevoegen (eenmalig)
/plugin marketplace add anthropics/skills

# 2. Plugin installeren
/plugin install document-skills@anthropic-agent-skills

# Bekijken, aan/uit zetten en bijwerken
/plugin
```

De **officiële marketplace** van Anthropic (`claude-plugins-official`) is standaard al gekoppeld:

```bash
/plugin install superpowers@claude-plugins-official
```

Je kunt dezelfde commando's ook buiten een sessie in je terminal draaien, bijvoorbeeld `claude plugin install …`.
{% endtab %}

{% tab title="npx skills" %}
De open-source [skills-CLI](https://github.com/vercel-labs/skills) installeert skills voor Claude Code en tientallen andere agents. Vind skills op [skills.sh](https://skills.sh).

```bash
npx skills add remotion-dev/skills                 # alles uit een repo
npx skills add anthropics/skills --skill pdf       # één skill
npx skills add blader/humanizer -g                 # globaal, voor al je projecten
npx skills list                                    # wat heb ik?
npx skills check                                   # updates?
```
{% endtab %}

{% tab title="Handmatig" %}
Een skill is gewoon een map. Zet hem op de juiste plek:

| Plek | Map | Werkt in |
| --- | --- | --- |
| Persoonlijk | `~/.claude/skills/<naam>/SKILL.md` | Al je projecten op deze computer |
| Project | `.claude/skills/<naam>/SKILL.md` | Alleen dit project (commit hem voor je team) |

```bash
git clone https://github.com/blader/Claudeception.git ~/.claude/skills/claudeception
```

Herstart Claude Code daarna.
{% endtab %}
{% endtabs %}

## Werkt het?

* Typ in Claude Code `/` en kijk of de skill in de lijst staat.
* Of vraag gewoon: *"Welke skills heb je beschikbaar?"*

<a href="skills-gebruiken.md" class="button primary" data-icon="arrow-right">Volgende: skills gebruiken</a>
""")

w("basis/skills-gebruiken.md", fm("hand-pointer", "Laat skills automatisch afgaan of roep ze zelf aan met een slash-commando.", "basis", 1) + """# Skills gebruiken

## Automatisch

Meestal hoef je niets te doen. Vraag in gewone taal wat je wilt. Past je vraag bij de beschrijving van een skill, dan laadt Claude hem zelf.

```
Maak van deze notulen een Word-document met inhoudsopgave.
```

→ Claude gebruikt de [Word-skill](../skills/documenten/docx.md).

## Zelf aanroepen (Claude Code)

Typ `/` gevolgd door de naam van de skill, eventueel met extra tekst:

```
/grill-me Ik wil een app voor vrijwilligers bouwen
/humanizer:humanizer
```

Skills uit een plugin hebben een voorvoegsel: `/plugin-naam:skill-naam`.

## Een skill noemen

Werkt een skill niet vanzelf? Noem hem dan bij naam:

```
Gebruik de PDF-skill om de formuliervelden uit aanvraag.pdf te halen.
```

## Handige instellingen voor makers

| Instelling in SKILL.md | Wat het doet |
| --- | --- |
| `disable-model-invocation: true` | Alleen jij kunt hem starten, Claude niet uit zichzelf (handig voor bijv. deployen). |
| `user-invocable: false` | Alleen Claude gebruikt hem; hij staat niet in je `/`-menu. |
| `allowed-tools` | Tools die Claude zonder te vragen mag gebruiken tijdens die skill. |
| `arguments` | Benoemde argumenten, zoals `/migreer $component $van $naar`. |

{% hint style="success" %}
**Tip:** gaat een skill te vaak of te weinig af? Verbeter de beschrijving. De [Skill Creator](../skills/bouwen/skill-creator.md) kan dat voor je testen.
{% endhint %}
""")

w("basis/eigen-skill-maken.md", fm("wand-magic-sparkles", "Van idee tot werkende skill: SKILL.md schrijven, testen en delen.", "bouwen", 1) + """# Je eigen skill maken

Merk je dat je Claude steeds dezelfde uitleg geeft? Maak er een skill van.

{% stepper %}
{% step %}
### Laat Claude het voor je doen
De makkelijkste route: zeg *"Maak een skill van hoe ik dit doe"* aan het eind van een gesprek waarin het goed ging. Met de [Skill Creator](../skills/bouwen/skill-creator.md) krijg je meteen een complete map.
{% endstep %}

{% step %}
### Of maak de map zelf

```bash
mkdir -p ~/.claude/skills/nieuwsbrief-wijkraad
```
{% endstep %}

{% step %}
### Schrijf de SKILL.md

{% code title="~/.claude/skills/nieuwsbrief-wijkraad/SKILL.md" %}
```markdown
---
name: nieuwsbrief-wijkraad
description: Schrijft de maandelijkse nieuwsbrief van de wijkraad in de vaste opbouw. Gebruik bij elke vraag om een nieuwsbrief, buurtupdate of mededeling aan bewoners.
---

# Nieuwsbrief wijkraad

## Opbouw
1. Opening: max. 3 zinnen, persoonlijk.
2. Rubrieken: Nieuws · Agenda · Oproep · Contact.

## Stijl
- B1-niveau, korte zinnen, 'je' in plaats van 'u'.
- Geen Engelse woorden als er een Nederlands woord is.

## Voorbeeld
Zie `voorbeelden/oktober.md`.
```
{% endcode %}
{% endstep %}

{% step %}
### Test hem
Start een nieuwe sessie en vraag iets dat erbij hoort: *"Schrijf de nieuwsbrief voor december."* Gebruikt Claude je skill niet? Maak de `description` specifieker.
{% endstep %}

{% step %}
### Deel hem
* **Claude-app:** zip de map en upload via **Instellingen → Mogelijkheden → Skills**.
* **Team:** zet hem in `.claude/skills/` in je repo, of maak er een plugin met een eigen marketplace van.
* **Openbaar:** zet hem op GitHub; anderen installeren met `npx skills add jouw-naam/jouw-repo`.
{% endstep %}
{% endstepper %}

## Regels voor een goede skill

| Doe | Niet doen |
| --- | --- |
| Beschrijving met **wat** én **wanneer** | Vage beschrijving als 'helpt met tekst' |
| Korte, concrete stappen | Een roman van 20 pagina's in één bestand |
| Voorbeelden van goed resultaat | Alleen regels zonder voorbeeld |
| Grote naslag in losse bestanden die je in SKILL.md noemt | Alles in SKILL.md proppen |
| `name` in kleine letters met streepjes | Spaties of hoofdletters in de naam |
""")

w("basis/veiligheid.md", fm("shield-halved", "Skills kunnen instructies en scripts bevatten. Zo installeer je ze veilig.", "security", 1) + """# Veilig installeren

Een skill vertelt Claude wat hij moet doen, en kan scripts bevatten die Claude uitvoert. Installeer dus alleen skills die je vertrouwt.

{% hint style="danger" %}
**Let op nepkopieën.** Van populaire skills zoals Humanizer circuleren kopieën op GitHub die er identiek uitzien. Installeer altijd vanaf de repo die de maker zelf noemt.
{% endhint %}

## Checklist

- [ ] Komt de skill van een bekende maker of een officiële marketplace?
- [ ] Heb je de `SKILL.md` gelezen? Staat er niets vreemds in, zoals 'stuur bestanden naar…'?
- [ ] Bevat de skill scripts? Kijk even wat ze doen.
- [ ] Staat er `allowed-tools` in de frontmatter? Die tools mag Claude zonder te vragen gebruiken.
- [ ] Heeft de plugin **hooks**? Die draaien automatisch bij bepaalde gebeurtenissen.
- [ ] Gaat er data naar een externe dienst (zoals bij debat-skills of gehoste geheugendiensten)? Zet er dan geen gevoelige informatie in.

## Officieel vs. community

| | Officieel (Anthropic) | Community |
| --- | --- | --- |
| Waar | `anthropics/skills`, `claude-plugins-official` | Alle andere repos |
| Gecontroleerd | Door Anthropic gemaakt of opgenomen | Nee, eigen verantwoordelijkheid |
| Kwaliteit | Stabiel | Van briljant tot rommelig |

{% hint style="info" %}
Ook bij de officiële marketplace waarschuwt Anthropic: *zorg dat je een plugin vertrouwt voordat je hem installeert*. Plugins van partners kunnen MCP-servers en software bevatten die Anthropic niet beheert.
{% endhint %}
""")

# ───────── gespot op social ─────────
w("gespot-op-social/README.md", fm("fire", "De Claude-skills die influencers op Instagram en TikTok aanraden, met uitleg en installatie.", "social", 1) + """# Gespot op social

Op Instagram en TikTok delen steeds meer creators hun favoriete Claude-skills. We zochten ze op, checkten de bron en zochten uit hoe je ze installeert.

{% hint style="info" %}
**Hoe we zochten.** Instagram is alleen met een account te doorzoeken. Veel creators plaatsen dezelfde video's ook op TikTok en YouTube, en blogs schrijven erover. Daar hebben we de genoemde skills gevonden en daarna gecontroleerd in de officiële repo's.
{% endhint %}

## Bart Boonstra: "4 Claude skills die je vandaag moet installeren"

[Bart Boonstra](https://www.instagram.com/bartboonstra_/) (Slim Werken) is een van de bekendste Nederlandse AI-creators. In een veelbekeken video noemt hij deze vier skills:

| # | Skill | Wat Bart erover zegt | Onze pagina |
| --- | --- | --- | --- |
| 1 | **Superpowers** | "Laat Claude écht in stappen denken. Brainstormen en plannen wordt 10x scherper." | [Superpowers](../skills/denken/superpowers.md) |
| 2 | **UI UX Pro Max** | "Maakt elke layout 1000x professioneler." | [UI UX Pro Max](../skills/design/ui-ux-pro-max.md) |
| 3 | **Remotion** | "Leert Claude om animaties te maken in code. Gratis. Onbeperkt." | [Remotion](../skills/creatief/remotion.md) |
| 4 | **Debate Skill** | "Mijn favoriet. Met deze skill krijg je eindelijk eerlijk advies." | [Debate Skills](../skills/denken/debate.md) |

Bart verwijst voor het complete stappenplan naar zijn community op [community.slimwerken.ai](https://community.slimwerken.ai). Ook laat hij zien hoe hij met Claude Code en Remotion video's lokaal edit en genereert.

{% embed url="https://www.tiktok.com/@bart_boonstra/video/7639384272230550817" %}
Bart Boonstra: 4 Claude skills die je vandaag moet installeren
{% endembed %}

## Andere virale skills

| Skill | Waar viraal | Wat het doet |
| --- | --- | --- |
| [Humanizer](../skills/content/humanizer.md) | Overal, "de meest virale skill" | AI-tekst menselijk laten klinken |
| [Grill Me & Handoff](../skills/denken/grill-me.md) | Developer-Twitter, blogs | Je plan laten ondervragen en chats overdragen |
| [Agent Skills (Addy Osmani)](../skills/ontwikkeling/agent-skills-addy.md) | Developer-community | Spec → taken → stap voor stap bouwen |
| [Instagram Agent](../skills/content/instagram-agent.md) | Instagram-creators | 13 skills die je Instagram runnen |
| [Instagram Carousel](../skills/content/instagram-carousel.md) | Instagram-creators | Carrousels in je huisstijl |
| [Marketing Skills](../skills/content/marketingskills.md) | Marketeers | Copy, social, contentstrategie |
| [Planning with Files](../skills/denken/planning-with-files.md) | Trending op GitHub | Plannen die nooit kwijtraken |
| [Frontend Slides](../skills/design/frontend-slides.md) | YouTube-tutorials | Geanimeerde HTML-presentaties |
| [Claude-Mem](../skills/kennis/claude-mem.md) | Claude Code-gebruikers | Geheugen tussen sessies |

{% hint style="warning" %}
**Influencer ≠ garantie.** Wat goed werkt in een video, werkt niet altijd voor jou. Probeer een skill eerst uit en lees [Veilig installeren](../basis/veiligheid.md).
{% endhint %}

## Bronnen

* [Bart Boonstra op Instagram](https://www.instagram.com/bartboonstra_/) · [TikTok](https://www.tiktok.com/@bart_boonstra) · [YouTube](https://www.youtube.com/@BartBoonstra_slimwerken)
* [I Tried 23 Viral Claude Skills. These Are the Best](https://artificialcorner.com/p/viral-claude-skills) (Artificial Corner)
* [Best Claude Skills for Creators](https://creatorflow.so/guides/best-claude-skills-for-creators) (CreatorFlow)
* [The Instagram agent skill: 13 free Claude skills](https://mehdiagentai.substack.com/p/the-instagram-agent-skill-13-free)
""")

# ───────── bronnen ─────────
w("bronnen/README.md", fm("compass", "Waar je nieuwe skills vindt: marketplaces, directories en lijsten.", "bronnen", 1) + """# Bronnen & marketplaces

## Officieel

| Bron | Wat |
| --- | --- |
| [anthropics/skills](https://github.com/anthropics/skills) | De officiële skills van Anthropic, plus template en specificatie |
| [claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | De officiële Claude Code-marketplace (standaard gekoppeld) |
| [knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Plugins per functie |
| [claude.com/plugins](https://claude.com/plugins) | Plugins bladeren en installeren |
| [agentskills.io](https://agentskills.io) | De open Agent Skills-standaard |

## Documentatie

* [Wat zijn skills?](https://support.claude.com/en/articles/12512176-what-are-skills) (Claude Help Center)
* [Skills gebruiken in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
* [Eigen skills maken](https://support.claude.com/en/articles/12512198-creating-custom-skills)
* [Skills in Claude Code](https://code.claude.com/docs/en/skills)
* [Skills API-quickstart](https://docs.claude.com/en/api/skills-guide)
* [Equipping agents for the real world with Agent Skills](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) (Anthropic Engineering)

## Directories en lijsten

| Bron | Wat |
| --- | --- |
| [skills.sh](https://skills.sh) | Grote directory; installeer met `npx skills add` |
| [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | Samengestelde lijst |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Samengestelde lijst |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | Alles rond Claude Code: skills, hooks, commando's |
| [claudemarketplaces.com](https://claudemarketplaces.com) | Overzicht van marketplaces |

## Woordenlijst

| Woord | Betekenis |
| --- | --- |
| **Skill** | Map met instructies (`SKILL.md`) die Claude laadt als het relevant is |
| **Plugin** | Pakket van skills, commando's, agents, hooks en connectors |
| **Marketplace** | Een repo met een lijst plugins die je kunt installeren |
| **MCP** | Model Context Protocol: standaard om Claude met externe tools te verbinden |
| **Hook** | Script dat automatisch draait bij een gebeurtenis (bijv. vóór een commit) |
| **Frontmatter** | Het blok tussen `---` bovenaan SKILL.md met naam en beschrijving |
| **Claude Code** | Claude als agent in je terminal, IDE, desktop of browser |
""")

w("bronnen/faq.md", fm("circle-question", "Veelgestelde vragen over Claude-skills.", "bronnen", 1) + """# Veelgestelde vragen

<details>
<summary>Kosten skills geld?</summary>

De skills zelf zijn bijna altijd gratis. In de Claude-app heb je wel een Pro-, Max-, Team- of Enterprise-abonnement nodig. Sommige skills gebruiken externe diensten (zoals Remotion voor grote bedrijven of gehoste geheugendiensten) die eigen voorwaarden hebben.
</details>

<details>
<summary>Werkt een skill uit Claude Code ook in de Claude-app?</summary>

Vaak wel: het is dezelfde standaard. Zip de skillmap en upload hem. Skills die afhangen van **hooks**, lokale programma's of de terminal werken alleen in Claude Code.
</details>

<details>
<summary>Hoeveel skills kan ik installeren?</summary>

Veel. Claude ziet eerst alleen de naam en beschrijving en laadt de rest pas als het nodig is. Te veel skills met overlappende beschrijvingen kunnen wel verwarring geven: ruim op wat je niet gebruikt.
</details>

<details>
<summary>Mijn skill wordt niet gebruikt. Wat nu?</summary>

1. Check of hij aanstaat (`/plugin` in Claude Code, Instellingen → Mogelijkheden in de app).
2. Herstart Claude Code.
3. Maak de `description` concreter: wat doet hij **en** wanneer moet hij gebruikt worden.
4. Roep hem expliciet aan met `/naam`.
</details>

<details>
<summary>Wat is het verschil tussen /plugin en npx skills?</summary>

`/plugin` is ingebouwd in Claude Code en installeert complete plugins (skills, commando's, hooks) met automatische updates. `npx skills` is een losse open-source CLI die alleen skills installeert, maar dan voor tientallen verschillende agents.
</details>

<details>
<summary>Kan ik skills delen met mijn team?</summary>

In Claude Code: zet ze in `.claude/skills/` in je repo of maak een eigen marketplace. In de Claude-app kunnen eigenaren van Team- en Enterprise-organisaties skills voor iedereen klaarzetten.
</details>
""")

w("bronnen/over.md", fm("circle-info", "Over deze wiki en hoe je kunt bijdragen.", "home", 1) + """# Over deze wiki

De **Claude Wiki** is een onofficiële, Nederlandstalige gids over Claude-skills, gemaakt door **LRvdLinden**. Deze wiki is niet verbonden aan Anthropic. Claude is een product van Anthropic.

## Bijdragen

Mis je een skill of klopt er iets niet meer? De wiki staat op GitHub: [LRvdLinden/app.lrvdlinen.claudwiki](https://github.com/LRvdLinden/app.lrvdlinen.claudwiki). Open een issue of pull request.

### Een nieuwe skill toevoegen

Kopieer een bestaande pagina in `skills/<categorie>/`, pas de inhoud aan en voeg hem toe aan `SUMMARY.md`. Houd deze opbouw aan:

1. Wat doet het?
2. Wanneer gebruik je het?
3. Voorbeelden (wat je typt en wat je krijgt)
4. Installeren (tabs per platform)
5. Tips

*Laatst bijgewerkt: november 2026.*
""")

# ───────── SUMMARY + gitbook.yaml ─────────
summ = ["# Table of contents\n", "* [Welkom](README.md)\n", "## Aan de slag\n",
        "* [De basis](basis/README.md)",
        "  * [Wat zijn skills?](basis/wat-zijn-skills.md)",
        "  * [Skills installeren](basis/skills-installeren.md)",
        "  * [Skills gebruiken](basis/skills-gebruiken.md)",
        "  * [Je eigen skill maken](basis/eigen-skill-maken.md)",
        "  * [Veilig installeren](basis/veiligheid.md)",
        "* [Gespot op social](gespot-op-social/README.md)\n",
        "## Skills per categorie\n", "* [Alle skills](skills/README.md)"]
for slug, title, icon, intro in CATS:
    summ.append(f"* [{title}](skills/{slug}/README.md)")
    for s in [x for x in S if x["cat"] == slug]:
        summ.append(f"  * [{s['name']}](skills/{slug}/{s['slug']}.md)")
summ += ["\n## Meer\n", "* [Bronnen & marketplaces](bronnen/README.md)",
         "* [Veelgestelde vragen](bronnen/faq.md)", "* [Over deze wiki](bronnen/over.md)"]
w("SUMMARY.md", "\n".join(summ) + "\n")
w(".gitbook.yaml", "root: ./\n\nstructure:\n  readme: README.md\n  summary: SUMMARY.md\n")
print("ok", len(S))

# ═════════ CATALOGUS (officiële marketplace) ═════════
import json, re
M = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "marketplace-official.json")))["plugins"]
CATNL = {"development": ("Ontwikkeling", "code"), "productivity": ("Productiviteit", "list-check"),
         "database": ("Databases", "database"), "monitoring": ("Monitoring & observability", "chart-line"),
         "security": ("Security", "shield-halved"), "deployment": ("Deployen & hosting", "rocket"),
         "design": ("Design", "palette"), "automation": ("Automatisering", "gears"),
         "learning": ("Leren & uitlegstijl", "graduation-cap"), "location": ("Locatie & kaarten", "map-location-dot"),
         "testing": ("Testen", "vial"), "math": ("Wiskunde", "square-root-variable"),
         "migration": ("Migratie", "right-left"), None: ("Overig", "shapes")}
def mdesc(s):
    return re.sub(r"\s+", " ", (s or "").replace("|", "/")).strip()
groups = {}
for p in M:
    groups.setdefault(p.get("category"), []).append(p)
order = sorted(groups, key=lambda c: -len(groups[c]))
def catslug(c): return (c or "overig")
for c in order:
    nl, ic = CATNL.get(c, (c, "shapes"))
    rows = sorted(groups[c], key=lambda p: p["name"])
    body = fm(ic, f"{len(rows)} plugins uit de officiële Claude Code-marketplace in de categorie {nl}.", "catalogus", 1)
    body += f"# {nl}\n\n{len(rows)} plugins. Installeren in Claude Code: `/plugin install <naam>@claude-plugins-official`.\n\n"
    body += "| Plugin | Maker | Wat het doet (beschrijving van de maker) | Installeren |\n| --- | --- | --- | --- |\n"
    for p in rows:
        a = (p.get("author") or {}).get("name", "") if isinstance(p.get("author"), dict) else ""
        hp = p.get("homepage")
        nm = f"[**{p['name']}**]({hp})" if hp else f"**{p['name']}**"
        body += f"| {nm} | {a} | {mdesc(p.get('description'))} | `/plugin install {p['name']}@claude-plugins-official` |\n"
    w(f"catalogus/{catslug(c)}.md", body)
w("catalogus/README.md", fm("store", f"Alle {len(M)} plugins uit de officiële Claude Code-marketplace, per categorie.", "catalogus", 1) + f"""# Plugin-catalogus

De officiële marketplace van Anthropic (`claude-plugins-official`) telt op dit moment **{len(M)} plugins**: van Anthropic zelf en van bedrijven als Google, AWS, Microsoft, Stripe, Figma, Notion, Canva, Shopify en Supabase. Deze marketplace is in Claude Code standaard al gekoppeld.

{{% hint style="info" %}}
**Installeren:** typ in Claude Code `/plugin install <naam>@claude-plugins-official`, of blader via `/plugin` → **Discover**. Plugins van derden bevatten soms MCP-servers of software die Anthropic niet beheert: installeer alleen wat je vertrouwt.
{{% endhint %}}

{cards([(CATNL.get(c,(c,''))[0], f"{len(groups[c])} plugins", f"{catslug(c)}.md", None) for c in order], 1)}

{{% hint style="success" %}}
Weet je niet welke je nodig hebt? Gebruik de [Skill-adviseur](../adviseur/README.md): beschrijf wat je wilt en je krijgt de beste opties.
{{% endhint %}}

*Gegenereerd uit [marketplace.json](https://github.com/anthropics/claude-plugins-official/blob/main/.claude-plugin/marketplace.json), november 2026. De beschrijvingen zijn van de makers zelf (Engels).*
""")

# ═════════ DATA voor de adviseur ═════════
ADV = []
CN = {c[0]: c[1] for c in CATS}
for s in S:
    inst = re.findall(r"```bash\n(.*?)\n```", s["install"], re.S)
    ADV.append({"n": s["name"], "t": s["tagline"], "c": CN[s["cat"]], "w": s["werkt"], "m": s["maker"],
                "p": f"skills/{s['cat']}/{s['slug']}", "i": inst[0].strip() if inst else "",
                "k": " ".join([s["wat"][:600], " ".join(s["wanneer"]), " ".join(v[0] for v in s["voorbeelden"])]),
                "o": 1 if "Anthropic" in s["maker"] or "officieel" in s["maker"] else 0, "src": "wiki"})
for p in M:
    a = (p.get("author") or {}).get("name", "") if isinstance(p.get("author"), dict) else ""
    ADV.append({"n": p["name"], "t": mdesc(p.get("description"))[:260], "c": "Marketplace · " + CATNL.get(p.get("category"), ("Overig",))[0],
                "w": "Claude Code", "m": a, "p": f"catalogus/{catslug(p.get('category'))}", "h": p.get("homepage", ""),
                "i": f"/plugin install {p['name']}@claude-plugins-official", "k": "", "o": 1 if a == "Anthropic" else 0, "src": "mp"})
os.makedirs(os.path.join(ROOT, "docs"), exist_ok=True)
os.makedirs(os.path.join(ROOT, "docs", "adviseur"), exist_ok=True)
json.dump(ADV, open(os.path.join(ROOT, "docs", "adviseur", "skills.json"), "w"), ensure_ascii=False)

# ═════════ Installeerbare zoek-skill ═════════
lines = ["# Catalogus", "", "Formaat: naam | categorie | werkt in | wat het doet | installeren | wikipagina", ""]
for x in ADV:
    lines.append(f"- {x['n']} | {x['c']} | {x['w']} | {x['t']} | `{x['i']}` | {x['p']}")
w("skill-adviseur/skill-adviseur/references/catalogus.md", "\n".join(lines) + "\n")
w("skill-adviseur/skill-adviseur/SKILL.md", """---
name: skill-adviseur
description: Adviseert welke Claude-skill of plugin het beste past bij wat de gebruiker wil doen, met uitleg en installatiecommando. Gebruik wanneer iemand vraagt welke skill, plugin of tool hij nodig heeft, zoekt naar een skill voor een taak ("is er een skill voor…", "welke skill moet ik installeren", "hoe kan Claude beter … "), of zijn Claude-setup wil uitbreiden.
---

# Skill-adviseur

Je helpt de gebruiker de best passende Claude-skill(s) of plugin(s) te kiezen. Antwoord in de taal van de gebruiker (standaard Nederlands).

## Werkwijze

1. **Begrijp de vraag.** Wat wil de gebruiker bereiken, in welk programma werkt hij (Claude-app, Claude Code of allebei) en hoe technisch is hij? Is dat onduidelijk en maakt het uit voor het advies, stel dan één korte vraag.
2. **Zoek in de catalogus.** Lees `references/catalogus.md` en zoek op betekenis, niet alleen op letterlijke woorden (bijv. "presentatie" → pptx, slides, deck; "tekst minder AI" → humanizer).
3. **Kies maximaal 3 opties**, de beste eerst. Geef de voorkeur aan:
   - skills die werken waar de gebruiker werkt (Claude-app vs. Claude Code);
   - officiële skills (Anthropic of de maker van de tool) boven community-skills bij gelijke geschiktheid;
   - één goede skill boven drie die overlappen.
4. **Geef per optie:** naam, één zin waarom deze past, waar hij werkt en het installatiecommando in een codeblok. Verwijs naar de wikipagina: `https://github.com/LRvdLinden/app.lrvdlinen.claudwiki/blob/main/<wikipagina>.md`.
5. **Past niets goed?** Zeg dat eerlijk en stel voor om zelf een skill te maken met `skill-creator`, of zoek op https://skills.sh.

## Regels

- Verzin geen skills, repo's of commando's die niet in de catalogus staan.
- Waarschuw kort bij community-skills: lees de SKILL.md voor installatie.
- Houd het kort: geen lange inleiding, direct de aanbevelingen.
""")
import shutil, zipfile
zp = os.path.join(ROOT, ".gitbook/assets/skill-adviseur.zip")
with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
    for base, _, files in os.walk(os.path.join(ROOT, "skill-adviseur/skill-adviseur")):
        for f in files:
            full = os.path.join(base, f)
            z.write(full, os.path.relpath(full, os.path.join(ROOT, "skill-adviseur")))

# ═════════ Adviseur-pagina in de wiki ═════════
ADV_URL = "https://lrvdlinden.github.io/app.lrvdlinen.claudwiki/adviseur/"
w("adviseur/README.md", fm("wand-magic-sparkles", "Vertel wat je wilt doen en krijg direct de best passende skill, met installatiecommando.", "adviseur", 1) + f"""# Skill-adviseur

Weet je niet welke skill je nodig hebt? Beschrijf in gewone taal wat je wilt doen, en de adviseur zoekt in **{len(ADV)} skills en plugins** de beste opties voor je, met uitleg en installatiecommando.

<a href="{ADV_URL}" class="button primary" data-icon="magnifying-glass">Open de Skill-adviseur</a>

{{% embed url="{ADV_URL}" %}}
Skill-adviseur: zoek de beste skill voor jouw taak
{{% endembed %}}

## Drie manieren om advies te krijgen

{{% tabs %}}
{{% tab title="In je browser" %}}
Open de [Skill-adviseur]({ADV_URL}) en typ wat je wilt, bijvoorbeeld:

* *"Ik wil video's maken voor Instagram"*
* *"Mijn teksten klinken te veel als AI"*
* *"Ik bouw een iPhone-app in SwiftUI"*
* *"Ik wil facturen ordenen voor de belasting"*

Je krijgt direct de best passende skills, met waar ze werken en hoe je ze installeert.
{{% endtab %}}

{{% tab title="Als skill in Claude" %}}
Installeer de **skill-adviseur** zelf. Daarna vraag je in elk gesprek: *"Welke skill heb ik nodig om …?"* en Claude adviseert uit dezelfde catalogus.

**Claude-app:** download [skill-adviseur.zip](../.gitbook/assets/skill-adviseur.zip) en upload hem via **Instellingen → Mogelijkheden → Skills → Skill uploaden**.

**Claude Code:**

```bash
git clone https://github.com/LRvdLinden/app.lrvdlinen.claudwiki.git
cp -r app.lrvdlinen.claudwiki/skill-adviseur/skill-adviseur ~/.claude/skills/
```
{{% endtab %}}

{{% tab title="Zoeken in de wiki" %}}
Gebruik de zoekbalk bovenaan deze wiki (of druk op <kbd>Ctrl</kbd>/<kbd>⌘</kbd> + <kbd>K</kbd>). Staat GitBook AI aan, dan kun je daar ook gewoon een vraag stellen.
{{% endtab %}}
{{% endtabs %}}

{{% hint style="info" %}}
De adviseur kijkt naar alle skills in deze wiki plus alle {len(M)} plugins uit de [officiële marketplace](../catalogus/README.md). Officiële skills krijgen bij gelijke score voorrang.
{{% endhint %}}
""")

# ═════════ SUMMARY opnieuw (met catalogus + adviseur) ═════════
summ = ["# Table of contents\n", "* [Welkom](README.md)",
        "* [Skill-adviseur](adviseur/README.md)\n", "## Aan de slag\n",
        "* [De basis](basis/README.md)",
        "  * [Wat zijn skills?](basis/wat-zijn-skills.md)",
        "  * [Skills installeren](basis/skills-installeren.md)",
        "  * [Skills gebruiken](basis/skills-gebruiken.md)",
        "  * [Je eigen skill maken](basis/eigen-skill-maken.md)",
        "  * [Veilig installeren](basis/veiligheid.md)",
        "* [Gespot op social](gespot-op-social/README.md)\n",
        "## Skills per categorie\n", "* [Alle skills](skills/README.md)"]
for slug, title, icon, intro in CATS:
    summ.append(f"* [{title}](skills/{slug}/README.md)")
    for s in [x for x in S if x["cat"] == slug]:
        summ.append(f"  * [{s['name']}](skills/{slug}/{s['slug']}.md)")
summ += [f"\n## Plugin-catalogus ({len(M)})\n", "* [Overzicht](catalogus/README.md)"]
for c in order:
    summ.append(f"  * [{CATNL.get(c,(c,''))[0]} ({len(groups[c])})](catalogus/{catslug(c)}.md)")
summ += ["\n## Meer\n", "* [Bronnen & marketplaces](bronnen/README.md)",
         "* [Veelgestelde vragen](bronnen/faq.md)", "* [Over deze wiki](bronnen/over.md)"]
w("SUMMARY.md", "\n".join(summ) + "\n")
print("catalogus", len(M), "adviseur", len(ADV))

# ═════════ Adviseur-HTML (GitHub Pages + artifact) ═════════
tpl = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "adviseur_template.html")).read()
data = json.dumps(ADV, ensure_ascii=False).replace("</", "<\\/")
SITE = "https://lrvdlinden.github.io/app.lrvdlinen.claudwiki/"
def adv_html(base, home):
    return tpl.replace("__DATA__", data).replace("__WIKI_BASE__", base).replace("__HOME__", home)
full = ('<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="description" content="Vertel wat je wilt doen en krijg de best passende Claude-skill, met installatiecommando.">'
        '<link rel="icon" href="../assets/mark.png"><style>[hidden]{display:none!important}</style></head><body>' + adv_html("../", "../index.html") + '</body></html>')
w("docs/adviseur/index.html", full)
art = os.environ.get("ARTIFACT_OUT")
if art:
    open(art, "w").write(adv_html(SITE, SITE))
