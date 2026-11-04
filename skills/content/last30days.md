---
description: >-
  Onderzoekt wat mensen de afgelopen 30 dagen écht zeggen over een onderwerp: Reddit, X, YouTube, TikTok en meer.
icon: magnifying-glass-chart
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

# Last 30 Days

| | |
| --- | --- |
| **Maker** | mvanhorn (community) |
| **Werkt in** | Claude Code (+ andere agents) |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) |

## Wat doet het?

In plaats van redactionele artikelen zoekt deze skill naar wat **mensen** zeggen: posts en engagement van Reddit, X, YouTube, TikTok, Hacker News, Polymarket, GitHub en het web, uit de laatste 30 dagen. Met een `doctor`-check zie je welke bronnen werken.

## Wanneer gebruik je het?

* Je wilt weten wat er nu speelt rond een onderwerp of concurrent.
* Je zoekt inspiratie voor actuele content.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
/last30days Claude skills
```
{% endcode %}

**Wat je krijgt:** Een overzicht van wat er de afgelopen maand over Claude-skills gezegd is, met bronnen.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add mvanhorn/last30days-skill
/plugin install last30days
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.
{% endtab %}

{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add mvanhorn/last30days-skill -g
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Installeer niet via beide methodes tegelijk; Claude Code ontdubbelt dat niet.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/mvanhorn/last30days-skill" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Schrijven, content & marketing</a>
