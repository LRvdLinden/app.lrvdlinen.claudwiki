---
description: >-
  Voegt na belangrijk advies 2 à 3 slimme controlevragen toe, zodat je de aannames zelf checkt.
icon: circle-question
cover: ../../.gitbook/assets/cover-denken.png
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

# Discernment Nudge

| | |
| --- | --- |
| **Maker** | Anthropic (officieel) |
| **Werkt in** | Claude-app, Claude Code, API |
| **Kosten** | Gratis |
| **Bron** | [github.com/anthropics/skills/tree/main/skills/discernment-nudge](https://github.com/anthropics/skills/tree/main/skills/discernment-nudge) |

## Wat doet het?

Nadat Claude je advies, een plan, een schatting of een analyse heeft gegeven, stelt deze skill 2 à 3 korte vervolgvragen die precies op dat antwoord ingaan: welke feiten je moet checken, welke aannames er onder zitten en welke context mogelijk ontbreekt. Maximaal één keer per gesprek, dus niet irritant.

## Wanneer gebruik je het?

* Je gebruikt Claude voor beslissingen en wilt kritisch blijven.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Maak een begroting voor ons buurtfeest.
```
{% endcode %}

**Wat je krijgt:** De begroting, met daaronder vragen als 'Klopt het aantal bezoekers waar dit op is gebaseerd?'

## Installeren

{% tabs %}
{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add anthropics/skills --skill discernment-nudge
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}

{% tab title="Claude-app" %}
1. Download de repo als ZIP: [github.com/anthropics/skills](https://github.com/anthropics/skills) → **Code → Download ZIP**.
2. Pak uit en zoek de map `skills/discernment-nudge` (daarin staat `SKILL.md`).
3. Maak van **alleen die map** een nieuwe ZIP. De mapnaam moet gelijk zijn aan de skillnaam.
4. Ga naar **Instellingen → Mogelijkheden → Skills** en klik op **Skill uploaden**.
5. Zet de skill aan.

Skills in de Claude-app vragen een Pro-, Max-, Team- of Enterprise-abonnement en **Code-uitvoering en bestanden maken** moet aanstaan.
{% endtab %}
{% endtabs %}


<a href="https://github.com/anthropics/skills/tree/main/skills/discernment-nudge" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Denken & plannen</a>
