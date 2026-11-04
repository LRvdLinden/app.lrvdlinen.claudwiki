---
description: >-
  Gives Claude Code a lasting memory: what happened in earlier sessions comes back automatically.
icon: memory
cover: ../../../.gitbook/assets/cover-en-kennis.png
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

# Claude-Mem

| | |
| --- | --- |
| **Maker** | thedotmack (community) |
| **Works in** | Claude Code (+ other agents) |
| **Cost** | Free and open source; the hosted memory service has a 30-day free trial, then your own plan or API key |
| **Source** | [github.com/thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) |

## What does it do?

Claude-Mem is a 'persistent memory compression system'. Through hooks it records what happens in your sessions, compresses it and adds relevant memories to new sessions. There is a local web viewer to search your memory. After installation it asks you to log in via an email link.

## When do you use it?

* You work on the same project for a long time and don't want to give context again and again.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
(just keep working)
```
{% endcode %}

**What you get:** In a new session Claude still knows which decisions and bug fixes were made earlier.

## Install

{% tabs %}
{% tab title="Installer (recommended)" %}
```bash
npx claude-mem install
```

The installer sets everything up and then asks you to log in via an email link (no credit card). Then you choose your memory provider: the claude-mem observer (30-day free trial), your own OpenRouter or Gemini key, or your Anthropic plan.
{% endtab %}

{% tab title="Claude Code" %}
First add the marketplace, then install the plugin. Type this in a Claude Code session:

```bash
/plugin marketplace add thedotmack/claude-mem
/plugin install claude-mem
```

Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Read the privacy information in the repo: the hosted storage is used by default.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/thedotmack/claude-mem" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Knowledge & memory</a>
