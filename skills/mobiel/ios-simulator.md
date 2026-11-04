---
description: >-
  Laat Claude je iOS-app bouwen, starten en testen in de Simulator, met 30 hulpscripts.
icon: tablet-screen-button
cover: ../../.gitbook/assets/cover-mobiel.png
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

# iOS Simulator Skill

| | |
| --- | --- |
| **Maker** | Conor Luddy (community) |
| **Werkt in** | Claude Code op macOS met Xcode |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/conorluddy/ios-simulator-skill](https://github.com/conorluddy/ios-simulator-skill) |

## Wat doet het?

Met deze skill kan Claude de iOS Simulator bedienen: apps bouwen en installeren, tikken en navigeren via de toegankelijkheidsboom, screenshots maken, logs lezen en problemen debuggen. De 30 scripts zijn geoptimaliseerd voor zowel mensen als agents.

## Wanneer gebruik je het?

* Je wilt dat Claude zelf controleert of zijn wijziging in de app werkt.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Bouw de app, open hem in de iPhone-simulator en test of het onboardingscherm goed werkt.
```
{% endcode %}

**Wat je krijgt:** Een testverslag met screenshots.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add conorluddy/ios-simulator-skill
/plugin install ios-simulator-skill@conorluddy
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Liever een MCP-server? De maker heeft ook XC-MCP.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/conorluddy/ios-simulator-skill" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Apps & mobiel</a>
