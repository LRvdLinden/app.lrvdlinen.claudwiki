---
description: >-
  Laat Claude echte acties doen in 1000+ apps: mail versturen, issues maken, berichten posten.
icon: link
cover: ../../.gitbook/assets/cover-productiviteit.png
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

# Connect Apps (Composio)

| | |
| --- | --- |
| **Maker** | Composio (community) |
| **Werkt in** | Claude Code |
| **Kosten** | Gratis te starten; Composio-account nodig |
| **Bron** | [github.com/ComposioHQ/awesome-claude-skills/tree/master/connect-apps-plugin](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/connect-apps-plugin) |

## Wat doet het?

Met deze plugin voert Claude acties uit in externe apps zoals Gmail, Slack en GitHub. Composio regelt het inloggen en verbindt met meer dan duizend apps. De repo bevat ook honderden 'automation'-skills per app.

## Wanneer gebruik je het?

* Je wilt dat Claude dingen dóét in je apps, niet alleen tekst schrijft.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Stuur een samenvatting van deze vergadering naar het team in Slack.
```
{% endcode %}

**Wat je krijgt:** Een bericht in je Slack-kanaal.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
```bash
git clone https://github.com/ComposioHQ/awesome-claude-skills.git
cd awesome-claude-skills
claude --plugin-dir ./connect-apps-plugin
```

Volg daarna de setup in de README.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* In de Claude-app kun je veel apps ook rechtstreeks koppelen via **Instellingen → Connectors**.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/ComposioHQ/awesome-claude-skills/tree/master/connect-apps-plugin" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Productiviteit & tools</a>
