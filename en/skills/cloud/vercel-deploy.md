---
description: >-
  Manage deployments, check build status and logs and configure domains on Vercel.
icon: rocket
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

# Vercel (deployen)

| | |
| --- | --- |
| **Maker** | Vercel · official Claude marketplace |
| **Works in** | Claude Code |
| **Cost** | Plugin free; requires a Vercel account |
| **Source** | [github.com/vercel/vercel-plugin](https://github.com/vercel/vercel-plugin) |

## What does it do?

The Vercel plugin lets Claude control your frontend infrastructure: manage deployments, check build status and logs and configure domains. Combine with the [Vercel Agent Skills](../ontwikkeling/vercel-agent-skills.md) for best practices.

## When do you use it?

* You host your website or app on Vercel.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Why did the last deployment fail? Show me the build log.
```
{% endcode %}

**What you get:** The error from the log and a fix.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install vercel@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/vercel/vercel-plugin" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Data, cloud & payments</a>
