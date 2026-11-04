---
description: >-
  Prachtige, geanimeerde HTML-presentaties maken of PowerPoints omzetten naar het web.
icon: display
cover: ../../.gitbook/assets/cover-design.png
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

# Frontend Slides

| | |
| --- | --- |
| **Maker** | Zara Zhang (community) |
| **Werkt in** | Claude Code (de SKILL.md werkt ook in andere agents) |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) |

## Wat doet het?

Frontend Slides maakt presentaties als één HTML-bestand met animaties, in plaats van een PowerPoint. Je hoeft geen designer te zijn: de skill laat je visueel kiezen tussen stijlen in plaats van abstracte vragen te stellen. Ook kan hij een bestaande `.pptx` omzetten naar een webpresentatie en exporteren naar PDF.

## Wanneer gebruik je het?

* Je geeft een talk of pitch en wilt iets dat opvalt.
* Je wilt een oude PowerPoint moderniseren.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Maak een pitch van 8 slides voor mijn nieuwe app, met strakke animaties.
```
{% endcode %}

**Wat je krijgt:** Eén HTML-bestand dat je in de browser presenteert.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add https://github.com/zarazhangrui/frontend-slides
/plugin install frontend-slides@frontend-slides
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.
{% endtab %}

{% tab title="Handmatig" %}
Kopieer de skillmap naar je persoonlijke skills-map (voor alle projecten) of naar `.claude/skills/` in één project:

```bash
git clone https://github.com/zarazhangrui/frontend-slides.git ~/.claude/skills/frontend-slides
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Er is een beginnersvideo in de README van de repo.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/zarazhangrui/frontend-slides" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Design & frontend</a>
