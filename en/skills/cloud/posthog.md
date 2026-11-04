---
description: >-
  PostHog analytics, feature flags, experiments and error tracking from Claude.
icon: chart-simple
cover: ../../../.gitbook/assets/cover-en-cloud.png
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

# PostHog

| | |
| --- | --- |
| **Maker** | PostHog · official Claude marketplace |
| **Works in** | Claude Code |
| **Cost** | Plugin free; requires a PostHog account |
| **Source** | [posthog.com/docs/model-context-protocol](https://posthog.com/docs/model-context-protocol) |

## What does it do?

With the PostHog plugin Claude looks at your product analytics, manages feature flags and experiments, tracks errors and pulls insights, without you opening the dashboard.

## When do you use it?

* You measure your app's usage with PostHog.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
How many users completed the new onboarding this week?
```
{% endcode %}

**What you get:** The number plus the trend.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install posthog@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://posthog.com/docs/model-context-protocol" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Data, cloud & payments</a>
