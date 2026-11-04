# Rule-based translations for install texts, makers, platforms and prices (NL → EN)
import re

CATS_EN = {
    "documenten": ("Documents & office", "Skills that let Claude create and edit real office files: Word, PDF, PowerPoint and Excel, plus help with internal communication and writing together."),
    "design": ("Design & frontend", "Out of the box, what Claude builds often looks a bit generic. These skills give Claude taste: styles, colour palettes, typography, themes and presentations that look professional."),
    "creatief": ("Creative & video", "Animations and videos in code, generative art, posters and GIFs. Ideal for content creators."),
    "denken": ("Thinking & planning", "Skills that make Claude think better before it starts: brainstorming, planning, questioning you critically, pushing back and handing work over neatly."),
    "ontwikkeling": ("Development & code", "For anyone building with Claude Code: engineering workflows, code reviews, testing, MCP servers, Vercel/React, Terraform and n8n."),
    "content": ("Writing, content & marketing", "Texts that don't sound like AI, Instagram content, carousels, trend research, SEO and marketing."),
    "kennis": ("Knowledge & memory", "Let Claude remember things between sessions, work with your Obsidian vault and let Claude learn new skills by itself."),
    "zakelijk": ("Business by role", "Complete skill packs (plugins) per function: sales, finance, legal, marketing, data, HR, operations, customer support and small business."),
    "security": ("Security & science", "Professional security analysis of code and a huge library of scientific skills."),
    "bouwen": ("Build your own skills", "The skills you use to create, test and improve your own skills."),
    "mobiel": ("Apps & mobile", "Skills for iOS, SwiftUI and React Native/Expo developers: from SwiftUI best practices to driving the iOS Simulator."),
    "cloud": ("Data, cloud & payments", "Official skills from Supabase, Neon, Cloudflare, AWS, Azure, HashiCorp, Hugging Face, Stripe and Sentry."),
    "productiviteit": ("Productivity & tools", "Handy everyday skills: organising files and invoices, Google Workspace, NotebookLM, learning from articles and videos, and connecting a thousand apps."),
    "media": ("Audio, images & visuals", "Speech and music with ElevenLabs, generating and enhancing images, diagrams and data visualisations."),
}

CATNL_EN = {"development": "Development", "productivity": "Productivity", "database": "Databases",
            "monitoring": "Monitoring & observability", "security": "Security", "deployment": "Deployment & hosting",
            "design": "Design", "automation": "Automation", "learning": "Learning & explanatory style",
            "location": "Location & maps", "testing": "Testing", "math": "Mathematics", "migration": "Migration", None: "Other"}

def maker(s):
    s = s.replace("(officieel van de makers)", "(official, by the makers)").replace("(officieel)", "(official)")
    s = s.replace("(community, Nederlands)", "(community, Dutch)").replace("(maker van Obsidian)", "(creator of Obsidian)")
    return s

def werkt(s):
    rep = [("Alle agents die de standaard ondersteunen", "All agents that support the standard"),
           ("Alleen Claude Code (lokaal), niet de web-app", "Only Claude Code (local), not the web app"),
           ("Losse tool (Python), output werkt in Claude", "Standalone tool (Python), output works in Claude"),
           ("Claude Code op macOS met Xcode", "Claude Code on macOS with Xcode"),
           ("(+ Codex CLI voor de debatten tussen twee modellen)", "(+ Codex CLI for the two-model debates)"),
           ("(API-sleutel nodig)", "(API key required)"), ("(de SKILL.md werkt ook in andere agents)", "(the SKILL.md also works in other agents)"),
           ("(en Claude-app met code-uitvoering)", "(and Claude app with code execution)"), ("(met de n8n-mcp-server)", "(with the n8n-mcp server)"),
           ("andere agents", "other agents"), (" en meer", " and more"), (" en ", " and "), ("Claude-app (desktop)", "Claude app (desktop)"),
           ("Claude-app", "Claude app")]
    for a, b in rep: s = s.replace(a, b)
    return s

def prijs(s):
    rep = {"Gratis": "Free", "Gratis (Apache 2.0)": "Free (Apache 2.0)", "Gratis (MIT)": "Free (MIT)",
           "Gratis (MIT), geen API-sleutel nodig": "Free (MIT), no API key needed", "Gratis (open source)": "Free (open source)",
           "Gratis bij betaald abonnement (source-available)": "Free with a paid plan (source-available)",
           "Gratis open source; de gehoste geheugendienst heeft 30 dagen gratis proef, daarna je eigen abonnement of API-sleutel": "Free and open source; the hosted memory service has a 30-day free trial, then your own plan or API key",
           "Gratis te starten; Composio-account nodig": "Free to start; Composio account required",
           "Plugin gratis; Firecrawl-diensten volgens hun prijzen": "Plugin free; Firecrawl services at their prices",
           "Skills gratis; ElevenLabs-API volgens hun prijzen": "Skills free; ElevenLabs API at their prices",
           "Skills gratis; Remotion zelf heeft een eigen licentie": "Skills free; Remotion itself has its own licence"}
    return rep.get(s, s)

LINES = {
 "Deze skill is **al ingebouwd** voor betaalde abonnementen.": "This skill is **already built in** for paid plans.",
 "1. Open **Instellingen → Mogelijkheden** (Settings → Capabilities).": "1. Open **Settings → Capabilities**.",
 "2. Zet **Code-uitvoering en bestanden maken** aan.": "2. Turn on **Code execution and file creation**.",
 "3. Scroll naar **Skills** en zet de skill aan.": "3. Scroll to **Skills** and switch the skill on.",
 "Daarna vraag je gewoon in gewone taal wat je wilt; Claude laadt de skill zelf.": "Then just ask for what you want in plain language; Claude loads the skill itself.",
 "In de Claude-app gebruikt Claude deze skill ook al automatisch zodra je om een bestand van dit type vraagt.": "In the Claude app, Claude already uses this skill automatically as soon as you ask for a file of this type.",
 "Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:": "First add the marketplace, then install the plugin. Type this in a Claude Code session:",
 "Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.": "Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.",
 "Dit installeert **document-skills**: Word, PDF, PowerPoint en Excel in één keer.": "This installs **document-skills**: Word, PDF, PowerPoint and Excel in one go.",
 "Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:": "With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:",
 "Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.": "Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.",
 "Dit installeert het hele pakket **example-skills** (o.a. deze skill).": "This installs the whole **example-skills** pack (including this skill).",
 "Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:": "This plugin is in the **official Anthropic marketplace**, which is connected by default:",
 "Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.": "Or browse via `/plugin` → **Discover** and pick the plugin from the list.",
 "De makers raden hun eigen installer aan:": "The makers recommend their own installer:",
 "Gebruik `ui-ux-pro-max-cli`; het oudere pakket `uipro-cli` is verouderd.": "Use `ui-ux-pro-max-cli`; the older `uipro-cli` package is outdated.",
 "3. Maak van **alleen die map** een nieuwe ZIP. De mapnaam moet gelijk zijn aan de skillnaam.": "3. Zip **only that folder** into a new ZIP. The folder name must match the skill name.",
 "4. Ga naar **Instellingen → Mogelijkheden → Skills** en klik op **Skill uploaden**.": "4. Go to **Settings → Capabilities → Skills** and click **Upload skill**.",
 "5. Zet de skill aan.": "5. Switch the skill on.",
 "Skills in de Claude-app vragen een Pro-, Max-, Team- of Enterprise-abonnement en **Code-uitvoering en bestanden maken** moet aanstaan.": "Skills in the Claude app require a Pro, Max, Team or Enterprise plan, and **Code execution and file creation** must be turned on.",
 "Open daarna `/plugin` en installeer **Impeccable**. Zeg 'ja' tegen de design-hook: die vangt de meeste fouten automatisch af.": "Then open `/plugin` and install **Impeccable**. Say 'yes' to the design hook: it catches most mistakes automatically.",
 "Kopieer de skillmap naar je persoonlijke skills-map (voor alle projecten) of naar `.claude/skills/` in één project:": "Copy the skill folder to your personal skills folder (for all projects) or to `.claude/skills/` in one project:",
 "Je hebt Node.js nodig en een Remotion-project (`npx create-video@latest`). Check de [Remotion-licentie](https://www.remotion.dev/license): voor bedrijven boven een bepaalde omvang is een betaalde licentie nodig.": "You need Node.js and a Remotion project (`npx create-video@latest`). Check the [Remotion licence](https://www.remotion.dev/license): companies above a certain size need a paid licence.",
 "De eigen marketplace van de maker, met extra gerelateerde plugins:": "The author's own marketplace, with extra related plugins:",
 "De collectie staat in de officiële marketplace:": "The collection is in the official marketplace:",
 "Kies in de installer welke skills je wilt en neem `setup-matt-pocock-skills` mee. Bijwerken: `npx skills@latest update`.": "Pick the skills you want in the installer and include `setup-matt-pocock-skills`. Update: `npx skills@latest update`.",
 "Voor de debatten tussen twee modellen heb je ook de Codex CLI nodig:": "For the two-model debates you also need the Codex CLI:",
 "Installeer daarna in Claude Code de Codex-plugin met `/install-plugin codex`.": "Then install the Codex plugin in Claude Code with `/install-plugin codex`.",
 "Vervang `code-review` door de plugin die je wilt, bijvoorbeeld `feature-dev`, `swift-lsp` of `security-guidance`.": "Replace `code-review` with the plugin you want, for example `feature-dev`, `swift-lsp` or `security-guidance`.",
 "Of voeg de marketplace toe met `/plugin marketplace add czlonkowski/n8n-skills` en kies daarna via `/plugin`.": "Or add the marketplace with `/plugin marketplace add czlonkowski/n8n-skills` and then choose via `/plugin`.",
 "De plugin luistert naar `/humanizer:humanizer` en vraagt Claude Code 2.1.142 of nieuwer.": "The plugin responds to `/humanizer:humanizer` and requires Claude Code 2.1.142 or newer.",
 "`/plugin` werkt alleen in een interactieve Claude Code-sessie.": "`/plugin` only works in an interactive Claude Code session.",
 "De repo heeft een aparte map `claude-ai` met instructies om de skill in de Claude-app te gebruiken (bestand plakken, ±5 minuten).": "The repo has a separate `claude-ai` folder with instructions for using the skill in the Claude app (paste a file, about 5 minutes).",
 "De installer zet alles klaar en vraagt je daarna in te loggen via een e-maillink (geen creditcard). Daarna kies je je geheugen-provider: de claude-mem observer (30 dagen gratis proef), een eigen OpenRouter- of Gemini-sleutel, of je Anthropic-abonnement.": "The installer sets everything up and then asks you to log in via an email link (no credit card). Then you choose your memory provider: the claude-mem observer (30-day free trial), your own OpenRouter or Gemini key, or your Anthropic plan.",
 "Optioneel: kopieer de activator-hook naar `~/.claude/hooks/` (zie de README).": "Optional: copy the activator hook to `~/.claude/hooks/` (see the README).",
 "Installeer de plugins in de Claude-desktopapp via [claude.com/plugins](https://claude.com/plugins/). Ze activeren zichzelf; skills gaan automatisch aan en de commando's verschijnen in je sessie.": "Install the plugins in the Claude desktop app via [claude.com/plugins](https://claude.com/plugins/). They activate themselves; skills switch on automatically and the commands appear in your session.",
 "Vervang `sales` door de plugin die je wilt.": "Replace `sales` with the plugin you want.",
 "Kies daarna via `/plugin` welke plugins je wilt installeren.": "Then choose via `/plugin` which plugins you want to install.",
 "Writing Skills zit in het Superpowers-pakket.": "Writing Skills is part of the Superpowers pack.",
 "Volg de stappen in [Je eigen skill maken](../../basis/eigen-skill-maken.md).": "Follow the steps in [Create your own skill](../../basis/eigen-skill-maken.md).",
 "Andere plugins: `serverless-eda`, `aws-agentic-ai`.": "Other plugins: `serverless-eda`, `aws-agentic-ai`.",
 "Volg daarna de setup in de README.": "Then follow the setup in the README.",
 "Alle 25 skills komen in één plugin. Bijwerken: `/plugin marketplace update ai-skills`.": "All 25 skills come in one plugin. Update: `/plugin marketplace update ai-skills`.",
 "Volg daarna de quickstart in de README.": "Then follow the quickstart in the README.",
 "Andere plugins: `customaize-agent`, `docs`, `fpf`, `kaizen`, `sadd` en meer.": "Other plugins: `customaize-agent`, `docs`, `fpf`, `kaizen`, `sadd` and more.",
 "Kopieer de hooks niet ook nog naar `settings.json`: de plugin laadt ze al.": "Don't also copy the hooks into `settings.json`: the plugin already loads them.",
 "Installeer de plugin rechtstreeks vanaf GitHub:": "Install the plugin straight from GitHub:",
 "Voor sommige skills heb je `tmux` nodig.": "Some skills need `tmux`.",
}
TABS = {"Claude-app": "Claude app", "Handmatig": "Manual", "CLI (aanbevolen)": "CLI (recommended)", "Voorwaarden": "Requirements",
        "Installer (aanbevolen)": "Installer (recommended)", "Starten": "Getting started", "Installeren": "Install"}
CODECOMM = {"# alle skills": "# all skills", "# eerst bekijken": "# browse first", "# alleen dit project": "# this project only",
            "# voor al je projecten (~/.claude/skills/)": "# for all your projects (~/.claude/skills/)",
            "# maakt symlinks in ~/.claude/skills/": "# creates symlinks in ~/.claude/skills/",
            "# map scannen": "# scan a folder", "# live pagina scannen": "# scan a live page",
            "# of ~/.claude/skills/ voor al je projecten": "# or ~/.claude/skills/ for all your projects",
            "/pad/naar/je/project": "/path/to/your/project"}

def install(t):
    t = re.sub(r"1\. Download de repo als ZIP: (.*?) → \*\*Code → Download ZIP\*\*\.", r"1. Download the repo as a ZIP: \1 → **Code → Download ZIP**.", t)
    t = re.sub(r"2\. Pak uit en zoek de map `(.*?)` \(daarin staat `SKILL\.md`\)\.", lambda m: f"2. Unzip and find the folder `{folder(m.group(1))}` (it contains `SKILL.md`).", t)
    for a, b in LINES.items(): t = t.replace(a, b)
    for a, b in TABS.items(): t = t.replace(f'title="{a}"', f'title="{b}"')
    for a, b in CODECOMM.items(): t = t.replace(a, b)
    return t

def folder(f):
    return {"humanizer (de hoofdmap van de repo, met SKILL.md)": "humanizer (the repo's root folder, with SKILL.md)",
            "(de hoofdmap, hernoem naar d3-viz)": "(the root folder, rename it to d3-viz)",
            "(de hoofdmap met SKILL.md)": "(the root folder with SKILL.md)",
            "(de skillmap met SKILL.md)": "(the skill folder with SKILL.md)"}.get(f, f)

def leftover_dutch(t):
    """Return lines that still look Dutch (for checking)."""
    nl = re.compile(r"\b(de|het|een|je|jouw|van|voor|met|naar|zoek|installeer|daarna|niet|wordt|maak|zet)\b", re.I)
    t = re.sub(r"```.*?```", "", t, flags=re.S)
    return [l for l in t.splitlines() if len(nl.findall(l)) >= 2]
