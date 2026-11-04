---
description: >-
  AI/ML-taken: datasets, modellen trainen en evalueren, Spaces, Gradio en de Hugging Face Hub.
icon: face-smile
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

# Hugging Face

| | |
| --- | --- |
| **Maker** | Hugging Face (officieel van de makers) |
| **Werkt in** | Claude Code (+ andere agents) |
| **Kosten** | Gratis |
| **Bron** | [github.com/huggingface/skills](https://github.com/huggingface/skills) |

## Wat doet het?

Skills voor machine learning op de Hugging Face Hub: de `hf`-CLI, datasets, Spaces en Gradio, modellen trainen (TRL, LoRA, vision, sentence-transformers), evaluaties, papers publiceren en lokaal modellen draaien.

## Wanneer gebruik je het?

* Je wilt een eigen model finetunen of een demo-Space maken.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Maak een Gradio-Space die Nederlandse tekst samenvat.
```
{% endcode %}

**Wat je krijgt:** Een werkende Space-repo.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add huggingface/skills
/plugin install hf-cli@huggingface/skills
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/huggingface/skills" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Data, cloud & betalen</a>
