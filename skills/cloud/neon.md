---
description: >-
  Skills voor Neon serverless Postgres: database, auth, functions, object storage en realtime.
icon: database
cover: ../../.gitbook/assets/cover-cloud.png
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

# Neon Postgres

| | |
| --- | --- |
| **Maker** | Neon (officieel van de makers) |
| **Werkt in** | Claude Code (+ andere agents) |
| **Kosten** | Gratis |
| **Bron** | [github.com/neondatabase/agent-skills](https://github.com/neondatabase/agent-skills) |

## Wat doet het?

Neon's eigen skills voor hun serverless Postgres-platform, inclusief branches voor elke feature, Neon Auth, functions, object storage, realtime en de AI-gateway.

## Wanneer gebruik je het?

* Je gebruikt (of overweegt) Neon als database.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Maak een Neon-branch voor deze feature en draai de migratie daarop.
```
{% endcode %}

**Wat je krijgt:** Een aparte databasebranch om veilig te testen.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add neondatabase/agent-skills
/plugin install neon-postgres@neon
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.
{% endtab %}

{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add neondatabase/agent-skills
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/neondatabase/agent-skills" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Data, cloud & betalen</a>
