"""Builds the English wiki (markdown) in en/ plus the English adviser data.
Usage: python3 tools/build_en.py
"""
import os, sys, re, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from data import S, CATS
from en_data import E
import i18n

ROOT = os.path.dirname(HERE)
OUTR = os.path.join(ROOT, "en")
A = ".gitbook/assets"

def w(path, body):
    full = os.path.join(OUTR, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(body)

def rel(depth): return "../" * depth

def fm(icon, desc, cover=None, depth=0, hero=False):
    # depth counts from en/, assets live one level higher
    lines = ["---", f"description: >-\n  {desc}", f"icon: {icon}"]
    if cover:
        lines += [f"cover: {rel(depth + 1)}{A}/cover-en-{cover}.png", "coverY: 0", "layout:", "  cover:", "    visible: true",
                  f"    size: {'hero' if hero else 'full'}", "  title:", "    visible: true", "  description:", "    visible: true",
                  "  tableOfContents:", "    visible: true", "  outline:", "    visible: true", "  pagination:", "    visible: true"]
    lines.append("---\n")
    return "\n".join(lines)

def cards(rows, depth):
    out = ['<table data-view="cards"><thead><tr><th></th><th></th>'
           '<th data-hidden data-card-target data-type="content-ref"></th>'
           '<th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody>']
    for t, txt, link, cov in rows:
        c = f'<a href="{rel(depth + 1)}{A}/cover-en-{cov}.png">cover-en-{cov}.png</a>' if cov else ""
        out.append(f'<tr><td><strong>{t}</strong></td><td>{txt}</td><td><a href="{link}">{link}</a></td><td>{c}</td></tr>')
    out.append("</tbody></table>")
    return "\n".join(out)

CN = {c[0]: i18n.CATS_EN[c[0]] for c in CATS}
CATS_EN = [(c[0], CN[c[0]][0], c[2], CN[c[0]][1]) for c in CATS]

def tr(s):
    x = E[s["slug"]]
    return dict(slug=s["slug"], cat=s["cat"], icon=s["icon"], name=x.get("name", s["name"]), tagline=x["t"], wat=x["w"],
                wanneer=x["wa"], voorbeelden=x["v"], tips=x.get("tips", []), social=x.get("soc"),
                maker=i18n.maker(s["maker"]), werkt=i18n.werkt(s["werkt"]), prijs=i18n.prijs(s["prijs"]),
                bron=s["bron"], install=i18n.install(s["install"]), official="Anthropic" in s["maker"])
SE = [tr(s) for s in S]

# ───────── skill pages ─────────
for s in SE:
    b = [fm(s["icon"], s["tagline"], s["cat"], 2), f"# {s['name']}\n"]
    if s["social"]:
        b.append(f'{{% hint style="danger" %}}\n**Spotted on social.** {s["social"]}\n{{% endhint %}}\n')
    b.append(f"""| | |
| --- | --- |
| **Maker** | {s['maker']} |
| **Works in** | {s['werkt']} |
| **Cost** | {s['prijs']} |
| **Source** | [{s['bron'].replace('https://', '')}]({s['bron']}) |
""")
    b.append(f"## What does it do?\n\n{s['wat']}\n")
    b.append("## When do you use it?\n\n" + "\n".join(f"* {x}" for x in s["wanneer"]) + "\n")
    b.append("## Examples\n")
    for i, (p, r) in enumerate(s["voorbeelden"], 1):
        b.append(f'{{% code title="Example {i}: what you type" overflow="wrap" %}}\n```\n{p}\n```\n{{% endcode %}}\n\n**What you get:** {r}\n')
    b.append(f"## Install\n\n{s['install']}\n")
    if s["tips"]:
        b.append('{% hint style="success" %}\n**Tips**\n\n' + "\n".join(f"* {t}" for t in s["tips"]) + "\n{% endhint %}\n")
    if not s["official"]:
        b.append('{% hint style="warning" %}\nCommunity skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).\n{% endhint %}\n')
    b.append(f'<a href="{s["bron"]}" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to {CN[s["cat"]][0]}</a>\n')
    w(f"skills/{s['cat']}/{s['slug']}.md", "\n".join(b))

for slug, title, icon, intro in CATS_EN:
    items = [s for s in SE if s["cat"] == slug]
    body = fm(icon, intro, slug, 2) + f"# {title}\n\n{intro}\n\n"
    body += cards([(s["name"], s["tagline"], f"{s['slug']}.md", None) for s in items], 2) + "\n\n"
    body += "## Quick overview\n\n| Skill | Works in | Maker |\n| --- | --- | --- |\n"
    body += "\n".join(f"| [{s['name']}]({s['slug']}.md) | {s['werkt']} | {s['maker']} |" for s in items) + "\n"
    w(f"skills/{slug}/README.md", body)

w("skills/README.md", fm("grid-2", f"All {len(SE)} Claude skills in this wiki, organised in {len(CATS_EN)} categories, each with examples and installation steps.", "home", 1) + f"""# All skills

Here you'll find {len(SE)} skills and skill packs across {len(CATS_EN)} categories. Every page explains **what** the skill does, **when** you use it, gives **examples** and shows **how to install** it.

{cards([(t, i, f"{s}/README.md", s) for s, t, ic, i in CATS_EN], 1)}

{{% hint style="info" %}}
**Official or community?** Anthropic's skills live in [anthropics/skills](https://github.com/anthropics/skills) and the official marketplace. Everything else comes from the community: often great, but always read what you install.
{{% endhint %}}
""")

# ───────── home ─────────
w("README.md", fm("house", "The guide to Claude skills: explanations, examples and installation for every skill.", "home", 0, hero=True) + f"""# Welcome to the Claude Wiki

**Skills make Claude better at exactly the work you do.** This wiki has {len(SE)} skills explained in {len(CATS_EN)} categories, plus a catalogue of every plugin in the official marketplace. In plain language we explain what skills are, how to install them and which skills are worth it: from Anthropic's official skills to the favourites influencers share on Instagram and TikTok.

<a href="adviseur/README.md" class="button primary" data-icon="wand-magic-sparkles">Find your skill</a> <a href="basis/wat-zijn-skills.md" class="button secondary" data-icon="rocket">Start here</a> <a href="skills/README.md" class="button secondary" data-icon="grid-2">See all skills</a>

## Where do you want to start?

{cards([
    ("Skill adviser", "Describe what you want to do and instantly get the best skill with its install command.", "adviseur/README.md", "adviseur"),
    ("What are skills?", "Understand in 5 minutes how skills work and why they're so useful.", "basis/wat-zijn-skills.md", "basis"),
    ("Install", "Step by step: in the Claude app, in Claude Code and via npx.", "basis/skills-installeren.md", "basis"),
    ("Spotted on social", "The skills Bart Boonstra and other creators recommend.", "gespot-op-social/README.md", "social"),
    ("Plugin catalogue", "Every plugin from the official Claude Code marketplace at a glance.", "catalogus/README.md", "catalogus"),
    ("Build your own skill", "From idea to a working SKILL.md in fifteen minutes.", "basis/eigen-skill-maken.md", "bouwen"),
], 0)}

## Categories

{cards([(t, i, f"skills/{s}/README.md", s) for s, t, ic, i in CATS_EN], 0)}

## Top 5 to start with

| # | Skill | Why |
| --- | --- | --- |
| 1 | [Skill Creator](skills/bouwen/skill-creator.md) | Turn your own way of working into a skill. |
| 2 | [Superpowers](skills/denken/superpowers.md) | Claude thinks and plans first, then builds. |
| 3 | [UI UX Pro Max](skills/design/ui-ux-pro-max.md) | Everything Claude designs looks professional straight away. |
| 4 | [Humanizer](skills/content/humanizer.md) | Texts that no longer sound like AI. |
| 5 | [Remotion](skills/creatief/remotion.md) | Make videos and animations with code. |

{{% hint style="info" %}}
**Unofficial wiki.** This wiki is made by LRvdLinden and is not affiliated with Anthropic. Claude is a product of Anthropic. Information updated in November 2026; skills change quickly, so check the source when in doubt.
{{% endhint %}}
""")

# ───────── basics ─────────
w("basis/README.md", fm("graduation-cap", "Everything you need to know before installing your first skill.", "basis", 1) + """# The basics

New to skills? Read these pages in order.

{% stepper %}
{% step %}
### [What are skills?](wat-zijn-skills.md)
The idea behind skills, and how they differ from plugins, MCP, projects and CLAUDE.md.
{% endstep %}
{% step %}
### [Install skills](skills-installeren.md)
In the Claude app, in Claude Code, via `npx skills` or manually.
{% endstep %}
{% step %}
### [Use skills](skills-gebruiken.md)
Let them trigger automatically or call them yourself with a slash command.
{% endstep %}
{% step %}
### [Create your own skill](eigen-skill-maken.md)
Write, test and share a SKILL.md.
{% endstep %}
{% step %}
### [Install safely](veiligheid.md)
What to watch out for with other people's skills.
{% endstep %}
{% endstepper %}
""")

w("basis/wat-zijn-skills.md", fm("lightbulb", "Skills are folders with instructions, scripts and files that Claude loads when they're needed.", "basis", 1) + """# What are skills?

A **skill** is a folder with instructions (and sometimes scripts and example files) that teaches Claude how to do a particular task well and consistently. Think of a work instruction you give a new colleague: *this is how we make a newsletter*, *this is our house style*, *this is how you test this app*.

The clever part: Claude only loads a skill **when it needs it**. Of every skill, Claude first sees only the name and a short description. Only when your question matches does it read the full instructions. That's why you can install dozens of skills without Claude getting slower or more confused.

## What does a skill look like?

```
my-skill/
├── SKILL.md          ← required: description + instructions
├── examples/         ← optional: example files
└── scripts/          ← optional: scripts Claude may run
```

{% code title="SKILL.md" %}
```markdown
---
name: neighbourhood-newsletter
description: Writes the monthly newsletter of the neighbourhood council in our fixed structure. Use for every request for a newsletter, neighbourhood update or announcement to residents.
---

# Neighbourhood newsletter

1. Start with a short personal opening (max. 3 sentences).
2. Then the fixed sections: News, Agenda, Call to action, Contact.
3. Write in plain language and address the reader as 'you'.
```
{% endcode %}

The **description** is the most important part: Claude uses it to decide whether the skill fits your question.

## Skills vs. the rest

| What | What is it? | Example |
| --- | --- | --- |
| **Skill** | A folder with instructions that Claude loads when relevant. | 'This is how we make an invoice.' |
| **Plugin** | A package that bundles skills, slash commands, agents, hooks and connections. | Superpowers, Anthropic's role plugins. |
| **MCP / connector** | A connection to an external service, so Claude can do things there. | Google Calendar, Notion, GitHub. |
| **Project** | A workspace in the Claude app with its own documents and instructions. | 'Council 2027' with all minutes. |
| **CLAUDE.md** | An instruction file for one code project in Claude Code. | 'Always use Swift 6 and test with XCTest.' |

{% hint style="info" %}
**One standard for everything.** Skills follow the open [Agent Skills standard](https://agentskills.io). A skill you write once works in the Claude app, in Claude Code and via the API, and often in other AI agents such as Codex and Cursor too.
{% endhint %}

## Where do skills work?

* **Claude app** (web, desktop, mobile): on Pro, Max, Team and Enterprise, with *Code execution and file creation* turned on.
* **Claude Code**: in your personal folder `~/.claude/skills/`, in a project in `.claude/skills/`, or via plugins.
* **Claude API**: ready-made and custom skills via the [Skills API](https://docs.claude.com/en/api/skills-guide).

<a href="skills-installeren.md" class="button primary" data-icon="arrow-right">Next: install skills</a>
""")

w("basis/skills-installeren.md", fm("download", "Step-by-step: install a skill in the Claude app, in Claude Code, via npx or manually.", "basis", 1) + """# Install skills

There are four ways. Which one you choose depends on where you use Claude.

{% tabs %}
{% tab title="Claude app" %}
**Turn on built-in skills**

1. Go to **Settings → Capabilities**.
2. Turn on **Code execution and file creation**.
3. Scroll to **Skills** and switch on the skills you want.

**Upload your own or a community skill**

{% stepper %}
{% step %}
### Download the skill
Download the folder containing the `SKILL.md`, for example via GitHub → **Code → Download ZIP**.
{% endstep %}
{% step %}
### Zip it
Zip **only the skill folder**. The folder name must match the skill name.
{% endstep %}
{% step %}
### Upload
Go to **Settings → Capabilities → Skills** and click **Upload skill**.
{% endstep %}
{% step %}
### Switch it on
Switch the skill on in the list. Done!
{% endstep %}
{% endstepper %}

{% hint style="info" %}
On Pro and Max, custom skills are private. On Team and Enterprise, owners can provision skills for the whole organisation.
{% endhint %}
{% endtab %}

{% tab title="Claude Code (plugins)" %}
Most skills are distributed as a **plugin** through a **marketplace** (a GitHub repo with a list of plugins).

```bash
# 1. Add the marketplace (once)
/plugin marketplace add anthropics/skills

# 2. Install the plugin
/plugin install document-skills@anthropic-agent-skills

# View, enable/disable and update
/plugin
```

Anthropic's **official marketplace** (`claude-plugins-official`) is connected by default:

```bash
/plugin install superpowers@claude-plugins-official
```

You can also run the same commands outside a session in your terminal, for example `claude plugin install …`.
{% endtab %}

{% tab title="npx skills" %}
The open-source [skills CLI](https://github.com/vercel-labs/skills) installs skills for Claude Code and dozens of other agents. Find skills on [skills.sh](https://skills.sh).

```bash
npx skills add remotion-dev/skills                 # everything in a repo
npx skills add anthropics/skills --skill pdf       # one skill
npx skills add blader/humanizer -g                 # globally, for all your projects
npx skills list                                    # what do I have?
npx skills check                                   # updates?
```
{% endtab %}

{% tab title="Manual" %}
A skill is just a folder. Put it in the right place:

| Place | Folder | Works in |
| --- | --- | --- |
| Personal | `~/.claude/skills/<name>/SKILL.md` | All your projects on this computer |
| Project | `.claude/skills/<name>/SKILL.md` | Only this project (commit it for your team) |

```bash
git clone https://github.com/blader/Claudeception.git ~/.claude/skills/claudeception
```

Restart Claude Code afterwards.
{% endtab %}
{% endtabs %}

## Does it work?

* Type `/` in Claude Code and check whether the skill is in the list.
* Or simply ask: *"Which skills do you have available?"*

<a href="skills-gebruiken.md" class="button primary" data-icon="arrow-right">Next: use skills</a>
""")

w("basis/skills-gebruiken.md", fm("hand-pointer", "Let skills trigger automatically or call them yourself with a slash command.", "basis", 1) + """# Use skills

## Automatically

Usually you don't have to do anything. Ask for what you want in plain language. If your question matches a skill's description, Claude loads it itself.

```
Turn these meeting minutes into a Word document with a table of contents.
```

→ Claude uses the [Word skill](../skills/documenten/docx.md).

## Call it yourself (Claude Code)

Type `/` followed by the skill's name, optionally with extra text:

```
/grill-me I want to build an app for volunteers
/humanizer:humanizer
```

Skills from a plugin have a prefix: `/plugin-name:skill-name`.

## Mention a skill

Doesn't a skill trigger by itself? Then mention it by name:

```
Use the PDF skill to extract the form fields from application.pdf.
```

## Handy settings for skill authors

| Setting in SKILL.md | What it does |
| --- | --- |
| `disable-model-invocation: true` | Only you can start it, not Claude on its own (handy for e.g. deploying). |
| `user-invocable: false` | Only Claude uses it; it's not in your `/` menu. |
| `allowed-tools` | Tools Claude may use without asking during that skill. |
| `arguments` | Named arguments, like `/migrate $component $from $to`. |

{% hint style="success" %}
**Tip:** does a skill trigger too often or too rarely? Improve the description. The [Skill Creator](../skills/bouwen/skill-creator.md) can test that for you.
{% endhint %}
""")

w("basis/eigen-skill-maken.md", fm("wand-magic-sparkles", "From idea to working skill: write, test and share a SKILL.md.", "bouwen", 1) + """# Create your own skill

Do you notice you keep giving Claude the same explanation? Turn it into a skill.

{% stepper %}
{% step %}
### Let Claude do it for you
The easiest route: say *"Turn the way I do this into a skill"* at the end of a conversation that went well. With the [Skill Creator](../skills/bouwen/skill-creator.md) you get a complete folder right away.
{% endstep %}

{% step %}
### Or create the folder yourself

```bash
mkdir -p ~/.claude/skills/neighbourhood-newsletter
```
{% endstep %}

{% step %}
### Write the SKILL.md

{% code title="~/.claude/skills/neighbourhood-newsletter/SKILL.md" %}
```markdown
---
name: neighbourhood-newsletter
description: Writes the monthly newsletter of the neighbourhood council in the fixed structure. Use for every request for a newsletter, neighbourhood update or announcement to residents.
---

# Neighbourhood newsletter

## Structure
1. Opening: max. 3 sentences, personal.
2. Sections: News · Agenda · Call to action · Contact.

## Style
- Plain language, short sentences, address the reader as 'you'.
- No jargon where a simple word will do.

## Example
See `examples/october.md`.
```
{% endcode %}
{% endstep %}

{% step %}
### Test it
Start a new session and ask something that fits: *"Write the newsletter for December."* Doesn't Claude use your skill? Make the `description` more specific.
{% endstep %}

{% step %}
### Share it
* **Claude app:** zip the folder and upload it via **Settings → Capabilities → Skills**.
* **Team:** put it in `.claude/skills/` in your repo, or turn it into a plugin with your own marketplace.
* **Public:** put it on GitHub; others install it with `npx skills add your-name/your-repo`.
{% endstep %}
{% endstepper %}

## Rules for a good skill

| Do | Don't |
| --- | --- |
| A description with **what** and **when** | A vague description like 'helps with text' |
| Short, concrete steps | A 20-page novel in one file |
| Examples of a good result | Only rules without an example |
| Large reference material in separate files you mention in SKILL.md | Cramming everything into SKILL.md |
| `name` in lowercase with hyphens | Spaces or capitals in the name |
""")

w("basis/veiligheid.md", fm("shield-halved", "Skills can contain instructions and scripts. This is how to install them safely.", "security", 1) + """# Install safely

A skill tells Claude what to do, and can contain scripts that Claude runs. So only install skills you trust.

{% hint style="danger" %}
**Watch out for fake copies.** Of popular skills like Humanizer, copies that look identical are circulating on GitHub. Always install from the repo the author names themselves.
{% endhint %}

## Checklist

- [ ] Does the skill come from a known author or an official marketplace?
- [ ] Have you read the `SKILL.md`? Is there nothing odd in it, like 'send files to…'?
- [ ] Does the skill contain scripts? Have a quick look at what they do.
- [ ] Is there `allowed-tools` in the frontmatter? Claude may use those tools without asking.
- [ ] Does the plugin have **hooks**? They run automatically on certain events.
- [ ] Does data go to an external service (as with debate skills or hosted memory services)? Then don't put sensitive information in it.

## Official vs. community

| | Official (Anthropic) | Community |
| --- | --- | --- |
| Where | `anthropics/skills`, `claude-plugins-official` | All other repos |
| Reviewed | Made or included by Anthropic | No, your own responsibility |
| Quality | Stable | From brilliant to messy |

{% hint style="info" %}
Even for the official marketplace, Anthropic warns: *make sure you trust a plugin before installing it*. Partner plugins can contain MCP servers and software that Anthropic does not control.
{% endhint %}
""")

# ───────── social ─────────
w("gespot-op-social/README.md", fm("fire", "The Claude skills influencers recommend on Instagram and TikTok, with explanations and installation.", "social", 1) + """# Spotted on social

More and more creators share their favourite Claude skills on Instagram and TikTok. We looked them up, checked the source and worked out how to install them.

{% hint style="info" %}
**How we searched.** Instagram can only be searched with an account. Many creators post the same videos on TikTok and YouTube too, and blogs write about them. That's where we found the skills mentioned, which we then checked in the official repos.
{% endhint %}

## Bart Boonstra: "4 Claude skills you should install today"

[Bart Boonstra](https://www.instagram.com/bartboonstra_/) (Slim Werken) is one of the best-known Dutch AI creators. In a much-viewed video (in Dutch) he names these four skills:

| # | Skill | What Bart says about it | Our page |
| --- | --- | --- | --- |
| 1 | **Superpowers** | "Makes Claude really think in steps. Brainstorming and planning get 10x sharper." | [Superpowers](../skills/denken/superpowers.md) |
| 2 | **UI UX Pro Max** | "Makes every layout 1000x more professional." | [UI UX Pro Max](../skills/design/ui-ux-pro-max.md) |
| 3 | **Remotion** | "Teaches Claude to make animations in code. Free. Unlimited." | [Remotion](../skills/creatief/remotion.md) |
| 4 | **Debate Skill** | "My favourite. With this skill you finally get honest advice." | [Debate Skills](../skills/denken/debate.md) |

For the complete step-by-step plan Bart refers to his community at [community.slimwerken.ai](https://community.slimwerken.ai). He also shows how he edits and generates videos locally with Claude Code and Remotion.

{% embed url="https://www.tiktok.com/@bart_boonstra/video/7639384272230550817" %}
Bart Boonstra: 4 Claude skills you should install today
{% endembed %}

## Other viral skills

| Skill | Where it went viral | What it does |
| --- | --- | --- |
| [Humanizer](../skills/content/humanizer.md) | Everywhere, "the most viral skill" | Makes AI text sound human |
| [Grill Me & Handoff](../skills/denken/grill-me.md) | Developer Twitter, blogs | Have your plan questioned and hand chats over |
| [Agent Skills (Addy Osmani)](../skills/ontwikkeling/agent-skills-addy.md) | Developer community | Spec → tasks → build step by step |
| [Instagram Agent](../skills/content/instagram-agent.md) | Instagram creators | 13 skills that run your Instagram |
| [Instagram Carousel](../skills/content/instagram-carousel.md) | Instagram creators | Carousels in your brand style |
| [Marketing Skills](../skills/content/marketingskills.md) | Marketers | Copy, social, content strategy |
| [Planning with Files](../skills/denken/planning-with-files.md) | Trending on GitHub | Plans that never get lost |
| [Frontend Slides](../skills/design/frontend-slides.md) | YouTube tutorials | Animated HTML presentations |
| [Claude-Mem](../skills/kennis/claude-mem.md) | Claude Code users | Memory between sessions |

{% hint style="warning" %}
**Influencer ≠ guarantee.** What works well in a video doesn't always work for you. Try a skill first and read [Install safely](../basis/veiligheid.md).
{% endhint %}

## Sources

* [Bart Boonstra on Instagram](https://www.instagram.com/bartboonstra_/) · [TikTok](https://www.tiktok.com/@bart_boonstra) · [YouTube](https://www.youtube.com/@BartBoonstra_slimwerken)
* [I Tried 23 Viral Claude Skills. These Are the Best](https://artificialcorner.com/p/viral-claude-skills) (Artificial Corner)
* [Best Claude Skills for Creators](https://creatorflow.so/guides/best-claude-skills-for-creators) (CreatorFlow)
* [The Instagram agent skill: 13 free Claude skills](https://mehdiagentai.substack.com/p/the-instagram-agent-skill-13-free)
""")

# ───────── resources ─────────
w("bronnen/README.md", fm("compass", "Where to find new skills: marketplaces, directories and lists.", "bronnen", 1) + """# Resources & marketplaces

## Official

| Source | What |
| --- | --- |
| [anthropics/skills](https://github.com/anthropics/skills) | Anthropic's official skills, plus template and specification |
| [claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | The official Claude Code marketplace (connected by default) |
| [knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Plugins per job function |
| [claude.com/plugins](https://claude.com/plugins) | Browse and install plugins |
| [agentskills.io](https://agentskills.io) | The open Agent Skills standard |

## Documentation

* [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills) (Claude Help Center)
* [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
* [Creating custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
* [Skills in Claude Code](https://code.claude.com/docs/en/skills)
* [Skills API quickstart](https://docs.claude.com/en/api/skills-guide)
* [Equipping agents for the real world with Agent Skills](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) (Anthropic Engineering)

## Directories and lists

| Source | What |
| --- | --- |
| [skills.sh](https://skills.sh) | Large directory; install with `npx skills add` |
| [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | Curated list |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Curated list |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | Everything around Claude Code: skills, hooks, commands |
| [claudemarketplaces.com](https://claudemarketplaces.com) | Overview of marketplaces |

## Glossary

| Word | Meaning |
| --- | --- |
| **Skill** | Folder with instructions (`SKILL.md`) that Claude loads when relevant |
| **Plugin** | Package of skills, commands, agents, hooks and connectors |
| **Marketplace** | A repo with a list of plugins you can install |
| **MCP** | Model Context Protocol: a standard for connecting Claude to external tools |
| **Hook** | Script that runs automatically on an event (e.g. before a commit) |
| **Frontmatter** | The block between `---` at the top of SKILL.md with name and description |
| **Claude Code** | Claude as an agent in your terminal, IDE, desktop or browser |
""")

w("bronnen/faq.md", fm("circle-question", "Frequently asked questions about Claude skills: what they cost, installing them, the Claude app versus Claude Code and sharing with your team.", "bronnen", 1) + """# Frequently asked questions

<details>
<summary>Do skills cost money?</summary>

The skills themselves are almost always free. In the Claude app you do need a Pro, Max, Team or Enterprise plan. Some skills use external services (like Remotion for large companies or hosted memory services) with their own terms.
</details>

<details>
<summary>Does a skill from Claude Code also work in the Claude app?</summary>

Often it does: it's the same standard. Zip the skill folder and upload it. Skills that depend on **hooks**, local programs or the terminal only work in Claude Code.
</details>

<details>
<summary>How many skills can I install?</summary>

Plenty. Claude first only sees the name and description and loads the rest only when needed. Too many skills with overlapping descriptions can cause confusion though: clean up what you don't use.
</details>

<details>
<summary>My skill isn't being used. What now?</summary>

1. Check that it is enabled (`/plugin` in Claude Code, Settings → Capabilities in the app).
2. Restart Claude Code.
3. Make the `description` more concrete: what it does **and** when it should be used.
4. Call it explicitly with `/name`.
</details>

<details>
<summary>What's the difference between /plugin and npx skills?</summary>

`/plugin` is built into Claude Code and installs complete plugins (skills, commands, hooks) with automatic updates. `npx skills` is a separate open-source CLI that only installs skills, but for dozens of different agents.
</details>

<details>
<summary>Can I share skills with my team?</summary>

In Claude Code: put them in `.claude/skills/` in your repo or create your own marketplace. In the Claude app, owners of Team and Enterprise organisations can provision skills for everyone.
</details>
""")

w("bronnen/over.md", fm("circle-info", "About the Claude Wiki: who makes it, why it is unofficial and how you can add a skill or improvement yourself.", "home", 1) + """# About this wiki

The **Claude Wiki** is an unofficial guide to Claude skills in Dutch and English, made by **LRvdLinden**. This wiki is not affiliated with Anthropic. Claude is a product of Anthropic.

## Contribute

Missing a skill or is something out of date? The wiki is on GitHub: [LRvdLinden/app.lrvdlinen.claudwiki](https://github.com/LRvdLinden/app.lrvdlinen.claudwiki). Open an issue or pull request.

### Adding a new skill

Add an `add(...)` block in `tools/data.py` (Dutch) and the matching entry in `tools/en_data.py` (English), then run the build scripts. Keep this structure:

1. What does it do?
2. When do you use it?
3. Examples (what you type and what you get)
4. Install (tabs per platform)
5. Tips

*Last updated: November 2026.*
""")

# ───────── catalogue ─────────
M = json.load(open(os.path.join(HERE, "marketplace-official.json")))["plugins"]
ICON = {"development": "code", "productivity": "list-check", "database": "database", "monitoring": "chart-line", "security": "shield-halved",
        "deployment": "rocket", "design": "palette", "automation": "gears", "learning": "graduation-cap", "location": "map-location-dot",
        "testing": "vial", "math": "square-root-variable", "migration": "right-left", None: "shapes"}
def md(s): return re.sub(r"\s+", " ", (s or "").replace("|", "/")).strip()
groups = {}
for p in M: groups.setdefault(p.get("category"), []).append(p)
order = sorted(groups, key=lambda c: -len(groups[c]))
cs = lambda c: c or "overig"
for c in order:
    nl = i18n.CATNL_EN[c]; rows = sorted(groups[c], key=lambda p: p["name"])
    body = fm(ICON.get(c, "shapes"), f"{len(rows)} plugins from the official Claude Code marketplace in the {nl} category.", "catalogus", 1)
    body += f"# {nl}\n\n{len(rows)} plugins. Install in Claude Code: `/plugin install <name>@claude-plugins-official`.\n\n"
    body += "| Plugin | Maker | What it does | Install |\n| --- | --- | --- | --- |\n"
    for p in rows:
        a = (p.get("author") or {}).get("name", "") if isinstance(p.get("author"), dict) else ""
        hp = p.get("homepage"); nm = f"[**{p['name']}**]({hp})" if hp else f"**{p['name']}**"
        body += f"| {nm} | {a} | {md(p.get('description'))} | `/plugin install {p['name']}@claude-plugins-official` |\n"
    w(f"catalogus/{cs(c)}.md", body)
w("catalogus/README.md", fm("store", f"All {len(M)} plugins from the official Claude Code marketplace, by category.", "catalogus", 1) + f"""# Plugin catalogue

Anthropic's official marketplace (`claude-plugins-official`) currently has **{len(M)} plugins**: from Anthropic itself and from companies like Google, AWS, Microsoft, Stripe, Figma, Notion, Canva, Shopify and Supabase. This marketplace is connected by default in Claude Code.

{{% hint style="info" %}}
**Install:** type `/plugin install <name>@claude-plugins-official` in Claude Code, or browse via `/plugin` → **Discover**. Third-party plugins sometimes contain MCP servers or software that Anthropic doesn't control: only install what you trust.
{{% endhint %}}

{cards([(i18n.CATNL_EN[c], f"{len(groups[c])} plugins", f"{cs(c)}.md", None) for c in order], 1)}

{{% hint style="success" %}}
Not sure which one you need? Use the [Skill adviser](../adviseur/README.md): describe what you want and get the best options.
{{% endhint %}}

*Generated from [marketplace.json](https://github.com/anthropics/claude-plugins-official/blob/main/.claude-plugin/marketplace.json), November 2026. Descriptions are written by the makers.*
""")

# ───────── adviser data + page ─────────
ADV = []
for s in SE:
    inst = re.findall(r"```bash\n(.*?)\n```", s["install"], re.S)
    ADV.append({"n": s["name"], "t": s["tagline"], "c": CN[s["cat"]][0], "w": s["werkt"], "m": s["maker"],
                "p": f"skills/{s['cat']}/{s['slug']}", "i": inst[0].strip() if inst else "",
                "k": " ".join([s["wat"][:600], " ".join(s["wanneer"]), " ".join(v[0] for v in s["voorbeelden"])]),
                "o": 1 if s["official"] or "official" in s["maker"] else 0, "src": "wiki"})
for p in M:
    a = (p.get("author") or {}).get("name", "") if isinstance(p.get("author"), dict) else ""
    ADV.append({"n": p["name"], "t": md(p.get("description"))[:260], "c": "Marketplace · " + i18n.CATNL_EN[p.get("category")],
                "w": "Claude Code", "m": a, "p": f"catalogus/{cs(p.get('category'))}", "h": p.get("homepage", ""),
                "i": f"/plugin install {p['name']}@claude-plugins-official", "k": "", "o": 1 if a == "Anthropic" else 0, "src": "mp"})
json.dump(ADV, open(os.path.join(HERE, "adv_en.json"), "w"), ensure_ascii=False)

ADV_URL = "https://lrvdlinden.github.io/app.lrvdlinen.claudwiki/en/adviseur/"
w("adviseur/README.md", fm("wand-magic-sparkles", "Describe what you want to do and instantly get the best-fitting skill, with its install command.", "adviseur", 1) + f"""# Skill adviser

Not sure which skill you need? Describe in plain language what you want to do, and the adviser searches **{len(ADV)} skills and plugins** for the best options, with an explanation and install command.

<a href="{ADV_URL}" class="button primary" data-icon="magnifying-glass">Open the Skill adviser</a>

{{% tabs %}}
{{% tab title="In your browser" %}}
Open the [Skill adviser]({ADV_URL}) and type what you want, for example *"I want to make videos for Instagram"* or *"I'm building an iPhone app in SwiftUI"*.
{{% endtab %}}
{{% tab title="As a skill in Claude" %}}
Install the **skill-adviseur** skill. Then ask in any conversation: *"Which skill do I need to …?"* and Claude advises from the same catalogue (it answers in your language).

**Claude app:** download [skill-adviseur.zip](../../.gitbook/assets/skill-adviseur.zip) and upload it via **Settings → Capabilities → Skills → Upload skill**.
{{% endtab %}}
{{% endtabs %}}
""")

# ───────── SUMMARY ─────────
summ = ["# Table of contents\n", "* [Welcome](README.md)", "* [Skill adviser](adviseur/README.md)\n", "## Getting started\n",
        "* [The basics](basis/README.md)", "  * [What are skills?](basis/wat-zijn-skills.md)", "  * [Install skills](basis/skills-installeren.md)",
        "  * [Use skills](basis/skills-gebruiken.md)", "  * [Create your own skill](basis/eigen-skill-maken.md)", "  * [Install safely](basis/veiligheid.md)",
        "* [Spotted on social](gespot-op-social/README.md)\n", "## Skills by category\n", "* [All skills](skills/README.md)"]
for slug, title, icon, intro in CATS_EN:
    summ.append(f"* [{title}](skills/{slug}/README.md)")
    for s in [x for x in SE if x["cat"] == slug]:
        summ.append(f"  * [{s['name']}](skills/{slug}/{s['slug']}.md)")
summ += [f"\n## Plugin catalogue ({len(M)})\n", "* [Overview](catalogus/README.md)"]
for c in order: summ.append(f"  * [{i18n.CATNL_EN[c]} ({len(groups[c])})](catalogus/{cs(c)}.md)")
summ += ["\n## More\n", "* [Resources & marketplaces](bronnen/README.md)", "* [FAQ](bronnen/faq.md)", "* [About this wiki](bronnen/over.md)"]
w("SUMMARY.md", "\n".join(summ) + "\n")
w(".gitbook.yaml", "root: ./\n\nstructure:\n  readme: README.md\n  summary: SUMMARY.md\n")
print("EN pages:", len(SE), "adviser:", len(ADV))
