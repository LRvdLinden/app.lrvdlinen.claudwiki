---
description: >-
  One command: from a URL (video, article, PDF) to clean text and an action plan to apply it.
icon: graduation-cap
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

# Tapestry (Learn This)

| | |
| --- | --- |
| **Maker** | Michal Parkola (community) |
| **Works in** | Claude Code |
| **Cost** | Free |
| **Source** | [github.com/michalparkola/tapestry-skills-for-claude-code](https://github.com/michalparkola/tapestry-skills-for-claude-code) |

## What does it do?

Say `learn-this <URL>` and the skill detects the content type (YouTube, article, PDF), pulls in the text cleanly and turns it into a **Ship-Learn-Next** action plan. Separate skills: youtube-transcript, article-extractor, ship-learn-next, scrum-sage, session-log and unblock-action.

## When do you use it?

* You watch lots of tutorials and want to actually do something with them.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
learn-this https://www.youtube.com/watch?v=...
```
{% endcode %}

**What you get:** Transcript plus a concrete step-by-step plan.

## Install

{% tabs %}
{% tab title="Manual" %}
Copy the skill folder to your personal skills folder (for all projects) or to `.claude/skills/` in one project:

```bash
git clone https://github.com/michalparkola/tapestry-skills-for-claude-code.git
cd tapestry-skills-for-claude-code
cp -r learn-this youtube-transcript article-extractor ship-learn-next ~/.claude/skills/
```
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/michalparkola/tapestry-skills-for-claude-code" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Productivity & tools</a>
