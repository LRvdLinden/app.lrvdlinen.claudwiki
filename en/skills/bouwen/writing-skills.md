---
description: >-
  The Superpowers approach to writing and testing skills, just like code.
icon: pen-ruler
cover: ../../../.gitbook/assets/cover-en-bouwen.png
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

# Writing Skills (Superpowers)

| | |
| --- | --- |
| **Maker** | obra (community) |
| **Works in** | Claude Code |
| **Cost** | Free (open source) |
| **Source** | [github.com/obra/superpowers/tree/main/skills/writing-skills](https://github.com/obra/superpowers/tree/main/skills/writing-skills) |

## What does it do?

Part of [Superpowers](../denken/superpowers.md). This skill treats writing skills as software development: first test whether Claude makes the mistake without the skill, then write the skill and then check whether it really changes the behaviour.

## When do you use it?

* You want skills that demonstrably work.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Write a skill that makes sure the tests always run before a commit.
```
{% endcode %}

**What you get:** A tested skill.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install superpowers@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.

Writing Skills is part of the Superpowers pack.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/obra/superpowers/tree/main/skills/writing-skills" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Build your own skills</a>
