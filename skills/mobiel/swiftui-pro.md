---
description: >-
  Agent-skill van Hacking with Swift: moderne SwiftUI-code voor iOS 26+ en Swift 6.
icon: mobile-screen
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

# SwiftUI Pro (Paul Hudson)

| | |
| --- | --- |
| **Maker** | Paul Hudson / twostraws (community) |
| **Werkt in** | Claude Code (+ Codex, Gemini) |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/twostraws/SwiftUI-Agent-Skill](https://github.com/twostraws/SwiftUI-Agent-Skill) |

## Wat doet het?

Paul Hudson, de maker van Hacking with Swift, heeft zijn SwiftUI-kennis in een skill gegoten. Hij is gericht op iOS 26 en nieuwer en recente Swift-versies, en zorgt dat Claude actuele API's en idiomen gebruikt en klassieke valkuilen vermijdt.

## Wanneer gebruik je het?

* Je bouwt SwiftUI-apps voor de nieuwste iOS-versies.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Bouw een lijst met zoeken, swipe-acties en pull-to-refresh in modern SwiftUI.
```
{% endcode %}

**Wat je krijgt:** Moderne, compacte SwiftUI-code.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add twostraws/SwiftUI-Agent-Skill
/plugin install swiftui-pro@swiftui-agent-skill
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.
{% endtab %}

{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add https://github.com/twostraws/swiftui-agent-skill --skill swiftui-pro
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Ook van Paul Hudson: [Swift Testing Pro](swift-testing-pro.md).
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/twostraws/SwiftUI-Agent-Skill" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Apps & mobiel</a>
