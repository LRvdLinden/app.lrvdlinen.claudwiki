---
description: >-
  Maakt geanimeerde GIF's die precies voldoen aan de eisen van Slack.
icon: face-grin-stars
cover: ../../.gitbook/assets/cover-creatief.png
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

# Slack GIF Creator

| | |
| --- | --- |
| **Maker** | Anthropic (officieel) |
| **Werkt in** | Claude-app, Claude Code, API |
| **Kosten** | Gratis (Apache 2.0) |
| **Bron** | [github.com/anthropics/skills/tree/main/skills/slack-gif-creator](https://github.com/anthropics/skills/tree/main/skills/slack-gif-creator) |

## Wat doet het?

Een skill met kennis en hulpmiddelen om GIF's te maken die goed werken in Slack: de juiste afmetingen en bestandsgrootte, plus validatie en animatie-ideeën.

## Wanneer gebruik je het?

* Je wilt een grappige GIF of custom emoji voor je team.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Maak een GIF van een dansende tostiapparaat voor Slack.
```
{% endcode %}

**Wat je krijgt:** Een geoptimaliseerde GIF.

## Installeren

{% tabs %}
{% tab title="Claude-app" %}
Deze skill is **al ingebouwd** voor betaalde abonnementen.

1. Open **Instellingen → Mogelijkheden** (Settings → Capabilities).
2. Zet **Code-uitvoering en bestanden maken** aan.
3. Scroll naar **Skills** en zet de skill aan.

Daarna vraag je gewoon in gewone taal wat je wilt; Claude laadt de skill zelf.
{% endtab %}

{% tab title="Claude Code" %}
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add anthropics/skills
/plugin install example-skills@anthropic-agent-skills
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.

Dit installeert het hele pakket **example-skills** (o.a. deze skill).
{% endtab %}

{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add anthropics/skills --skill slack-gif-creator
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}


<a href="https://github.com/anthropics/skills/tree/main/skills/slack-gif-creator" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Creatief & video</a>
