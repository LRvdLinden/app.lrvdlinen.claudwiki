---
description: >-
  Rewrites AI-sounding text so it reads like a person wrote it, without changing the content.
icon: user-pen
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

# Humanizer

{% hint style="danger" %}
**Spotted on social.** The most viral skill right now according to Artificial Corner. Watch out: look-alike copies are circulating, so only install from the official repo.
{% endhint %}

| | |
| --- | --- |
| **Maker** | blader (community) |
| **Works in** | Claude Code, Claude app (+ Codex and more) |
| **Cost** | Free (open source) |
| **Source** | [github.com/blader/humanizer](https://github.com/blader/humanizer) |

## What does it do?

Humanizer is based on Wikipedia's list *Signs of AI writing*, the guide Wikipedia editors use to spot AI text. The skill removes typical AI tricks: 'not X but Y' contrasts, punchy one-liners at the end, forced triads, dashes everywhere, inflated claims, sales language, stock AI words and bold labels. Your message stays the same, only the tone becomes more human.

## When do you use it?

* You post on LinkedIn or Instagram and don't want it to smell of AI.
* You want to strip a Claude draft of its AI tics.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
/humanizer Rewrite this LinkedIn post so it sounds like me.
```
{% endcode %}

**What you get:** The same post, but more natural and without AI patterns.

## Install

{% tabs %}
{% tab title="Claude Code" %}
First add the marketplace, then install the plugin. Type this in a Claude Code session:

```bash
/plugin marketplace add blader/humanizer
/plugin install humanizer@humanizer
```

Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.

The plugin responds to `/humanizer:humanizer` and requires Claude Code 2.1.142 or newer.
{% endtab %}

{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills add blader/humanizer --global --agent claude-code
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}

{% tab title="Claude app" %}
1. Download the repo as a ZIP: [github.com/blader/humanizer](https://github.com/blader/humanizer) → **Code → Download ZIP**.
2. Unzip and find the folder `humanizer (the repo's root folder, with SKILL.md)` (it contains `SKILL.md`).
3. Zip **only that folder** into a new ZIP. The folder name must match the skill name.
4. Go to **Settings → Capabilities → Skills** and click **Upload skill**.
5. Switch the skill on.

Skills in the Claude app require a Pro, Max, Team or Enterprise plan, and **Code execution and file creation** must be turned on.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Always check you have the real repo: github.com/blader/humanizer.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/blader/humanizer" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Writing, content & marketing</a>
