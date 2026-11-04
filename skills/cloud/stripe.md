---
description: >-
  Officiële Stripe-skills en best practices voor betalingen, Connect en upgrades van de API.
icon: stripe
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

# Stripe

| | |
| --- | --- |
| **Maker** | Stripe (officieel van de makers) |
| **Werkt in** | Claude Code (+ andere agents) |
| **Kosten** | Gratis |
| **Bron** | [github.com/stripe/ai](https://github.com/stripe/ai) |

## Wat doet het?

Stripe's eigen skills: best practices voor betalingen, Stripe Connect, Stripe Apps, documentatie opzoeken en de API upgraden. Gecombineerd met de Stripe MCP-server kan Claude veilig met je Stripe-account werken.

## Wanneer gebruik je het?

* Je wilt betalingen of abonnementen in je app of website.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Voeg een maandabonnement toe met Stripe Checkout en een webhook.
```
{% endcode %}

**Wat je krijgt:** Checkout-integratie plus webhook-handler.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install stripe@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.
{% endtab %}

{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add https://docs.stripe.com
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Handmatig geïnstalleerde skills updaten niet vanzelf: `npx skills update -y`.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/stripe/ai" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Data, cloud & betalen</a>
