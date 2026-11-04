---
description: >-
  Send and receive email with Resend: API, agent inbox, React Email and good deliverability.
icon: envelope
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

# Resend

| | |
| --- | --- |
| **Maker** | Resend · official Claude marketplace |
| **Works in** | Claude Code |
| **Cost** | Plugin free; requires a Resend account |
| **Source** | [resend.com](https://resend.com) |

## What does it do?

Skills from Resend for email in your app: the email API, an inbox for agents, the CLI, React Email components and deliverability best practices (so your mail doesn't land in spam). Includes the Resend MCP server.

## When do you use it?

* Your app needs to send emails, like a welcome mail or password reset.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Create a welcome email with React Email and send it via Resend after sign-up.
```
{% endcode %}

**What you get:** An email template and the sending code.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install resend@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://resend.com" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Data, cloud & payments</a>
