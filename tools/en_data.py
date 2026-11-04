# English translations of the skill data (keyed by slug)
E = {}
def e(slug, **k): E[slug] = k

# ───────── DOCUMENTS ─────────
e("docx", t="Creates, reads and edits Word documents with formatting, a table of contents and tracked changes.",
  w="The Word skill powers the Word files Claude makes for you. It knows how a `.docx` works inside: headings, styles, tables, headers and footers, page numbers, tables of contents, images and even **tracked changes** and comments. It can also read and edit existing Word files, or use a template (`.dotx`) as a starting point.",
  wa=["You really need a `.docx`, for example for a municipality, school or client.", "You want an existing Word file reviewed with visible changes.", "You want to fill a letter template in your house style."],
  v=[("Turn these meeting minutes into a clean Word document with a table of contents, page numbers and our logo in the header.", "A formatted `.docx` file to download."),
     ("Read contract.docx and suggest improvements as tracked changes.", "The original document with tracked changes you can accept or reject in Word.")],
  tips=["Say 'as a Word file' explicitly if you want a .docx; otherwise Claude may pick another format.", "Upload your own template (.dotx) so Claude uses your house style."])
e("pdf", t="Everything with PDFs: extract text and tables, merge, split, fill in forms, OCR and watermarks.",
  w="The PDF skill gives Claude a complete toolbox for PDF files. It extracts text and tables, merges or splits files, rotates pages, adds watermarks, fills in PDF forms, encrypts or decrypts files and makes scanned PDFs searchable with OCR. It can also create new PDFs.",
  wa=["You want data from a stack of invoices or reports in a table.", "You need to fill in a PDF form.", "You have a scan you want to search."],
  v=[("Extract the date, supplier and total amount from these 12 invoices (PDF) and put them in a table.", "An overview table, optionally as Excel."),
     ("Merge these three PDFs, rotate page 4 upright and put a 'DRAFT' watermark on every page.", "One new PDF.")],
  tips=["For scanned documents, ask for OCR explicitly.", "For large PDFs, ask for a table of contents first and then zoom in."])
e("pptx", t="Creates and edits PowerPoint presentations, including templates, speaker notes and layouts.",
  w="With the PowerPoint skill Claude builds complete presentations as `.pptx`: slides with titles, bullet points, images, charts and speaker notes. It can also read an existing presentation or template (`.potx`), extract its text, edit slides, or merge and split presentations.",
  wa=["You need to deliver a presentation as a PowerPoint file.", "You want an existing presentation updated in your house style.", "You want the content of a presentation summarised."],
  v=[("Create a 10-slide presentation about our neighbourhood plans for 2027, with speaker notes on every slide.", "A `.pptx` you can open in PowerPoint or Keynote."),
     ("Use template brand.potx and turn this report into slides.", "A presentation in your template.")],
  tips=["Want a quick web presentation instead of a file? Have a look at [Frontend Slides](../design/frontend-slides.md)."])
e("xlsx", t="Open and clean up spreadsheets, add formulas and charts, or build new sheets.",
  w="The Excel skill lets Claude create and edit real spreadsheets: `.xlsx`, `.xlsm`, `.csv` and `.tsv`. It adds columns and **working formulas**, creates charts, fixes formatting, cleans messy data (wrong header rows, empty rows) and converts between formats.",
  wa=["You need a budget, schedule or overview you will keep editing in Excel.", "You have a messy export that needs cleaning.", "You want charts for your numbers."],
  v=[("Create a budget for the street party with income, expenses, a total formula and a pie chart.", "An `.xlsx` with working formulas."),
     ("This CSV export is a mess. Clean it up, fix the dates and turn it into a tidy Excel file.", "A cleaned-up spreadsheet.")],
  tips=["Ask Claude to use formulas instead of fixed numbers, so your sheet stays usable when you change something."])
e("doc-coauthoring", t="A structured way to write documents, proposals and specs together with Claude.",
  w="Instead of producing a text in one go, this skill guides you through a fixed process: first Claude gathers the context from you, then it writes and refines in rounds, and finally it checks whether the document works for the reader. Useful for proposals, technical specifications, decision documents and policy papers.",
  wa=["You are writing a proposal, policy note or spec and want it to be really solid.", "You have lots of loose information that needs to become one clear piece."],
  v=[("Help me write a proposal to the municipality for more lighting in the park.", "Claude first asks targeted questions, then writes in steps and checks the result from the reader's point of view.")], tips=[])
e("internal-comms", t="Writes internal communication in fixed formats: status updates, newsletters, FAQs and incident reports.",
  w="This skill contains example formats for all kinds of internal communication: status reports, leadership updates, newsletters, FAQs, incident reports and project updates. The idea: you adapt the formats to how your organisation likes it, so every piece is consistent.",
  wa=["You regularly write updates or newsletters.", "You want incident reports to always have the same structure."],
  v=[("Write an incident report about last night's outage: cause, impact, fix and follow-up actions.", "A report in a fixed, businesslike structure.")],
  tips=["Make your own copy and replace the example formats with your organisation's."])

# ───────── DESIGN ─────────
e("frontend-design", t="Gives Claude a distinct design taste, so interfaces don't look like a standard template.",
  w="Frontend Design teaches Claude to choose a **clear aesthetic direction** for every interface first: typography, colour, composition and details. The goal is for a website or app to look deliberate instead of 'like every AI site'. It is also available as a plugin in the official Claude Code marketplace.",
  wa=["You let Claude build a website, landing page or app screen.", "You want to give an existing design its own character."],
  v=[("Build a landing page for my weather app. Pick a bold, distinctive style, no standard purple gradient.", "A page with a recognisable, deliberate style.")],
  tips=["Add a few words of atmosphere ('calm Scandinavian', 'retro newspaper', 'luxury night') for even better results."])
e("ui-ux-pro-max", t="A searchable design library with dozens of styles, 192 colour palettes, 74 font pairings and 119 UX guidelines.",
  soc="Tip from Bart Boonstra: *'UI UX Pro Max makes every layout 1000x more professional. Literally.'*",
  w="UI UX Pro Max is one of the most popular community skills. It gives Claude a local, searchable database of UI styles (glassmorphism, bento grid, brutalism, dark mode…), colour palettes per product type, font pairings with Google Fonts, UX guidelines and anti-patterns, icons, animation presets and chart types. Claude looks up the best-fitting style, colours and typography for your request and applies them consistently. The package also includes extra skills for banners, branding, design systems and slides.",
  wa=["You are building a website, dashboard or app and want it to look professional straight away.", "You want a design system (colours, fonts, spacing) proposed.", "You want an existing screen reviewed for UX and accessibility."],
  v=[("Create a dashboard for an alerting app. Find a fitting style and colour palette.", "A dashboard with a well-reasoned style, palette and font choice."),
     ("Review this settings screen for UX mistakes and accessibility.", "A list of concrete improvements.")],
  tips=["Combine with [Frontend Design](frontend-design.md) or [Impeccable](impeccable.md) for even more control."])
e("impeccable", t="A design vocabulary for your agent: commands like polish, bolder, critique and audit, plus a detector for 'AI slop'.",
  w="Impeccable gives Claude a shared language to steer designs. You say *polish*, *bolder*, *critique* or *audit* and Claude knows exactly what you mean. It includes a detector that spots typical AI design mistakes ('slop'), and a hook that automatically checks every UI file Claude edits before it says it is done. The CLI also works on its own, for example in your CI.",
  wa=["You want to improve a design in small, targeted steps.", "You want to be warned automatically about generic-looking UI."],
  v=[("critique the homepage and then polish the hero section", "First a critical review, then a refined hero."),
     ("npx impeccable detect src/", "A scan of your code for typical AI design patterns.")],
  tips=["Documentation: [impeccable.style/docs](https://impeccable.style/docs)."])
e("theme-factory", t="Ten ready-made themes (colour + font) to style slides, documents and web pages in one go.",
  w="Theme Factory is a toolkit with ten preset themes with matching colours and fonts. You apply them to anything Claude makes: presentations, documents, reports or HTML pages. If no theme fits, Claude invents a new one on the spot.",
  wa=["You quickly want a consistent look across several pieces.", "You don't know which colours go together."],
  v=[("Show me the themes and then apply the calmest one to this presentation.", "An overview of themes and a styled presentation.")], tips=[])
e("brand-guidelines", t="Example of a brand skill: applies fixed brand colours and typography to everything Claude makes.",
  w="This skill applies Anthropic's house style (colours and fonts). It is mainly interesting as an **example**: copy it, replace the colours and fonts with your brand's, and Claude will make everything in your house style from then on.",
  wa=["You want Claude to use your brand colours and fonts by default.", "You want to learn how a brand skill is built."],
  v=[("Use my brand skill to make a flyer for the neighbourhood evening.", "A flyer in your colours and fonts.")],
  tips=["See [Create your own skill](../../basis/eigen-skill-maken.md) to turn it into your own house style."])
e("canvas-design", t="Creates posters, art and static designs as PNG or PDF, based on its own design philosophy.",
  w="Canvas Design has Claude first formulate a design philosophy and then create an original visual design: a poster, artwork or other static piece, as `.png` or `.pdf`. The skill is aimed at creating original work instead of copying existing work.",
  wa=["You need a poster, invitation or art print."],
  v=[("Design an A3 poster for the King's Day activities in our neighbourhood, as a PDF.", "A print-ready poster.")], tips=[])
e("web-artifacts-builder", t="Builds large, complex web artifacts with React, Tailwind CSS and shadcn/ui.",
  w="You don't need this skill for simple pages. But want a bigger artifact with several parts, state management or routing? Then this skill sets up a modern stack (React, Tailwind CSS, shadcn/ui) and bundles everything into one artifact.",
  wa=["You want an extensive tool or mini app as an artifact.", "You need several screens or components."],
  v=[("Build a volunteer planning tool with a week view, filters and a form.", "An interactive mini app as an artifact.")], tips=[])
e("frontend-slides", t="Beautiful, animated HTML presentations, or convert PowerPoints to the web.",
  w="Frontend Slides creates presentations as a single HTML file with animations, instead of a PowerPoint. You don't need to be a designer: the skill lets you choose between styles visually instead of asking abstract questions. It can also convert an existing `.pptx` into a web presentation and export to PDF.",
  wa=["You are giving a talk or pitch and want something that stands out.", "You want to modernise an old PowerPoint."],
  v=[("Create an 8-slide pitch for my new app, with slick animations.", "One HTML file you present in the browser.")],
  tips=["There is a beginner video in the repo's README."])

# ───────── CREATIVE ─────────
e("remotion", t="Teaches Claude to make videos and animations in code (React), locally and without limits.",
  soc="Tip from Bart Boonstra: *'Remotion is the skill that teaches Claude to make animations in code. All the animations in my videos are built with it.'*",
  w="Remotion is a framework for making videos with React code. The official Remotion skills teach Claude the best practices: setting up a project, animations and transitions, captions, maps, multimedia, interactivity and rendering to MP4. You describe what you want to see, Claude writes the code and you render the video locally on your own computer.",
  wa=["You make content for social media and want animations or infographics.", "You want to generate videos with captions or data visualisations.", "You want a fixed video template you reuse again and again."],
  v=[("Make a 15-second vertical Remotion video (1080x1920) in which the five main features of my app fly in one by one.", "A Remotion project you render to an MP4."),
     ("Add animated captions to this video.", "A video with captions in your own style.")],
  tips=["Start with the `remotion-best-practices` skill; it points Claude to the right sub-skill."])
e("algorithmic-art", t="Generative art with p5.js: flow fields, particle systems and interactive parameters.",
  w="With this skill Claude makes art with code in p5.js, with a fixed 'seed' so you can reproduce a nice result. You get sliders to explore parameters live. Meant for original work, not for imitating existing artists.",
  wa=["You want a unique background, wallpaper or visual.", "You want to play with generative art."],
  v=[("Create a flow field in the colours of the Dutch flag with sliders for density and speed.", "An interactive art page.")], tips=[])
e("slack-gif-creator", t="Creates animated GIFs that meet Slack's requirements exactly.",
  w="A skill with knowledge and tools for making GIFs that work well in Slack: the right dimensions and file size, plus validation and animation ideas.",
  wa=["You want a funny GIF or custom emoji for your team."],
  v=[("Make a GIF of a dancing toaster for Slack.", "An optimised GIF.")], tips=[])

# ───────── THINKING ─────────
e("superpowers", t="A complete working method: brainstorming, writing plans, test-first building, systematic debugging and verification.",
  soc="Tip from Bart Boonstra: *'Superpowers makes Claude really think in steps. Brainstorming and planning get 10x sharper.'*",
  w="Superpowers is one of the best-known skill packs. It is a complete development method, built from separate skills that complement each other: **brainstorming** (sharpening the idea together first), **writing-plans** and **executing-plans**, **test-driven-development**, **systematic-debugging**, **verification-before-completion** (prove it works first), requesting and receiving code reviews, working with git worktrees and subagents. A starter skill makes sure Claude actually uses them. Brainstorming also works outside software: for a talk, a business or a renovation.",
  wa=["You are starting a new feature or project.", "Claude jumps into code too quickly and misses the bigger picture.", "You are stuck on a bug and want a systematic approach."],
  v=[("I want to add a widget to my app. Let's brainstorm first.", "Claude asks questions first, proposes designs and writes a plan before writing any code."),
     ("The tests have been failing since the last update. Debug this systematically.", "Claude first finds and proves the cause before fixing anything.")],
  tips=["Use several tools (Claude Code and Codex)? Install Superpowers separately for each tool."])
e("grill-me", t="Have Claude grill your plan relentlessly before it starts, and summarise long chats so you can continue.",
  soc="Went viral through 'I Tried 23 Viral Claude Skills' (Artificial Corner), among others.",
  w="Two skills stand out in Matt Pocock's popular collection. **Grill Me** is a 'relentless interview': Claude keeps asking about your goals, audience, scope and what can go wrong, until your plan is really sharp. **Handoff** condenses a long conversation into a handoff document, so you can continue in a new chat or with another agent without losing context. The collection also contains skills for TDD, code reviews, specs, tickets and more.",
  wa=["You have an idea but don't know exactly what you want yet.", "Your conversation is getting too long and Claude starts forgetting things."],
  v=[("/grill-me I want to build an app for volunteers in my neighbourhood.", "A series of sharp questions, one at a time, until everything is clear."),
     ("/handoff", "A compact handoff document to paste into a new session.")], tips=[])
e("planning-with-files", t="Keeps a plan, findings and progress in files on disk, so Claude never loses track.",
  w="On long tasks an AI agent sometimes forgets where it was. Planning with Files solves that with three files: `task_plan.md`, `findings.md` and `progress.md`. Hooks add the important planning context on every turn, and the plan even survives a `/clear`. That lets Claude work through a big project step by step.",
  wa=["You let Claude do a large, multi-step project.", "You want to be able to look back at what was done and found."],
  v=[("Plan the migration of my app to a new iOS version with planning-with-files.", "A plan on disk that Claude works through and updates step by step.")],
  tips=["The hooks only work in Claude Code (and other agents with hooks), not in the Claude app."])
e("debate", t="Lets AIs debate each other so you get honest, challenged advice instead of a yes-man.",
  soc="Bart Boonstra calls a 'Debate Skill' his favourite: *'AI agrees with you nine times out of ten. Not anymore.'* He doesn't say which repo he uses exactly; this is a well-documented variant.",
  w="This collection contains three skills. **strategy-debate**: Claude and Codex (OpenAI) each build a position independently, critique each other and reach a synthesis. **creator-critic**: one generates options, the other assesses them; this one also works with Claude alone. **options-challenge**: compares several routes, tests the trade-offs and ranks them (requires Codex). Because the models have different blind spots, more comes to the surface than with a single answer.",
  wa=["You face a strategic choice and don't want a yes-man.", "You want to pressure-test ideas (names, prices, positioning)."],
  v=[("/strategy-debate Topic: Should I offer my app for free with ads or as a paid app? Constraints: small audience, solo developer.", "Two well-argued positions, mutual critique and final advice."),
     ("/creator-critic Creator: Claude. Critic: Claude. Finalizer: Claude. Log File: none. Brief: Come up with names for a neighbourhood app.", "Options, critique and a short shortlist, with Claude only.")],
  tips=["Your question may go to both Anthropic and OpenAI: don't put sensitive information in it.", "Claude only? Use `creator-critic` with Claude in all roles."])
e("discernment-nudge", t="Adds 2–3 smart check questions after important advice, so you verify the assumptions yourself.",
  w="After Claude has given you advice, a plan, an estimate or an analysis, this skill asks 2–3 short follow-up questions tied to that exact answer: which facts to check, which assumptions are underneath and what context may be missing. At most once per conversation, so it doesn't get annoying.",
  wa=["You use Claude for decisions and want to stay critical."],
  v=[("Make a budget for our street party.", "The budget, followed by questions like 'Is the number of visitors this is based on correct?'")], tips=[])

# ───────── DEVELOPMENT ─────────
e("agent-skills-addy", t="Production-grade engineering workflows: write a spec, break it into tasks, build step by step, test and ship.",
  soc="Went viral through 'I Tried 23 Viral Claude Skills' (Artificial Corner), among others.",
  w="Addy Osmani (Google Chrome) bundled the workflows and quality gates of senior engineers into about 25 skills. Think **spec-driven-development**, **planning-and-task-breakdown**, **incremental-implementation**, test-driven development, code review, security, performance, documentation and ADRs, CI/CD and launch. Claude records progress in files, so work stays consistent and verifiable.",
  wa=["You build serious software with Claude Code.", "You want Claude to write a spec before it builds."],
  v=[("First write a spec for the new search feature, split it into tasks and then build them one by one.", "A spec, a task list and incremental commits.")],
  tips=["Getting an SSH error on `/plugin install`? Use the HTTPS URL: `/plugin marketplace add https://github.com/addyosmani/agent-skills.git`."])
e("official-dev-plugins", name="Official dev plugins", t="Anthropic's own Claude Code plugins: code review, feature-dev, commits, PR review, security and hooks.",
  w="The official marketplace contains plugins that Anthropic maintains itself. A selection:\n\n| Plugin | What it does |\n| --- | --- |\n| `code-review` | Automated PR review with several specialised agents and a confidence score |\n| `feature-dev` | Complete feature workflow: explore the codebase, design the architecture, quality check |\n| `commit-commands` | Quick commands to commit, push and create PRs |\n| `pr-review-toolkit` | Review agents for comments, tests, error handling, types and simplification |\n| `security-guidance` | Warns about insecure code (injection, XSS, SSRF, hardcoded secrets and more) |\n| `hookify` | Easily create hooks to prevent unwanted behaviour |\n| `claude-md-management` | Keeps your CLAUDE.md files up to date and in good shape |\n| `claude-code-setup` | Analyses your codebase and suggests fitting hooks, skills and MCP servers |\n| `code-simplifier` | Makes code clearer without changing behaviour |\n| `playground` | Creates interactive HTML playgrounds with live preview |\n| `ralph-loop` | Lets Claude keep working in a loop until a task is really done |\n\nThere are also language plugins (LSP) for Swift, TypeScript, Python, Kotlin and Rust, among others.",
  wa=["You work with Claude Code on a real codebase.", "You want to standardise reviews and commits."],
  v=[("/code-review", "A review of your current PR with findings and scores."), ("/feature-dev Add dark mode to the settings", "A guided workflow from exploring to shipping.")],
  tips=["The `swift-lsp` plugin is also handy if you build iOS apps."])
e("mcp-builder", t="Guide to building good MCP servers yourself in Python (FastMCP) or TypeScript.",
  w="With MCP (Model Context Protocol) you connect Claude to external services through tools. This skill guides Claude in building a high-quality MCP server: good tool names and descriptions, error handling and testing, in Python (FastMCP) or Node/TypeScript.",
  wa=["You want to connect Claude to your own API, like your Homey app or a database."],
  v=[("Build an MCP server that exposes the notifications from my own API as a tool.", "A working MCP server with tools and tests.")], tips=[])
e("webapp-testing", t="Tests local web apps with Playwright: clicking, taking screenshots and reading browser logs.",
  w="A toolkit that lets Claude operate your local web application through Playwright: open pages, fill in forms, test buttons, take screenshots and read console logs to track down errors.",
  wa=["You want to check that your website or PWA still works after a change."],
  v=[("Start the app on localhost:3000, test the login form and take a screenshot of every step.", "A test report with screenshots and any errors.")], tips=[])
e("claude-api", t="Up-to-date reference for building with the Claude API and SDKs: models, pricing, tools, streaming and caching.",
  w="This skill makes sure that when building AI applications Claude doesn't work from memory, but uses the current documentation: model IDs, pricing, parameters, streaming, tool use, MCP, agents, prompt caching and migrating between models.",
  wa=["You are building an app that uses the Claude API."],
  v=[("Add a feature to my app that summarises notifications with the Claude API, using prompt caching.", "Code that uses the correct, current API calls.")], tips=[])
e("vercel-agent-skills", t="React and Next.js best practices, web design guidelines and deploying to Vercel.",
  w="Vercel publishes skills with its own best practices: **react-best-practices**, **composition-patterns**, **react-native-skills**, **react-view-transitions**, **web-design-guidelines**, **writing-guidelines**, **deploy-to-vercel** and **vercel-optimize** (an audit of costs, performance and caching).",
  wa=["You build with React, Next.js or React Native.", "You host on Vercel."],
  v=[("Review this page against the web-design-guidelines.", "A list of concrete improvements."), ("Deploy this project to Vercel.", "A live preview URL.")],
  tips=["On [skills.sh](https://skills.sh) you'll find thousands of skills you can install with the same CLI."])
e("n8n-skills", t="Expert knowledge for building flawless n8n workflows via the n8n MCP server.",
  w="Fourteen cooperating skills, a router skill and hooks that teach Claude how n8n really works: expressions, configuring nodes, Code nodes in JavaScript or Python, validation and workflow patterns. Meant to work together with the [n8n-mcp](https://github.com/czlonkowski/n8n-mcp) server, so Claude can build workflows directly in your n8n.",
  wa=["You automate with n8n and want Claude to build or fix workflows."],
  v=[("Build an n8n workflow that fetches the weather forecast every morning and sends it to Telegram.", "A validated workflow in your n8n.")],
  tips=["Install the n8n-mcp server first; without it Claude can't reach your n8n."])
e("terraform-skill", t="Best practices for Terraform and OpenTofu: modules, testing, CI/CD and production-ready infrastructure.",
  w="Made by a well-known Terraform expert. The skill helps Claude structure modules, test infrastructure code, set up CI/CD and write secure production code, for AWS, Azure and GCP.",
  wa=["You manage infrastructure as code."],
  v=[("Set up a Terraform module for a static website on AWS, with tests.", "A clean module with a test setup.")], tips=[])

# ───────── CONTENT ─────────
e("humanizer", t="Rewrites AI-sounding text so it reads like a person wrote it, without changing the content.",
  soc="The most viral skill right now according to Artificial Corner. Watch out: look-alike copies are circulating, so only install from the official repo.",
  w="Humanizer is based on Wikipedia's list *Signs of AI writing*, the guide Wikipedia editors use to spot AI text. The skill removes typical AI tricks: 'not X but Y' contrasts, punchy one-liners at the end, forced triads, dashes everywhere, inflated claims, sales language, stock AI words and bold labels. Your message stays the same, only the tone becomes more human.",
  wa=["You post on LinkedIn or Instagram and don't want it to smell of AI.", "You want to strip a Claude draft of its AI tics."],
  v=[("/humanizer Rewrite this LinkedIn post so it sounds like me.", "The same post, but more natural and without AI patterns.")],
  tips=["Always check you have the real repo: github.com/blader/humanizer."])
e("marketingskills", t="A big collection of marketing skills: copywriting, social, content strategy, CRO, SEO and marketing psychology.",
  w="A collection for marketers and founders. Including **copywriting** (pages, posts and ads), **social** (content for six platforms, including Instagram and TikTok), **content-strategy** (from goal to content plan and calendar), **marketing-psychology** (persuasion principles, hooks and calls to action), plus conversion optimisation, SEO and analytics.",
  wa=["You want a landing page or ad that converts.", "You want a content calendar for your app."],
  v=[("Write three variants of the App Store description for my app, with different hooks.", "Three well-argued variants."),
     ("Make a 4-week Instagram content plan for the launch of my app.", "A calendar with topics, formats and hooks.")], tips=[])
e("instagram-agent", t="Thirteen skills that run an Instagram account: Reels with scorable hooks, captions, carousels, stories and DMs.",
  soc="Widely shared by Instagram creators; several blogs have written complete installation guides for it.",
  w="A pack of thirteen skills (`ig-reel`, `ig-caption`, `ig-carousel`, `ig-story`, `ig-viral`, `ig-plan`, `ig-audit`, `ig-profile`, `ig-dm`, `ig-reply`, `ig-comment`, `ig-repurpose` and `ig-human`). They write Reels based on 26 hook formulas and score the hook, research what goes viral, lint your captions and remove AI language. Nothing needs to be connected.",
  wa=["You want to post consistently for your app or organisation.", "You want better hooks and captions."],
  v=[("Write a 30-second Reel script about 'Why your neighbours are your best security' with a scoring hook.", "A script with a hook score and caption."),
     ("Audit my Instagram profile and give 5 improvements.", "A profile audit.")], tips=[])
e("instagram-carousel", t="Pixel-perfect Instagram carousels in your own brand style, exported to PNG and PDF.",
  w="On first use you set up your brand once (name, handle, photo, accent colour, style). After that Claude creates carousels in four styles: Bold Impact, Tweet Post, Clean Editorial and Product Showcase, with a progress bar, arrows and a CTA slide. Export to PNG and PDF.",
  wa=["You want to make carousels quickly without Canva."],
  v=[("Create a 6-slide carousel: '5 tips for a safer neighbourhood'.", "Six slides in your brand style, ready to post.")], tips=[])
e("last30days", t="Researches what people really say about a topic in the last 30 days: Reddit, X, YouTube, TikTok and more.",
  w="Instead of editorial articles, this skill looks for what **people** say: posts and engagement from Reddit, X, YouTube, TikTok, Hacker News, Polymarket, GitHub and the web, from the last 30 days. A `doctor` check shows which sources work.",
  wa=["You want to know what's going on right now around a topic or competitor.", "You're looking for inspiration for timely content."],
  v=[("/last30days Claude skills", "An overview of what was said about Claude skills over the past month, with sources.")],
  tips=["Don't install it via both methods at once; Claude Code doesn't deduplicate that."])
e("claude-seo", t="Complete SEO audit: technical SEO, Core Web Vitals, schema.org, local SEO and visibility in AI search engines.",
  w="An SEO plugin with dozens of sub-skills and specialised agents: technical SEO, Core Web Vitals, E-E-A-T, schema.org, AI search engines (GEO), local SEO, e-commerce and international SEO.",
  wa=["You want your website audited before you promote it."],
  v=[("Do a full SEO audit of https://yourwebsite.com", "A report with priorities and concrete fixes.")], tips=[])

# ───────── KNOWLEDGE ─────────
e("claude-mem", t="Gives Claude Code a lasting memory: what happened in earlier sessions comes back automatically.",
  w="Claude-Mem is a 'persistent memory compression system'. Through hooks it records what happens in your sessions, compresses it and adds relevant memories to new sessions. There is a local web viewer to search your memory. After installation it asks you to log in via an email link.",
  wa=["You work on the same project for a long time and don't want to give context again and again."],
  v=[("(just keep working)", "In a new session Claude still knows which decisions and bug fixes were made earlier.")],
  tips=["Read the privacy information in the repo: the hosted storage is used by default."])
e("claudeception", t="Lets Claude Code write new skills itself from what it discovers while working.",
  w="Every session an AI agent starts from scratch. If Claude spent an hour solving an obscure error, that knowledge is gone next time. Claudeception fixes that: when Claude discovers something non-obvious (a workaround, debugging trick or project pattern), it saves it as a new skill. With a similar problem that skill is loaded automatically.",
  wa=["You often run into the same kind of problems.", "You want your setup to get smarter the more you work."],
  v=[("/claudeception", "Claude reviews the session and turns it into a new skill where useful."), ("Save this as a skill.", "A new SKILL.md in your skills folder.")], tips=[])
e("obsidian-skills", t="Official skills from Obsidian's creator: notes, Bases, JSON Canvas and the Obsidian CLI.",
  w="Skills for working with your Obsidian vault: **obsidian-markdown** (Obsidian's flavour of Markdown), **obsidian-bases**, **json-canvas**, **obsidian-cli** (read, create and search notes via the CLI) and **defuddle** (pull in web pages cleanly).",
  wa=["You use Obsidian as a second brain."],
  v=[("Turn today's meeting notes into a note in my vault with links to the projects involved.", "A clean Obsidian note with [[links]].")],
  tips=["Want diagrams in Obsidian? Have a look at [Axton's Obsidian Visual Skills](https://github.com/axtonliu/axton-obsidian-visual-skills) for Excalidraw, Mermaid and Canvas."])

# ───────── BUSINESS ─────────
KWP_EN = [("productivity", "Productivity", "Tasks, calendars, daily workflows and personal context"),
       ("sales", "Sales", "Researching prospects, preparing calls, pipeline, outreach and battlecards"),
       ("customer-support", "Customer support", "Triaging tickets, drafting replies, escalations and knowledge base articles"),
       ("product-management", "Product management", "Specs, roadmaps, user research and stakeholder updates"),
       ("marketing", "Marketing", "Content, campaigns, brand voice, competition and reporting"),
       ("legal", "Legal", "Contract review, NDA triage, compliance and risk"),
       ("finance", "Finance", "Journal entries, reconciliations, financial statements and audits"),
       ("data", "Data", "SQL, statistics, dashboards and validation"),
       ("design", "Design", "Design critique, accessibility, handoff, UX copy and research"),
       ("engineering", "Engineering", "Architecture, reviews, debugging, incidents and standups"),
       ("human-resources", "HR", "Recruiting, onboarding, reviews and policy"),
       ("operations", "Operations", "Processes, risks, runbooks and status reports"),
       ("enterprise-search", "Enterprise search", "One query across mail, chat, documents and wikis"),
       ("small-business", "Small business", "Chasing invoices, cash flow, social content, proposals and more"),
       ("bio-research", "Bio research", "Literature, genomics and preclinical research")]
e("knowledge-work-plugins", name="Anthropic role plugins", t="Ready-made packs of skills, commands and connectors per job function: sales, finance, legal, marketing and more.",
  w="Anthropic made a plugin per job function. Each plugin bundles **skills** (domain knowledge Claude uses automatically), **commands** (like `/sales:call-prep` or `/data:write-query`) and **connectors** to the tools of that role (Slack, HubSpot, Notion, Jira, Snowflake…). They are meant as a starting point: adapt them with your own terms, processes and tools.\n\n| Plugin | For |\n| --- | --- |\n" + "\n".join(f"| `{a}` | **{b}**: {c} |" for a, b, c in KWP_EN),
  wa=["You want to use Claude as a specialist for a particular role.", "You want your team to get consistent results."],
  v=[("/sales:call-prep Meeting with a municipality about a new neighbourhood app", "Call preparation with background and questions."),
     ("/small-business:invoice-chase", "Overview of outstanding invoices with draft reminders.")],
  tips=["Use the `cowork-plugin-management` plugin to create or adapt a plugin for your own role."])

# ───────── SECURITY ─────────
e("trail-of-bits", t="Dozens of professional security skills from a renowned security firm: audits, Semgrep, fuzzing and supply chain.",
  w="Trail of Bits is a renowned security company. Their marketplace contains skills and plugins for security analysis: differential reviews, static analysis, writing Semgrep rules, supply-chain risks, insecure defaults, property-based testing, mutation testing, finding vulnerability variants and more.",
  wa=["You want your own code (for example an app with user data) audited."],
  v=[("Check my dependencies for supply-chain risks.", "A risk overview per package.")],
  tips=["Only use these skills on code and systems you have permission for."])
e("scientific-skills", t="A library of 170+ scientific skills: biology, chemistry, medicine, physics and data analysis.",
  w="A collection of over 170 research skills: biology, chemistry, medicine, physics, engineering, earth sciences, data analysis and scientific communication. Follows the open Agent Skills standard.",
  wa=["You do (hobby) research or data analysis with scientific sources."],
  v=[("Analyse this measurement data and make a publication-ready chart with an explanation.", "Analysis and chart following scientific conventions.")], tips=[])

# ───────── BUILDING ─────────
e("skill-creator", t="The skill for making skills: set up, improve, test with evals and optimise the description.",
  w="Skill Creator guides you through making your own skill: what should it do, when should it trigger, which scripts or examples belong with it. Then it tests the skill with evals, measures performance (including variance) and optimises the description so Claude picks it at the right moment.",
  wa=["You notice you keep giving Claude the same instructions.", "Your existing skill doesn't trigger (or triggers too often)."],
  v=[("Turn my standard workflow for publishing an app update into a skill.", "A complete skill folder with SKILL.md, ready to upload."),
     ("My skill is never used. Improve the description and test it.", "An improved description with test results.")],
  tips=["In the Claude app you can also simply say: 'turn this into a skill'."])
e("writing-skills", t="The Superpowers approach to writing and testing skills, just like code.",
  w="Part of [Superpowers](../denken/superpowers.md). This skill treats writing skills as software development: first test whether Claude makes the mistake without the skill, then write the skill and then check whether it really changes the behaviour.",
  wa=["You want skills that demonstrably work."],
  v=[("Write a skill that makes sure the tests always run before a commit.", "A tested skill.")], tips=[])
e("template", name="Skill template & specification", t="The official template and the open Agent Skills specification as a starting point.",
  w="The official repo contains a minimal template and the specification of the open **Agent Skills** standard ([agentskills.io](https://agentskills.io)). That standard is now supported by dozens of agents, so a skill you write once works in Claude Code, Codex, Cursor and more.",
  wa=["You want to set up a skill from scratch yourself."],
  v=[("Use the official template to create a skill 'meeting-minutes'.", "A folder with a valid SKILL.md.")], tips=[])

# ───────── MOBILE ─────────
e("swiftui-expert", t="SwiftUI best practices: state management, view composition, performance, new SDK changes and Liquid Glass.",
  w="Antoine van der Lee (SwiftLee) is a well-known Dutch iOS developer. This skill bundles practical SwiftUI knowledge into compact references for agents and code reviews: how to manage state well, compose views, keep an eye on performance, apply the latest SDK changes and adopt **Liquid Glass**. A second skill, `update-swiftui-apis`, helps replace deprecated APIs.",
  wa=["You are building an iOS, iPadOS or macOS app in SwiftUI.", "You want Claude to write modern SwiftUI instead of outdated patterns."],
  v=[("Review this SwiftUI view for state management and performance.", "Concrete improvements, like @Observable instead of ObservableObject."), ("Adapt the settings screen to Liquid Glass.", "Code that uses the new design language correctly.")],
  tips=["From the same author: [Swift Concurrency](swift-concurrency.md) and [Xcode Build Optimization](xcode-build-optimization.md)."])
e("swiftui-pro", t="Agent skill from Hacking with Swift: modern SwiftUI code for iOS 26+ and Swift 6.",
  w="Paul Hudson, creator of Hacking with Swift, poured his SwiftUI knowledge into a skill. It targets iOS 26 and later and recent Swift versions, and makes sure Claude uses current APIs and idioms and avoids classic pitfalls.",
  wa=["You build SwiftUI apps for the latest iOS versions."],
  v=[("Build a list with search, swipe actions and pull-to-refresh in modern SwiftUI.", "Modern, compact SwiftUI code.")],
  tips=["Also by Paul Hudson: [Swift Testing Pro](swift-testing-pro.md)."])
e("swift-concurrency", t="Helps Claude with async/await, actors, Sendable and migrating to Swift 6 strict concurrency.",
  w="Swift Concurrency is tricky, and AI agents often get it wrong. This skill gives Claude the right knowledge about async/await, actors, `@MainActor`, `Sendable`, tasks and resolving strict-concurrency warnings in Swift 6.",
  wa=["You get Swift 6 concurrency errors.", "You want to convert old completion handlers to async/await."],
  v=[("Fix all Sendable warnings in this module without @unchecked.", "A correct, safe solution per warning.")], tips=[])
e("xcode-build-optimization", t="Six skills that measure and speed up your Xcode builds: clean, incremental, compile hotspots and SPM.",
  w="An orchestrator skill with five specialists: benchmark, compilation analysis, project settings, Swift Package Manager analysis and a fixer. Claude first measures how long your builds take, finds the bottlenecks and suggests targeted improvements.",
  wa=["Your builds are slow and you want to know why."],
  v=[("Benchmark my project and make the incremental build faster.", "Measurements before and after, with the changes in between.")],
  tips=["Install all six skills: the orchestrator needs the specialists."])
e("swift-testing-pro", t="Writing good tests with the new Swift Testing framework (@Test, #expect).",
  w="Teaches Claude the modern Swift Testing framework: `@Test`, `#expect`, parameterised tests, traits and converting XCTest to Swift Testing.",
  wa=["You want to add tests to your Swift app.", "You are migrating from XCTest."],
  v=[("Write Swift Testing tests for this DateFormatter helper, including edge cases.", "Parameterised tests with clear names.")], tips=[])
e("ios-simulator", t="Lets Claude build, launch and test your iOS app in the Simulator, with 30 helper scripts.",
  w="With this skill Claude can operate the iOS Simulator: build and install apps, tap and navigate through the accessibility tree, take screenshots, read logs and debug problems. The 30 scripts are optimised for both humans and agents.",
  wa=["You want Claude to check for itself that its change works in the app."],
  v=[("Build the app, open it in the iPhone simulator and test whether the onboarding screen works.", "A test report with screenshots.")],
  tips=["Prefer an MCP server? The author also has XC-MCP."])
e("expo", t="Official Expo skills: building React Native apps, Expo Router, EAS Build/Update and publishing to the stores.",
  w="Over twenty skills from Expo itself: project structure, Expo Router, native UI and animations, data fetching, building modules, upgrading, web-to-native, App Clips and the EAS services (builds, updates, hosting, workflows and publishing to the App Store and Play Store).",
  wa=["You are building a cross-platform app with React Native and Expo."],
  v=[("Upgrade this Expo project to the latest SDK.", "A guided upgrade with the right steps."), ("Set up EAS Update so I can roll out fixes without a new build.", "Configuration and explanation.")], tips=[])

# ───────── CLOUD ─────────
e("supabase", t="Official Supabase skills and Postgres best practices for database, auth and storage.",
  w="Two skills: **supabase** (working with the Supabase platform: database, auth, storage, edge functions) and **supabase-postgres-best-practices** (good schemas, indexes, row level security and queries).",
  wa=["Your app uses Supabase as its backend."],
  v=[("Design a schema for notifications with row level security per user.", "SQL migrations with RLS policies.")],
  tips=["Also in the official marketplace as `supabase`."])
e("neon", t="Skills for Neon serverless Postgres: database, auth, functions, object storage and realtime.",
  w="Neon's own skills for its serverless Postgres platform, including branches for every feature, Neon Auth, functions, object storage, realtime and the AI gateway.",
  wa=["You use (or are considering) Neon as your database."],
  v=[("Create a Neon branch for this feature and run the migration on it.", "A separate database branch to test safely.")], tips=[])
e("cloudflare", t="Building on Cloudflare: Workers, Durable Objects, Agents SDK, Wrangler, Turnstile and more.",
  w="A collection of skills for the Cloudflare Developer Platform: Workers best practices, Durable Objects, the Agents SDK, Wrangler, Next.js on Cloudflare, web performance, Turnstile and the email service. The plugin also installs the Cloudflare MCP server.",
  wa=["You host your website or API on Cloudflare."],
  v=[("Convert this API to a Cloudflare Worker with caching.", "A Worker plus wrangler configuration.")], tips=[])
e("aws-skills", t="AWS development: CDK, serverless/event-driven architecture, cost optimisation and Bedrock AgentCore.",
  w="Plugins for AWS with MCP integrations: CDK best practices, serverless and event-driven patterns, cost management, SST and deploying AI agents with Bedrock AgentCore. With the AWS Documentation MCP, Claude uses up-to-date AWS documentation.",
  wa=["You build or manage infrastructure on AWS."],
  v=[("Analyse my AWS costs and give the three biggest savings.", "A cost report with actions.")],
  tips=["The official marketplace also contains AWS plugins from Amazon itself, such as `aws-core` and `aws-serverless`. See the [catalogue](../../catalogus/README.md)."])
e("microsoft-azure", t="Hundreds of skills from Microsoft for Azure SDKs, AKS, Application Insights and Microsoft AI Foundry.",
  w="Skills, agents, AGENTS.md templates and MCP configurations for anyone working with Azure: from Azure SDKs in Python, .NET, Java and TypeScript to AKS troubleshooting, cost optimisation and Microsoft AI Foundry. There is also a `deep-wiki` plugin.",
  wa=["You build on Azure or with Microsoft AI services."],
  v=[("Add Application Insights to this Node app.", "Instrumentation following Microsoft's guidelines.")],
  tips=["Don't install everything at once: pick the skills for your language and services."])
e("hashicorp", t="Official skills for Terraform (style guide, tests, stacks, modules) and Packer images.",
  w="The makers of Terraform provide skills for the Terraform style guide, testing, stacks, policies, importing existing resources, refactoring modules and even building your own providers. For Packer there are skills to build AWS, Azure and Windows images.",
  wa=["You manage infrastructure with Terraform or build machine images with Packer."],
  v=[("Import these existing S3 buckets into Terraform.", "Import blocks and the matching configuration.")],
  tips=["See also the community variant [Terraform Skill](../ontwikkeling/terraform-skill.md)."])
e("huggingface", t="AI/ML tasks: datasets, training and evaluating models, Spaces, Gradio and the Hugging Face Hub.",
  w="Skills for machine learning on the Hugging Face Hub: the `hf` CLI, datasets, Spaces and Gradio, training models (TRL, LoRA, vision, sentence-transformers), evaluations, publishing papers and running models locally.",
  wa=["You want to fine-tune your own model or build a demo Space."],
  v=[("Create a Gradio Space that summarises Dutch text.", "A working Space repo.")], tips=[])
e("stripe", t="Official Stripe skills and best practices for payments, Connect and API upgrades.",
  w="Stripe's own skills: best practices for payments, Stripe Connect, Stripe Apps, looking up documentation and upgrading the API. Combined with the Stripe MCP server, Claude can work with your Stripe account safely.",
  wa=["You want payments or subscriptions in your app or website."],
  v=[("Add a monthly subscription with Stripe Checkout and a webhook.", "Checkout integration plus webhook handler.")],
  tips=["Manually installed skills don't update themselves: `npx skills update -y`."])
e("sentry", t="The skills Sentry uses internally: finding bugs, code reviews, commits, PRs and security reviews.",
  w="Sentry shares the skills of its own engineers: `find-bugs`, `code-review`, `security-review`, `commit`, `pr-writer`, `iterate-pr`, a GitHub Actions security review, `skill-scanner` (checks skills for risks) and more.",
  wa=["You want to adopt professional dev workflows.", "You want to scan other people's skills for risks."],
  v=[("/find-bugs", "A list of likely bugs in your current changes.")],
  tips=["For error monitoring itself: the `sentry` plugin in the official marketplace."])
e("firecrawl", t="Searching and reading the web for your agent: search, scrape pages, leads, SEO audits and deep research.",
  w="Connects Claude to Firecrawl's search and scrape tools, with skills for deep research, reading documentation, finding and enriching leads, job postings, brand identity and SEO audits.",
  wa=["You want thorough web research with clean page content."],
  v=[("Do deep research on neighbourhood watch apps in the Netherlands and summarise it.", "A report with sources.")], tips=[])

# ───────── PRODUCTIVITY ─────────
e("connect-apps", t="Lets Claude take real actions in 1000+ apps: send mail, create issues, post messages.",
  w="With this plugin Claude takes actions in external apps like Gmail, Slack and GitHub. Composio handles the login and connects to more than a thousand apps. The repo also contains hundreds of 'automation' skills per app.",
  wa=["You want Claude to actually do things in your apps, not just write text."],
  v=[("Send a summary of this meeting to the team in Slack.", "A message in your Slack channel.")],
  tips=["In the Claude app you can also connect many apps directly via **Settings → Connectors**."])
e("file-organizer", t="Tidies folders smartly: finds duplicates, proposes a better structure and automates the clean-up.",
  w="Claude looks at your folders, understands what's in them, finds duplicate files, proposes a more logical folder structure and carries out the clean-up for you.",
  wa=["Your Downloads or documents folder is chaos."],
  v=[("Tidy up my Downloads folder: group by type and find duplicates.", "A proposal and, after approval, a tidy folder.")],
  tips=["Let Claude make a proposal first before it moves anything."])
e("invoice-organizer", t="Organises invoices and receipts for your tax return: extracts data, renames and sorts.",
  w="Reads messy invoices and receipts, extracts date, supplier and amount, gives them a consistent name and sorts them into logical folders.",
  wa=["You need to get your bookkeeping in order for VAT or income tax."],
  v=[("Organise all invoices in this folder by quarter and supplier.", "Neatly renamed and sorted files.")], tips=[])
e("meeting-insights", t="Analyses meeting transcripts for communication patterns and gives personal feedback.",
  w="Reads meeting transcripts and shows where you avoid conflict, use lots of filler words, dominate the conversation or miss chances to listen. Useful for improving how you lead meetings.",
  wa=["You chair a lot of meetings and want to lead better."],
  v=[("Analyse the transcripts of the last three meetings and give me feedback as chair.", "Patterns and concrete tips.")], tips=[])
e("changelog-generator", t="Turns your git commits into clear release notes for users.",
  w="Analyses your commit history, categorises changes (new, improved, fixed) and translates technical commits into clear, customer-friendly release notes.",
  wa=["You are publishing a new version of your app and want 'What's new' text."],
  v=[("Create release notes for everything since tag v2.3.0, in Dutch and English.", "Release notes in two languages.")], tips=[])
e("tailored-resume", t="Creates a CV tailored to a job posting, so your relevant experience comes first.",
  w="Analyses a job description and rewrites your CV so that the experience, skills and results that count for this job stand out most.",
  wa=["You are applying and want a targeted CV per vacancy."],
  v=[("Here is my CV and the job posting. Make a tailored CV.", "An adapted CV with the right emphasis.")],
  tips=["Then have it made into a Word file with the [Word skill](../documenten/docx.md)."])
e("domain-brainstormer", t="Comes up with creative domain names and checks whether they're free on .com, .io, .dev, .ai and more.",
  w="Generates domain names that fit your project and checks availability across several extensions.",
  wa=["You are starting a new project or app."],
  v=[("Come up with 15 domain names for a neighbourhood app and check whether .nl and .app are free.", "A list of available options.")], tips=[])
e("raffle-winner-picker", t="Picks random winners from a list or spreadsheet, fairly and transparently.",
  w="For giveaways, raffles and draws: Claude picks random winners from a list, CSV or Google Sheet, in a verifiable way.",
  wa=["You are organising a giveaway or raffle."],
  v=[("Pick 3 winners from this list of entries, without duplicate email addresses.", "Three winners with an explanation of the draw.")], tips=[])
e("google-workspace-skills", t="25 skills for Gmail, Calendar, Docs, Sheets, Slides, Drive, plus Postgres, Telegram, WhatsApp and more.",
  w="A collection of portable skills: Gmail, Google Calendar, Chat, Docs, Sheets, Slides and Drive, but also Deep Research via Gemini, Imagen for images, NotebookLM, Jules, Outline, Atlassian, Azure DevOps, Postgres/MySQL/MSSQL (read-only) and Telegram and WhatsApp.",
  wa=["You want Claude Code to work with your Google account or databases."],
  v=[("Find the latest emails from the municipality in my Gmail and put the appointments in my calendar.", "Calendar items based on your mail.")],
  tips=["In the Claude app you can also connect Google through Connectors, without a skill."])
e("notebooklm", t="Lets Claude Code talk directly to NotebookLM for answers based only on your own documents.",
  w="Claude asks questions of your NotebookLM notebooks and gets answers based exclusively on the sources you uploaded there. Useful when you want reliable answers without made-up content.",
  wa=["You keep all your policy documents or manuals in NotebookLM."],
  v=[("Ask my notebook 'Neighbourhood policy' what it says about green maintenance.", "An answer with source references from your notebook.")],
  tips=["The same author also has an MCP version."])
e("tapestry", t="One command: from a URL (video, article, PDF) to clean text and an action plan to apply it.",
  w="Say `learn-this <URL>` and the skill detects the content type (YouTube, article, PDF), pulls in the text cleanly and turns it into a **Ship-Learn-Next** action plan. Separate skills: youtube-transcript, article-extractor, ship-learn-next, scrum-sage, session-log and unblock-action.",
  wa=["You watch lots of tutorials and want to actually do something with them."],
  v=[("learn-this https://www.youtube.com/watch?v=...", "Transcript plus a concrete step-by-step plan.")], tips=[])
e("epub", t="Converts markdown, research or chat summaries into a neat e-book (EPUB3).",
  w="Turns markdown documents into professional EPUB3 e-books that work on Apple Books, Kobo, e-readers and more. Perfect for reading research or long articles offline.",
  wa=["You want to read a long document or this wiki as an e-book."],
  v=[("Turn these 5 articles into one e-book with a table of contents.", "An .epub file.")], tips=[])
e("skill-seekers", t="Automatically turns any documentation website, GitHub repo, PDF or video into a Claude skill.",
  w="Skill Seekers fetches documentation (websites, GitHub repos, PDFs, videos, notebooks) and packages it as a skill. That way you give Claude expert knowledge of a tool or API it doesn't know yet, in a few minutes.",
  wa=["You work with a niche API or tool Claude knows little about."],
  v=[("skill-seekers scrape --url https://docs.example.com", "A ready-made skill folder to install.")], tips=[])
e("family-history", t="Help with planning family tree and genealogy research.",
  w="Helps you structure genealogy research: what do you already know, which sources do you consult, how do you record findings and what are the next steps.",
  wa=["You are researching your family history."],
  v=[("Help me make a research plan for my great-grandfather, born around 1890 in Gelderland.", "A plan with sources such as archives and registers.")],
  tips=["For the Netherlands, WieWasWie and Open Archieven are good starting points."])

# ───────── MEDIA ─────────
e("elevenlabs", t="Text-to-speech, speech-to-text, music, sound effects, dubbing and voice agents.",
  w="Skills for the ElevenLabs API: text-to-speech, speech-to-text, music, sound effects, dubbing, voice changer, voice isolation, realtime and building voice agents.",
  wa=["You want a voice-over, podcast intro or speech feature in your app."],
  v=[("Make a Dutch voice-over of this script with a calm voice.", "An audio file.")],
  tips=["You need an ElevenLabs API key; the `setup-api-key` skill helps you."])
e("excalidraw-diagram", t="Creates beautiful Excalidraw diagrams from plain language: diagrams that explain, not just boxes and arrows.",
  w="The shapes in the diagram follow the idea they explain: fans for one-to-many, timelines for sequences, converging lines for aggregation. So you don't get a boring grid of cards but a diagram that tells a story.",
  wa=["You want to explain an architecture, process or idea visually."],
  v=[("Draw how an alert travels from the control room via the server to the app.", "An .excalidraw file.")], tips=[])
e("obsidian-visual", t="Create Canvas, Excalidraw and Mermaid diagrams from text, for use in Obsidian.",
  w="Three skills: **excalidraw-diagram**, **mermaid-visualizer** and **obsidian-canvas-creator**. They turn text into diagrams you open directly in Obsidian.",
  wa=["You use Obsidian and want to visualise notes."],
  v=[("Make an Obsidian canvas of these project notes.", "A .canvas file with cards and connections.")], tips=[])
e("d3-viz", name="D3.js Visualisation", t="Interactive data visualisations with D3.js: charts, networks and maps.",
  w="Teaches Claude to make custom charts, network diagrams and geographic visualisations with D3.js, with full control over transitions and interaction.",
  wa=["Standard charts aren't enough and you want something custom."],
  v=[("Make an interactive map of the Netherlands with the number of incidents per municipality.", "A D3 map with tooltips.")], tips=[])
e("csv-summarizer", t="Upload a CSV and instantly get an analysis with statistics, trends and charts.",
  w="Automatically detects what kind of data you have (sales, customers, financial, survey) and creates a complete analysis with statistics, correlations, distributions, trends and visualisations, without you first having to say what you want to know.",
  wa=["You have an export and want to know quickly what's in it."],
  v=[("(upload survey.csv)", "A summary with the main insights and charts.")], tips=[])
e("image-enhancer", t="Makes images and screenshots sharper and clearer for presentations and social.",
  w="Improves resolution, sharpness and clarity of images, especially screenshots. Ideal for documentation, presentations and social media.",
  wa=["Your screenshots look blurry in your presentation or App Store page."],
  v=[("Sharpen all screenshots in this folder for my presentation.", "Improved images.")], tips=[])
e("stitch", t="Working with Google Stitch: generating designs, extracting design.md and converting to React or shadcn/ui.",
  w="Skills for Google Stitch, Google's AI design tool: generating and improving designs, extracting a `design.md` from an existing design, managing your design system and converting designs to React, React Native, shadcn/ui or a Vite dashboard.",
  wa=["You design in Stitch and want to bring it to code quickly."],
  v=[("Convert this Stitch design into React components with shadcn/ui.", "Component code that follows the design.")], tips=[])

# ───────── EXTRA ─────────
e("playwright-skill", t="Lets Claude write and run Playwright scripts itself, from simple page tests to long flows.",
  w="A general browser automation skill: Claude writes and runs Playwright code on the spot, for tests, checking forms or walking through a complete user flow.",
  wa=["You want your web app tested or checked automatically."],
  v=[("Test the sign-up flow on my site and report what goes wrong.", "A test run with screenshots and findings.")],
  tips=["See also the official [Webapp Testing](webapp-testing.md)."])
e("context-engineering-kit", t="Advanced techniques: DDD, kaizen, subagent-driven development, critique and prompt engineering.",
  w="A big set of plugins with techniques for better AI development: software architecture and DDD, kaizen (continuous improvement), subagent-driven development, reflection and critique, prompt engineering, documentation and creating your own commands, hooks and skills.",
  wa=["You want to get the most out of Claude Code on big projects."],
  v=[("/critique", "A critical assessment of the latest work by several 'judges'.")],
  tips=["Documentation: [neolab.gitbook.io/cek](https://neolab.gitbook.io/cek/)."])
e("everything-claude-code", t="A complete 'agent harness': agents, skills, commands, hooks and rules in one big package.",
  w="ECC is an extensive system of agents, skills, commands and hooks for Claude Code, meant as a complete 'operating system' for your agent. Big and extensive: mainly interesting for experienced users.",
  wa=["You want a ready-made, extensive Claude Code setup."],
  v=[("(after installation) /plan Add payments", "A guided planning and build flow.")],
  tips=["Choose either the plugin or manual installation, not both."])
e("superpowers-lab", t="Experimental Superpowers skills: finding duplicate functions, interactive terminals with tmux and more.",
  w="New techniques that are still being refined: `finding-duplicate-functions` (finds functions that do the same thing but are written differently, typical of AI code), `using-tmux-for-interactive-commands`, `mcp-cli` and `windows-vm`.",
  wa=["You already use Superpowers and want to try new techniques."],
  v=[("Find duplicate functions in this codebase.", "A list of functions you can merge.")], tips=[])
e("anydesign", t="Analyses an image, website or Figma file and turns it into a structured design.md.",
  w="Turns images, websites and Figma files into a readable design specification: design system, component inventory and instructions to rebuild it. Single elements (a navbar, a 3D illustration) can be copied as a 'rebuild prompt'.",
  wa=["You want to capture the style of your own design so you can keep building consistently."],
  v=[("Make a design.md from this screenshot of my app.", "Colours, typography, spacing and components at a glance.")],
  tips=["Use this for your own designs or with permission; don't just copy someone else's design."])
