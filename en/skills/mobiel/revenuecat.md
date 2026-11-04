---
description: >-
  Set up in-app purchases and subscriptions: products, entitlements and offerings in RevenueCat.
icon: cart-shopping
cover: ../../../.gitbook/assets/cover-en-mobiel.png
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

# RevenueCat

| | |
| --- | --- |
| **Maker** | RevenueCat · official Claude marketplace |
| **Works in** | Claude Code |
| **Cost** | Plugin free; requires a RevenueCat account |
| **Source** | [www.revenuecat.com](https://www.revenuecat.com) |

## What does it do?

With the RevenueCat plugin Claude configures your in-app purchases: projects, apps, products, entitlements and offerings, without opening the RevenueCat dashboard. Ideal for iOS and Android apps with subscriptions.

## When do you use it?

* You want a subscription or one-time purchase in your app.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Create a 'Pro' offering with a monthly and a yearly subscription.
```
{% endcode %}

**What you get:** A ready-made offering in RevenueCat.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install revenuecat@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://www.revenuecat.com" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Apps & mobile</a>
