---
description: >-
  Productieklare engineering-workflows: spec schrijven, taken opsplitsen, stap voor stap bouwen, testen en opleveren.
icon: diagram-project
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

# Agent Skills (Addy Osmani)

{% hint style="danger" %}
**Gespot op social.** Viraal gegaan via o.a. 'I Tried 23 Viral Claude Skills' (Artificial Corner).
{% endhint %}

| | |
| --- | --- |
| **Maker** | Addy Osmani (community) |
| **Werkt in** | Claude Code (+ andere agents) |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) |

## Wat doet het?

Addy Osmani (Google Chrome) bundelde de werkwijzen en kwaliteitspoorten van senior engineers in zo'n 25 skills. Denk aan **spec-driven-development**, **planning-and-task-breakdown**, **incremental-implementation**, test-driven-development, code review, security, performance, documentatie en ADR's, CI/CD en lancering. Claude legt voortgang vast in bestanden, zodat werk consistent en controleerbaar blijft.

## Wanneer gebruik je het?

* Je bouwt serieuze software met Claude Code.
* Je wilt dat Claude eerst een spec schrijft voordat hij bouwt.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Schrijf eerst een spec voor de nieuwe zoekfunctie, splits die op in taken en bouw ze daarna één voor één.
```
{% endcode %}

**Wat je krijgt:** Een spec, een takenlijst en incrementele commits.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add addyosmani/agent-skills
/plugin install agent-skills@addy-agent-skills
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.
{% endtab %}

{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add addyosmani/agent-skills          # alle skills
npx skills add addyosmani/agent-skills --list   # eerst bekijken
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Krijg je bij `/plugin install` een SSH-fout? Gebruik de HTTPS-URL: `/plugin marketplace add https://github.com/addyosmani/agent-skills.git`.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/addyosmani/agent-skills" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Ontwikkelen & code</a>
