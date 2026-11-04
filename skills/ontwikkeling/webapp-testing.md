---
description: >-
  Test lokale webapps met Playwright: klikken, screenshots maken en browserlogs bekijken.
icon: vial
cover: ../../.gitbook/assets/cover-ontwikkeling.png
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

# Webapp Testing

| | |
| --- | --- |
| **Maker** | Anthropic (officieel) |
| **Werkt in** | Claude Code (en Claude-app met code-uitvoering) |
| **Kosten** | Gratis (Apache 2.0) |
| **Bron** | [github.com/anthropics/skills/tree/main/skills/webapp-testing](https://github.com/anthropics/skills/tree/main/skills/webapp-testing) |

## Wat doet het?

Een toolkit waarmee Claude je lokale webapplicatie bedient via Playwright: pagina's openen, formulieren invullen, knoppen testen, screenshots maken en console-logs lezen om fouten op te sporen.

## Wanneer gebruik je het?

* Je wilt controleren of je website of PWA werkt na een wijziging.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Start de app op localhost:3000, test het inlogformulier en maak screenshots van elke stap.
```
{% endcode %}

**Wat je krijgt:** Een testverslag met screenshots en eventuele fouten.

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
npx skills add anthropics/skills --skill webapp-testing
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}


<a href="https://github.com/anthropics/skills/tree/main/skills/webapp-testing" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Ontwikkelen & code</a>
