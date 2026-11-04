---
description: >-
  Zoek en maak Jira-issues, beheer sprints en lees Confluence-documentatie.
icon: atlassian
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

# Atlassian (Jira & Confluence)

| | |
| --- | --- |
| **Maker** | Atlassian · officiële Claude-marketplace |
| **Werkt in** | Claude Code |
| **Kosten** | Plugin gratis; je hebt een Atlassian-account nodig |
| **Bron** | [github.com/atlassian/atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server) |

## Wat doet het?

De Atlassian-plugin verbindt Claude met Jira en Confluence. Claude zoekt en maakt issues, beheert sprints en raadpleegt documentatie in Confluence, zodat je ontwikkelwerk en documentatie op één lijn blijven.

## Wanneer gebruik je het?

* Je organisatie werkt met Jira of Confluence.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Welke Jira-issues staan nog open in de huidige sprint en wie is eigenaar?
```
{% endcode %}

**Wat je krijgt:** Een overzicht per eigenaar.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install atlassian@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/atlassian/atlassian-mcp-server" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Apps koppelen</a>
