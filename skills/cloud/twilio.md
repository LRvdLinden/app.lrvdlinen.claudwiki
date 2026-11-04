---
description: >-
  Kennis voor sms, spraak, WhatsApp, Verify, SendGrid en 30+ andere Twilio-producten.
icon: comment-sms
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

# Twilio

| | |
| --- | --- |
| **Maker** | Twilio · officiële Claude-marketplace |
| **Werkt in** | Claude Code |
| **Kosten** | Plugin gratis; je hebt een Twilio-account nodig |
| **Bron** | [www.twilio.com](https://www.twilio.com) |

## Wat doet het?

Twilio Skills vertellen Claude welke API's je gebruikt, in welke volgorde en wat je moet vermijden. Ze dekken sms, spraak, WhatsApp, Verify (verificatiecodes), SendGrid, compliance en meer dan dertig andere producten.

## Wanneer gebruik je het?

* Je wilt sms- of WhatsApp-meldingen of tweestapsverificatie in je app.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Voeg tweestapsverificatie via sms toe met Twilio Verify.
```
{% endcode %}

**Wat je krijgt:** Werkende verificatiecode-flow.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install twilio-developer-kit@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://www.twilio.com" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Data, cloud & betalen</a>
