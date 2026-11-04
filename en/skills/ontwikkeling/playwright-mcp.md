---
description: >-
  Microsoft's Playwright MCP server: Claude drives a browser, takes screenshots and tests your web app.
icon: masks-theater
cover: ../../../.gitbook/assets/cover-en-ontwikkeling.png
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

# Playwright (MCP)

| | |
| --- | --- |
| **Maker** | Microsoft · official Claude marketplace |
| **Works in** | Claude Code |
| **Cost** | Free |
| **Source** | [github.com/anthropics/claude-plugins-public/tree/main/external_plugins/playwright](https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/playwright) |

## What does it do?

With this plugin Claude gets a real browser through Microsoft's Playwright MCP server. It opens pages, clicks, fills in forms, takes screenshots and runs end-to-end tests.

## When do you use it?

* You want Claude to check for itself that your website works.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Open my site, log in with the test account and check that the dashboard loads.
```
{% endcode %}

**What you get:** A test report with screenshots.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install playwright@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/playwright" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Development & code</a>
