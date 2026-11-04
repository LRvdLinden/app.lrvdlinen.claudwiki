---
description: >-
  Kant-en-klare workflows om je bedrijf te runnen: facturen najagen, cashflow, social content, offertes, belasting en meer. Bij geld of klanten keur jij elke stap goed.
icon: store
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

# Mkb / kleine ondernemers (rol-plugin)

| | |
| --- | --- |
| **Maker** | Anthropic (officieel) |
| **Werkt in** | Claude-app (desktop), Claude Code |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/anthropics/knowledge-work-plugins/tree/main/small-business](https://github.com/anthropics/knowledge-work-plugins/tree/main/small-business) |

## Wat doet het?

De rol-plugin **small-business** van Anthropic bundelt skills, commando's en koppelingen voor deze functie. Kant-en-klare workflows om je bedrijf te runnen: facturen najagen, cashflow, social content, offertes, belasting en meer. Bij geld of klanten keur jij elke stap goed. Je roept de onderdelen aan als `/small-business:<skill>`.

**Skills in deze plugin:** `monday-brief`, `invoice-chase`, `cash-flow-snapshot`, `proposal-builder`, `social-content-engine`, `lead-finder`, `tax-prep`, `review-reputation`, `payroll-prep`, `close-month`.

Zie ook het [overzicht van alle rol-plugins](knowledge-work-plugins.md).

## Wanneer gebruik je het?

* Je werkt in deze rol en wilt vaste, goede workflows.
* Je wilt de plugin aanpassen met je eigen tools en werkwijze.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
/small-business:invoice-chase
```
{% endcode %}

**Wat je krijgt:** Openstaande facturen met conceptherinneringen.

## Installeren

{% tabs %}
{% tab title="Claude-app" %}
Installeer de plugin in de Claude-desktopapp via [claude.com/plugins](https://claude.com/plugins/). Skills gaan vanzelf aan en de commando's verschijnen in je sessie.
{% endtab %}

{% tab title="Claude Code" %}
```bash
claude plugin marketplace add anthropics/knowledge-work-plugins
claude plugin install small-business@knowledge-work-plugins
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Pas de plugin aan je eigen tools aan via het bestand `.mcp.json` in de plugin.
{% endhint %}


<a href="https://github.com/anthropics/knowledge-work-plugins/tree/main/small-business" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Zakelijk per rol</a>
