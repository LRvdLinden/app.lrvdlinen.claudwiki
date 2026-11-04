---
description: >-
  Helpt Claude met async/await, actors, Sendable en de migratie naar Swift 6-strict concurrency.
icon: arrows-split-up-and-left
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

# Swift Concurrency

| | |
| --- | --- |
| **Maker** | Antoine van der Lee (community, Nederlands) |
| **Werkt in** | Claude Code (+ andere agents) |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/AvdLee/Swift-Concurrency-Agent-Skill](https://github.com/AvdLee/Swift-Concurrency-Agent-Skill) |

## Wat doet het?

Swift Concurrency is lastig, en AI-agents maken er vaak fouten in. Deze skill geeft Claude de juiste kennis over async/await, actors, `@MainActor`, `Sendable`, tasks en het oplossen van strict-concurrency-waarschuwingen in Swift 6.

## Wanneer gebruik je het?

* Je krijgt Swift 6-concurrencyfouten.
* Je wilt oude completion handlers omzetten naar async/await.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Los alle Sendable-waarschuwingen in deze module op zonder @unchecked.
```
{% endcode %}

**Wat je krijgt:** Een correcte, veilige oplossing per waarschuwing.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add AvdLee/Swift-Concurrency-Agent-Skill
/plugin install swift-concurrency@swift-concurrency-agent-skill
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.
{% endtab %}

{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills@latest add https://github.com/avdlee/swift-concurrency-agent-skill --skill swift-concurrency
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/AvdLee/Swift-Concurrency-Agent-Skill" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Apps & mobiel</a>
