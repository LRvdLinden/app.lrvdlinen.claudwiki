---
description: >-
  Create content, plan campaigns, keep your brand voice consistent, track competitors and report results.
icon: bullhorn
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

# Marketing (role plugin)

| | |
| --- | --- |
| **Maker** | Anthropic (official) |
| **Works in** | Claude app (desktop), Claude Code |
| **Cost** | Free (open source) |
| **Source** | [github.com/anthropics/knowledge-work-plugins/tree/main/marketing](https://github.com/anthropics/knowledge-work-plugins/tree/main/marketing) |

## What does it do?

Anthropic's **marketing** role plugin bundles skills, commands and connectors for this job function. Create content, plan campaigns, keep your brand voice consistent, track competitors and report results. You call its parts as `/marketing:<skill>`.

**Skills in this plugin:** `content-creation`, `draft-content`, `campaign-plan`, `email-sequence`, `brand-review`, `competitive-brief`, `seo-audit`, `performance-report`.

See also the [overview of all role plugins](knowledge-work-plugins.md).

## When do you use it?

* You work in or with this role and want solid, consistent workflows.
* You want to adapt the plugin to your own tools and way of working.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
/marketing:content-creation
```
{% endcode %}

**What you get:** The matching workflow, step by step.

## Install

{% tabs %}
{% tab title="Claude app" %}
Install the plugin in the Claude desktop app via [claude.com/plugins](https://claude.com/plugins/). Skills switch on automatically and the commands appear in your session.
{% endtab %}

{% tab title="Claude Code" %}
```bash
claude plugin marketplace add anthropics/knowledge-work-plugins
claude plugin install marketing@knowledge-work-plugins
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Adapt the plugin to your own tools through the plugin's `.mcp.json` file.
{% endhint %}

<a href="https://github.com/anthropics/knowledge-work-plugins/tree/main/marketing" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Business by role</a>
