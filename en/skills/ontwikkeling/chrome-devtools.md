---
description: >-
  Control and inspect a live Chrome browser: performance traces, network traffic and console errors.
icon: chrome
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

# Chrome DevTools

| | |
| --- | --- |
| **Maker** | Google · official Claude marketplace |
| **Works in** | Claude Code |
| **Cost** | Free |
| **Source** | [github.com/ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) |

## What does it do?

With Chrome DevTools MCP Claude looks along in a real Chrome browser. It records performance traces, analyses network requests, reads console messages with source-mapped stack traces and automates actions with Puppeteer.

## When do you use it?

* Your website is slow and you want to know why.
* You're hunting a bug that only happens in the browser.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Record a performance trace of my homepage and tell me what makes it slow.
```
{% endcode %}

**What you get:** The biggest bottlenecks with concrete fixes.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install chrome-devtools-mcp@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/ChromeDevTools/chrome-devtools-mcp" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Development & code</a>
