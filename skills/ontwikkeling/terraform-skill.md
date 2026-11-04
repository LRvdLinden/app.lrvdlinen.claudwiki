---
description: >-
  Best practices voor Terraform en OpenTofu: modules, testen, CI/CD en productieklare infrastructuur.
icon: cloud
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

# Terraform Skill

| | |
| --- | --- |
| **Maker** | Anton Babenko (community) |
| **Werkt in** | Claude Code (+ andere agents) |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/antonbabenko/terraform-skill](https://github.com/antonbabenko/terraform-skill) |

## Wat doet het?

Gemaakt door een bekende Terraform-expert. De skill helpt Claude bij het structureren van modules, het testen van infrastructuurcode, het opzetten van CI/CD en het schrijven van veilige productiecode, voor AWS, Azure en GCP.

## Wanneer gebruik je het?

* Je beheert infrastructuur als code.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Zet een Terraform-module op voor een statische website op AWS met tests.
```
{% endcode %}

**Wat je krijgt:** Een nette module met testopzet.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add antonbabenko/agent-plugins
/plugin install terraform-skill@antonbabenko
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/antonbabenko/terraform-skill" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Ontwikkelen & code</a>
