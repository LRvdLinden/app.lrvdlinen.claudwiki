# GitBook live zetten + branding

Deze repo is klaar voor **GitBook Git Sync**. `.gitbook.yaml` wijst naar `README.md` (startpagina) en `SUMMARY.md` (navigatie).

## 1. Site aanmaken en koppelen

1. Log in op [app.gitbook.com](https://app.gitbook.com) en maak een **nieuwe site** aan met de naam **Claude Wiki**. Kies **niet** het standaardsjabloon.
2. Open de lege space van de site en kies **Configure → Git Sync → GitHub**.
3. Installeer of autoriseer de GitBook GitHub-app voor de repo `LRvdLinden/app.lrvdlinen.claudwiki`, branch `main`.
4. Kies als eerste synchronisatie **GitHub → GitBook**.
   > ⚠️ Kies niet GitBook → GitHub, anders wordt de inhoud van de repo overschreven met een lege space.
5. Wacht tot de import klaar is en klik op **Publish**.

## 2. Branding (Customize)

| Instelling | Waarde |
| --- | --- |
| Titel | Claude Wiki |
| Logo (licht thema) | `.gitbook/assets/logo-light.png` |
| Logo (donker thema) | `.gitbook/assets/logo-dark.png` |
| Favicon / icoon | `.gitbook/assets/mark.png` |
| Primaire kleur | `#6366F1` (indigo) |
| Tint | Primary color |
| Thema | Gradient (anders: Tint), standaard **Dark** |
| Lettertype | Inter |
| Hoeken | Rounded |
| Iconen | Duotone |
| Links in header | `Alle skills` → `/skills` · `Gespot op social` → `/gespot-op-social` · `GitHub` → repo-URL |
| Footer | "Onofficiële wiki door LRvdLinden · Claude is een product van Anthropic" |
| Taal | Nederlands |

### Kleurpalet

| Rol | Kleur |
| --- | --- |
| Primair | `#6366F1` |
| Accent | `#A855F7` |
| Highlight (ster) | `#FBBF24` |
| Achtergrond donker | `#0B0F1F` |

Elke categorie heeft een eigen cover in `.gitbook/assets/cover-<categorie>.png` (1990×480) met een eigen accentkleur. Die worden automatisch gebruikt via de frontmatter van de pagina's.

## 3. Skill-adviseur live zetten (GitHub Pages)

De adviseur staat in `docs/index.html`. Zet GitHub Pages aan:

1. Ga naar **Settings → Pages** van deze repo.
2. Kies bij **Source**: *Deploy from a branch*, branch `main`, map `/docs`, en klik op **Save**.
3. Na een minuut staat hij op `https://lrvdlinden.github.io/app.lrvdlinen.claudwiki/`. De wikipagina *Skill-adviseur* verwijst daar al naar.

Staat GitBook live? Bouw de adviseur dan opnieuw met de GitBook-URL, zodat de links naar de wikipagina's wijzen:

```bash
cd tools && WIKI_BASE=https://<jouw-site>.gitbook.io/claude-wiki python3 build_wiki.py ..
```

Zet in GitBook ook **AI-zoeken (GitBook Assistant)** aan, als je abonnement dat ondersteunt. Dan kunnen bezoekers in de zoekbalk ook een vraag stellen.
