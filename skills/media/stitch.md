---
description: >-
  Werken met Google Stitch: designs genereren, design.md extraheren en omzetten naar React of shadcn/ui.
icon: object-group
cover: ../../.gitbook/assets/cover-media.png
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

# Google Stitch Skills

| | |
| --- | --- |
| **Maker** | Google Labs (officieel van de makers) |
| **Werkt in** | Claude Code (+ Codex, Gemini CLI, Cursor) |
| **Kosten** | Gratis |
| **Bron** | [github.com/google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) |

## Wat doet het?

Skills voor Google Stitch, Google's AI-designtool: designs genereren en verbeteren, een `design.md` uit een bestaand ontwerp halen, je designsysteem beheren en ontwerpen omzetten naar React, React Native, shadcn/ui of een Vite-dashboard.

## Wanneer gebruik je het?

* Je ontwerpt in Stitch en wilt het snel naar code brengen.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Zet dit Stitch-ontwerp om naar React-componenten met shadcn/ui.
```
{% endcode %}

**Wat je krijgt:** Componentcode die het ontwerp volgt.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
```bash
npx plugins add google-labs-code/stitch-skills --scope project --target claude-code
```
{% endtab %}

{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add google-labs-code/stitch-skills
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/google-labs-code/stitch-skills" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Audio, beeld & visuals</a>
