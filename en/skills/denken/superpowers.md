---
description: >-
  A complete working method: brainstorming, writing plans, test-first building, systematic debugging and verification.
icon: bolt
cover: ../../../.gitbook/assets/cover-en-denken.png
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

# Superpowers

{% hint style="danger" %}
**Spotted on social.** Tip from Bart Boonstra: *'Superpowers makes Claude really think in steps. Brainstorming and planning get 10x sharper.'*
{% endhint %}

| | |
| --- | --- |
| **Maker** | Jesse Vincent / obra (community) |
| **Works in** | Claude Code (+ Codex, Antigravity and more) |
| **Cost** | Free (open source) |
| **Source** | [github.com/obra/superpowers](https://github.com/obra/superpowers) |

## What does it do?

Superpowers is one of the best-known skill packs. It is a complete development method, built from separate skills that complement each other: **brainstorming** (sharpening the idea together first), **writing-plans** and **executing-plans**, **test-driven-development**, **systematic-debugging**, **verification-before-completion** (prove it works first), requesting and receiving code reviews, working with git worktrees and subagents. A starter skill makes sure Claude actually uses them. Brainstorming also works outside software: for a talk, a business or a renovation.

## When do you use it?

* You are starting a new feature or project.
* Claude jumps into code too quickly and misses the bigger picture.
* You are stuck on a bug and want a systematic approach.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
I want to add a widget to my app. Let's brainstorm first.
```
{% endcode %}

**What you get:** Claude asks questions first, proposes designs and writes a plan before writing any code.

{% code title="Example 2: what you type" overflow="wrap" %}
```
The tests have been failing since the last update. Debug this systematically.
```
{% endcode %}

**What you get:** Claude first finds and proves the cause before fixing anything.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install superpowers@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.
{% endtab %}

{% tab title="Superpowers-marketplace" %}
The author's own marketplace, with extra related plugins:

```bash
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Use several tools (Claude Code and Codex)? Install Superpowers separately for each tool.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/obra/superpowers" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Thinking & planning</a>
