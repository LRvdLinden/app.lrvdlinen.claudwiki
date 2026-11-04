---
description: >-
  Postgres-databases beheren met Prisma: schema-migraties, SQL-query's en Prisma Postgres aanmaken.
icon: database
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

# Prisma

| | |
| --- | --- |
| **Maker** | Prisma · officiële Claude-marketplace |
| **Werkt in** | Claude Code |
| **Kosten** | Gratis |
| **Bron** | [prisma.io](https://prisma.io) |

## Wat doet het?

Met de Prisma-plugin maakt Claude Prisma Postgres-databases aan, voert schema-migraties uit, draait SQL-query's en beheert connection strings, rechtstreeks vanuit je ontwikkelomgeving.

## Wanneer gebruik je het?

* Je gebruikt Prisma als ORM.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Voeg een veld 'gelezen' toe aan Melding en maak de migratie.
```
{% endcode %}

**Wat je krijgt:** Een bijgewerkt schema en een migratie.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install prisma@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://prisma.io" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Data, cloud & betalen</a>
