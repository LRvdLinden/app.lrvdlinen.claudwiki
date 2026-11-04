---
description: >-
  Gesprekken voorbereiden, samenvatten en opvolgen, accounts onderzoeken, je pipeline bewaken en outreach schrijven.
icon: chart-line
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

# Sales (rol-plugin)

| | |
| --- | --- |
| **Maker** | Anthropic (officieel) |
| **Werkt in** | Claude-app (desktop), Claude Code |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/anthropics/knowledge-work-plugins/tree/main/sales](https://github.com/anthropics/knowledge-work-plugins/tree/main/sales) |

## Wat doet het?

De rol-plugin **sales** van Anthropic bundelt skills, commando's en koppelingen voor deze functie. Gesprekken voorbereiden, samenvatten en opvolgen, accounts onderzoeken, je pipeline bewaken en outreach schrijven. Je roept de onderdelen aan als `/sales:<skill>`.

**Skills in deze plugin:** `call-prep`, `call-summary`, `account-research`, `daily-briefing`, `deal-review`, `draft-outreach`, `forecast`, `handle-objection`, `pipeline-review`, `win-loss-review`.

Zie ook het [overzicht van alle rol-plugins](knowledge-work-plugins.md).

## Wanneer gebruik je het?

* Je werkt in deze rol en wilt vaste, goede workflows.
* Je wilt de plugin aanpassen met je eigen tools en werkwijze.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
/sales:call-prep Gesprek met een nieuwe klant morgen om 10:00
```
{% endcode %}

**Wat je krijgt:** Een voorbereiding met achtergrond, vragen en doelen.

## Installeren

{% tabs %}
{% tab title="Claude-app" %}
Installeer de plugin in de Claude-desktopapp via [claude.com/plugins](https://claude.com/plugins/). Skills gaan vanzelf aan en de commando's verschijnen in je sessie.
{% endtab %}

{% tab title="Claude Code" %}
```bash
claude plugin marketplace add anthropics/knowledge-work-plugins
claude plugin install sales@knowledge-work-plugins
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Pas de plugin aan je eigen tools aan via het bestand `.mcp.json` in de plugin.
{% endhint %}


<a href="https://github.com/anthropics/knowledge-work-plugins/tree/main/sales" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Zakelijk per rol</a>
