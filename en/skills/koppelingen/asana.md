---
description: >-
  Create and manage tasks, search projects and track progress in Asana.
icon: check-double
cover: ../../../.gitbook/assets/cover-en-koppelingen.png
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

# Asana

| | |
| --- | --- |
| **Maker** | Asana · official Claude marketplace |
| **Works in** | Claude Code |
| **Cost** | Plugin free; requires a Asana account |
| **Source** | [github.com/anthropics/claude-plugins-public/tree/main/external_plugins/asana](https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/asana) |

## What does it do?

The Asana plugin connects Claude to Asana: create and assign tasks, search projects and track progress. You set up an Asana app once with the `/asana-setup` command.

## When do you use it?

* You plan projects in Asana.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Create an Asana task with a deadline for every action in these minutes.
```
{% endcode %}

**What you get:** Asana tasks with owners and deadlines.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install asana@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.

Then once: `/asana-setup`.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/asana" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Connect your apps</a>
