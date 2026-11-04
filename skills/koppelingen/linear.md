---
description: >-
  Issues maken en bijwerken, projecten beheren en zoeken in Linear.
icon: list-check
cover: ../../.gitbook/assets/cover-koppelingen.png
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

# Linear

| | |
| --- | --- |
| **Maker** | Linear · officiële Claude-marketplace |
| **Werkt in** | Claude Code |
| **Kosten** | Plugin gratis; je hebt een account bij Linear nodig |
| **Bron** | [github.com/anthropics/claude-plugins-public/tree/main/external_plugins/linear](https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/linear) |

## Wat doet het?

Met de Linear-plugin maakt Claude issues aan, beheert projecten, werkt statussen bij en zoekt in je werkruimtes. Ideaal om bugs of taken direct vanuit je code in Linear te zetten.

## Wanneer gebruik je het?

* Je plant je softwarewerk in Linear.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Zet deze drie bugs als issues in Linear, project 'App 2.0', met prioriteit hoog.
```
{% endcode %}

**Wat je krijgt:** Drie nieuwe Linear-issues.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install linear@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/linear" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Apps koppelen</a>
