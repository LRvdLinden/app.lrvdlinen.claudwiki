---
description: >-
  Manage Firestore, Authentication, Cloud Functions, Hosting and Storage from Claude.
icon: fire
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

# Firebase

| | |
| --- | --- |
| **Maker** | Google · official Claude marketplace |
| **Works in** | Claude Code |
| **Cost** | Plugin free; requires a Google account |
| **Source** | [github.com/anthropics/claude-plugins-public/tree/main/external_plugins/firebase](https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/firebase) |

## What does it do?

The Firebase plugin gives Claude access to your Firebase backend: Firestore databases, authentication, cloud functions, hosting and storage. Handy for apps that use Firebase as their backend, like many iOS apps.

## When do you use it?

* Your app uses Firebase.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Write a Firestore rule so users can only read their own notifications.
```
{% endcode %}

**What you get:** Firestore security rules plus explanation.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install firebase@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/firebase" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Data, cloud & payments</a>
