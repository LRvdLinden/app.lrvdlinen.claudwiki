---
description: >-
  Agent skill from Hacking with Swift: modern SwiftUI code for iOS 26+ and Swift 6.
icon: mobile-screen
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

# SwiftUI Pro (Paul Hudson)

| | |
| --- | --- |
| **Maker** | Paul Hudson / twostraws (community) |
| **Works in** | Claude Code (+ Codex, Gemini) |
| **Cost** | Free (open source) |
| **Source** | [github.com/twostraws/SwiftUI-Agent-Skill](https://github.com/twostraws/SwiftUI-Agent-Skill) |

## What does it do?

Paul Hudson, creator of Hacking with Swift, poured his SwiftUI knowledge into a skill. It targets iOS 26 and later and recent Swift versions, and makes sure Claude uses current APIs and idioms and avoids classic pitfalls.

## When do you use it?

* You build SwiftUI apps for the latest iOS versions.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Build a list with search, swipe actions and pull-to-refresh in modern SwiftUI.
```
{% endcode %}

**What you get:** Modern, compact SwiftUI code.

## Install

{% tabs %}
{% tab title="Claude Code" %}
First add the marketplace, then install the plugin. Type this in a Claude Code session:

```bash
/plugin marketplace add twostraws/SwiftUI-Agent-Skill
/plugin install swiftui-pro@swiftui-agent-skill
```

Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.
{% endtab %}

{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills add https://github.com/twostraws/swiftui-agent-skill --skill swiftui-pro
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Also by Paul Hudson: [Swift Testing Pro](swift-testing-pro.md).
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/twostraws/SwiftUI-Agent-Skill" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Apps & mobile</a>
