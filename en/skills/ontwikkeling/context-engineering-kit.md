---
description: >-
  Advanced techniques: DDD, kaizen, subagent-driven development, critique and prompt engineering.
icon: sliders
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

# Context Engineering Kit

| | |
| --- | --- |
| **Maker** | NeoLab (community) |
| **Works in** | Claude Code (+ OpenCode, Cursor and more) |
| **Cost** | Free (open source) |
| **Source** | [github.com/NeoLabHQ/context-engineering-kit](https://github.com/NeoLabHQ/context-engineering-kit) |

## What does it do?

A big set of plugins with techniques for better AI development: software architecture and DDD, kaizen (continuous improvement), subagent-driven development, reflection and critique, prompt engineering, documentation and creating your own commands, hooks and skills.

## When do you use it?

* You want to get the most out of Claude Code on big projects.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
/critique
```
{% endcode %}

**What you get:** A critical assessment of the latest work by several 'judges'.

## Install

{% tabs %}
{% tab title="Claude Code" %}
```bash
/plugin marketplace add NeoLabHQ/context-engineering-kit
/plugin install ddd@NeoLabHQ/context-engineering-kit
```

Other plugins: `customaize-agent`, `docs`, `fpf`, `kaizen`, `sadd` and more.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Documentation: [neolab.gitbook.io/cek](https://neolab.gitbook.io/cek/).
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/NeoLabHQ/context-engineering-kit" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Development & code</a>
