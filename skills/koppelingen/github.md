---
description: >-
  De officiële GitHub MCP-server: issues, pull requests, code reviews en repo's doorzoeken.
icon: github
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

# GitHub

| | |
| --- | --- |
| **Maker** | GitHub · officiële Claude-marketplace |
| **Werkt in** | Claude Code |
| **Kosten** | Plugin gratis; je hebt een GitHub-account nodig |
| **Bron** | [github.com/anthropics/claude-plugins-public/tree/main/external_plugins/github](https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/github) |

## Wat doet het?

Met de GitHub-plugin werkt Claude rechtstreeks met GitHub: issues aanmaken, pull requests beheren en reviewen, repositories doorzoeken en de volledige GitHub-API gebruiken vanuit Claude Code.

## Wanneer gebruik je het?

* Je beheert je code en issues op GitHub.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Maak issues aan voor alle TODO's in deze map en label ze als 'tech-debt'.
```
{% endcode %}

**Wat je krijgt:** Nieuwe GitHub-issues met labels.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install github@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/github" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Apps koppelen</a>
