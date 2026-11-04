---
description: >-
  Creates a CV tailored to a job posting, so your relevant experience comes first.
icon: id-card
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

# Tailored Resume Generator

| | |
| --- | --- |
| **Maker** | ComposioHQ (community) |
| **Works in** | Claude Code, Claude app |
| **Cost** | Free |
| **Source** | [github.com/ComposioHQ/awesome-claude-skills/tree/master/tailored-resume-generator](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/tailored-resume-generator) |

## What does it do?

Analyses a job description and rewrites your CV so that the experience, skills and results that count for this job stand out most.

## When do you use it?

* You are applying and want a targeted CV per vacancy.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Here is my CV and the job posting. Make a tailored CV.
```
{% endcode %}

**What you get:** An adapted CV with the right emphasis.

## Install

{% tabs %}
{% tab title="Claude app" %}
1. Download the repo as a ZIP: [github.com/ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) → **Code → Download ZIP**.
2. Unzip and find the folder `tailored-resume-generator` (it contains `SKILL.md`).
3. Zip **only that folder** into a new ZIP. The folder name must match the skill name.
4. Go to **Settings → Capabilities → Skills** and click **Upload skill**.
5. Switch the skill on.

Skills in the Claude app require a Pro, Max, Team or Enterprise plan, and **Code execution and file creation** must be turned on.
{% endtab %}

{% tab title="Manual" %}
Copy the skill folder to your personal skills folder (for all projects) or to `.claude/skills/` in one project:

```bash
git clone https://github.com/ComposioHQ/awesome-claude-skills.git
cp -r awesome-claude-skills/tailored-resume-generator ~/.claude/skills/
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Then have it made into a Word file with the [Word skill](../documenten/docx.md).
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/ComposioHQ/awesome-claude-skills/tree/master/tailored-resume-generator" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Productivity & tools</a>
