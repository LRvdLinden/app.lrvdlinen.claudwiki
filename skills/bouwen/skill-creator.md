---
description: >-
  De skill om skills te maken: opzetten, verbeteren, testen met evals en de beschrijving optimaliseren.
icon: hammer
cover: ../../.gitbook/assets/cover-bouwen.png
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

# Skill Creator

| | |
| --- | --- |
| **Maker** | Anthropic (officieel) |
| **Werkt in** | Claude-app, Claude Code, API |
| **Kosten** | Gratis (Apache 2.0) |
| **Bron** | [github.com/anthropics/skills/tree/main/skills/skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) |

## Wat doet het?

Skill Creator begeleidt je bij het maken van een eigen skill: wat moet hij doen, wanneer moet hij afgaan, welke scripts of voorbeelden horen erbij. Daarna test hij de skill met evals, meet hij prestaties (ook met varianties) en optimaliseert hij de beschrijving zodat Claude hem op het juiste moment kiest.

## Wanneer gebruik je het?

* Je merkt dat je Claude steeds dezelfde instructies geeft.
* Je bestaande skill gaat niet (of te vaak) af.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Maak een skill van mijn vaste werkwijze voor het publiceren van een app-update.
```
{% endcode %}

**Wat je krijgt:** Een complete skillmap met SKILL.md, klaar om te uploaden.

{% code title="Voorbeeld 2: wat je typt" overflow="wrap" %}
```
Mijn skill wordt nooit gebruikt. Verbeter de beschrijving en test het.
```
{% endcode %}

**Wat je krijgt:** Een verbeterde beschrijving met testresultaten.

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
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install skill-creator@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.
{% endtab %}

{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add anthropics/skills --skill skill-creator
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* In de Claude-app kun je ook gewoon zeggen: 'maak hier een skill van'.
{% endhint %}


<a href="https://github.com/anthropics/skills/tree/main/skills/skill-creator" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Zelf skills bouwen</a>
