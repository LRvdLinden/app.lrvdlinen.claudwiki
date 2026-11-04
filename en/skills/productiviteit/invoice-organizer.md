---
description: >-
  Organises invoices and receipts for your tax return: extracts data, renames and sorts.
icon: file-invoice-dollar
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

# Invoice Organizer

| | |
| --- | --- |
| **Maker** | ComposioHQ (community) |
| **Works in** | Claude Code, Claude app |
| **Cost** | Free |
| **Source** | [github.com/ComposioHQ/awesome-claude-skills/tree/master/invoice-organizer](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/invoice-organizer) |

## What does it do?

Reads messy invoices and receipts, extracts date, supplier and amount, gives them a consistent name and sorts them into logical folders.

## When do you use it?

* You need to get your bookkeeping in order for VAT or income tax.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Organise all invoices in this folder by quarter and supplier.
```
{% endcode %}

**What you get:** Neatly renamed and sorted files.

## Install

{% tabs %}
{% tab title="Manual" %}
Copy the skill folder to your personal skills folder (for all projects) or to `.claude/skills/` in one project:

```bash
git clone https://github.com/ComposioHQ/awesome-claude-skills.git
cp -r awesome-claude-skills/invoice-organizer ~/.claude/skills/
```
{% endtab %}

{% tab title="Claude app" %}
1. Download the repo as a ZIP: [github.com/ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) → **Code → Download ZIP**.
2. Unzip and find the folder `invoice-organizer` (it contains `SKILL.md`).
3. Zip **only that folder** into a new ZIP. The folder name must match the skill name.
4. Go to **Settings → Capabilities → Skills** and click **Upload skill**.
5. Switch the skill on.

Skills in the Claude app require a Pro, Max, Team or Enterprise plan, and **Code execution and file creation** must be turned on.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/ComposioHQ/awesome-claude-skills/tree/master/invoice-organizer" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Productivity & tools</a>
