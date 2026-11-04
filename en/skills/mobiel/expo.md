---
description: >-
  Official Expo skills: building React Native apps, Expo Router, EAS Build/Update and publishing to the stores.
icon: react
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

# Expo Skills

| | |
| --- | --- |
| **Maker** | Expo (official, by the makers) |
| **Works in** | Claude Code (+ Codex, Cursor and more) |
| **Cost** | Free |
| **Source** | [github.com/expo/skills](https://github.com/expo/skills) |

## What does it do?

Over twenty skills from Expo itself: project structure, Expo Router, native UI and animations, data fetching, building modules, upgrading, web-to-native, App Clips and the EAS services (builds, updates, hosting, workflows and publishing to the App Store and Play Store).

## When do you use it?

* You are building a cross-platform app with React Native and Expo.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Upgrade this Expo project to the latest SDK.
```
{% endcode %}

**What you get:** A guided upgrade with the right steps.

{% code title="Example 2: what you type" overflow="wrap" %}
```
Set up EAS Update so I can roll out fixes without a new build.
```
{% endcode %}

**What you get:** Configuration and explanation.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install expo@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.
{% endtab %}

{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills@latest add expo/skills --skill '*'
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/expo/skills" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Apps & mobile</a>
