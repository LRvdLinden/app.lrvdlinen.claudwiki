---
description: >-
  AWS-ontwikkeling: CDK, serverless/event-driven architectuur, kostenoptimalisatie en Bedrock AgentCore.
icon: aws
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

# AWS Skills

| | |
| --- | --- |
| **Maker** | zxkane (community) |
| **Werkt in** | Claude Code |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/zxkane/aws-skills](https://github.com/zxkane/aws-skills) |

## Wat doet het?

Plugins voor AWS met MCP-koppelingen: CDK-best practices, serverless en event-driven patronen, kostenbeheer, SST en het uitrollen van AI-agents met Bedrock AgentCore. Met de AWS Documentation MCP gebruikt Claude actuele AWS-documentatie.

## Wanneer gebruik je het?

* Je bouwt of beheert infrastructuur op AWS.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Analyseer mijn AWS-kosten en geef de drie grootste besparingen.
```
{% endcode %}

**Wat je krijgt:** Een kostenrapport met acties.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
```bash
/plugin marketplace add zxkane/aws-skills
/plugin install aws-common@aws-skills
/plugin install aws-iac@aws-skills
/plugin install aws-cost-ops@aws-skills
```

Andere plugins: `serverless-eda`, `aws-agentic-ai`.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* In de officiële marketplace staan ook AWS-plugins van Amazon zelf, zoals `aws-core` en `aws-serverless`. Zie de [catalogus](../../catalogus/README.md).
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/zxkane/aws-skills" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Data, cloud & betalen</a>
