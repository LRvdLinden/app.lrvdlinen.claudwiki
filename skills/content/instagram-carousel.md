---
description: >-
  Pixel-perfecte Instagram-carrousels in je eigen huisstijl, export naar PNG en PDF.
icon: images
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

# Instagram Carousel

| | |
| --- | --- |
| **Maker** | Jeevan Bavandla (community) |
| **Werkt in** | Claude Code, Claude-app |
| **Kosten** | Gratis (MIT) |
| **Bron** | [github.com/jeevanbavandla/instagram-carousel-skill](https://github.com/jeevanbavandla/instagram-carousel-skill) |

## Wat doet het?

Bij het eerste gebruik stel je eenmalig je merk in (naam, handle, foto, accentkleur, stijl). Daarna maakt Claude carrousels in vier stijlen: Bold Impact, Tweet Post, Clean Editorial en Product Showcase, met voortgangsbalk, pijltjes en een CTA-slide. Exporteren kan als PNG en PDF.

## Wanneer gebruik je het?

* Je wilt snel carrousels maken zonder Canva.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Maak een carrousel van 6 slides: '5 tips voor een veiligere wijk'.
```
{% endcode %}

**Wat je krijgt:** Zes slides in je huisstijl, klaar om te posten.

## Installeren

{% tabs %}
{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add jeevanbavandla/instagram-carousel-skill -g
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}

{% tab title="Claude-app" %}
De repo heeft een aparte map `claude-ai` met instructies om de skill in de Claude-app te gebruiken (bestand plakken, ±5 minuten).
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/jeevanbavandla/instagram-carousel-skill" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Schrijven, content & marketing</a>
