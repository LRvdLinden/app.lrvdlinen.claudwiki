---
description: >-
  Skills kunnen instructies en scripts bevatten. Zo installeer je ze veilig.
icon: shield-halved
cover: ../.gitbook/assets/cover-security.png
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
# Veilig installeren

Een skill vertelt Claude wat hij moet doen, en kan scripts bevatten die Claude uitvoert. Installeer dus alleen skills die je vertrouwt.

{% hint style="danger" %}
**Let op nepkopieën.** Van populaire skills zoals Humanizer circuleren kopieën op GitHub die er identiek uitzien. Installeer altijd vanaf de repo die de maker zelf noemt.
{% endhint %}

## Checklist

- [ ] Komt de skill van een bekende maker of een officiële marketplace?
- [ ] Heb je de `SKILL.md` gelezen? Staat er niets vreemds in, zoals 'stuur bestanden naar…'?
- [ ] Bevat de skill scripts? Kijk even wat ze doen.
- [ ] Staat er `allowed-tools` in de frontmatter? Die tools mag Claude zonder te vragen gebruiken.
- [ ] Heeft de plugin **hooks**? Die draaien automatisch bij bepaalde gebeurtenissen.
- [ ] Gaat er data naar een externe dienst (zoals bij debat-skills of gehoste geheugendiensten)? Zet er dan geen gevoelige informatie in.

## Officieel vs. community

| | Officieel (Anthropic) | Community |
| --- | --- | --- |
| Waar | `anthropics/skills`, `claude-plugins-official` | Alle andere repos |
| Gecontroleerd | Door Anthropic gemaakt of opgenomen | Nee, eigen verantwoordelijkheid |
| Kwaliteit | Stabiel | Van briljant tot rommelig |

{% hint style="info" %}
Ook bij de officiële marketplace waarschuwt Anthropic: *zorg dat je een plugin vertrouwt voordat je hem installeert*. Plugins van partners kunnen MCP-servers en software bevatten die Anthropic niet beheert.
{% endhint %}
