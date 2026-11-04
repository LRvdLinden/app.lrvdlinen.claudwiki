---
description: >-
  Een complete werkmethode: brainstormen, plannen schrijven, test-first bouwen, systematisch debuggen en controleren.
icon: bolt
cover: ../../.gitbook/assets/cover-denken.png
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

# Superpowers

{% hint style="danger" %}
**Gespot op social.** Tip van Bart Boonstra: *'Superpowers laat Claude écht in stappen denken. Brainstormen en plannen wordt 10x scherper.'*
{% endhint %}

| | |
| --- | --- |
| **Maker** | Jesse Vincent / obra (community) |
| **Werkt in** | Claude Code (+ Codex, Antigravity en meer) |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/obra/superpowers](https://github.com/obra/superpowers) |

## Wat doet het?

Superpowers is een van de bekendste skillpakketten. Het is een complete ontwikkelmethode, opgebouwd uit losse skills die elkaar aanvullen: **brainstorming** (eerst samen het idee scherp krijgen), **writing-plans** en **executing-plans**, **test-driven-development**, **systematic-debugging**, **verification-before-completion** (eerst bewijzen dat iets werkt), code reviews vragen en ontvangen, werken met git worktrees en subagents. Een start-skill zorgt dat Claude ze ook echt gebruikt. Brainstorming werkt ook buiten software: voor een talk, een bedrijf of een verbouwing.

## Wanneer gebruik je het?

* Je begint aan een nieuwe feature of een nieuw project.
* Claude springt te snel naar code en mist het grotere plaatje.
* Je zit vast met een bug en wilt een systematische aanpak.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Ik wil een widget toevoegen aan mijn app. Laten we eerst brainstormen.
```
{% endcode %}

**Wat je krijgt:** Claude stelt eerst vragen, stelt ontwerpen voor en schrijft daarna een plan voordat hij code schrijft.

{% code title="Voorbeeld 2: wat je typt" overflow="wrap" %}
```
De tests falen sinds de laatste update. Debug dit systematisch.
```
{% endcode %}

**Wat je krijgt:** Claude zoekt eerst de oorzaak en bewijst die, voordat hij iets repareert.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install superpowers@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.
{% endtab %}

{% tab title="Superpowers-marketplace" %}
De eigen marketplace van de maker, met extra gerelateerde plugins:

```bash
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Gebruik je meerdere tools (Claude Code én Codex)? Installeer Superpowers dan per tool apart.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/obra/superpowers" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Denken & plannen</a>
