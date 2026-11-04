---
description: >-
  De skills die Sentry intern gebruikt: bugs vinden, code reviews, commits, PR's en security reviews.
icon: bug
cover: ../../.gitbook/assets/cover-cloud.png
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

# Sentry Skills

| | |
| --- | --- |
| **Maker** | Sentry (officieel van de makers) |
| **Werkt in** | Claude Code |
| **Kosten** | Gratis |
| **Bron** | [github.com/getsentry/skills](https://github.com/getsentry/skills) |

## Wat doet het?

Sentry deelt de skills van hun eigen engineers: `find-bugs`, `code-review`, `security-review`, `commit`, `pr-writer`, `iterate-pr`, een GitHub Actions-securityreview, `skill-scanner` (controleert skills op risico's) en meer.

## Wanneer gebruik je het?

* Je wilt professionele dev-workflows overnemen.
* Je wilt skills van anderen scannen op risico's.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
/find-bugs
```
{% endcode %}

**Wat je krijgt:** Een lijst met waarschijnlijke bugs in je huidige wijzigingen.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
```bash
claude plugin marketplace add getsentry/skills
claude plugin install sentry-skills@sentry-skills
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Voor foutmonitoring zelf: de plugin `sentry` in de officiële marketplace.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/getsentry/skills" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Data, cloud & betalen</a>
