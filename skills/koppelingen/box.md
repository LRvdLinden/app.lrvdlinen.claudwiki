---
description: >-
  Zoek en organiseer bestanden in Box en laat Box AI vragen beantwoorden over je documenten.
icon: box
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

# Box

| | |
| --- | --- |
| **Maker** | Box · officiële Claude-marketplace |
| **Werkt in** | Claude Code |
| **Kosten** | Plugin gratis; je hebt een account bij Box nodig |
| **Bron** | [github.com/box/skills](https://github.com/box/skills) |

## Wat doet het?

Met de Box-plugin zoekt Claude bestanden, ordent mappen en werkt samen met je team in Box. Via Box AI beantwoordt hij vragen, vat hij documenten samen en haalt hij gegevens eruit.

## Wanneer gebruik je het?

* Je organisatie bewaart documenten in Box.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Vat alle contracten in de map 'Leveranciers 2026' samen.
```
{% endcode %}

**Wat je krijgt:** Een samenvatting per contract.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install box@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/box/skills" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Apps koppelen</a>
