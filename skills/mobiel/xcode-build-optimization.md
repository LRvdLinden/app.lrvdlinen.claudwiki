---
description: >-
  Zes skills die je Xcode-builds meten en versnellen: clean, incrementeel, compile-hotspots en SPM.
icon: gauge-high
cover: ../../.gitbook/assets/cover-mobiel.png
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

# Xcode Build Optimization

| | |
| --- | --- |
| **Maker** | Antoine van der Lee (community, Nederlands) |
| **Werkt in** | Claude Code (+ andere agents) |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/AvdLee/Xcode-Build-Optimization-Agent-Skill](https://github.com/AvdLee/Xcode-Build-Optimization-Agent-Skill) |

## Wat doet het?

Een orchestrator-skill met vijf specialisten: benchmark, compilatie-analyse, projectinstellingen, Swift Package Manager-analyse en een fixer. Claude meet eerst hoe lang je builds duren, zoekt de knelpunten en stelt gerichte verbeteringen voor.

## Wanneer gebruik je het?

* Je builds zijn traag en je wilt weten waarom.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Benchmark mijn project en maak de incrementele build sneller.
```
{% endcode %}

**Wat je krijgt:** Metingen vooraf en achteraf, met de aanpassingen ertussen.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add AvdLee/Xcode-Build-Optimization-Agent-Skill
/plugin install xcode-build-skills@xcode-build-skills
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.
{% endtab %}

{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add https://github.com/avdlee/xcode-build-optimization-agent-skill
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Installeer alle zes de skills: de orchestrator heeft de specialisten nodig.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/AvdLee/Xcode-Build-Optimization-Agent-Skill" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Apps & mobiel</a>
