---
description: >-
  Open and clean up spreadsheets, add formulas and charts, or build new sheets.
icon: file-excel
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

# Excel (xlsx)

| | |
| --- | --- |
| **Maker** | Anthropic (official) |
| **Works in** | Claude app, Claude Code, API |
| **Cost** | Free with a paid plan (source-available) |
| **Source** | [github.com/anthropics/skills/tree/main/skills/xlsx](https://github.com/anthropics/skills/tree/main/skills/xlsx) |

## What does it do?

The Excel skill lets Claude create and edit real spreadsheets: `.xlsx`, `.xlsm`, `.csv` and `.tsv`. It adds columns and **working formulas**, creates charts, fixes formatting, cleans messy data (wrong header rows, empty rows) and converts between formats.

## When do you use it?

* You need a budget, schedule or overview you will keep editing in Excel.
* You have a messy export that needs cleaning.
* You want charts for your numbers.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Create a budget for the street party with income, expenses, a total formula and a pie chart.
```
{% endcode %}

**What you get:** An `.xlsx` with working formulas.

{% code title="Example 2: what you type" overflow="wrap" %}
```
This CSV export is a mess. Clean it up, fix the dates and turn it into a tidy Excel file.
```
{% endcode %}

**What you get:** A cleaned-up spreadsheet.

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
npx skills add anthropics/skills --skill xlsx
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Ask Claude to use formulas instead of fixed numbers, so your sheet stays usable when you change something.
{% endhint %}

<a href="https://github.com/anthropics/skills/tree/main/skills/xlsx" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Documents & office</a>
