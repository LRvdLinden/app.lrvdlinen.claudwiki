---
description: >-
  Experimental Superpowers skills: finding duplicate functions, interactive terminals with tmux and more.
icon: flask
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

# Superpowers Lab

| | |
| --- | --- |
| **Maker** | obra (community) |
| **Works in** | Claude Code |
| **Cost** | Free (open source) |
| **Source** | [github.com/obra/superpowers-lab](https://github.com/obra/superpowers-lab) |

## What does it do?

New techniques that are still being refined: `finding-duplicate-functions` (finds functions that do the same thing but are written differently, typical of AI code), `using-tmux-for-interactive-commands`, `mcp-cli` and `windows-vm`.

## When do you use it?

* You already use Superpowers and want to try new techniques.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Find duplicate functions in this codebase.
```
{% endcode %}

**What you get:** A list of functions you can merge.

## Install

{% tabs %}
{% tab title="Claude Code" %}
Install the plugin straight from GitHub:

```bash
claude plugin install https://github.com/obra/superpowers-lab
```

Some skills need `tmux`.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/obra/superpowers-lab" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Thinking & planning</a>
