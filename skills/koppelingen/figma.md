---
description: >-
  Lees Figma-ontwerpen, haal componenten en design tokens eruit en zet designs om naar code.
icon: figma
cover: ../../.gitbook/assets/cover-koppelingen.png
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

# Figma

| | |
| --- | --- |
| **Maker** | Figma · officiële Claude-marketplace |
| **Werkt in** | Claude Code |
| **Kosten** | Plugin gratis; je hebt een account bij Figma nodig |
| **Bron** | [github.com/figma/mcp-server-guide](https://github.com/figma/mcp-server-guide) |

## Wat doet het?

Met de Figma-plugin kijkt Claude rechtstreeks in je Figma-bestanden. Hij leest frames en componenten, haalt kleuren, typografie en spacing (design tokens) op en zet een ontwerp om naar werkende code. Zo verdwijnt het overtypen tussen design en development.

## Wanneer gebruik je het?

* Je ontwerpt in Figma en wilt het snel naar code brengen.
* Je wilt dat de code exact dezelfde kleuren en spacing gebruikt als het ontwerp.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Bouw het scherm 'Instellingen' uit mijn Figma-bestand na in SwiftUI.
```
{% endcode %}

**Wat je krijgt:** SwiftUI-code die het ontwerp volgt, met de juiste kleuren en maten.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install figma@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/figma/mcp-server-guide" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Apps koppelen</a>
