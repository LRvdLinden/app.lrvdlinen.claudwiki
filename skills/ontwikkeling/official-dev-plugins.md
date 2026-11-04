---
description: >-
  Anthropics eigen Claude Code-plugins: code review, feature-dev, commits, PR-review, security en hooks.
icon: puzzle-piece
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

# Officiële dev-plugins

| | |
| --- | --- |
| **Maker** | Anthropic (officieel) |
| **Werkt in** | Claude Code |
| **Kosten** | Gratis |
| **Bron** | [github.com/anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |

## Wat doet het?

In de officiële marketplace staan plugins die Anthropic zelf onderhoudt. Een greep:

| Plugin | Wat het doet |
| --- | --- |
| `code-review` | Automatische PR-review met meerdere gespecialiseerde agents en een betrouwbaarheidsscore |
| `feature-dev` | Complete feature-workflow: codebase verkennen, architectuur ontwerpen, kwaliteitscheck |
| `commit-commands` | Snelle commando's om te committen, pushen en PR's te maken |
| `pr-review-toolkit` | Review-agents voor comments, tests, foutafhandeling, types en vereenvoudiging |
| `security-guidance` | Waarschuwt bij onveilige code (injectie, XSS, SSRF, hardcoded secrets en meer) |
| `hookify` | Maakt eenvoudig hooks om ongewenst gedrag te voorkomen |
| `claude-md-management` | Houdt je CLAUDE.md-bestanden actueel en goed |
| `claude-code-setup` | Analyseert je codebase en stelt passende hooks, skills en MCP-servers voor |
| `code-simplifier` | Maakt code helderder zonder gedrag te veranderen |
| `playground` | Maakt interactieve HTML-playgrounds met live preview |
| `ralph-loop` | Laat Claude in een lus doorwerken tot een taak echt af is |

Daarnaast zijn er taal-plugins (LSP) voor o.a. Swift, TypeScript, Python, Kotlin en Rust.

## Wanneer gebruik je het?

* Je werkt met Claude Code aan een echte codebase.
* Je wilt reviews en commits standaardiseren.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
/code-review
```
{% endcode %}

**Wat je krijgt:** Een review van je huidige PR met bevindingen en scores.

{% code title="Voorbeeld 2: wat je typt" overflow="wrap" %}
```
/feature-dev Voeg dark mode toe aan de instellingen
```
{% endcode %}

**Wat je krijgt:** Een begeleide workflow van verkennen tot opleveren.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install code-review@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.

Vervang `code-review` door de plugin die je wilt, bijvoorbeeld `feature-dev`, `swift-lsp` of `security-guidance`.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Ook de plugin `swift-lsp` is handig als je iOS-apps bouwt.
{% endhint %}


<a href="https://github.com/anthropics/claude-plugins-official" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Ontwikkelen & code</a>
