---
description: >-
  Lets Claude Code talk directly to NotebookLM for answers based only on your own documents.
icon: book-open-reader
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

# NotebookLM Skill

| | |
| --- | --- |
| **Maker** | PleasePrompto (community) |
| **Works in** | Only Claude Code (local), not the web app |
| **Cost** | Free |
| **Source** | [github.com/PleasePrompto/notebooklm-skill](https://github.com/PleasePrompto/notebooklm-skill) |

## What does it do?

Claude asks questions of your NotebookLM notebooks and gets answers based exclusively on the sources you uploaded there. Useful when you want reliable answers without made-up content.

## When do you use it?

* You keep all your policy documents or manuals in NotebookLM.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Ask my notebook 'Neighbourhood policy' what it says about green maintenance.
```
{% endcode %}

**What you get:** An answer with source references from your notebook.

## Install

{% tabs %}
{% tab title="Manual" %}
Copy the skill folder to your personal skills folder (for all projects) or to `.claude/skills/` in one project:

```bash
mkdir -p ~/.claude/skills && cd ~/.claude/skills
git clone https://github.com/PleasePrompto/notebooklm-skill notebooklm
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* The same author also has an MCP version.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/PleasePrompto/notebooklm-skill" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Productivity & tools</a>
