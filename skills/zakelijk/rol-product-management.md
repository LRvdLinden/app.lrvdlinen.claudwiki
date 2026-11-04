---
description: >-
  Feature-specs schrijven, roadmaps plannen, gebruikersonderzoek samenvatten en stakeholders op de hoogte houden.
icon: diagram-project
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

# Productmanagement (rol-plugin)

| | |
| --- | --- |
| **Maker** | Anthropic (officieel) |
| **Werkt in** | Claude-app (desktop), Claude Code |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/anthropics/knowledge-work-plugins/tree/main/product-management](https://github.com/anthropics/knowledge-work-plugins/tree/main/product-management) |

## Wat doet het?

De rol-plugin **product-management** van Anthropic bundelt skills, commando's en koppelingen voor deze functie. Feature-specs schrijven, roadmaps plannen, gebruikersonderzoek samenvatten en stakeholders op de hoogte houden. Je roept de onderdelen aan als `/product-management:<skill>`.

**Skills in deze plugin:** `write-spec`, `roadmap-update`, `sprint-planning`, `synthesize-research`, `stakeholder-update`, `competitive-brief`, `metrics-review`, `product-brainstorming`.

Zie ook het [overzicht van alle rol-plugins](knowledge-work-plugins.md).

## Wanneer gebruik je het?

* Je werkt in deze rol en wilt vaste, goede workflows.
* Je wilt de plugin aanpassen met je eigen tools en werkwijze.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
/product-management:write-spec
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
claude plugin install product-management@knowledge-work-plugins
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Pas de plugin aan je eigen tools aan via het bestand `.mcp.json` in de plugin.
{% endhint %}


<a href="https://github.com/anthropics/knowledge-work-plugins/tree/main/product-management" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Zakelijk per rol</a>
