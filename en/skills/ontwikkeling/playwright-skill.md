---
description: >-
  Lets Claude write and run Playwright scripts itself, from simple page tests to long flows.
icon: masks-theater
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

# Playwright Skill

| | |
| --- | --- |
| **Maker** | lackeyjb (community) |
| **Works in** | Claude Code (+ Cursor and more) |
| **Cost** | Free (open source) |
| **Source** | [github.com/lackeyjb/playwright-skill](https://github.com/lackeyjb/playwright-skill) |

## What does it do?

A general browser automation skill: Claude writes and runs Playwright code on the spot, for tests, checking forms or walking through a complete user flow.

## When do you use it?

* You want your web app tested or checked automatically.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Test the sign-up flow on my site and report what goes wrong.
```
{% endcode %}

**What you get:** A test run with screenshots and findings.

## Install

{% tabs %}
{% tab title="Claude Code" %}
First add the marketplace, then install the plugin. Type this in a Claude Code session:

```bash
/plugin marketplace add lackeyjb/playwright-skill
/plugin install playwright-skill@playwright-skill
```

Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.
{% endtab %}

{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills add lackeyjb/playwright-skill --skill playwright-skill --agent claude-code --global --yes
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* See also the official [Webapp Testing](webapp-testing.md).
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/lackeyjb/playwright-skill" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Development & code</a>
