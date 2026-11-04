---
description: >-
  Everything with PDFs: extract text and tables, merge, split, fill in forms, OCR and watermarks.
icon: file-pdf
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

# PDF

| | |
| --- | --- |
| **Maker** | Anthropic (official) |
| **Works in** | Claude app, Claude Code, API |
| **Cost** | Free with a paid plan (source-available) |
| **Source** | [github.com/anthropics/skills/tree/main/skills/pdf](https://github.com/anthropics/skills/tree/main/skills/pdf) |

## What does it do?

The PDF skill gives Claude a complete toolbox for PDF files. It extracts text and tables, merges or splits files, rotates pages, adds watermarks, fills in PDF forms, encrypts or decrypts files and makes scanned PDFs searchable with OCR. It can also create new PDFs.

## When do you use it?

* You want data from a stack of invoices or reports in a table.
* You need to fill in a PDF form.
* You have a scan you want to search.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Extract the date, supplier and total amount from these 12 invoices (PDF) and put them in a table.
```
{% endcode %}

**What you get:** An overview table, optionally as Excel.

{% code title="Example 2: what you type" overflow="wrap" %}
```
Merge these three PDFs, rotate page 4 upright and put a 'DRAFT' watermark on every page.
```
{% endcode %}

**What you get:** One new PDF.

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
npx skills add anthropics/skills --skill pdf
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* For scanned documents, ask for OCR explicitly.
* For large PDFs, ask for a table of contents first and then zoom in.
{% endhint %}

<a href="https://github.com/anthropics/skills/tree/main/skills/pdf" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Documents & office</a>
