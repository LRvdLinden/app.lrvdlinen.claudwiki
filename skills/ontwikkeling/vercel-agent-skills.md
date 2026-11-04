---
description: >-
  React- en Next.js-best practices, webdesign-richtlijnen en deployen naar Vercel.
icon: rocket
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

# Vercel Agent Skills

| | |
| --- | --- |
| **Maker** | Vercel (officieel van de makers) |
| **Werkt in** | Claude Code (+ andere agents) |
| **Kosten** | Gratis |
| **Bron** | [github.com/vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) |

## Wat doet het?

Vercel publiceert skills met hun eigen best practices: **react-best-practices**, **composition-patterns**, **react-native-skills**, **react-view-transitions**, **web-design-guidelines**, **writing-guidelines**, **deploy-to-vercel** en **vercel-optimize** (een audit op kosten, performance en caching).

## Wanneer gebruik je het?

* Je bouwt met React, Next.js of React Native.
* Je host op Vercel.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Review deze pagina op de web-design-guidelines.
```
{% endcode %}

**Wat je krijgt:** Een lijst met concrete verbeteringen.

{% code title="Voorbeeld 2: wat je typt" overflow="wrap" %}
```
Deploy dit project naar Vercel.
```
{% endcode %}

**Wat je krijgt:** Een live preview-URL.

## Installeren

{% tabs %}
{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add vercel-labs/agent-skills
npx skills add vercel-labs/agent-skills --skill web-design-guidelines -a claude-code
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Op [skills.sh](https://skills.sh) vind je duizenden skills die je met dezelfde CLI installeert.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/vercel-labs/agent-skills" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Ontwikkelen & code</a>
