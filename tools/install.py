# Bouwstenen voor installatie-tabs (GitBook-markdown)

APP_NOTE = ("Skills in de Claude-app vragen een Pro-, Max-, Team- of Enterprise-abonnement "
            "en **Code-uitvoering en bestanden maken** moet aanstaan.")


def tab(title, body):
    return f'{{% tab title="{title}" %}}\n{body.strip()}\n{{% endtab %}}'


def tabs(*items):
    return "{% tabs %}\n" + "\n\n".join(items) + "\n{% endtabs %}"


def code(cmd, lang="bash", title=None):
    block = f"```{lang}\n{cmd.strip()}\n```"
    if title:
        return f'{{% code title="{title}" %}}\n{block}\n{{% endcode %}}'
    return block


def cc_market(marketplace, plugin, extra=""):
    return tab("Claude Code", f"""
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

{code(f"/plugin marketplace add {marketplace}\n/plugin install {plugin}", "bash")}

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.
{extra}""")


def cc_official(plugin, extra=""):
    return tab("Claude Code", f"""
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

{code(f"/plugin install {plugin}@claude-plugins-official")}

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.
{extra}""")


def npx(cmd, extra=""):
    return tab("npx skills", f"""
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

{code(cmd)}

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{extra}""")


def app_builtin(extra=""):
    return tab("Claude-app", f"""
Deze skill is **al ingebouwd** voor betaalde abonnementen.

1. Open **Instellingen → Mogelijkheden** (Settings → Capabilities).
2. Zet **Code-uitvoering en bestanden maken** aan.
3. Scroll naar **Skills** en zet de skill aan.

Daarna vraag je gewoon in gewone taal wat je wilt; Claude laadt de skill zelf.
{extra}""")


def app_zip(repo, folder, extra=""):
    return tab("Claude-app", f"""
1. Download de repo als ZIP: [github.com/{repo}](https://github.com/{repo}) → **Code → Download ZIP**.
2. Pak uit en zoek de map `{folder}` (daarin staat `SKILL.md`).
3. Maak van **alleen die map** een nieuwe ZIP. De mapnaam moet gelijk zijn aan de skillnaam.
4. Ga naar **Instellingen → Mogelijkheden → Skills** en klik op **Skill uploaden**.
5. Zet de skill aan.

{APP_NOTE}
{extra}""")


def manual(cmds, extra=""):
    return tab("Handmatig", f"""
Kopieer de skillmap naar je persoonlijke skills-map (voor alle projecten) of naar `.claude/skills/` in één project:

{code(cmds)}
{extra}""")


def official_example(skill):
    """Skills uit anthropics/skills (example-skills)."""
    return tabs(
        app_builtin(),
        cc_market("anthropics/skills", "example-skills@anthropic-agent-skills",
                  "\nDit installeert het hele pakket **example-skills** (o.a. deze skill)."),
        npx(f"npx skills add anthropics/skills --skill {skill}"),
    )


def official_doc(skill):
    return tabs(
        app_builtin("\nIn de Claude-app gebruikt Claude deze skill ook al automatisch zodra je om een bestand van dit type vraagt."),
        cc_market("anthropics/skills", "document-skills@anthropic-agent-skills",
                  "\nDit installeert **document-skills**: Word, PDF, PowerPoint en Excel in één keer."),
        npx(f"npx skills add anthropics/skills --skill {skill}"),
    )
