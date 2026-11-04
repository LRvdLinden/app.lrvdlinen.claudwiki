---
description: >-
  Where to find new skills: marketplaces, directories and lists.
icon: compass
cover: ../../.gitbook/assets/cover-en-bronnen.png
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
# Resources & marketplaces

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
