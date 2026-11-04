---
description: >-
  Skills zijn mappen met instructies, scripts en bestanden die Claude laadt wanneer ze nodig zijn.
icon: lightbulb
cover: ../.gitbook/assets/cover-basis.png
coverY: 0
layout:
  cover:
    visible: true
    size: full
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---
# Wat zijn skills?

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
