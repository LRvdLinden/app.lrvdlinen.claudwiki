---
description: >-
  E-mail versturen en ontvangen met Resend: API, agent-inbox, React Email en goede bezorgbaarheid.
icon: envelope
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

# Resend

| | |
| --- | --- |
| **Maker** | Resend · officiële Claude-marketplace |
| **Werkt in** | Claude Code |
| **Kosten** | Plugin gratis; je hebt een account bij Resend nodig |
| **Bron** | [resend.com](https://resend.com) |

## Wat doet het?

Skills van Resend voor e-mail in je app: de e-mail-API, een inbox voor agents, de CLI, React Email-componenten en best practices voor bezorgbaarheid (zodat je mail niet in spam belandt). Inclusief de Resend MCP-server.

## Wanneer gebruik je het?

* Je app moet e-mails versturen, zoals een welkomstmail of wachtwoordreset.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Maak een welkomstmail met React Email en verstuur hem via Resend na registratie.
```
{% endcode %}

**Wat je krijgt:** Een e-mailtemplate en de verzendcode.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install resend@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://resend.com" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Data, cloud & betalen</a>
