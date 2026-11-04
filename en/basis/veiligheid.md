---
description: >-
  Skills can contain instructions and scripts. This is how to install them safely.
icon: shield-halved
cover: ../../.gitbook/assets/cover-en-security.png
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
# Install safely

A skill tells Claude what to do, and can contain scripts that Claude runs. So only install skills you trust.

{% hint style="danger" %}
**Watch out for fake copies.** Of popular skills like Humanizer, copies that look identical are circulating on GitHub. Always install from the repo the author names themselves.
{% endhint %}

## Checklist

- [ ] Does the skill come from a known author or an official marketplace?
- [ ] Have you read the `SKILL.md`? Is there nothing odd in it, like 'send files to…'?
- [ ] Does the skill contain scripts? Have a quick look at what they do.
- [ ] Is there `allowed-tools` in the frontmatter? Claude may use those tools without asking.
- [ ] Does the plugin have **hooks**? They run automatically on certain events.
- [ ] Does data go to an external service (as with debate skills or hosted memory services)? Then don't put sensitive information in it.

## Official vs. community

| | Official (Anthropic) | Community |
| --- | --- | --- |
| Where | `anthropics/skills`, `claude-plugins-official` | All other repos |
| Reviewed | Made or included by Anthropic | No, your own responsibility |
| Quality | Stable | From brilliant to messy |

{% hint style="info" %}
Even for the official marketplace, Anthropic warns: *make sure you trust a plugin before installing it*. Partner plugins can contain MCP servers and software that Anthropic does not control.
{% endhint %}
