---
description: >-
  Creates, reads and edits Word documents with formatting, a table of contents and tracked changes.
icon: file-word
cover: ../../../.gitbook/assets/cover-en-documenten.png
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

# Word (docx)

| | |
| --- | --- |
| **Maker** | Anthropic (official) |
| **Works in** | Claude app, Claude Code, API |
| **Cost** | Free with a paid plan (source-available) |
| **Source** | [github.com/anthropics/skills/tree/main/skills/docx](https://github.com/anthropics/skills/tree/main/skills/docx) |

## What does it do?

The Word skill powers the Word files Claude makes for you. It knows how a `.docx` works inside: headings, styles, tables, headers and footers, page numbers, tables of contents, images and even **tracked changes** and comments. It can also read and edit existing Word files, or use a template (`.dotx`) as a starting point.

## When do you use it?

* You really need a `.docx`, for example for a municipality, school or client.
* You want an existing Word file reviewed with visible changes.
* You want to fill a letter template in your house style.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Turn these meeting minutes into a clean Word document with a table of contents, page numbers and our logo in the header.
```
{% endcode %}

**What you get:** A formatted `.docx` file to download.

{% code title="Example 2: what you type" overflow="wrap" %}
```
Read contract.docx and suggest improvements as tracked changes.
```
{% endcode %}

**What you get:** The original document with tracked changes you can accept or reject in Word.

## Install

{% tabs %}
{% tab title="Claude app" %}
This skill is **already built in** for paid plans.

1. Open **Settings → Capabilities**.
2. Turn on **Code execution and file creation**.
3. Scroll to **Skills** and switch the skill on.

Then just ask for what you want in plain language; Claude loads the skill itself.

In the Claude app, Claude already uses this skill automatically as soon as you ask for a file of this type.
{% endtab %}

{% tab title="Claude Code" %}
First add the marketplace, then install the plugin. Type this in a Claude Code session:

```bash
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
```

Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.

This installs **document-skills**: Word, PDF, PowerPoint and Excel in one go.
{% endtab %}

{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills add anthropics/skills --skill docx
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Say 'as a Word file' explicitly if you want a .docx; otherwise Claude may pick another format.
* Upload your own template (.dotx) so Claude uses your house style.
{% endhint %}

<a href="https://github.com/anthropics/skills/tree/main/skills/docx" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Documents & office</a>
