---
description: >-
  Laat Claude zelf Playwright-scripts schrijven en draaien, van simpele paginatests tot lange flows.
icon: masks-theater
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

# Playwright Skill

| | |
| --- | --- |
| **Maker** | lackeyjb (community) |
| **Werkt in** | Claude Code (+ Cursor en meer) |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/lackeyjb/playwright-skill](https://github.com/lackeyjb/playwright-skill) |

## Wat doet het?

Een algemene browserautomatisering-skill: Claude schrijft en draait Playwright-code ter plekke, voor tests, het controleren van formulieren of het doorlopen van een complete gebruikersflow.

## Wanneer gebruik je het?

* Je wilt je webapp automatisch laten testen of controleren.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Test de registratieflow op mijn site en meld wat er misgaat.
```
{% endcode %}

**Wat je krijgt:** Een testrun met screenshots en bevindingen.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add lackeyjb/playwright-skill
/plugin install playwright-skill@playwright-skill
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.
{% endtab %}

{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add lackeyjb/playwright-skill --skill playwright-skill --agent claude-code --global --yes
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Zie ook de officiële [Webapp Testing](webapp-testing.md).
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/lackeyjb/playwright-skill" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Ontwikkelen & code</a>
