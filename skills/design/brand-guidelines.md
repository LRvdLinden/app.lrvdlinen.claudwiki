---
description: >-
  Voorbeeld van een huisstijl-skill: past vaste merkkleuren en typografie toe op alles wat Claude maakt.
icon: copyright
cover: ../../.gitbook/assets/cover-design.png
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

# Brand Guidelines

| | |
| --- | --- |
| **Maker** | Anthropic (officieel) |
| **Werkt in** | Claude-app, Claude Code, API |
| **Kosten** | Gratis (Apache 2.0) |
| **Bron** | [github.com/anthropics/skills/tree/main/skills/brand-guidelines](https://github.com/anthropics/skills/tree/main/skills/brand-guidelines) |

## Wat doet het?

Deze skill past de huisstijl van Anthropic toe (kleuren en lettertypen). Hij is vooral interessant als **voorbeeld**: kopieer hem, vervang de kleuren en fonts door die van jouw merk en Claude maakt voortaan alles in jouw huisstijl.

## Wanneer gebruik je het?

* Je wilt dat Claude standaard jouw merkkleuren en fonts gebruikt.
* Je wilt leren hoe een huisstijl-skill is opgebouwd.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Maak met mijn huisstijl-skill een flyer voor de buurtavond.
```
{% endcode %}

**Wat je krijgt:** Een flyer in jouw kleuren en lettertypen.

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
npx skills add anthropics/skills --skill brand-guidelines
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Zie [Je eigen skill maken](../../basis/eigen-skill-maken.md) om er je eigen huisstijl van te maken.
{% endhint %}


<a href="https://github.com/anthropics/skills/tree/main/skills/brand-guidelines" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Design & frontend</a>
