---
description: >-
  Lets Claude build, launch and test your iOS app in the Simulator, with 30 helper scripts.
icon: tablet-screen-button
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

# iOS Simulator Skill

| | |
| --- | --- |
| **Maker** | Conor Luddy (community) |
| **Works in** | Claude Code on macOS with Xcode |
| **Cost** | Free (open source) |
| **Source** | [github.com/conorluddy/ios-simulator-skill](https://github.com/conorluddy/ios-simulator-skill) |

## What does it do?

With this skill Claude can operate the iOS Simulator: build and install apps, tap and navigate through the accessibility tree, take screenshots, read logs and debug problems. The 30 scripts are optimised for both humans and agents.

## When do you use it?

* You want Claude to check for itself that its change works in the app.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Build the app, open it in the iPhone simulator and test whether the onboarding screen works.
```
{% endcode %}

**What you get:** A test report with screenshots.

## Install

{% tabs %}
{% tab title="Claude Code" %}
First add the marketplace, then install the plugin. Type this in a Claude Code session:

```bash
/plugin marketplace add conorluddy/ios-simulator-skill
/plugin install ios-simulator-skill@conorluddy
```

Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Prefer an MCP server? The author also has XC-MCP.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/conorluddy/ios-simulator-skill" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Apps & mobile</a>
