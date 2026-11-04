---
description: >-
  Standups, code reviews, architecture decisions, incident response and technical documentation.
icon: gears
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

# Engineering (role plugin)

| | |
| --- | --- |
| **Maker** | Anthropic (official) |
| **Works in** | Claude app (desktop), Claude Code |
| **Cost** | Free (open source) |
| **Source** | [github.com/anthropics/knowledge-work-plugins/tree/main/engineering](https://github.com/anthropics/knowledge-work-plugins/tree/main/engineering) |

## What does it do?

Anthropic's **engineering** role plugin bundles skills, commands and connectors for this job function. Standups, code reviews, architecture decisions, incident response and technical documentation. You call its parts as `/engineering:<skill>`.

**Skills in this plugin:** `standup`, `code-review`, `architecture`, `system-design`, `debug`, `incident-response`, `deploy-checklist`, `documentation`, `tech-debt`, `testing-strategy`.

See also the [overview of all role plugins](knowledge-work-plugins.md).

## When do you use it?

* You work in or with this role and want solid, consistent workflows.
* You want to adapt the plugin to your own tools and way of working.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
/engineering:standup
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
claude plugin install engineering@knowledge-work-plugins
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Adapt the plugin to your own tools through the plugin's `.mcp.json` file.
{% endhint %}

<a href="https://github.com/anthropics/knowledge-work-plugins/tree/main/engineering" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Business by role</a>
