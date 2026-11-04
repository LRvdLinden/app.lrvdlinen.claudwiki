---
description: >-
  Ordent facturen en bonnetjes voor de belastingaangifte: gegevens eruit halen, hernoemen en sorteren.
icon: file-invoice-dollar
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

# Invoice Organizer

| | |
| --- | --- |
| **Maker** | ComposioHQ (community) |
| **Werkt in** | Claude Code, Claude-app |
| **Kosten** | Gratis |
| **Bron** | [github.com/ComposioHQ/awesome-claude-skills/tree/master/invoice-organizer](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/invoice-organizer) |

## Wat doet het?

Leest rommelige facturen en bonnetjes, haalt datum, leverancier en bedrag eruit, geeft ze een consistente naam en sorteert ze in logische mappen.

## Wanneer gebruik je het?

* Je moet je administratie op orde brengen voor de btw of inkomstenbelasting.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Orden alle facturen in deze map per kwartaal en leverancier.
```
{% endcode %}

**Wat je krijgt:** Netjes hernoemde en gesorteerde bestanden.

## Installeren

{% tabs %}
{% tab title="Handmatig" %}
Kopieer de skillmap naar je persoonlijke skills-map (voor alle projecten) of naar `.claude/skills/` in één project:

```bash
git clone https://github.com/ComposioHQ/awesome-claude-skills.git
cp -r awesome-claude-skills/invoice-organizer ~/.claude/skills/
```
{% endtab %}

{% tab title="Claude-app" %}
1. Download de repo als ZIP: [github.com/ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) → **Code → Download ZIP**.
2. Pak uit en zoek de map `invoice-organizer` (daarin staat `SKILL.md`).
3. Maak van **alleen die map** een nieuwe ZIP. De mapnaam moet gelijk zijn aan de skillnaam.
4. Ga naar **Instellingen → Mogelijkheden → Skills** en klik op **Skill uploaden**.
5. Zet de skill aan.

Skills in de Claude-app vragen een Pro-, Max-, Team- of Enterprise-abonnement en **Code-uitvoering en bestanden maken** moet aanstaan.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/ComposioHQ/awesome-claude-skills/tree/master/invoice-organizer" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Productiviteit & tools</a>
