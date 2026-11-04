---
description: >-
  Maakt en bewerkt PowerPoint-presentaties, inclusief sjablonen, notities en layouts.
icon: file-powerpoint
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

# PowerPoint (pptx)

| | |
| --- | --- |
| **Maker** | Anthropic (officieel) |
| **Werkt in** | Claude-app, Claude Code, API |
| **Kosten** | Gratis bij betaald abonnement (source-available) |
| **Bron** | [github.com/anthropics/skills/tree/main/skills/pptx](https://github.com/anthropics/skills/tree/main/skills/pptx) |

## Wat doet het?

Met de PowerPoint-skill bouwt Claude complete presentaties als `.pptx`: dia's met titels, opsommingen, afbeeldingen, grafieken en sprekersnotities. Hij kan ook een bestaande presentatie of een sjabloon (`.potx`) lezen, de tekst eruit halen, dia's aanpassen of presentaties samenvoegen en splitsen.

## Wanneer gebruik je het?

* Je moet een presentatie aanleveren als PowerPoint-bestand.
* Je wilt een bestaande presentatie in je huisstijl laten bijwerken.
* Je wilt de inhoud van een presentatie samenvatten.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Maak een presentatie van 10 dia's over de plannen van de wijkraad voor 2027, met sprekersnotities per dia.
```
{% endcode %}

**Wat je krijgt:** Een `.pptx` die je in PowerPoint of Keynote opent.

{% code title="Voorbeeld 2: wat je typt" overflow="wrap" %}
```
Gebruik sjabloon huisstijl.potx en zet dit rapport om naar dia's.
```
{% endcode %}

**Wat je krijgt:** Een presentatie in jouw sjabloon.

## Installeren

{% tabs %}
{% tab title="Claude-app" %}
Deze skill is **al ingebouwd** voor betaalde abonnementen.

1. Open **Instellingen → Mogelijkheden** (Settings → Capabilities).
2. Zet **Code-uitvoering en bestanden maken** aan.
3. Scroll naar **Skills** en zet de skill aan.

Daarna vraag je gewoon in gewone taal wat je wilt; Claude laadt de skill zelf.

In de Claude-app gebruikt Claude deze skill ook al automatisch zodra je om een bestand van dit type vraagt.
{% endtab %}

{% tab title="Claude Code" %}
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.

Dit installeert **document-skills**: Word, PDF, PowerPoint en Excel in één keer.
{% endtab %}

{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add anthropics/skills --skill pptx
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Wil je geen bestand maar een snelle webpresentatie? Kijk naar [Frontend Slides](../design/frontend-slides.md).
{% endhint %}


<a href="https://github.com/anthropics/skills/tree/main/skills/pptx" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Documenten & kantoor</a>
