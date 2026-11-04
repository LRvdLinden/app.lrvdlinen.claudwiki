---
description: >-
  Goede tests schrijven met het nieuwe Swift Testing-framework (@Test, #expect).
icon: flask-vial
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

# Swift Testing Pro

| | |
| --- | --- |
| **Maker** | Paul Hudson / twostraws (community) |
| **Werkt in** | Claude Code (+ Codex, Gemini) |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/twostraws/Swift-Testing-Agent-Skill](https://github.com/twostraws/Swift-Testing-Agent-Skill) |

## Wat doet het?

Leert Claude het moderne Swift Testing-framework: `@Test`, `#expect`, geparametriseerde tests, traits en het omzetten van XCTest naar Swift Testing.

## Wanneer gebruik je het?

* Je wilt tests toevoegen aan je Swift-app.
* Je migreert van XCTest.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Schrijf Swift Testing-tests voor deze DateFormatter-helper, inclusief randgevallen.
```
{% endcode %}

**Wat je krijgt:** Geparametriseerde tests met duidelijke namen.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add twostraws/Swift-Testing-Agent-Skill
/plugin install swift-testing-pro@swift-testing-agent-skill
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.
{% endtab %}

{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add https://github.com/twostraws/swift-testing-agent-skill --skill swift-testing-pro
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/twostraws/Swift-Testing-Agent-Skill" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Apps & mobiel</a>
