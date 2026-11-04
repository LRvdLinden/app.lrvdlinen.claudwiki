---
description: >-
  Step-by-step: install a skill in the Claude app, in Claude Code, via npx or manually.
icon: download
cover: ../../.gitbook/assets/cover-en-basis.png
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
# Install skills

There are four ways. Which one you choose depends on where you use Claude.

{% tabs %}
{% tab title="Claude app" %}
**Turn on built-in skills**

1. Go to **Settings → Capabilities**.
2. Turn on **Code execution and file creation**.
3. Scroll to **Skills** and switch on the skills you want.

**Upload your own or a community skill**

{% stepper %}
{% step %}
### Download the skill
Download the folder containing the `SKILL.md`, for example via GitHub → **Code → Download ZIP**.
{% endstep %}
{% step %}
### Zip it
Zip **only the skill folder**. The folder name must match the skill name.
{% endstep %}
{% step %}
### Upload
Go to **Settings → Capabilities → Skills** and click **Upload skill**.
{% endstep %}
{% step %}
### Switch it on
Switch the skill on in the list. Done!
{% endstep %}
{% endstepper %}

{% hint style="info" %}
On Pro and Max, custom skills are private. On Team and Enterprise, owners can provision skills for the whole organisation.
{% endhint %}
{% endtab %}

{% tab title="Claude Code (plugins)" %}
Most skills are distributed as a **plugin** through a **marketplace** (a GitHub repo with a list of plugins).

```bash
# 1. Add the marketplace (once)
/plugin marketplace add anthropics/skills

# 2. Install the plugin
/plugin install document-skills@anthropic-agent-skills

# View, enable/disable and update
/plugin
```

Anthropic's **official marketplace** (`claude-plugins-official`) is connected by default:

```bash
/plugin install superpowers@claude-plugins-official
```

You can also run the same commands outside a session in your terminal, for example `claude plugin install …`.
{% endtab %}

{% tab title="npx skills" %}
The open-source [skills CLI](https://github.com/vercel-labs/skills) installs skills for Claude Code and dozens of other agents. Find skills on [skills.sh](https://skills.sh).

```bash
npx skills add remotion-dev/skills                 # everything in a repo
npx skills add anthropics/skills --skill pdf       # one skill
npx skills add blader/humanizer -g                 # globally, for all your projects
npx skills list                                    # what do I have?
npx skills check                                   # updates?
```
{% endtab %}

{% tab title="Manual" %}
A skill is just a folder. Put it in the right place:

| Place | Folder | Works in |
| --- | --- | --- |
| Personal | `~/.claude/skills/<name>/SKILL.md` | All your projects on this computer |
| Project | `.claude/skills/<name>/SKILL.md` | Only this project (commit it for your team) |

```bash
git clone https://github.com/blader/Claudeception.git ~/.claude/skills/claudeception
```

Restart Claude Code afterwards.
{% endtab %}
{% endtabs %}

## Does it work?

* Type `/` in Claude Code and check whether the skill is in the list.
* Or simply ask: *"Which skills do you have available?"*

<a href="skills-gebruiken.md" class="button primary" data-icon="arrow-right">Next: use skills</a>
