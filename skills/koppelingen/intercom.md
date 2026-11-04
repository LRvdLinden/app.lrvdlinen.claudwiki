---
description: >-
  Zoek in klantgesprekken, analyseer supportpatronen en zoek contacten en bedrijven op.
icon: comments
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

# Intercom

| | |
| --- | --- |
| **Maker** | Intercom · officiële Claude-marketplace |
| **Werkt in** | Claude Code |
| **Kosten** | Plugin gratis; je hebt een Intercom-werkruimte nodig |
| **Bron** | [github.com/intercom/claude-plugin-external](https://github.com/intercom/claude-plugin-external) |

## Wat doet het?

De Intercom-plugin geeft Claude realtime inzicht in je klantcontact: gesprekken doorzoeken, patronen in supportvragen analyseren, contacten en bedrijven opzoeken en zelfs de Intercom Messenger installeren.

## Wanneer gebruik je het?

* Je doet klantenservice via Intercom.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Wat zijn de vijf meest gestelde vragen van deze maand?
```
{% endcode %}

**Wat je krijgt:** Een top 5 met voorbeelden.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install intercom@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/intercom/claude-plugin-external" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Apps koppelen</a>
