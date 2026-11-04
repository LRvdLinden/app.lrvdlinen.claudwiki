---
description: >-
  Laat Claude Code zelf nieuwe skills schrijven van wat hij tijdens het werk ontdekt.
icon: infinity
cover: ../../.gitbook/assets/cover-kennis.png
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

# Claudeception

| | |
| --- | --- |
| **Maker** | blader (community) |
| **Werkt in** | Claude Code |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/blader/Claudeception](https://github.com/blader/Claudeception) |

## Wat doet het?

Elke sessie begint een AI-agent vanaf nul. Heeft Claude een uur een obscure fout opgelost, dan ben je die kennis de volgende keer kwijt. Claudeception lost dat op: als Claude iets niet-voor-de-hand-liggends ontdekt (een workaround, debugtruc of projectpatroon), slaat hij het op als nieuwe skill. Bij een vergelijkbaar probleem wordt die skill automatisch geladen.

## Wanneer gebruik je het?

* Je loopt vaak tegen dezelfde soort problemen aan.
* Je wilt dat je setup slimmer wordt naarmate je meer werkt.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
/claudeception
```
{% endcode %}

**Wat je krijgt:** Claude bekijkt de sessie en maakt er waar zinvol een nieuwe skill van.

{% code title="Voorbeeld 2: wat je typt" overflow="wrap" %}
```
Sla dit op als skill.
```
{% endcode %}

**Wat je krijgt:** Een nieuwe SKILL.md in je skills-map.

## Installeren

{% tabs %}
{% tab title="Handmatig" %}
Kopieer de skillmap naar je persoonlijke skills-map (voor alle projecten) of naar `.claude/skills/` in één project:

```bash
git clone https://github.com/blader/Claudeception.git ~/.claude/skills/claudeception
```

Optioneel: kopieer de activator-hook naar `~/.claude/hooks/` (zie de README).
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/blader/Claudeception" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Kennis & geheugen</a>
