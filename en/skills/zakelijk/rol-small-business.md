---
description: >-
  Ready-made workflows to run your business: chasing invoices, cash flow, social content, proposals, taxes and more. You approve every step that touches money or customers.
icon: store
cover: ../../../.gitbook/assets/cover-en-zakelijk.png
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

# Small business (role plugin)

| | |
| --- | --- |
| **Maker** | Anthropic (official) |
| **Works in** | Claude app (desktop), Claude Code |
| **Cost** | Free (open source) |
| **Source** | [github.com/anthropics/knowledge-work-plugins/tree/main/small-business](https://github.com/anthropics/knowledge-work-plugins/tree/main/small-business) |

## What does it do?

Anthropic's **small-business** role plugin bundles skills, commands and connectors for this job function. Ready-made workflows to run your business: chasing invoices, cash flow, social content, proposals, taxes and more. You approve every step that touches money or customers. You call its parts as `/small-business:<skill>`.

**Skills in this plugin:** `monday-brief`, `invoice-chase`, `cash-flow-snapshot`, `proposal-builder`, `social-content-engine`, `lead-finder`, `tax-prep`, `review-reputation`, `payroll-prep`, `close-month`.

See also the [overview of all role plugins](knowledge-work-plugins.md).

## When do you use it?

* You work in or with this role and want solid, consistent workflows.
* You want to adapt the plugin to your own tools and way of working.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
/small-business:invoice-chase
```
{% endcode %}

**What you get:** Outstanding invoices with draft reminders.

## Install

{% tabs %}
{% tab title="Claude app" %}
Install the plugin in the Claude desktop app via [claude.com/plugins](https://claude.com/plugins/). Skills switch on automatically and the commands appear in your session.
{% endtab %}

{% tab title="Claude Code" %}
```bash
claude plugin marketplace add anthropics/knowledge-work-plugins
claude plugin install small-business@knowledge-work-plugins
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Adapt the plugin to your own tools through the plugin's `.mcp.json` file.
{% endhint %}

<a href="https://github.com/anthropics/knowledge-work-plugins/tree/main/small-business" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Business by role</a>
