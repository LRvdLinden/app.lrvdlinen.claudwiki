---
description: >-
  Alles met PDF's: tekst en tabellen eruit halen, samenvoegen, splitsen, formulieren invullen, OCR en watermerken.
icon: file-pdf
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

# PDF

| | |
| --- | --- |
| **Maker** | Anthropic (officieel) |
| **Werkt in** | Claude-app, Claude Code, API |
| **Kosten** | Gratis bij betaald abonnement (source-available) |
| **Bron** | [github.com/anthropics/skills/tree/main/skills/pdf](https://github.com/anthropics/skills/tree/main/skills/pdf) |

## Wat doet het?

De PDF-skill geeft Claude een complete gereedschapskist voor PDF-bestanden. Hij haalt tekst en tabellen uit PDF's, voegt bestanden samen of splitst ze, draait pagina's, voegt watermerken toe, vult PDF-formulieren in, versleutelt of ontsleutelt bestanden en maakt gescande PDF's doorzoekbaar met OCR. Ook kan hij nieuwe PDF's maken.

## Wanneer gebruik je het?

* Je wilt gegevens uit een stapel facturen of rapporten in een tabel.
* Je moet een PDF-formulier invullen.
* Je hebt een scan die je wilt doorzoeken.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Haal uit deze 12 facturen (PDF) de datum, leverancier en het totaalbedrag en zet het in een tabel.
```
{% endcode %}

**Wat je krijgt:** Een overzichtstabel, eventueel als Excel.

{% code title="Voorbeeld 2: wat je typt" overflow="wrap" %}
```
Voeg deze drie PDF's samen, zet pagina 4 rechtop en zet een watermerk 'CONCEPT' op elke pagina.
```
{% endcode %}

**Wat je krijgt:** Eén nieuwe PDF.

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
npx skills add anthropics/skills --skill pdf
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Bij gescande documenten: vraag expliciet om OCR.
* Voor grote PDF's: vraag eerst om een inhoudsoverzicht en zoom daarna in.
{% endhint %}


<a href="https://github.com/anthropics/skills/tree/main/skills/pdf" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Documenten & kantoor</a>
