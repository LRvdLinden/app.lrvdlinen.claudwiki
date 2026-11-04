---
description: >-
  Bouwen op Cloudflare: Workers, Durable Objects, Agents SDK, Wrangler, Turnstile en meer.
icon: cloudflare
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

# Cloudflare

| | |
| --- | --- |
| **Maker** | Cloudflare (officieel van de makers) |
| **Werkt in** | Claude Code (+ andere agents) |
| **Kosten** | Gratis |
| **Bron** | [github.com/cloudflare/skills](https://github.com/cloudflare/skills) |

## Wat doet het?

Een collectie skills voor het Cloudflare Developer Platform: Workers-best practices, Durable Objects, de Agents SDK, Wrangler, Next.js op Cloudflare, web-performance, Turnstile en de e-maildienst. De plugin installeert ook de Cloudflare MCP-server.

## Wanneer gebruik je het?

* Je host je website of API op Cloudflare.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Zet deze API om naar een Cloudflare Worker met caching.
```
{% endcode %}

**Wat je krijgt:** Een Worker plus wrangler-configuratie.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add cloudflare/skills
/plugin install cloudflare@cloudflare
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.
{% endtab %}

{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add https://github.com/cloudflare/skills
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/cloudflare/skills" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Data, cloud & betalen</a>
