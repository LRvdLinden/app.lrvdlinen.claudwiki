---
description: >-
  Maakt een interactief HTML-rapport van je Claude Code-gebruik: tokens, cache, subagents, skills en de duurste prompts.
icon: chart-pie
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

# Session Report

| | |
| --- | --- |
| **Maker** | Anthropic · officiële Claude-marketplace |
| **Werkt in** | Claude Code |
| **Kosten** | Gratis |
| **Bron** | [github.com/anthropics/claude-plugins-official/tree/main/plugins/session-report](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/session-report) |

## Wat doet het?

Session Report leest je lokale Claude Code-transcripten en maakt er een verkenbaar HTML-rapport van: hoeveel tokens je gebruikte, hoe goed de cache werkte, welke subagents en skills draaiden en welke prompts het meest kostten.

## Wanneer gebruik je het?

* Je wilt weten waar je gebruik naartoe gaat.
* Je wilt je prompts efficiënter maken.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
/session-report
```
{% endcode %}

**Wat je krijgt:** Een HTML-rapport over je recente sessies.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install session-report@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.
{% endtab %}
{% endtabs %}


<a href="https://github.com/anthropics/claude-plugins-official/tree/main/plugins/session-report" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Ontwikkelen & code</a>
