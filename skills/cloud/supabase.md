---
description: >-
  Officiële Supabase-skills en Postgres-best practices voor database, auth en storage.
icon: bolt-lightning
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

# Supabase

| | |
| --- | --- |
| **Maker** | Supabase (officieel van de makers) |
| **Werkt in** | Claude Code (+ 18 andere agents) |
| **Kosten** | Gratis |
| **Bron** | [github.com/supabase/agent-skills](https://github.com/supabase/agent-skills) |

## Wat doet het?

Twee skills: **supabase** (werken met het Supabase-platform: database, auth, storage, edge functions) en **supabase-postgres-best-practices** (goede schema's, indexen, row level security en query's).

## Wanneer gebruik je het?

* Je app gebruikt Supabase als backend.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Ontwerp een schema voor meldingen met row level security per gebruiker.
```
{% endcode %}

**Wat je krijgt:** SQL-migraties met RLS-policies.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
```bash
claude plugin marketplace add supabase/agent-skills
claude plugin install supabase@supabase-agent-skills
claude plugin install postgres-best-practices@supabase-agent-skills
```
{% endtab %}

{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add supabase/agent-skills
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Staat ook in de officiële marketplace als `supabase`.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/supabase/agent-skills" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Data, cloud & betalen</a>
