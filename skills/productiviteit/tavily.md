---
description: >-
  Realtime webdata voor je AI-apps: zoeken, uitlezen, crawlen en onderzoek via de Tavily-API's.
icon: globe
cover: ../../.gitbook/assets/cover-productiviteit.png
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

# Tavily

| | |
| --- | --- |
| **Maker** | Tavily · officiële Claude-marketplace |
| **Werkt in** | Claude Code |
| **Kosten** | Plugin gratis; je hebt een API-sleutel van Tavily nodig |
| **Bron** | [www.tavily.com/](https://www.tavily.com/) |

## Wat doet het?

Met de Tavily-plugin bouwt Claude AI-toepassingen die actuele webdata gebruiken via de zoek-, extract-, crawl- en research-API's van Tavily.

## Wanneer gebruik je het?

* Je bouwt een app die actuele informatie van het web nodig heeft.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Bouw een functie die elke ochtend het nieuws over mijn gemeente samenvat.
```
{% endcode %}

**Wat je krijgt:** Code die Tavily gebruikt om nieuws op te halen.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install tavily@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://www.tavily.com/" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Productiviteit & tools</a>
