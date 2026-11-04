---
description: >-
  Laat Claude je plan genadeloos ondervragen voordat hij begint, en vat lange chats samen om verder te gaan.
icon: fire-flame-curved
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

# Grill Me & Handoff

{% hint style="danger" %}
**Gespot op social.** Viraal gegaan via o.a. 'I Tried 23 Viral Claude Skills' (Artificial Corner).
{% endhint %}

| | |
| --- | --- |
| **Maker** | Matt Pocock (community) |
| **Werkt in** | Claude Code (+ Cursor, Codex en andere agents) |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/mattpocock/skills](https://github.com/mattpocock/skills) |

## Wat doet het?

Uit de populaire skillcollectie van Matt Pocock springen twee skills eruit. **Grill Me** is een 'meedogenloos interview': Claude vraagt door over je doelen, doelgroep, scope en wat er mis kan gaan, totdat je plan echt scherp is. **Handoff** vat een lang gesprek samen in een overdrachtsdocument, zodat je verder kunt in een nieuwe chat of met een andere agent zonder context kwijt te raken. De collectie bevat verder skills voor TDD, code reviews, specs, tickets en meer.

## Wanneer gebruik je het?

* Je hebt een idee maar weet nog niet precies wat je wilt.
* Je gesprek wordt te lang en Claude begint dingen te vergeten.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
/grill-me Ik wil een app maken voor vrijwilligers in de wijk.
```
{% endcode %}

**Wat je krijgt:** Een reeks scherpe vragen, één voor één, tot alles helder is.

{% code title="Voorbeeld 2: wat je typt" overflow="wrap" %}
```
/handoff
```
{% endcode %}

**Wat je krijgt:** Een compact overdrachtsdocument om in een nieuwe sessie te plakken.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
De collectie staat in de officiële marketplace:

```bash
claude plugin install mattpocock-skills@claude-plugins-official
```
{% endtab %}

{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills@latest add mattpocock/skills
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.

Kies in de installer welke skills je wilt en neem `setup-matt-pocock-skills` mee. Bijwerken: `npx skills@latest update`.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/mattpocock/skills" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Denken & plannen</a>
