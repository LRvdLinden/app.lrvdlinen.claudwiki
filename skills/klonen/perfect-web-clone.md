---
description: >-
  Pixel-perfecte kopie van een webpagina: plak een URL en krijg een gemeten Vite + React-replica.
icon: ruler-combined
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

# Perfect Web Clone

| | |
| --- | --- |
| **Maker** | ericshang98 (community) |
| **Werkt in** | Claude Code (+ andere agents) |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/ericshang98/perfect-web-clone-skill](https://github.com/ericshang98/perfect-web-clone-skill) |

## Wat doet het?

Deze skill is een strak 'speelboek' voor pixel-perfect klonen. Na één opdracht (`clone https://…`) moet de agent vastleggen, plannen, bouwen, meten en repareren tot de kloon door een reeks keuringen komt: volledige capture, complete structuur, echte interacties, gewicht en een visuele score per sectie. De hulptool `pwc` doet het meten en kijken.

## Wanneer gebruik je het?

* Je wilt dat de kopie er echt tot op de pixel hetzelfde uitziet.
* Je wilt meetbaar bewijs dat de kloon klopt.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
clone https://mijn-landingspagina.nl
```
{% endcode %}

**Wat je krijgt:** Een Vite + React-project plus een rapport met scores per sectie.

## Installeren

{% tabs %}
{% tab title="Handmatig" %}
```bash
git clone https://github.com/ericshang98/perfect-web-clone-skill.git ~/.claude/skills/perfect-web-clone
```

Voor het meten heb je ook de tool [Perfect-Web-Clone (pwc)](https://github.com/ericshang98/Perfect-Web-Clone) nodig; zie de README.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Gebruik dit alleen voor je eigen sites en apps, of met toestemming. Logo's, merkuitingen en teksten blijven van de eigenaar, en nabouwen om je als een ander voor te doen (phishing) is verboden. Check ook de gebruiksvoorwaarden van de site.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/ericshang98/perfect-web-clone-skill" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Sites & apps klonen</a>
