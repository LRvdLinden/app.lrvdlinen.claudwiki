---
description: >-
  Analyses meeting transcripts for communication patterns and gives personal feedback.
icon: people-group
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

# Meeting Insights Analyzer

| | |
| --- | --- |
| **Maker** | ComposioHQ (community) |
| **Works in** | Claude Code, Claude app |
| **Cost** | Free |
| **Source** | [github.com/ComposioHQ/awesome-claude-skills/tree/master/meeting-insights-analyzer](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/meeting-insights-analyzer) |

## What does it do?

Reads meeting transcripts and shows where you avoid conflict, use lots of filler words, dominate the conversation or miss chances to listen. Useful for improving how you lead meetings.

## When do you use it?

* You chair a lot of meetings and want to lead better.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Analyse the transcripts of the last three meetings and give me feedback as chair.
```
{% endcode %}

**What you get:** Patterns and concrete tips.

## Install

{% tabs %}
{% tab title="Manual" %}
Copy the skill folder to your personal skills folder (for all projects) or to `.claude/skills/` in one project:

```bash
git clone https://github.com/ComposioHQ/awesome-claude-skills.git
cp -r awesome-claude-skills/meeting-insights-analyzer ~/.claude/skills/
```
{% endtab %}

{% tab title="Claude app" %}
1. Download the repo as a ZIP: [github.com/ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) → **Code → Download ZIP**.
2. Unzip and find the folder `meeting-insights-analyzer` (it contains `SKILL.md`).
3. Zip **only that folder** into a new ZIP. The folder name must match the skill name.
4. Go to **Settings → Capabilities → Skills** and click **Upload skill**.
5. Switch the skill on.

Skills in the Claude app require a Pro, Max, Team or Enterprise plan, and **Code execution and file creation** must be turned on.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/ComposioHQ/awesome-claude-skills/tree/master/meeting-insights-analyzer" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Productivity & tools</a>
