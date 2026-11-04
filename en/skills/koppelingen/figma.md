---
description: >-
  Read Figma designs, extract components and design tokens and turn designs into code.
icon: figma
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

# Figma

| | |
| --- | --- |
| **Maker** | Figma · official Claude marketplace |
| **Works in** | Claude Code |
| **Cost** | Plugin free; requires a Figma account |
| **Source** | [github.com/figma/mcp-server-guide](https://github.com/figma/mcp-server-guide) |

## What does it do?

With the Figma plugin Claude looks straight into your Figma files. It reads frames and components, pulls out colours, typography and spacing (design tokens) and turns a design into working code. No more retyping between design and development.

## When do you use it?

* You design in Figma and want to bring it to code quickly.
* You want the code to use exactly the same colours and spacing as the design.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Rebuild the 'Settings' screen from my Figma file in SwiftUI.
```
{% endcode %}

**What you get:** SwiftUI code that follows the design, with the right colours and sizes.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install figma@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/figma/mcp-server-guide" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Connect your apps</a>
