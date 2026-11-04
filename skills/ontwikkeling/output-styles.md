---
description: >-
  Laat Claude uitleggen wat hij doet (Explanatory) of jou zelf stukken code laten schrijven om van te leren (Learning).
icon: chalkboard-user
cover: ../../.gitbook/assets/cover-ontwikkeling.png
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

# Learning & Explanatory output styles

| | |
| --- | --- |
| **Maker** | Anthropic · officiële Claude-marketplace |
| **Werkt in** | Claude Code |
| **Kosten** | Gratis |
| **Bron** | [github.com/anthropics/claude-plugins-public/tree/main/plugins/learning-output-style](https://github.com/anthropics/claude-plugins-public/tree/main/plugins/learning-output-style) |

## Wat doet het?

Twee plugins van Anthropic die de manier van antwoorden veranderen. **learning-output-style** vraagt je op belangrijke momenten zelf een stukje code te schrijven, zodat je leert in plaats van alleen kijkt. **explanatory-output-style** voegt uitleg toe over waarom Claude bepaalde keuzes maakt en welke patronen in je codebase zitten.

## Wanneer gebruik je het?

* Je wilt programmeren leren terwijl je met Claude bouwt.
* Je wilt begrijpen waarom Claude iets op een bepaalde manier doet.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
(na installatie) Voeg een zoekfunctie toe aan mijn app.
```
{% endcode %}

**Wat je krijgt:** Claude bouwt mee en laat jou het belangrijkste stuk schrijven, met uitleg.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install learning-output-style@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Voor de uitlegvariant: `/plugin install explanatory-output-style@claude-plugins-official`.
{% endhint %}


<a href="https://github.com/anthropics/claude-plugins-public/tree/main/plugins/learning-output-style" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Ontwikkelen & code</a>
