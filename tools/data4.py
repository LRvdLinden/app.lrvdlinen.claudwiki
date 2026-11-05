# Clone-skills voor websites en apps (NL + EN)
from install import tabs, tab
from en_data import E

NEWCATS4 = [("klonen", "Sites & apps klonen", "clone",
             "Skills die een bestaande website of app analyseren en nabouwen als nette, bewerkbare code. Handig om je eigen site te migreren, verloren broncode terug te halen of te leren hoe iets gemaakt is. Kloon alleen sites en apps die van jou zijn of waarvoor je toestemming hebt.")]
CAT_EN4 = ("Clone sites & apps", "Skills that analyse an existing website or app and rebuild it as clean, editable code. Handy for migrating your own site, recovering lost source code or learning how something was made. Only clone sites and apps you own or have permission for.")

WARN_NL = "Gebruik dit alleen voor je eigen sites en apps, of met toestemming. Logo's, merkuitingen en teksten blijven van de eigenaar, en nabouwen om je als een ander voor te doen (phishing) is verboden. Check ook de gebruiksvoorwaarden van de site."
WARN_EN = "Only use this for your own sites and apps, or with permission. Logos, brand assets and copy belong to their owners, and rebuilding a site to impersonate someone (phishing) is illegal. Also check the site's terms of service."

S4 = []
def add(slug, name, icon, maker, werkt, prijs, bron, social, nl, en, inst_nl, inst_en, werkt_en, prijs_en):
    t, w, wa, v, tips = nl
    S4.append(dict(slug=slug, name=name, cat="klonen", icon=icon, tagline=t, wat=w, wanneer=wa, voorbeelden=v, tips=tips + [WARN_NL],
                   maker=maker, werkt=werkt, prijs=prijs, bron=bron, install=inst_nl, **({"social": social[0]} if social else {})))
    t2, w2, wa2, v2, tips2 = en
    E[slug] = dict(t=t2, w=w2, wa=wa2, v=v2, tips=tips2 + [WARN_EN], werkt=werkt_en, prijs=prijs_en, install=inst_en,
                   **({"soc": social[1]} if social else {}))

add("ai-website-cloner", "AI Website Cloner", "clone", "JCodesMore (community)", "Claude Code (+ Codex, Cursor, OpenCode)", "Gratis (open source)",
    "https://github.com/JCodesMore/ai-website-cloner-template",
    ("Met ruim 13.000 sterren op GitHub de bekendste clone-skill: één commando en je agent bouwt een website na.",
     "With over 13,000 stars on GitHub the best-known clone skill: one command and your agent rebuilds a website."),
    ("Geef je agent een URL en hij bouwt de website na als een nette Next.js-app.",
     "Een projecttemplate met de skill `/clone-website`. Claude werkt in vier stappen: **Map** (welke pagina's wordt welke route), **Observe** (desktop- en mobiele weergave bekijken, echte afbeeldingen, iconen en lettertypes ophalen, hover- en klikstaten uitproberen), **Build** (bewerkbare componenten en werkende interacties bouwen, eventueel verdeeld over subagents) en **Compare** (bron en kloon naast elkaar vergelijken en verschillen repareren). Het resultaat is een Next.js 16-app met React 19, TypeScript, shadcn/ui en Tailwind CSS v4, plus vergelijkingsscreenshots.",
     ["Je wilt je eigen site van WordPress, Webflow of Squarespace overzetten naar moderne code.", "De broncode van je site is kwijt, maar de site staat nog online.", "Je wilt leren hoe een professionele site zijn layout en animaties maakt."],
     [("/clone-website https://mijn-oude-site.nl", "Een Next.js-project dat er hetzelfde uitziet en werkt, klaar om verder te bewerken.")],
     ["Het werkt het best met Claude Code met browsertoegang (bijv. Claude in Chrome of een Playwright-MCP).", "Je hebt Node.js 24 of nieuwer nodig."]),
    ("Give your agent a URL and it rebuilds the website as a clean Next.js app.",
     "A project template with the `/clone-website` skill. Claude works in four steps: **Map** (which page becomes which route), **Observe** (inspect desktop and mobile, extract real images, icons and fonts, try hover and click states), **Build** (build editable components and working interactions, optionally split across subagents) and **Compare** (compare source and clone side by side and repair differences). The result is a Next.js 16 app with React 19, TypeScript, shadcn/ui and Tailwind CSS v4, plus comparison screenshots.",
     ["You want to move your own site from WordPress, Webflow or Squarespace to modern code.", "Your site's source code is lost, but the site is still online.", "You want to learn how a professional site achieves its layout and animations."],
     [("/clone-website https://my-old-site.com", "A Next.js project that looks and works the same, ready for further editing.")],
     ["Works best with Claude Code with browser access (e.g. Claude in Chrome or a Playwright MCP).", "You need Node.js 24 or newer."]),
    tabs(tab("Claude Code", "Maak een eigen kopie van het template en open die in Claude Code:\n\n```bash\ngit clone https://github.com/JCodesMore/ai-website-cloner-template.git mijn-kloon\ncd mijn-kloon && npm install\nclaude\n```\n\nTyp daarna in Claude Code:\n\n```\n/clone-website https://voorbeeld.nl\n```\n\nOp GitHub kan het ook met **Use this template** → **Create repository**.")),
    tabs(tab("Claude Code", "Make your own copy of the template and open it in Claude Code:\n\n```bash\ngit clone https://github.com/JCodesMore/ai-website-cloner-template.git my-clone\ncd my-clone && npm install\nclaude\n```\n\nThen type in Claude Code:\n\n```\n/clone-website https://example.com\n```\n\nOn GitHub you can also use **Use this template** → **Create repository**.")),
    "Claude Code (+ Codex, Cursor, OpenCode)", "Free (open source)")

add("perfect-web-clone", "Perfect Web Clone", "ruler-combined", "ericshang98 (community)", "Claude Code (+ andere agents)", "Gratis (open source)",
    "https://github.com/ericshang98/perfect-web-clone-skill", None,
    ("Pixel-perfecte kopie van een webpagina: plak een URL en krijg een gemeten Vite + React-replica.",
     "Deze skill is een strak 'speelboek' voor pixel-perfect klonen. Na één opdracht (`clone https://…`) moet de agent vastleggen, plannen, bouwen, meten en repareren tot de kloon door een reeks keuringen komt: volledige capture, complete structuur, echte interacties, gewicht en een visuele score per sectie. De hulptool `pwc` doet het meten en kijken.",
     ["Je wilt dat de kopie er echt tot op de pixel hetzelfde uitziet.", "Je wilt meetbaar bewijs dat de kloon klopt."],
     [("clone https://mijn-landingspagina.nl", "Een Vite + React-project plus een rapport met scores per sectie.")], []),
    ("Pixel-perfect copy of a web page: paste a URL and get a measured Vite + React replica.",
     "This skill is a strict playbook for pixel-perfect cloning. After one request (`clone https://…`) the agent must capture, plan, build, measure and repair until the clone passes a set of gates: complete capture, complete structure, real interactions, weight and a visual score per section. The helper tool `pwc` does the measuring and looking.",
     ["You want the copy to really look identical down to the pixel.", "You want measurable proof that the clone is right."],
     [("clone https://my-landing-page.com", "A Vite + React project plus a report with scores per section.")], []),
    tabs(tab("Handmatig", "```bash\ngit clone https://github.com/ericshang98/perfect-web-clone-skill.git ~/.claude/skills/perfect-web-clone\n```\n\nVoor het meten heb je ook de tool [Perfect-Web-Clone (pwc)](https://github.com/ericshang98/Perfect-Web-Clone) nodig; zie de README.")),
    tabs(tab("Manual", "```bash\ngit clone https://github.com/ericshang98/perfect-web-clone-skill.git ~/.claude/skills/perfect-web-clone\n```\n\nFor measuring you also need the [Perfect-Web-Clone (pwc)](https://github.com/ericshang98/Perfect-Web-Clone) tool; see the README.")),
    "Claude Code (+ other agents)", "Free (open source)")

add("web-clone", "Web Clone (echte bron eerst)", "code-compare", "Jane-xiaoer (community)", "Claude Code", "Gratis (open source)",
    "https://github.com/Jane-xiaoer/claude-skill-web-clone", None,
    ("Een methode om websites trouw te klonen zonder verzonnen code: eerst de echte broncode, dan pas nabouwen.",
     "AI-tools maken vaak 'kloonanalyses' vol code die er goed uitziet maar verzonnen is. Deze skill werkt anders: een beslisboom in zes stappen en scripts die eerst de echte bron ophalen. Statische HTML/CSS-sites worden gespiegeld met `wget --mirror`, React-, Vue- en Next-sites worden op een template nagebouwd, en bij sites met meerdere pagina's worden eerst alle routes in kaart gebracht. Ook voor WebGL-sites is er een aanpak.",
     ["Je wilt een kloon die gebaseerd is op de echte code, niet op gokwerk.", "Je wilt een site offline kunnen bekijken of bestuderen."],
     [("Kloon mijn portfoliosite zodat ik hem offline kan aanpassen.", "Een lokale kopie volgens de best passende methode.")], []),
    ("A method for faithfully cloning websites without made-up code: real source first, then rebuild.",
     "AI tools often produce 'clone analyses' full of plausible-looking but fabricated code. This skill works differently: a six-step decision tree and scripts that fetch the real source first. Static HTML/CSS sites are mirrored with `wget --mirror`, React, Vue and Next sites are rebuilt on a template, and for multi-page sites all routes are mapped first. There is also an approach for WebGL sites.",
     ["You want a clone based on the real code, not guesswork.", "You want to view or study a site offline."],
     [("Clone my portfolio site so I can edit it offline.", "A local copy using the best-fitting method.")], []),
    tabs(tab("Handmatig", "```bash\ngit clone https://github.com/Jane-xiaoer/claude-skill-web-clone.git ~/.claude/skills/web-clone\n```")),
    tabs(tab("Manual", "```bash\ngit clone https://github.com/Jane-xiaoer/claude-skill-web-clone.git ~/.claude/skills/web-clone\n```")),
    "Claude Code", "Free (open source)")
E["web-clone"]["name"] = "Web Clone (real source first)"

add("clone-to-nextjs", "Clone to Next.js", "copy", "Aisahub (community)", "Claude Code", "Gratis (open source)",
    "https://github.com/Aisahub/skill-clone-to-nextjs", None,
    ("Spiegelt een eenvoudige informatieve website (praktijk, restaurant, portfolio) direct naar een Next.js-project.",
     "Bedoeld voor simpele informatieve sites zoals een huisartsenpraktijk, restaurant, portfolio of bedrijfspresentatie. Elke pagina wordt in een echte Chromium-browser (Playwright) gerenderd, er wordt naar beneden gescrold zodat alles laadt, en daarna worden alle bestanden opgehaald en links herschreven. Het resultaat is een Next.js App Router-project.",
     ["Je wilt een kleine, eenvoudige site snel naar Next.js overzetten."],
     [("Zet de website van onze wijkvereniging om naar een Next.js-project.", "Een Next.js-project met alle pagina's en afbeeldingen.")], []),
    ("Mirrors a simple informational website (practice, restaurant, portfolio) straight into a Next.js project.",
     "Meant for simple informational sites like a clinic, restaurant, portfolio or company intro. Every page is rendered in a real Chromium browser (Playwright), scrolled to the bottom so everything loads, after which all assets are downloaded and links rewritten. The result is a Next.js App Router project.",
     ["You want to move a small, simple site to Next.js quickly."],
     [("Convert our residents' association website into a Next.js project.", "A Next.js project with all pages and images.")], []),
    tabs(tab("Handmatig", "```bash\ngit clone https://github.com/Aisahub/skill-clone-to-nextjs ~/.claude/skills/clone-to-nextjs\n```\n\nDe skill is direct beschikbaar in je volgende Claude Code-sessie.")),
    tabs(tab("Manual", "```bash\ngit clone https://github.com/Aisahub/skill-clone-to-nextjs ~/.claude/skills/clone-to-nextjs\n```\n\nThe skill is available right away in your next Claude Code session.")),
    "Claude Code", "Free (open source)")

add("rea", "REA – Reverse Engineer Anything", "microchip", "morluto (community)", "Claude Code (+ Codex, Cursor, Gemini CLI en meer)", "Gratis (open source)",
    "https://github.com/morluto/rea",
    ("Viraal gegaan via o.a. 'I Tried 23 Viral Claude Skills' (Artificial Corner).", "Went viral through 'I Tried 23 Viral Claude Skills' (Artificial Corner), among others."),
    ("Zie je een functie in een app die je mooi vindt? REA zoekt uit hoe hij werkt, tot op binair niveau, zodat je hem kunt nabouwen.",
     "REA (Reverse Engineer Anything) is de 'clone-skill' voor apps. Hij analyseert native apps, Electron/JavaScript-apps, verpakte programma's, firmware en webapps, legt uit hoe een functie werkt, vergelijkt versies, decompileert code en begeleidt een reconstructie. Voor native analyse kan hij Hopper, Ghidra of IDA gebruiken. Daarnaast kan REA van een live webapp een testomgeving (AgentEnv) bouwen.",
     ["Je ziet een functie in een app en wilt een eenvoudigere versie in je eigen app bouwen.", "Je wilt begrijpen wat een programma op je computer precies doet."],
     [("Hoe werkt de zoekbalk in deze desktop-app? Bouw een eenvoudige versie voor mijn app.", "Een uitleg van de werking plus een eigen, vereenvoudigde implementatie.")],
     ["Gebruik REA alleen op software waarvoor je dat mag; sommige licenties verbieden reverse engineering."]),
    ("See a feature you like in an app? REA works out how it works, down to the binary level, so you can rebuild it.",
     "REA (Reverse Engineer Anything) is the 'clone skill' for apps. It analyses native apps, Electron/JavaScript apps, packaged programs, firmware and web apps, explains how a feature works, compares versions, decompiles code and guides a reconstruction. For native analysis it can use Hopper, Ghidra or IDA. REA can also build a test environment (AgentEnv) from a live web app.",
     ["You see a feature in an app and want to build a simpler version in your own app.", "You want to understand exactly what a program on your computer does."],
     [("How does the search bar in this desktop app work? Build a simple version for my app.", "An explanation of how it works plus your own, simplified implementation.")],
     ["Only use REA on software you're allowed to analyse; some licences forbid reverse engineering."]),
    tabs(tab("Installer", "```bash\nnpx rea-agents setup\n```\n\nDe setup registreert REA bij je agent (Claude Code, Codex, Cursor en meer) en installeert de bijbehorende werkinstructies. Installeer alleen via de officiële bronnen: de repo, [rea.tools](https://rea.tools/) of het npm-pakket `rea-agents`.")),
    tabs(tab("Installer", "```bash\nnpx rea-agents setup\n```\n\nSetup registers REA with your agent (Claude Code, Codex, Cursor and more) and installs the matching workflow instructions. Only install from the official sources: the repo, [rea.tools](https://rea.tools/) or the `rea-agents` npm package.")),
    "Claude Code (+ Codex, Cursor, Gemini CLI and more)", "Free (open source)")
