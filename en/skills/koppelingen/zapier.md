---
description: >-
  Connect 8,000+ apps and run Zapier actions from Claude.
icon: bolt
cover: ../../../.gitbook/assets/cover-en-koppelingen.png
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

# Zapier

| | |
| --- | --- |
| **Maker** | Zapier · official Claude marketplace |
| **Works in** | Claude Code |
| **Cost** | Plugin free; requires a Zapier account |
| **Source** | [github.com/zapier/zapier-mcp/tree/main/plugins/zapier](https://github.com/zapier/zapier-mcp/tree/main/plugins/zapier) |

## What does it do?

The Zapier plugin opens the door to more than 8,000 apps. Claude finds the right Zapier action, enables it and runs it: from a row in Google Sheets to a text message or a Teams message.

## When do you use it?

* The app you want to connect has no plugin of its own.
* You already use Zapier for automations.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Put every new sign-up from this form into Google Sheets and send me a text.
```
{% endcode %}

**What you get:** A working Zapier action.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install zapier@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/zapier/zapier-mcp/tree/main/plugins/zapier" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Connect your apps</a>
