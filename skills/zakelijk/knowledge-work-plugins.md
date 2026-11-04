---
description: >-
  Kant-en-klare pakketten met skills, commando's en koppelingen per functie: sales, finance, legal, marketing en meer.
icon: briefcase
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

# Rol-plugins van Anthropic

| | |
| --- | --- |
| **Maker** | Anthropic (officieel) |
| **Werkt in** | Claude-app (desktop), Claude Code |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |

## Wat doet het?

Anthropic heeft per functie een plugin gemaakt. Elke plugin bundelt **skills** (domeinkennis die Claude automatisch gebruikt), **commando's** (zoals `/sales:call-prep` of `/data:write-query`) en **connectors** naar de tools van die rol (Slack, HubSpot, Notion, Jira, Snowflake…). Ze zijn bedoeld als startpunt: pas ze aan met je eigen termen, processen en tools.

| Plugin | Waarvoor |
| --- | --- |
| `productivity` | **Productiviteit**: Taken, agenda's, dagelijkse workflows en persoonlijke context |
| `sales` | **Sales**: Prospects onderzoeken, calls voorbereiden, pipeline, outreach en battlecards |
| `customer-support` | **Klantenservice**: Tickets triëren, antwoorden opstellen, escalaties en kennisbankartikelen |
| `product-management` | **Productmanagement**: Specs, roadmaps, gebruikersonderzoek en stakeholder-updates |
| `marketing` | **Marketing**: Content, campagnes, merkstem, concurrentie en rapportages |
| `legal` | **Juridisch**: Contracten reviewen, NDA's triëren, compliance en risico's |
| `finance` | **Finance**: Journaalposten, afstemmingen, jaarrekeningen en audits |
| `data` | **Data**: SQL, statistiek, dashboards en validatie |
| `design` | **Design**: Design-kritiek, toegankelijkheid, handoff, UX-copy en onderzoek |
| `engineering` | **Engineering**: Architectuur, reviews, debuggen, incidenten en standups |
| `human-resources` | **HR**: Werving, onboarding, beoordelingen en beleid |
| `operations` | **Operations**: Processen, risico's, runbooks en statusrapporten |
| `enterprise-search` | **Zoeken in de organisatie**: Eén zoekvraag over mail, chat, documenten en wiki's |
| `small-business` | **Mkb / kleine ondernemers**: Facturen najagen, cashflow, social content, offertes en meer |
| `bio-research` | **Bio-onderzoek**: Literatuur, genomics en preklinisch onderzoek |

## Wanneer gebruik je het?

* Je wilt Claude als specialist voor een bepaalde rol inzetten.
* Je wilt dat je team consistente uitkomsten krijgt.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
/sales:call-prep Gesprek met een gemeente over een nieuwe buurt-app
```
{% endcode %}

**Wat je krijgt:** Een gespreksvoorbereiding met achtergrond en vragen.

{% code title="Voorbeeld 2: wat je typt" overflow="wrap" %}
```
/small-business:invoice-chase
```
{% endcode %}

**Wat je krijgt:** Overzicht van openstaande facturen met conceptherinneringen.

## Installeren

{% tabs %}
{% tab title="Claude-app" %}
Installeer de plugins in de Claude-desktopapp via [claude.com/plugins](https://claude.com/plugins/). Ze activeren zichzelf; skills gaan automatisch aan en de commando's verschijnen in je sessie.
{% endtab %}

{% tab title="Claude Code" %}
```bash
claude plugin marketplace add anthropics/knowledge-work-plugins
claude plugin install sales@knowledge-work-plugins
```

Vervang `sales` door de plugin die je wilt.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Gebruik de plugin `cowork-plugin-management` om zelf een plugin voor jouw rol te maken of aan te passen.
{% endhint %}


<a href="https://github.com/anthropics/knowledge-work-plugins" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Zakelijk per rol</a>
