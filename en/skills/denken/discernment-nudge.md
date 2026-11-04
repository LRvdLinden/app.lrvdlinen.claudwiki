---
description: >-
  Adds 2–3 smart check questions after important advice, so you verify the assumptions yourself.
icon: circle-question
cover: ../../../.gitbook/assets/cover-en-denken.png
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

# Discernment Nudge

| | |
| --- | --- |
| **Maker** | Anthropic (official) |
| **Works in** | Claude app, Claude Code, API |
| **Cost** | Free |
| **Source** | [github.com/anthropics/skills/tree/main/skills/discernment-nudge](https://github.com/anthropics/skills/tree/main/skills/discernment-nudge) |

## What does it do?

After Claude has given you advice, a plan, an estimate or an analysis, this skill asks 2–3 short follow-up questions tied to that exact answer: which facts to check, which assumptions are underneath and what context may be missing. At most once per conversation, so it doesn't get annoying.

## When do you use it?

* You use Claude for decisions and want to stay critical.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Make a budget for our street party.
```
{% endcode %}

**What you get:** The budget, followed by questions like 'Is the number of visitors this is based on correct?'

## Install

{% tabs %}
{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills add anthropics/skills --skill discernment-nudge
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}

{% tab title="Claude app" %}
1. Download the repo as a ZIP: [github.com/anthropics/skills](https://github.com/anthropics/skills) → **Code → Download ZIP**.
2. Unzip and find the folder `skills/discernment-nudge` (it contains `SKILL.md`).
3. Zip **only that folder** into a new ZIP. The folder name must match the skill name.
4. Go to **Settings → Capabilities → Skills** and click **Upload skill**.
5. Switch the skill on.

Skills in the Claude app require a Pro, Max, Team or Enterprise plan, and **Code execution and file creation** must be turned on.
{% endtab %}
{% endtabs %}

<a href="https://github.com/anthropics/skills/tree/main/skills/discernment-nudge" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Thinking & planning</a>
