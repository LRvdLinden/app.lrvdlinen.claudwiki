---
description: >-
  Een methode om websites trouw te klonen zonder verzonnen code: eerst de echte broncode, dan pas nabouwen.
icon: code-compare
cover: ../../.gitbook/assets/cover-klonen.png
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

# Web Clone (echte bron eerst)

| | |
| --- | --- |
| **Maker** | Jane-xiaoer (community) |
| **Werkt in** | Claude Code |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) |

## Wat doet het?

AI-tools maken vaak 'kloonanalyses' vol code die er goed uitziet maar verzonnen is. Deze skill werkt anders: een beslisboom in zes stappen en scripts die eerst de echte bron ophalen. Statische HTML/CSS-sites worden gespiegeld met `wget --mirror`, React-, Vue- en Next-sites worden op een template nagebouwd, en bij sites met meerdere pagina's worden eerst alle routes in kaart gebracht. Ook voor WebGL-sites is er een aanpak.

## Wanneer gebruik je het?

* Je wilt een kloon die gebaseerd is op de echte code, niet op gokwerk.
* Je wilt een site offline kunnen bekijken of bestuderen.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Kloon mijn portfoliosite zodat ik hem offline kan aanpassen.
```
{% endcode %}

**Wat je krijgt:** Een lokale kopie volgens de best passende methode.

## Installeren

{% tabs %}
{% tab title="Handmatig" %}
```bash
git clone https://github.com/Jane-xiaoer/claude-skill-web-clone.git ~/.claude/skills/web-clone
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Gebruik dit alleen voor je eigen sites en apps, of met toestemming. Logo's, merkuitingen en teksten blijven van de eigenaar, en nabouwen om je als een ander voor te doen (phishing) is verboden. Check ook de gebruiksvoorwaarden van de site.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/Jane-xiaoer/claude-skill-web-clone" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Sites & apps klonen</a>
