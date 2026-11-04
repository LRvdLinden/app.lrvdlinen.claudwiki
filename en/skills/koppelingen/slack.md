---
description: >-
  Search Slack messages, read channels and threads and quickly find earlier discussions.
icon: slack
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

# Slack

| | |
| --- | --- |
| **Maker** | Slack · official Claude marketplace |
| **Works in** | Claude Code |
| **Cost** | Plugin free; requires a Slack account |
| **Source** | [github.com/slackapi/slack-mcp-plugin/tree/main](https://github.com/slackapi/slack-mcp-plugin/tree/main) |

## What does it do?

With the Slack plugin Claude searches your Slack workspace: messages, channels and threads. That way it quickly finds the context of an earlier discussion or decision, without you having to scroll.

## When do you use it?

* Important agreements are buried somewhere in Slack.
* You want a summary of a busy thread.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
What was decided in #development last week about the release?
```
{% endcode %}

**What you get:** A summary with links to the messages.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install slack@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/slackapi/slack-mcp-plugin/tree/main" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Connect your apps</a>
