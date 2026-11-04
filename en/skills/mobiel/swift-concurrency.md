---
description: >-
  Helps Claude with async/await, actors, Sendable and migrating to Swift 6 strict concurrency.
icon: arrows-split-up-and-left
cover: ../../../.gitbook/assets/cover-en-mobiel.png
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

# Swift Concurrency

| | |
| --- | --- |
| **Maker** | Antoine van der Lee (community, Dutch) |
| **Works in** | Claude Code (+ other agents) |
| **Cost** | Free (open source) |
| **Source** | [github.com/AvdLee/Swift-Concurrency-Agent-Skill](https://github.com/AvdLee/Swift-Concurrency-Agent-Skill) |

## What does it do?

Swift Concurrency is tricky, and AI agents often get it wrong. This skill gives Claude the right knowledge about async/await, actors, `@MainActor`, `Sendable`, tasks and resolving strict-concurrency warnings in Swift 6.

## When do you use it?

* You get Swift 6 concurrency errors.
* You want to convert old completion handlers to async/await.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Fix all Sendable warnings in this module without @unchecked.
```
{% endcode %}

**What you get:** A correct, safe solution per warning.

## Install

{% tabs %}
{% tab title="Claude Code" %}
First add the marketplace, then install the plugin. Type this in a Claude Code session:

```bash
/plugin marketplace add AvdLee/Swift-Concurrency-Agent-Skill
/plugin install swift-concurrency@swift-concurrency-agent-skill
```

Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.
{% endtab %}

{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills@latest add https://github.com/avdlee/swift-concurrency-agent-skill --skill swift-concurrency
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/AvdLee/Swift-Concurrency-Agent-Skill" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Apps & mobile</a>
