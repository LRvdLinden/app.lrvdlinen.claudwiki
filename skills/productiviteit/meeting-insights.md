---
description: >-
  Analyseert vergadertranscripten op communicatiepatronen en geeft persoonlijke feedback.
icon: people-group
cover: ../../.gitbook/assets/cover-productiviteit.png
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

# Meeting Insights Analyzer

| | |
| --- | --- |
| **Maker** | ComposioHQ (community) |
| **Werkt in** | Claude Code, Claude-app |
| **Kosten** | Gratis |
| **Bron** | [github.com/ComposioHQ/awesome-claude-skills/tree/master/meeting-insights-analyzer](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/meeting-insights-analyzer) |

## Wat doet het?

Leest transcripten van vergaderingen en laat zien waar je conflict vermijdt, veel stopwoorden gebruikt, het gesprek domineert of kansen mist om te luisteren. Handig om je gespreksleiding te verbeteren.

## Wanneer gebruik je het?

* Je zit veel vergaderingen voor en wilt beter leiden.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Analyseer de transcripten van de laatste drie vergaderingen en geef me feedback als voorzitter.
```
{% endcode %}

**Wat je krijgt:** Patronen en concrete tips.

## Installeren

{% tabs %}
{% tab title="Handmatig" %}
Kopieer de skillmap naar je persoonlijke skills-map (voor alle projecten) of naar `.claude/skills/` in één project:

```bash
git clone https://github.com/ComposioHQ/awesome-claude-skills.git
cp -r awesome-claude-skills/meeting-insights-analyzer ~/.claude/skills/
```
{% endtab %}

{% tab title="Claude-app" %}
1. Download de repo als ZIP: [github.com/ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) → **Code → Download ZIP**.
2. Pak uit en zoek de map `meeting-insights-analyzer` (daarin staat `SKILL.md`).
3. Maak van **alleen die map** een nieuwe ZIP. De mapnaam moet gelijk zijn aan de skillnaam.
4. Ga naar **Instellingen → Mogelijkheden → Skills** en klik op **Skill uploaden**.
5. Zet de skill aan.

Skills in de Claude-app vragen een Pro-, Max-, Team- of Enterprise-abonnement en **Code-uitvoering en bestanden maken** moet aanstaan.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/ComposioHQ/awesome-claude-skills/tree/master/meeting-insights-analyzer" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Productiviteit & tools</a>
