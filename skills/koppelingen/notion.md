---
description: >-
  Zoek in Notion, maak en wijzig pagina's en beheer databases vanuit Claude.
icon: book
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

# Notion

| | |
| --- | --- |
| **Maker** | Notion · officiële Claude-marketplace |
| **Werkt in** | Claude Code |
| **Kosten** | Plugin gratis; je hebt een account bij Notion nodig |
| **Bron** | [github.com/makenotion/claude-code-notion-plugin](https://github.com/makenotion/claude-code-notion-plugin) |

## Wat doet het?

De Notion-plugin geeft Claude toegang tot je Notion-werkruimte. Hij zoekt pagina's op, maakt nieuwe documenten, werkt bestaande bij en beheert databases. Handig als je documentatie, notulen of planningen in Notion bijhoudt.

## Wanneer gebruik je het?

* Je team werkt in Notion.
* Je wilt dat Claude documentatie direct op de juiste plek zet.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Zet de notulen van vandaag als nieuwe pagina in de Notion-database 'Vergaderingen'.
```
{% endcode %}

**Wat je krijgt:** Een nieuwe Notion-pagina met de notulen.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install notion@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/makenotion/claude-code-notion-plugin" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Apps koppelen</a>
