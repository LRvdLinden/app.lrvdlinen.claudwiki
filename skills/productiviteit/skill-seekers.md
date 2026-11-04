---
description: >-
  Zet elke documentatiewebsite, GitHub-repo, PDF of video automatisch om in een Claude-skill.
icon: magnifying-glass-plus
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

# Skill Seekers

| | |
| --- | --- |
| **Maker** | yusufkaraaslan (community) |
| **Werkt in** | Losse tool (Python), output werkt in Claude |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) |

## Wat doet het?

Skill Seekers haalt documentatie op (websites, GitHub-repo's, PDF's, video's, notebooks) en verpakt die als skill. Zo geef je Claude in een paar minuten expertkennis van een tool of API die hij nog niet kent.

## Wanneer gebruik je het?

* Je werkt met een niche-API of tool waar Claude weinig van weet.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
skill-seekers scrape --url https://docs.voorbeeld.nl
```
{% endcode %}

**Wat je krijgt:** Een kant-en-klare skillmap om te installeren.

## Installeren

{% tabs %}
{% tab title="Installeren" %}
```bash
pip install skill-seekers
```

Volg daarna de quickstart in de README.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/yusufkaraaslan/Skill_Seekers" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Productiviteit & tools</a>
