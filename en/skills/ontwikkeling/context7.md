---
description: >-
  Fetches up-to-date, version-specific documentation and code examples, so Claude doesn't use outdated APIs.
icon: book-open
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

# Context7

| | |
| --- | --- |
| **Maker** | Upstash · official Claude marketplace |
| **Works in** | Claude Code |
| **Cost** | Free |
| **Source** | [github.com/anthropics/claude-plugins-public/tree/main/external_plugins/context7](https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/context7) |

## What does it do?

Context7 (by Upstash) connects Claude to a hosted documentation service. Claude pulls the documentation and code examples for exactly the version of a library you use. No local Node.js required.

## When do you use it?

* Claude uses functions that don't (or no longer) exist in your version.
* You work with a fast-changing framework.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Use context7 and build this with the latest version of Next.js.
```
{% endcode %}

**What you get:** Code that follows the current documentation.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install context7@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/context7" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Development & code</a>
