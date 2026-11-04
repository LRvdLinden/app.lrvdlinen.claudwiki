---
description: >-
  A design vocabulary for your agent: commands like polish, bolder, critique and audit, plus a detector for 'AI slop'.
icon: gem
cover: ../../../.gitbook/assets/cover-en-design.png
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

# Impeccable

| | |
| --- | --- |
| **Maker** | Paul Bakaus (community) |
| **Works in** | Claude Code (+ Cursor, Codex, Copilot and more) |
| **Cost** | Free (open source) |
| **Source** | [github.com/pbakaus/impeccable](https://github.com/pbakaus/impeccable) |

## What does it do?

Impeccable gives Claude a shared language to steer designs. You say *polish*, *bolder*, *critique* or *audit* and Claude knows exactly what you mean. It includes a detector that spots typical AI design mistakes ('slop'), and a hook that automatically checks every UI file Claude edits before it says it is done. The CLI also works on its own, for example in your CI.

## When do you use it?

* You want to improve a design in small, targeted steps.
* You want to be warned automatically about generic-looking UI.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
critique the homepage and then polish the hero section
```
{% endcode %}

**What you get:** First a critical review, then a refined hero.

{% code title="Example 2: what you type" overflow="wrap" %}
```
npx impeccable detect src/
```
{% endcode %}

**What you get:** A scan of your code for typical AI design patterns.

## Install

{% tabs %}
{% tab title="Claude Code" %}
```bash
/plugin marketplace add pbakaus/impeccable
```

Then open `/plugin` and install **Impeccable**. Say 'yes' to the design hook: it catches most mistakes automatically.
{% endtab %}

{% tab title="CLI" %}
```bash
npx impeccable detect src/                  # scan a folder
npx impeccable detect https://example.com   # scan a live page
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Documentation: [impeccable.style/docs](https://impeccable.style/docs).
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/pbakaus/impeccable" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Design & frontend</a>
