---
description: >-
  Laat AI's met elkaar in debat gaan zodat je eerlijk, tegengesproken advies krijgt in plaats van een ja-knikker.
icon: comments
cover: ../../.gitbook/assets/cover-denken.png
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

# Debate Skills

{% hint style="danger" %}
**Gespot op social.** Bart Boonstra noemt een 'Debate Skill' zijn favoriet: *'AI praat negen van de tien keer met je mee. Niet meer.'* Welke repo hij precies gebruikt, noemt hij niet in de post; deze is een goed gedocumenteerde variant.
{% endhint %}

| | |
| --- | --- |
| **Maker** | biyachuev (community) |
| **Werkt in** | Claude Code (+ Codex CLI voor de debatten tussen twee modellen) |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/biyachuev/claude-debate-skills](https://github.com/biyachuev/claude-debate-skills) |

## Wat doet het?

Deze collectie bevat drie skills. **strategy-debate**: Claude en Codex (OpenAI) bouwen los van elkaar een standpunt op, bekritiseren elkaar en komen tot een synthese. **creator-critic**: de ene genereert opties, de andere beoordeelt ze; deze werkt ook met alleen Claude. **options-challenge**: vergelijkt meerdere routes, test de afwegingen en rangschikt ze (vereist Codex). Omdat de modellen verschillende blinde vlekken hebben, komt er meer boven tafel dan bij één antwoord.

## Wanneer gebruik je het?

* Je staat voor een strategische keuze en wilt geen ja-knikker.
* Je wilt ideeën (namen, prijzen, positionering) onder druk testen.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
/strategy-debate Topic: Moet ik mijn app gratis met advertenties of betaald aanbieden? Constraints: kleine doelgroep, solo-ontwikkelaar.
```
{% endcode %}

**Wat je krijgt:** Twee onderbouwde standpunten, onderlinge kritiek en een eindadvies.

{% code title="Voorbeeld 2: wat je typt" overflow="wrap" %}
```
/creator-critic Creator: Claude. Critic: Claude. Finalizer: Claude. Log File: none. Brief: Bedenk namen voor een buurt-app.
```
{% endcode %}

**Wat je krijgt:** Opties, kritiek en een korte shortlist, alleen met Claude.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
```bash
claude plugin install --source https://github.com/biyachuev/claude-debate-skills.git
```

Voor de debatten tussen twee modellen heb je ook de Codex CLI nodig:

```bash
npm install -g @openai/codex && codex login
```

Installeer daarna in Claude Code de Codex-plugin met `/install-plugin codex`.
{% endtab %}

{% tab title="Handmatig" %}
Kopieer de skillmap naar je persoonlijke skills-map (voor alle projecten) of naar `.claude/skills/` in één project:

```bash
git clone https://github.com/biyachuev/claude-debate-skills.git
cd claude-debate-skills && ./install.sh   # maakt symlinks in ~/.claude/skills/
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Je vraag kan naar zowel Anthropic als OpenAI gaan: zet er geen gevoelige informatie in.
* Alleen Claude? Gebruik `creator-critic` met Claude in alle rollen.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/biyachuev/claude-debate-skills" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Denken & plannen</a>
