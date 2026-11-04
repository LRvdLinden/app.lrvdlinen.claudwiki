---
description: >-
  Verbind meer dan 8.000 apps en voer Zapier-acties uit vanuit Claude.
icon: bolt
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

# Zapier

| | |
| --- | --- |
| **Maker** | Zapier · officiële Claude-marketplace |
| **Werkt in** | Claude Code |
| **Kosten** | Plugin gratis; je hebt een account bij Zapier nodig |
| **Bron** | [github.com/zapier/zapier-mcp/tree/main/plugins/zapier](https://github.com/zapier/zapier-mcp/tree/main/plugins/zapier) |

## Wat doet het?

De Zapier-plugin opent de deur naar meer dan 8.000 apps. Claude zoekt de juiste Zapier-actie, zet hem aan en voert hem uit: van een rij in Google Sheets tot een sms of een bericht in Teams.

## Wanneer gebruik je het?

* De app die je wilt koppelen heeft geen eigen plugin.
* Je gebruikt Zapier al voor automatiseringen.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Zet elke nieuwe aanmelding uit dit formulier in Google Sheets en stuur me een sms.
```
{% endcode %}

**Wat je krijgt:** Een werkende Zapier-actie.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install zapier@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/zapier/zapier-mcp/tree/main/plugins/zapier" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Apps koppelen</a>
