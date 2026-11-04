---
description: >-
  Officiële MongoDB-plugin: verbinden, data verkennen, query's optimaliseren en betrouwbare code genereren.
icon: leaf
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

# MongoDB

| | |
| --- | --- |
| **Maker** | MongoDB · officiële Claude-marketplace |
| **Werkt in** | Claude Code |
| **Kosten** | Gratis |
| **Bron** | [www.mongodb.com/docs/mcp-server/overview/](https://www.mongodb.com/docs/mcp-server/overview/) |

## Wat doet het?

De officiële MongoDB-plugin (MCP-server plus skills) laat Claude verbinden met je databases, data verkennen, collecties beheren, query's optimaliseren en code schrijven volgens de best practices.

## Wanneer gebruik je het?

* Je gebruikt MongoDB of MongoDB Atlas.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Waarom is deze query traag? Stel een index voor.
```
{% endcode %}

**Wat je krijgt:** Een analyse en een passende index.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install mongodb@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://www.mongodb.com/docs/mcp-server/overview/" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Data, cloud & betalen</a>
