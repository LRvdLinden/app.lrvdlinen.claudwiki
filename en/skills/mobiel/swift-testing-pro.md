---
description: >-
  Writing good tests with the new Swift Testing framework (@Test, #expect).
icon: flask-vial
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

# Swift Testing Pro

| | |
| --- | --- |
| **Maker** | Paul Hudson / twostraws (community) |
| **Works in** | Claude Code (+ Codex, Gemini) |
| **Cost** | Free (open source) |
| **Source** | [github.com/twostraws/Swift-Testing-Agent-Skill](https://github.com/twostraws/Swift-Testing-Agent-Skill) |

## What does it do?

Teaches Claude the modern Swift Testing framework: `@Test`, `#expect`, parameterised tests, traits and converting XCTest to Swift Testing.

## When do you use it?

* You want to add tests to your Swift app.
* You are migrating from XCTest.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Write Swift Testing tests for this DateFormatter helper, including edge cases.
```
{% endcode %}

**What you get:** Parameterised tests with clear names.

## Install

{% tabs %}
{% tab title="Claude Code" %}
First add the marketplace, then install the plugin. Type this in a Claude Code session:

```bash
/plugin marketplace add twostraws/Swift-Testing-Agent-Skill
/plugin install swift-testing-pro@swift-testing-agent-skill
```

Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.
{% endtab %}

{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills add https://github.com/twostraws/swift-testing-agent-skill --skill swift-testing-pro
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/twostraws/Swift-Testing-Agent-Skill" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Apps & mobile</a>
