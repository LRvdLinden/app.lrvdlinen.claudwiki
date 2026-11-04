---
description: >-
  Eén zoekvraag over al je bedrijfstools: mail, chat, documenten en wiki's.
icon: magnifying-glass
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

# Zoeken in de organisatie (rol-plugin)

| | |
| --- | --- |
| **Maker** | Anthropic (officieel) |
| **Werkt in** | Claude-app (desktop), Claude Code |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/anthropics/knowledge-work-plugins/tree/main/enterprise-search](https://github.com/anthropics/knowledge-work-plugins/tree/main/enterprise-search) |

## Wat doet het?

De rol-plugin **enterprise-search** van Anthropic bundelt skills, commando's en koppelingen voor deze functie. Eén zoekvraag over al je bedrijfstools: mail, chat, documenten en wiki's. Je roept de onderdelen aan als `/enterprise-search:<skill>`.

**Skills in deze plugin:** `search`, `search-strategy`, `digest`, `knowledge-synthesis`, `source-management`.

Zie ook het [overzicht van alle rol-plugins](knowledge-work-plugins.md).

## Wanneer gebruik je het?

* Je werkt in deze rol en wilt vaste, goede workflows.
* Je wilt de plugin aanpassen met je eigen tools en werkwijze.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
/enterprise-search:search
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
claude plugin install enterprise-search@knowledge-work-plugins
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Pas de plugin aan je eigen tools aan via het bestand `.mcp.json` in de plugin.
{% endhint %}


<a href="https://github.com/anthropics/knowledge-work-plugins/tree/main/enterprise-search" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Zakelijk per rol</a>
