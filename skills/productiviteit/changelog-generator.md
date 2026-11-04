---
description: >-
  Maakt van je git-commits heldere release notes voor gebruikers.
icon: clock-rotate-left
cover: ../../.gitbook/assets/cover-productiviteit.png
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

# Changelog Generator

| | |
| --- | --- |
| **Maker** | ComposioHQ (community) |
| **Werkt in** | Claude Code |
| **Kosten** | Gratis |
| **Bron** | [github.com/ComposioHQ/awesome-claude-skills/tree/master/changelog-generator](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/changelog-generator) |

## Wat doet het?

Analyseert je commitgeschiedenis, deelt wijzigingen in (nieuw, verbeterd, opgelost) en vertaalt technische commits naar duidelijke, klantvriendelijke release notes.

## Wanneer gebruik je het?

* Je publiceert een nieuwe versie van je app en wilt 'Wat is er nieuw'-tekst.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Maak release notes voor alles sinds tag v2.3.0, in het Nederlands en Engels.
```
{% endcode %}

**Wat je krijgt:** Release notes in twee talen.

## Installeren

{% tabs %}
{% tab title="Handmatig" %}
Kopieer de skillmap naar je persoonlijke skills-map (voor alle projecten) of naar `.claude/skills/` in één project:

```bash
git clone https://github.com/ComposioHQ/awesome-claude-skills.git
cp -r awesome-claude-skills/changelog-generator ~/.claude/skills/
```
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/ComposioHQ/awesome-claude-skills/tree/master/changelog-generator" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Productiviteit & tools</a>
