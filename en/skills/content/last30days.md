---
description: >-
  Researches what people really say about a topic in the last 30 days: Reddit, X, YouTube, TikTok and more.
icon: magnifying-glass-chart
cover: ../../../.gitbook/assets/cover-en-content.png
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

# Last 30 Days

| | |
| --- | --- |
| **Maker** | mvanhorn (community) |
| **Works in** | Claude Code (+ other agents) |
| **Cost** | Free (open source) |
| **Source** | [github.com/mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) |

## What does it do?

Instead of editorial articles, this skill looks for what **people** say: posts and engagement from Reddit, X, YouTube, TikTok, Hacker News, Polymarket, GitHub and the web, from the last 30 days. A `doctor` check shows which sources work.

## When do you use it?

* You want to know what's going on right now around a topic or competitor.
* You're looking for inspiration for timely content.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
/last30days Claude skills
```
{% endcode %}

**What you get:** An overview of what was said about Claude skills over the past month, with sources.

## Install

{% tabs %}
{% tab title="Claude Code" %}
First add the marketplace, then install the plugin. Type this in a Claude Code session:

```bash
/plugin marketplace add mvanhorn/last30days-skill
/plugin install last30days
```

Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.
{% endtab %}

{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills add mvanhorn/last30days-skill -g
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Don't install it via both methods at once; Claude Code doesn't deduplicate that.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/mvanhorn/last30days-skill" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Writing, content & marketing</a>
