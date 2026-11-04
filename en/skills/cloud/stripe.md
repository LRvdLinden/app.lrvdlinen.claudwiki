---
description: >-
  Official Stripe skills and best practices for payments, Connect and API upgrades.
icon: stripe
cover: ../../../.gitbook/assets/cover-en-cloud.png
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
| **Maker** | Stripe (official, by the makers) |
| **Works in** | Claude Code (+ other agents) |
| **Cost** | Free |
| **Source** | [github.com/stripe/ai](https://github.com/stripe/ai) |

## What does it do?

Stripe's own skills: best practices for payments, Stripe Connect, Stripe Apps, looking up documentation and upgrading the API. Combined with the Stripe MCP server, Claude can work with your Stripe account safely.

## When do you use it?

* You want payments or subscriptions in your app or website.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Add a monthly subscription with Stripe Checkout and a webhook.
```
{% endcode %}

**What you get:** Checkout integration plus webhook handler.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install stripe@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.
{% endtab %}

{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills add https://docs.stripe.com
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Manually installed skills don't update themselves: `npx skills update -y`.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/stripe/ai" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Data, cloud & payments</a>
