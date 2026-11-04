---
description: >-
  Have Claude explain what it does (Explanatory) or let you write pieces of code yourself to learn from (Learning).
icon: chalkboard-user
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

# Learning & Explanatory output styles

| | |
| --- | --- |
| **Maker** | Anthropic · official Claude marketplace |
| **Works in** | Claude Code |
| **Cost** | Free |
| **Source** | [github.com/anthropics/claude-plugins-public/tree/main/plugins/learning-output-style](https://github.com/anthropics/claude-plugins-public/tree/main/plugins/learning-output-style) |

## What does it do?

Two plugins from Anthropic that change how Claude answers. **learning-output-style** asks you to write a bit of code yourself at key moments, so you learn instead of just watching. **explanatory-output-style** adds explanations about why Claude makes certain choices and which patterns are in your codebase.

## When do you use it?

* You want to learn to code while building with Claude.
* You want to understand why Claude does something a certain way.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
(after installing) Add a search feature to my app.
```
{% endcode %}

**What you get:** Claude builds with you and lets you write the key part, with explanations.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install learning-output-style@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.

{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* For the explanatory variant: `/plugin install explanatory-output-style@claude-plugins-official`.
{% endhint %}

<a href="https://github.com/anthropics/claude-plugins-public/tree/main/plugins/learning-output-style" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Development & code</a>
