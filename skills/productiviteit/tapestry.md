---
description: >-
  Eén commando: van een URL (video, artikel, PDF) naar schone tekst én een actieplan om het toe te passen.
icon: graduation-cap
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

# Tapestry (Learn This)

| | |
| --- | --- |
| **Maker** | Michal Parkola (community) |
| **Werkt in** | Claude Code |
| **Kosten** | Gratis |
| **Bron** | [github.com/michalparkola/tapestry-skills-for-claude-code](https://github.com/michalparkola/tapestry-skills-for-claude-code) |

## Wat doet het?

Zeg `learn-this <URL>` en de skill herkent het type inhoud (YouTube, artikel, PDF), haalt de tekst schoon binnen en maakt er een **Ship-Learn-Next**-actieplan van. Losse skills: youtube-transcript, article-extractor, ship-learn-next, scrum-sage, session-log en unblock-action.

## Wanneer gebruik je het?

* Je kijkt veel tutorials en wilt er ook echt iets mee doen.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
learn-this https://www.youtube.com/watch?v=...
```
{% endcode %}

**Wat je krijgt:** Transcript plus een concreet stappenplan.

## Installeren

{% tabs %}
{% tab title="Handmatig" %}
Kopieer de skillmap naar je persoonlijke skills-map (voor alle projecten) of naar `.claude/skills/` in één project:

```bash
git clone https://github.com/michalparkola/tapestry-skills-for-claude-code.git
cd tapestry-skills-for-claude-code
cp -r learn-this youtube-transcript article-extractor ship-learn-next ~/.claude/skills/
```
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/michalparkola/tapestry-skills-for-claude-code" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Productiviteit & tools</a>
