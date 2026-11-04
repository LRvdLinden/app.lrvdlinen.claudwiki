---
description: >-
  Een gestructureerde werkwijze om samen met Claude documenten, voorstellen en specs te schrijven.
icon: people-arrows
cover: ../../.gitbook/assets/cover-documenten.png
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

# Doc Co-authoring

| | |
| --- | --- |
| **Maker** | Anthropic (officieel) |
| **Werkt in** | Claude-app, Claude Code, API |
| **Kosten** | Gratis (Apache 2.0) |
| **Bron** | [github.com/anthropics/skills/tree/main/skills/doc-coauthoring](https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring) |

## Wat doet het?

In plaats van in één keer een tekst uit te spugen, leidt deze skill je door een vast proces: eerst haalt Claude de context bij je op, daarna schrijft en verfijnt hij in rondes en tot slot controleert hij of het document werkt voor de lezer. Handig voor voorstellen, technische specificaties, beslisdocumenten en beleidsstukken.

## Wanneer gebruik je het?

* Je schrijft een voorstel, beleidsnotitie of spec en wilt dat het écht klopt.
* Je hebt veel losse informatie die in een helder stuk moet.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Help me een voorstel te schrijven aan de gemeente voor meer verlichting in het park.
```
{% endcode %}

**Wat je krijgt:** Claude stelt eerst gerichte vragen, schrijft dan in stappen en checkt het resultaat vanuit de lezer.

## Installeren

{% tabs %}
{% tab title="Claude-app" %}
Deze skill is **al ingebouwd** voor betaalde abonnementen.

1. Open **Instellingen → Mogelijkheden** (Settings → Capabilities).
2. Zet **Code-uitvoering en bestanden maken** aan.
3. Scroll naar **Skills** en zet de skill aan.

Daarna vraag je gewoon in gewone taal wat je wilt; Claude laadt de skill zelf.
{% endtab %}

{% tab title="Claude Code" %}
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add anthropics/skills
/plugin install example-skills@anthropic-agent-skills
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.

Dit installeert het hele pakket **example-skills** (o.a. deze skill).
{% endtab %}

{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add anthropics/skills --skill doc-coauthoring
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}


<a href="https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Documenten & kantoor</a>
