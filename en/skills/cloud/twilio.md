---
description: >-
  Knowledge for SMS, voice, WhatsApp, Verify, SendGrid and 30+ other Twilio products.
icon: comment-sms
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

# Twilio

| | |
| --- | --- |
| **Maker** | Twilio · official Claude marketplace |
| **Works in** | Claude Code |
| **Cost** | Plugin free; requires a Twilio account |
| **Source** | [www.twilio.com](https://www.twilio.com) |

## What does it do?

Twilio Skills tell Claude which APIs to use, in what order and what to avoid. They cover SMS, voice, WhatsApp, Verify (verification codes), SendGrid, compliance and more than thirty other products.

## When do you use it?

* You want SMS or WhatsApp notifications or two-factor authentication in your app.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Add two-factor authentication via SMS with Twilio Verify.
```
{% endcode %}

**What you get:** A working verification-code flow.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install twilio-developer-kit@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://www.twilio.com" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Data, cloud & payments</a>
