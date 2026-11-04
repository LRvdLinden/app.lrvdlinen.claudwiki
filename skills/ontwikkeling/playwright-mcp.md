---
description: >-
  De Playwright MCP-server van Microsoft: Claude bedient een browser, maakt screenshots en test je webapp.
icon: masks-theater
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

# Playwright (MCP)

| | |
| --- | --- |
| **Maker** | Microsoft · officiële Claude-marketplace |
| **Werkt in** | Claude Code |
| **Kosten** | Gratis |
| **Bron** | [github.com/anthropics/claude-plugins-public/tree/main/external_plugins/playwright](https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/playwright) |

## Wat doet het?

Met deze plugin krijgt Claude een echte browser via de Playwright MCP-server van Microsoft. Hij opent pagina's, klikt, vult formulieren in, maakt screenshots en voert end-to-end-tests uit.

## Wanneer gebruik je het?

* Je wilt dat Claude zelf controleert of je website werkt.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Open mijn site, log in met het testaccount en controleer of het dashboard laadt.
```
{% endcode %}

**Wat je krijgt:** Een testverslag met screenshots.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install playwright@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/playwright" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Ontwikkelen & code</a>
