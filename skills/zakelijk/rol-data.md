---
description: >-
  SQL schrijven, datasets verkennen, statistische analyses, visualisaties en dashboards.
icon: database
cover: ../../.gitbook/assets/cover-zakelijk.png
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

# Data (rol-plugin)

| | |
| --- | --- |
| **Maker** | Anthropic (officieel) |
| **Werkt in** | Claude-app (desktop), Claude Code |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/anthropics/knowledge-work-plugins/tree/main/data](https://github.com/anthropics/knowledge-work-plugins/tree/main/data) |

## Wat doet het?

De rol-plugin **data** van Anthropic bundelt skills, commando's en koppelingen voor deze functie. SQL schrijven, datasets verkennen, statistische analyses, visualisaties en dashboards. Je roept de onderdelen aan als `/data:<skill>`.

**Skills in deze plugin:** `write-query`, `sql-queries`, `explore-data`, `statistical-analysis`, `create-viz`, `build-dashboard`, `validate-data`, `analyze`.

Zie ook het [overzicht van alle rol-plugins](knowledge-work-plugins.md).

## Wanneer gebruik je het?

* Je werkt in deze rol en wilt vaste, goede workflows.
* Je wilt de plugin aanpassen met je eigen tools en werkwijze.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
/data:write-query
```
{% endcode %}

**Wat je krijgt:** De bijbehorende workflow, stap voor stap.

## Installeren

{% tabs %}
{% tab title="Claude-app" %}
Installeer de plugin in de Claude-desktopapp via [claude.com/plugins](https://claude.com/plugins/). Skills gaan vanzelf aan en de commando's verschijnen in je sessie.
{% endtab %}

{% tab title="Claude Code" %}
```bash
claude plugin marketplace add anthropics/knowledge-work-plugins
claude plugin install data@knowledge-work-plugins
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Pas de plugin aan je eigen tools aan via het bestand `.mcp.json` in de plugin.
{% endhint %}


<a href="https://github.com/anthropics/knowledge-work-plugins/tree/main/data" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Zakelijk per rol</a>
