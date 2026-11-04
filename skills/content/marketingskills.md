---
description: >-
  Een grote collectie marketingskills: copywriting, social, contentstrategie, CRO, SEO en marketingpsychologie.
icon: chart-line
cover: ../../.gitbook/assets/cover-content.png
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

# Marketing Skills

| | |
| --- | --- |
| **Maker** | Corey Haines (community) |
| **Werkt in** | Claude Code (+ Codex, Cursor en meer) |
| **Kosten** | Gratis (MIT) |
| **Bron** | [github.com/coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) |

## Wat doet het?

Een collectie voor marketeers en founders. Onder andere **copywriting** (pagina's, posts en advertenties), **social** (content voor zes platforms, waaronder Instagram en TikTok), **content-strategy** (van doel naar contentplan en kalender), **marketing-psychology** (overtuigingsprincipes, hooks en call-to-actions), plus conversie-optimalisatie, SEO en analytics.

## Wanneer gebruik je het?

* Je wilt een landingspagina of advertentie die converteert.
* Je wilt een contentkalender voor je app.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Schrijf drie varianten van de App Store-beschrijving voor mijn app, met verschillende hooks.
```
{% endcode %}

**Wat je krijgt:** Drie onderbouwde varianten.

{% code title="Voorbeeld 2: wat je typt" overflow="wrap" %}
```
Maak een contentplan voor 4 weken Instagram voor de lancering van mijn app.
```
{% endcode %}

**Wat je krijgt:** Een kalender met onderwerpen, formats en hooks.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add coreyhaines31/marketingskills
/plugin install marketing-skills
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.

`/plugin` werkt alleen in een interactieve Claude Code-sessie.
{% endtab %}

{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add coreyhaines31/marketingskills -a claude-code
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/coreyhaines31/marketingskills" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Schrijven, content & marketing</a>
