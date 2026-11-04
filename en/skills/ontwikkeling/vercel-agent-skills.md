---
description: >-
  React and Next.js best practices, web design guidelines and deploying to Vercel.
icon: rocket
cover: ../../../.gitbook/assets/cover-en-ontwikkeling.png
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

# Vercel Agent Skills

| | |
| --- | --- |
| **Maker** | Vercel (official, by the makers) |
| **Works in** | Claude Code (+ other agents) |
| **Cost** | Free |
| **Source** | [github.com/vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) |

## What does it do?

Vercel publishes skills with its own best practices: **react-best-practices**, **composition-patterns**, **react-native-skills**, **react-view-transitions**, **web-design-guidelines**, **writing-guidelines**, **deploy-to-vercel** and **vercel-optimize** (an audit of costs, performance and caching).

## When do you use it?

* You build with React, Next.js or React Native.
* You host on Vercel.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Review this page against the web-design-guidelines.
```
{% endcode %}

**What you get:** A list of concrete improvements.

{% code title="Example 2: what you type" overflow="wrap" %}
```
Deploy this project to Vercel.
```
{% endcode %}

**What you get:** A live preview URL.

## Install

{% tabs %}
{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills add vercel-labs/agent-skills
npx skills add vercel-labs/agent-skills --skill web-design-guidelines -a claude-code
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* On [skills.sh](https://skills.sh) you'll find thousands of skills you can install with the same CLI.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/vercel-labs/agent-skills" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Development & code</a>
