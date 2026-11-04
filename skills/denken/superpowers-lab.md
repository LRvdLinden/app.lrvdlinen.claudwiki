---
description: >-
  Experimentele Superpowers-skills: dubbele functies opsporen, interactieve terminals met tmux en meer.
icon: flask
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

# Superpowers Lab

| | |
| --- | --- |
| **Maker** | obra (community) |
| **Werkt in** | Claude Code |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/obra/superpowers-lab](https://github.com/obra/superpowers-lab) |

## Wat doet het?

Nieuwe technieken die nog worden verfijnd: `finding-duplicate-functions` (zoekt functies die hetzelfde doen maar anders geschreven zijn, typisch voor AI-code), `using-tmux-for-interactive-commands`, `mcp-cli` en `windows-vm`.

## Wanneer gebruik je het?

* Je gebruikt Superpowers al en wilt nieuwe technieken proberen.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Zoek dubbele functies in deze codebase.
```
{% endcode %}

**Wat je krijgt:** Een lijst met functies die je kunt samenvoegen.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Installeer de plugin rechtstreeks vanaf GitHub:

```bash
claude plugin install https://github.com/obra/superpowers-lab
```

Voor sommige skills heb je `tmux` nodig.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/obra/superpowers-lab" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Denken & plannen</a>
