---
description: >-
  SwiftUI-best practices: state management, view-opbouw, performance, nieuwe SDK-wijzigingen en Liquid Glass.
icon: swift
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

# SwiftUI Expert (Antoine van der Lee)

| | |
| --- | --- |
| **Maker** | Antoine van der Lee / SwiftLee (community, Nederlands) |
| **Werkt in** | Claude Code (+ Codex, Cursor en andere agents) |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/AvdLee/SwiftUI-Agent-Skill](https://github.com/AvdLee/SwiftUI-Agent-Skill) |

## Wat doet het?

Antoine van der Lee (SwiftLee) is een bekende Nederlandse iOS-ontwikkelaar. Deze skill bundelt praktische SwiftUI-kennis in compacte naslag voor agents en code reviews: hoe je state goed beheert, views opbouwt, performance bewaakt, de nieuwste SDK-wijzigingen toepast en **Liquid Glass** adopteert. Een tweede skill, `update-swiftui-apis`, helpt verouderde API's te vervangen.

## Wanneer gebruik je het?

* Je bouwt een iOS-, iPadOS- of macOS-app in SwiftUI.
* Je wilt dat Claude moderne SwiftUI schrijft in plaats van verouderde patronen.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Review deze SwiftUI-view op state management en performance.
```
{% endcode %}

**Wat je krijgt:** Concrete verbeteringen, zoals @Observable in plaats van ObservableObject.

{% code title="Voorbeeld 2: wat je typt" overflow="wrap" %}
```
Pas het instellingenscherm aan naar Liquid Glass.
```
{% endcode %}

**Wat je krijgt:** Code die de nieuwe designtaal correct gebruikt.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add AvdLee/SwiftUI-Agent-Skill
/plugin install swiftui-expert@swiftui-expert-skill
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.
{% endtab %}

{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills@latest add https://github.com/avdlee/swiftui-agent-skill --skill swiftui-expert-skill
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Van dezelfde maker: [Swift Concurrency](swift-concurrency.md) en [Xcode Build Optimization](xcode-build-optimization.md).
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/AvdLee/SwiftUI-Agent-Skill" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Apps & mobiel</a>
