---
description: >-
  Officiële skills voor Terraform (stijlgids, tests, stacks, modules) en Packer-images.
icon: cubes-stacked
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

# HashiCorp Terraform & Packer

| | |
| --- | --- |
| **Maker** | HashiCorp (officieel van de makers) |
| **Werkt in** | Claude Code (+ andere agents) |
| **Kosten** | Gratis |
| **Bron** | [github.com/hashicorp/agent-skills](https://github.com/hashicorp/agent-skills) |

## Wat doet het?

De makers van Terraform leveren skills voor de Terraform-stijlgids, testen, stacks, policies, importeren van bestaande resources, modules refactoren en zelfs eigen providers bouwen. Voor Packer zijn er skills om AWS-, Azure- en Windows-images te bouwen.

## Wanneer gebruik je het?

* Je beheert infrastructuur met Terraform of bouwt machine-images met Packer.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Importeer deze bestaande S3-buckets in Terraform.
```
{% endcode %}

**Wat je krijgt:** Import-blokken en de bijbehorende configuratie.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
```bash
claude plugin marketplace add hashicorp/agent-skills
claude plugin install terraform@hashicorp
claude plugin install packer@hashicorp
```
{% endtab %}

{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add hashicorp/agent-skills
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Zie ook de community-variant [Terraform Skill](../ontwikkeling/terraform-skill.md).
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/hashicorp/agent-skills" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Data, cloud & betalen</a>
