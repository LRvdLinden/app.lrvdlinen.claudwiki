---
description: >-
  Turns your git commits into clear release notes for users.
icon: clock-rotate-left
cover: ../../../.gitbook/assets/cover-en-productiviteit.png
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

# Changelog Generator

| | |
| --- | --- |
| **Maker** | ComposioHQ (community) |
| **Works in** | Claude Code |
| **Cost** | Free |
| **Source** | [github.com/ComposioHQ/awesome-claude-skills/tree/master/changelog-generator](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/changelog-generator) |

## What does it do?

Analyses your commit history, categorises changes (new, improved, fixed) and translates technical commits into clear, customer-friendly release notes.

## When do you use it?

* You are publishing a new version of your app and want 'What's new' text.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Create release notes for everything since tag v2.3.0, in Dutch and English.
```
{% endcode %}

**What you get:** Release notes in two languages.

## Install

{% tabs %}
{% tab title="Manual" %}
Copy the skill folder to your personal skills folder (for all projects) or to `.claude/skills/` in one project:

```bash
git clone https://github.com/ComposioHQ/awesome-claude-skills.git
cp -r awesome-claude-skills/changelog-generator ~/.claude/skills/
```
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/ComposioHQ/awesome-claude-skills/tree/master/changelog-generator" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Productivity & tools</a>
