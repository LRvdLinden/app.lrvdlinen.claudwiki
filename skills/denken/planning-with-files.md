---
description: >-
  Houdt een plan, bevindingen en voortgang bij in bestanden op schijf, zodat Claude nooit de draad kwijtraakt.
icon: list-check
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

# Planning with Files

| | |
| --- | --- |
| **Maker** | OthmanAdi (community) |
| **Werkt in** | Claude Code (+ Codex, Cursor, Copilot en 70+ andere agents) |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) |

## Wat doet het?

Bij lange taken vergeet een AI-agent soms waar hij was. Planning with Files lost dat op met drie bestanden: `task_plan.md`, `findings.md` en `progress.md`. Hooks voegen bij elke beurt de belangrijke planningscontext toe, en het plan overleeft zelfs een `/clear`. Daardoor kan Claude een groot project in stappen afwerken.

## Wanneer gebruik je het?

* Je laat Claude een groot, meerstappig project doen.
* Je wilt kunnen terugzien wat er is gedaan en gevonden.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Plan de migratie van mijn app naar een nieuwe iOS-versie met planning-with-files.
```
{% endcode %}

**Wat je krijgt:** Een plan op schijf dat Claude stap voor stap afwerkt en bijwerkt.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add OthmanAdi/planning-with-files
/plugin install planning-with-files@planning-with-files
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.
{% endtab %}

{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add OthmanAdi/planning-with-files
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* De hooks werken alleen in Claude Code (en andere agents met hooks), niet in de Claude-app.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/OthmanAdi/planning-with-files" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Denken & plannen</a>
