---
description: >-
  De Superpowers-aanpak om skills te schrijven en te testen, net als code.
icon: pen-ruler
cover: ../../.gitbook/assets/cover-bouwen.png
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

# Writing Skills (Superpowers)

| | |
| --- | --- |
| **Maker** | obra (community) |
| **Werkt in** | Claude Code |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/obra/superpowers/tree/main/skills/writing-skills](https://github.com/obra/superpowers/tree/main/skills/writing-skills) |

## Wat doet het?

Onderdeel van [Superpowers](../denken/superpowers.md). Deze skill behandelt het schrijven van skills als softwareontwikkeling: eerst testen of Claude zonder de skill de fout maakt, dan de skill schrijven en daarna controleren of hij het gedrag echt verandert.

## Wanneer gebruik je het?

* Je wilt skills die aantoonbaar werken.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Schrijf een skill die ervoor zorgt dat je altijd eerst de tests draait voor een commit.
```
{% endcode %}

**Wat je krijgt:** Een geteste skill.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install superpowers@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.

Writing Skills zit in het Superpowers-pakket.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/obra/superpowers/tree/main/skills/writing-skills" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Zelf skills bouwen</a>
