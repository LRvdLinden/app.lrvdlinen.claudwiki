---
description: >-
  Repositories, merge requests, CI/CD-pipelines, issues en wiki's in GitLab.
icon: gitlab
cover: ../../.gitbook/assets/cover-koppelingen.png
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
| **Maker** | GitLab · officiële Claude-marketplace |
| **Werkt in** | Claude Code |
| **Kosten** | Plugin gratis; je hebt een GitLab-account nodig |
| **Bron** | [github.com/anthropics/claude-plugins-public/tree/main/external_plugins/gitlab](https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/gitlab) |

## Wat doet het?

De GitLab-plugin koppelt Claude aan het GitLab DevOps-platform: repositories beheren, merge requests, CI/CD-pipelines volgen, issues en wiki's.

## Wanneer gebruik je het?

* Je team gebruikt GitLab in plaats van GitHub.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Waarom faalt de laatste pipeline op main?
```
{% endcode %}

**Wat je krijgt:** De foutmelding uit de pipeline plus een voorstel voor de oplossing.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install gitlab@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/gitlab" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Apps koppelen</a>
