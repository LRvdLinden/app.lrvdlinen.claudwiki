---
description: >-
  Geef je agent een URL en hij bouwt de website na als een nette Next.js-app.
icon: clone
cover: ../../.gitbook/assets/cover-klonen.png
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

# AI Website Cloner

{% hint style="danger" %}
**Gespot op social.** Met ruim 13.000 sterren op GitHub de bekendste clone-skill: één commando en je agent bouwt een website na.
{% endhint %}

| | |
| --- | --- |
| **Maker** | JCodesMore (community) |
| **Werkt in** | Claude Code (+ Codex, Cursor, OpenCode) |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) |

## Wat doet het?

Een projecttemplate met de skill `/clone-website`. Claude werkt in vier stappen: **Map** (welke pagina's wordt welke route), **Observe** (desktop- en mobiele weergave bekijken, echte afbeeldingen, iconen en lettertypes ophalen, hover- en klikstaten uitproberen), **Build** (bewerkbare componenten en werkende interacties bouwen, eventueel verdeeld over subagents) en **Compare** (bron en kloon naast elkaar vergelijken en verschillen repareren). Het resultaat is een Next.js 16-app met React 19, TypeScript, shadcn/ui en Tailwind CSS v4, plus vergelijkingsscreenshots.

## Wanneer gebruik je het?

* Je wilt je eigen site van WordPress, Webflow of Squarespace overzetten naar moderne code.
* De broncode van je site is kwijt, maar de site staat nog online.
* Je wilt leren hoe een professionele site zijn layout en animaties maakt.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
/clone-website https://mijn-oude-site.nl
```
{% endcode %}

**Wat je krijgt:** Een Next.js-project dat er hetzelfde uitziet en werkt, klaar om verder te bewerken.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Maak een eigen kopie van het template en open die in Claude Code:

```bash
git clone https://github.com/JCodesMore/ai-website-cloner-template.git mijn-kloon
cd mijn-kloon && npm install
claude
```

Typ daarna in Claude Code:

```
/clone-website https://voorbeeld.nl
```

Op GitHub kan het ook met **Use this template** → **Create repository**.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Het werkt het best met Claude Code met browsertoegang (bijv. Claude in Chrome of een Playwright-MCP).
* Je hebt Node.js 24 of nieuwer nodig.
* Gebruik dit alleen voor je eigen sites en apps, of met toestemming. Logo's, merkuitingen en teksten blijven van de eigenaar, en nabouwen om je als een ander voor te doen (phishing) is verboden. Check ook de gebruiksvoorwaarden van de site.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/JCodesMore/ai-website-cloner-template" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Sites & apps klonen</a>
