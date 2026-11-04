---
description: >-
  Spreadsheets openen, opschonen, formules en grafieken toevoegen of nieuwe sheets bouwen.
icon: file-excel
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

# Excel (xlsx)

| | |
| --- | --- |
| **Maker** | Anthropic (officieel) |
| **Werkt in** | Claude-app, Claude Code, API |
| **Kosten** | Gratis bij betaald abonnement (source-available) |
| **Bron** | [github.com/anthropics/skills/tree/main/skills/xlsx](https://github.com/anthropics/skills/tree/main/skills/xlsx) |

## Wat doet het?

De Excel-skill laat Claude echte spreadsheets maken en bewerken: `.xlsx`, `.xlsm`, `.csv` en `.tsv`. Hij voegt kolommen en **werkende formules** toe, maakt grafieken, zet opmaak goed, ruimt rommelige data op (verkeerde kopregels, lege rijen) en zet bestanden om tussen formaten.

## Wanneer gebruik je het?

* Je hebt een begroting, planning of overzicht nodig dat je verder bewerkt in Excel.
* Je hebt een rommelige export die opgeschoond moet worden.
* Je wilt grafieken bij je cijfers.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Maak een begroting voor het buurtfeest met inkomsten, uitgaven, een totaalformule en een cirkeldiagram.
```
{% endcode %}

**Wat je krijgt:** Een `.xlsx` met werkende formules.

{% code title="Voorbeeld 2: wat je typt" overflow="wrap" %}
```
Deze CSV-export is een rommeltje. Schoon hem op, zet de datums goed en maak er een nette Excel van.
```
{% endcode %}

**Wat je krijgt:** Een opgeschoonde spreadsheet.

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
npx skills add anthropics/skills --skill xlsx
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Vraag Claude om formules te gebruiken in plaats van vaste getallen, dan blijft je sheet bruikbaar als je iets aanpast.
{% endhint %}


<a href="https://github.com/anthropics/skills/tree/main/skills/xlsx" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Documenten & kantoor</a>
