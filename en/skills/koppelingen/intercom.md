---
description: >-
  Search customer conversations, analyse support patterns and look up contacts and companies.
icon: comments
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

# Intercom

| | |
| --- | --- |
| **Maker** | Intercom · official Claude marketplace |
| **Works in** | Claude Code |
| **Cost** | Plugin free; requires a Intercom account |
| **Source** | [github.com/intercom/claude-plugin-external](https://github.com/intercom/claude-plugin-external) |

## What does it do?

The Intercom plugin gives Claude real-time insight into your customer contact: search conversations, analyse patterns in support questions, look up contacts and companies and even install the Intercom Messenger.

## When do you use it?

* You do customer support through Intercom.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
What are the five most-asked questions this month?
```
{% endcode %}

**What you get:** A top 5 with examples.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install intercom@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/intercom/claude-plugin-external" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Connect your apps</a>
