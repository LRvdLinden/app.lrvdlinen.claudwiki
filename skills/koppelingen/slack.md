---
description: >-
  Zoek in Slack-berichten, lees kanalen en threads en vind snel eerdere discussies.
icon: slack
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

# Slack

| | |
| --- | --- |
| **Maker** | Slack · officiële Claude-marketplace |
| **Werkt in** | Claude Code |
| **Kosten** | Plugin gratis; je hebt een Slack-werkruimte nodig |
| **Bron** | [github.com/slackapi/slack-mcp-plugin/tree/main](https://github.com/slackapi/slack-mcp-plugin/tree/main) |

## Wat doet het?

Met de Slack-plugin zoekt Claude in je Slack-werkruimte: berichten, kanalen en threads. Zo vindt hij snel de context van een eerdere discussie of beslissing, zonder dat je zelf hoeft te scrollen.

## Wanneer gebruik je het?

* Belangrijke afspraken staan ergens in Slack.
* Je wilt een samenvatting van een drukke thread.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Wat is er vorige week in #ontwikkeling besloten over de release?
```
{% endcode %}

**Wat je krijgt:** Een samenvatting met links naar de berichten.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install slack@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/slackapi/slack-mcp-plugin/tree/main" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Apps koppelen</a>
