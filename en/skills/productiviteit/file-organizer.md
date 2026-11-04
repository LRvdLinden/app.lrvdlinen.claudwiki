---
description: >-
  Tidies folders smartly: finds duplicates, proposes a better structure and automates the clean-up.
icon: folder-tree
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

# File Organizer

| | |
| --- | --- |
| **Maker** | ComposioHQ (community) |
| **Works in** | Claude Code, Claude app |
| **Cost** | Free |
| **Source** | [github.com/ComposioHQ/awesome-claude-skills/tree/master/file-organizer](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/file-organizer) |

## What does it do?

Claude looks at your folders, understands what's in them, finds duplicate files, proposes a more logical folder structure and carries out the clean-up for you.

## When do you use it?

* Your Downloads or documents folder is chaos.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Tidy up my Downloads folder: group by type and find duplicates.
```
{% endcode %}

**What you get:** A proposal and, after approval, a tidy folder.

## Install

{% tabs %}
{% tab title="Manual" %}
Copy the skill folder to your personal skills folder (for all projects) or to `.claude/skills/` in one project:

```bash
git clone https://github.com/ComposioHQ/awesome-claude-skills.git
cp -r awesome-claude-skills/file-organizer ~/.claude/skills/
```
{% endtab %}

{% tab title="Claude app" %}
1. Download the repo as a ZIP: [github.com/ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) → **Code → Download ZIP**.
2. Unzip and find the folder `file-organizer` (it contains `SKILL.md`).
3. Zip **only that folder** into a new ZIP. The folder name must match the skill name.
4. Go to **Settings → Capabilities → Skills** and click **Upload skill**.
5. Switch the skill on.

Skills in the Claude app require a Pro, Max, Team or Enterprise plan, and **Code execution and file creation** must be turned on.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Let Claude make a proposal first before it moves anything.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/ComposioHQ/awesome-claude-skills/tree/master/file-organizer" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Productivity & tools</a>
