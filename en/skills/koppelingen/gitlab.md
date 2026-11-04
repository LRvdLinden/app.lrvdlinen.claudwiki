---
description: >-
  Repositories, merge requests, CI/CD pipelines, issues and wikis in GitLab.
icon: gitlab
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

# GitLab

| | |
| --- | --- |
| **Maker** | GitLab · official Claude marketplace |
| **Works in** | Claude Code |
| **Cost** | Plugin free; requires a GitLab account |
| **Source** | [github.com/anthropics/claude-plugins-public/tree/main/external_plugins/gitlab](https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/gitlab) |

## What does it do?

The GitLab plugin connects Claude to the GitLab DevOps platform: manage repositories, merge requests, follow CI/CD pipelines, issues and wikis.

## When do you use it?

* Your team uses GitLab instead of GitHub.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Why is the latest pipeline on main failing?
```
{% endcode %}

**What you get:** The error from the pipeline plus a proposed fix.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install gitlab@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/gitlab" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Connect your apps</a>
