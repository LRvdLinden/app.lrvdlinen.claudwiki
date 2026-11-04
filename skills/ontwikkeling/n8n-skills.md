---
description: >-
  Expertkennis om foutloze n8n-workflows te bouwen via de n8n-MCP-server.
icon: diagram-next
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

# n8n Skills

| | |
| --- | --- |
| **Maker** | czlonkowski (community) |
| **Werkt in** | Claude Code (met de n8n-mcp-server) |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) |

## Wat doet het?

Veertien samenwerkende skills, een router-skill en hooks die Claude leren hoe n8n echt werkt: expressies, nodes configureren, Code-nodes in JavaScript of Python, validatie en workflow-patronen. Bedoeld om samen te werken met de [n8n-mcp](https://github.com/czlonkowski/n8n-mcp)-server, zodat Claude workflows direct in je n8n kan bouwen.

## Wanneer gebruik je het?

* Je automatiseert met n8n en wilt dat Claude workflows bouwt of repareert.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Bouw een n8n-workflow die elke ochtend het weerbericht ophaalt en naar Telegram stuurt.
```
{% endcode %}

**Wat je krijgt:** Een gevalideerde workflow in je n8n.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
```bash
/plugin install czlonkowski/n8n-skills
```

Of voeg de marketplace toe met `/plugin marketplace add czlonkowski/n8n-skills` en kies daarna via `/plugin`.
{% endtab %}

{% tab title="Handmatig" %}
Kopieer de skillmap naar je persoonlijke skills-map (voor alle projecten) of naar `.claude/skills/` in één project:

```bash
git clone https://github.com/czlonkowski/n8n-skills.git
cp -r n8n-skills/skills/* ~/.claude/skills/
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Installeer eerst de n8n-mcp-server; zonder die server kan Claude niet bij je n8n.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/czlonkowski/n8n-skills" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Ontwikkelen & code</a>
