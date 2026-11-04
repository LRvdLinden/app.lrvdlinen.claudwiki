---
description: >-
  Interactive data visualisations with D3.js: charts, networks and maps.
icon: chart-area
cover: ../../../.gitbook/assets/cover-en-media.png
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

# D3.js Visualisation

| | |
| --- | --- |
| **Maker** | Chris von Csefalvay (community) |
| **Works in** | Claude Code, Claude app |
| **Cost** | Free |
| **Source** | [github.com/chrisvoncsefalvay/claude-d3js-skill](https://github.com/chrisvoncsefalvay/claude-d3js-skill) |

## What does it do?

Teaches Claude to make custom charts, network diagrams and geographic visualisations with D3.js, with full control over transitions and interaction.

## When do you use it?

* Standard charts aren't enough and you want something custom.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Make an interactive map of the Netherlands with the number of incidents per municipality.
```
{% endcode %}

**What you get:** A D3 map with tooltips.

## Install

{% tabs %}
{% tab title="Claude app" %}
1. Download the repo as a ZIP: [github.com/chrisvoncsefalvay/claude-d3js-skill](https://github.com/chrisvoncsefalvay/claude-d3js-skill) → **Code → Download ZIP**.
2. Unzip and find the folder `(the root folder, rename it to d3-viz)` (it contains `SKILL.md`).
3. Zip **only that folder** into a new ZIP. The folder name must match the skill name.
4. Go to **Settings → Capabilities → Skills** and click **Upload skill**.
5. Switch the skill on.

Skills in the Claude app require a Pro, Max, Team or Enterprise plan, and **Code execution and file creation** must be turned on.
{% endtab %}

{% tab title="Manual" %}
Copy the skill folder to your personal skills folder (for all projects) or to `.claude/skills/` in one project:

```bash
git clone https://github.com/chrisvoncsefalvay/claude-d3js-skill.git ~/.claude/skills/d3-viz
```
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/chrisvoncsefalvay/claude-d3js-skill" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Audio, images & visuals</a>
