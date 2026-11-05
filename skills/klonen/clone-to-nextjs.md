---
description: >-
  Spiegelt een eenvoudige informatieve website (praktijk, restaurant, portfolio) direct naar een Next.js-project.
icon: copy
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

# Clone to Next.js

| | |
| --- | --- |
| **Maker** | Aisahub (community) |
| **Werkt in** | Claude Code |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/Aisahub/skill-clone-to-nextjs](https://github.com/Aisahub/skill-clone-to-nextjs) |

## Wat doet het?

Bedoeld voor simpele informatieve sites zoals een huisartsenpraktijk, restaurant, portfolio of bedrijfspresentatie. Elke pagina wordt in een echte Chromium-browser (Playwright) gerenderd, er wordt naar beneden gescrold zodat alles laadt, en daarna worden alle bestanden opgehaald en links herschreven. Het resultaat is een Next.js App Router-project.

## Wanneer gebruik je het?

* Je wilt een kleine, eenvoudige site snel naar Next.js overzetten.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Zet de website van onze wijkvereniging om naar een Next.js-project.
```
{% endcode %}

**Wat je krijgt:** Een Next.js-project met alle pagina's en afbeeldingen.

## Installeren

{% tabs %}
{% tab title="Handmatig" %}
```bash
git clone https://github.com/Aisahub/skill-clone-to-nextjs ~/.claude/skills/clone-to-nextjs
```

De skill is direct beschikbaar in je volgende Claude Code-sessie.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Gebruik dit alleen voor je eigen sites en apps, of met toestemming. Logo's, merkuitingen en teksten blijven van de eigenaar, en nabouwen om je als een ander voor te doen (phishing) is verboden. Check ook de gebruiksvoorwaarden van de site.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/Aisahub/skill-clone-to-nextjs" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Sites & apps klonen</a>
