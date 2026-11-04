---
description: >-
  SwiftUI best practices: state management, view composition, performance, new SDK changes and Liquid Glass.
icon: swift
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

# SwiftUI Expert (Antoine van der Lee)

| | |
| --- | --- |
| **Maker** | Antoine van der Lee / SwiftLee (community, Dutch) |
| **Works in** | Claude Code (+ Codex, Cursor and other agents) |
| **Cost** | Free (open source) |
| **Source** | [github.com/AvdLee/SwiftUI-Agent-Skill](https://github.com/AvdLee/SwiftUI-Agent-Skill) |

## What does it do?

Antoine van der Lee (SwiftLee) is a well-known Dutch iOS developer. This skill bundles practical SwiftUI knowledge into compact references for agents and code reviews: how to manage state well, compose views, keep an eye on performance, apply the latest SDK changes and adopt **Liquid Glass**. A second skill, `update-swiftui-apis`, helps replace deprecated APIs.

## When do you use it?

* You are building an iOS, iPadOS or macOS app in SwiftUI.
* You want Claude to write modern SwiftUI instead of outdated patterns.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Review this SwiftUI view for state management and performance.
```
{% endcode %}

**What you get:** Concrete improvements, like @Observable instead of ObservableObject.

{% code title="Example 2: what you type" overflow="wrap" %}
```
Adapt the settings screen to Liquid Glass.
```
{% endcode %}

**What you get:** Code that uses the new design language correctly.

## Install

{% tabs %}
{% tab title="Claude Code" %}
First add the marketplace, then install the plugin. Type this in a Claude Code session:

```bash
/plugin marketplace add AvdLee/SwiftUI-Agent-Skill
/plugin install swiftui-expert@swiftui-expert-skill
```

Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.
{% endtab %}

{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills@latest add https://github.com/avdlee/swiftui-agent-skill --skill swiftui-expert-skill
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* From the same author: [Swift Concurrency](swift-concurrency.md) and [Xcode Build Optimization](xcode-build-optimization.md).
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/AvdLee/SwiftUI-Agent-Skill" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Apps & mobile</a>
