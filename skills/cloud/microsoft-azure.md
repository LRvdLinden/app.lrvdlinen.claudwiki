---
description: >-
  Honderden skills van Microsoft voor Azure-SDK's, AKS, Application Insights en Microsoft AI Foundry.
icon: microsoft
cover: ../../.gitbook/assets/cover-cloud.png
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

# Microsoft Azure Skills

| | |
| --- | --- |
| **Maker** | Microsoft (officieel van de makers) |
| **Werkt in** | Claude Code (+ Copilot en andere agents) |
| **Kosten** | Gratis |
| **Bron** | [github.com/microsoft/skills](https://github.com/microsoft/skills) |

## Wat doet het?

Skills, agents, AGENTS.md-sjablonen en MCP-configuraties voor wie met Azure werkt: van Azure SDK's in Python, .NET, Java en TypeScript tot AKS-troubleshooting, kostenoptimalisatie en Microsoft AI Foundry. Er is ook een `deep-wiki`-plugin.

## Wanneer gebruik je het?

* Je bouwt op Azure of met Microsoft AI-diensten.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Voeg Application Insights toe aan deze Node-app.
```
{% endcode %}

**Wat je krijgt:** Instrumentatie volgens Microsoft's richtlijnen.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add microsoft/skills
/plugin install azure@skills
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.
{% endtab %}

{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add microsoft/skills
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Installeer niet alles tegelijk: kies de skills voor jouw taal en diensten.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/microsoft/skills" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Data, cloud & betalen</a>
