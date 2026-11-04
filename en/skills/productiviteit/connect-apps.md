---
description: >-
  Lets Claude take real actions in 1000+ apps: send mail, create issues, post messages.
icon: link
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

# Connect Apps (Composio)

| | |
| --- | --- |
| **Maker** | Composio (community) |
| **Works in** | Claude Code |
| **Cost** | Free to start; Composio account required |
| **Source** | [github.com/ComposioHQ/awesome-claude-skills/tree/master/connect-apps-plugin](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/connect-apps-plugin) |

## What does it do?

With this plugin Claude takes actions in external apps like Gmail, Slack and GitHub. Composio handles the login and connects to more than a thousand apps. The repo also contains hundreds of 'automation' skills per app.

## When do you use it?

* You want Claude to actually do things in your apps, not just write text.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Send a summary of this meeting to the team in Slack.
```
{% endcode %}

**What you get:** A message in your Slack channel.

## Install

{% tabs %}
{% tab title="Claude Code" %}
```bash
git clone https://github.com/ComposioHQ/awesome-claude-skills.git
cd awesome-claude-skills
claude --plugin-dir ./connect-apps-plugin
```

Then follow the setup in the README.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* In the Claude app you can also connect many apps directly via **Settings → Connectors**.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/ComposioHQ/awesome-claude-skills/tree/master/connect-apps-plugin" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Productivity & tools</a>
