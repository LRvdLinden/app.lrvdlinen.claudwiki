---
description: >-
  Actuele naslag voor bouwen met de Claude API en SDK's: modellen, prijzen, tools, streaming en caching.
icon: server
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

# Claude API

| | |
| --- | --- |
| **Maker** | Anthropic (officieel) |
| **Werkt in** | Claude Code, Claude-app, API |
| **Kosten** | Gratis |
| **Bron** | [github.com/anthropics/skills/tree/main/skills/claude-api](https://github.com/anthropics/skills/tree/main/skills/claude-api) |

## Wat doet het?

Deze skill zorgt dat Claude bij het bouwen van AI-toepassingen niet uit zijn geheugen werkt, maar de actuele documentatie gebruikt: model-ID's, prijzen, parameters, streaming, tool use, MCP, agents, prompt caching en migratie tussen modellen.

## Wanneer gebruik je het?

* Je bouwt een app die de Claude API gebruikt.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Voeg aan mijn app een functie toe die meldingen samenvat met de Claude API, met prompt caching.
```
{% endcode %}

**Wat je krijgt:** Code die de juiste, actuele API-aanroepen gebruikt.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add anthropics/skills
/plugin install claude-api@anthropic-agent-skills
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.
{% endtab %}

{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add anthropics/skills --skill claude-api
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}


<a href="https://github.com/anthropics/skills/tree/main/skills/claude-api" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Ontwikkelen & code</a>
