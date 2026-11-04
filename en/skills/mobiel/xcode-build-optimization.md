---
description: >-
  Six skills that measure and speed up your Xcode builds: clean, incremental, compile hotspots and SPM.
icon: gauge-high
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

# Xcode Build Optimization

| | |
| --- | --- |
| **Maker** | Antoine van der Lee (community, Dutch) |
| **Works in** | Claude Code (+ other agents) |
| **Cost** | Free (open source) |
| **Source** | [github.com/AvdLee/Xcode-Build-Optimization-Agent-Skill](https://github.com/AvdLee/Xcode-Build-Optimization-Agent-Skill) |

## What does it do?

An orchestrator skill with five specialists: benchmark, compilation analysis, project settings, Swift Package Manager analysis and a fixer. Claude first measures how long your builds take, finds the bottlenecks and suggests targeted improvements.

## When do you use it?

* Your builds are slow and you want to know why.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Benchmark my project and make the incremental build faster.
```
{% endcode %}

**What you get:** Measurements before and after, with the changes in between.

## Install

{% tabs %}
{% tab title="Claude Code" %}
First add the marketplace, then install the plugin. Type this in a Claude Code session:

```bash
/plugin marketplace add AvdLee/Xcode-Build-Optimization-Agent-Skill
/plugin install xcode-build-skills@xcode-build-skills
```

Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.
{% endtab %}

{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills add https://github.com/avdlee/xcode-build-optimization-agent-skill
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Install all six skills: the orchestrator needs the specialists.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/AvdLee/Xcode-Build-Optimization-Agent-Skill" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Apps & mobile</a>
