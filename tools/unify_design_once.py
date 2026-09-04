from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
STYLES = ROOT / "assets" / "styles.css"
EDITORIAL = ROOT / "assets" / "editorial-v2.css"
MARKER = "/* === Unified design system · 2026-09-04 === */"

TYPE_SCALE = """
  --type-label:13px;
  --type-note:15px;
  --type-ui:16px;
  --type-body:18px;
  --type-lead:21px;
  --type-h3:27px;
  --type-section:clamp(38px,3.8vw,48px);
  --type-page:clamp(48px,5.2vw,68px);
  --type-home:clamp(56px,5.9vw,80px);
""".rstrip()

UNIFIED_CSS = r'''
/* Unified typography and reading rhythm */
body{line-height:1.6}
.brand span span,.eyebrow,.kicker,.tag,.footer-title,.breadcrumb,.story-meta,.journal-meta,.dossier-title,.archive-label,.archive-feature-meta,.archive-date,.archive-reading,.article-meta,.article-author span,.editorial-byline span,.editorial-signature span,.editorial-signature small,.journal-principles span,.booking-label{font-size:var(--type-label);line-height:1.35}
.hero-note,.hero-trust div,.voice-intro .stat-label,.voice-source,.location .details,.location .site,.meta,.editorial-foot,.journal-evidence,.contact-link,.map-link{font-size:var(--type-label);line-height:1.55}
footer p,footer a{font-size:14px;line-height:1.55}
.navlinks,.nav-cta,.btn{font-size:var(--type-label)}

.hero h1{font-size:var(--type-home);line-height:1.03;letter-spacing:-.04em}
.page-hero h1{font-size:var(--type-page);line-height:1.06;letter-spacing:-.04em;max-width:920px}
.article-hero h1{font-size:clamp(46px,5vw,66px);line-height:1.06;letter-spacing:-.04em;max-width:920px}
h2{font-size:var(--type-section);line-height:1.09;letter-spacing:-.035em}
.section-head h2,.voice-intro h2,.cta-band h2{font-size:var(--type-section);line-height:1.09}
.copy h2,.prose h2{font-size:clamp(34px,3.2vw,44px);line-height:1.12}
.journal-head h2,.editorial-mast h2{font-size:clamp(42px,4.4vw,54px);line-height:1.06;letter-spacing:-.045em}
.archive-feature h2{font-size:clamp(38px,4vw,48px);line-height:1.08}
h3,.card h3,.voice-card h3,.location h3,.article-card h3,.dossier-item h3,.archive-row h3,.method-grid h3,.side-story h3{font-size:var(--type-h3);line-height:1.18}
.journal-lead h3,.feature-story h3{font-size:clamp(34px,3.4vw,44px);line-height:1.08;letter-spacing:-.035em}

.lead,.page-hero p,.journal-deck,.article-lede{font-size:var(--type-lead);line-height:1.42}
.section-head p,.journal-intro p,.manifesto-copy{font-size:20px;line-height:1.55}
.prose,.article-prose{max-width:760px}
.prose p,.prose li,.article-prose p,.article-prose li{font-size:var(--type-body);line-height:1.65}
.article-prose>p:first-child{font-size:var(--type-lead);line-height:1.58}
.copy p{font-size:17px;line-height:1.65}
.card p,.voice-card p,.location p,.article-card p,.dossier-item p,.archive-row p,.method-grid p,.side-story p,.journal-lead p{font-size:15px;line-height:1.62}
.journal-deck{font-size:var(--type-lead)}
.quote{font-size:clamp(34px,3.8vw,48px);line-height:1.12}
.care-statement{font-size:var(--type-lead);line-height:1.5}
.institution-note{font-size:var(--type-label);line-height:1.6}
.hero-proof span{font-size:var(--type-label)}
.voice-summary{font-size:var(--type-ui);line-height:1.65}

/* One reading measure for long-form text; layout components keep their own widths. */
.prose,.article-prose,.article-lede{max-width:760px}

/* Phone-first contact actions */
.location .phone.phone-cta{display:flex;flex-direction:column;align-items:flex-start;justify-content:center;gap:2px;min-height:56px;width:100%;margin-top:18px;padding:10px 14px;border:1px solid var(--deep);background:#fff;color:var(--ink);font-family:var(--sans);font-size:inherit;text-decoration:none}
.location .phone.phone-cta:hover{border-color:var(--blue);color:var(--blue)}
.phone-cta span{font-size:var(--type-label);font-weight:750;line-height:1.3}
.phone-cta strong{font-family:var(--serif);font-size:24px;font-weight:500;line-height:1.15}

@media(max-width:760px){
 :root{--type-body:17px;--type-lead:20px;--type-h3:24px;--type-section:clamp(32px,8vw,38px);--type-page:clamp(38px,10vw,46px);--type-home:clamp(48px,13vw,58px)}
 .hero h1{font-size:var(--type-home)}
 .page-hero h1,.article-hero h1{font-size:var(--type-page)}
 .section-head h2,.voice-intro h2,.cta-band h2,h2{font-size:var(--type-section)}
 .copy h2,.prose h2{font-size:clamp(30px,7.8vw,36px)}
 .journal-head h2,.editorial-mast h2{font-size:clamp(34px,9vw,42px)}
 .journal-lead h3,.feature-story h3{font-size:clamp(30px,8vw,36px)}
 .section-head p,.journal-intro p,.manifesto-copy{font-size:19px}
 .phone-cta strong{font-size:23px}
}
'''.strip()


def ensure_scale(css: str) -> str:
    if "--type-label:" in css:
        return css
    m = re.search(r":root\{(.*?)\n\}", css, flags=re.S)
    if not m:
        raise RuntimeError("Blocco :root non trovato in styles.css")
    body = m.group(1).rstrip()
    replacement = ":root{" + body + "\n" + TYPE_SCALE + "\n}"
    return css[:m.start()] + replacement + css[m.end():]


def relative_prefix(path: Path) -> str:
    return "../" if path.parent != ROOT else ""


def footer(prefix: str) -> str:
    p = prefix
    return f'''<footer><div class="container"><div class="footer-grid"><div><a class="brand" href="{p}index.html"><span class="monogram">GL</span><span><strong>Giancarlo Lupi</strong><span>Neurochirurgo · MD PhD</span></span></a><p style="max-width:430px;margin-top:18px">Sito professionale personale dedicato a neurochirurgia, colonna vertebrale, informazione clinica e innovazione. I contenuti non sostituiscono la valutazione medica individuale.</p></div><div><div class="footer-title">Percorso</div><p><a href="{p}index.html">Home</a><br><a href="{p}colonna.html">Colonna vertebrale</a><br><a href="{p}neurochirurgia.html">Neurochirurgia</a><br><a href="{p}seconda-opinione.html">Seconda opinione</a><br><a href="{p}sedi.html">Sedi e contatti</a></p></div><div><div class="footer-title">Informazioni</div><p><a href="{p}medico.html">Il medico</a><br><a href="{p}cv-pubblicazioni.html">CV e pubblicazioni</a><br><a href="{p}rassegna-stampa.html">Rassegna stampa</a><br><a href="{p}approfondimenti.html">Approfondimenti</a><br><a href="{p}documentazione-clinica.html">Documentazione clinica</a><br><a href="{p}privacy.html">Privacy e note informative</a></p><p>Pisa · Ponsacco · Massa</p></div></div><div class="footer-bottom"><span>© 2026 Giancarlo Lupi. Tutti i diritti riservati.</span><span>Sito professionale personale · indipendente dalle strutture presso cui viene svolta attività clinica</span></div></div></footer>'''


def clean_html(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    original = text

    # Tutte le pagine usano un solo foglio di stile.
    text = re.sub(r'<link[^>]+href="(?:\.\./)?assets/editorial-v2\.css"[^>]*>\s*', '', text)

    # Le dimensioni dei titoli sono governate solo dal sistema tipografico CSS.
    text = re.sub(r'(<h[1-3]\b[^>]*?)\s+style="font-size:[^"]+"([^>]*>)', r'\1\2', text)

    # Footer unico e statico, con link relativi corretti anche negli articoli.
    new_footer = footer(relative_prefix(path))
    text, count = re.subn(r'<footer\b.*?</footer>', new_footer, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f"Footer non sostituito correttamente in {path.relative_to(ROOT)}")

    if path.name == "sedi.html" and path.parent == ROOT:
        phones = {
            '+39050586217': ('Pisa', '050 586217'),
            '+393516216891': ('Ponsacco', '+39 351 621 6891'),
            '+39058541847': ('Massa', '0585 41847'),
        }
        for tel, (city, number) in phones.items():
            pattern = rf'<a class="phone(?: phone-cta)?" href="tel:{re.escape(tel)}">.*?</a>'
            replacement = f'<a class="phone phone-cta" href="tel:{tel}" aria-label="Chiama la segreteria di {city}: {number}"><span>Chiama la segreteria di {city}</span><strong>{number}</strong></a>'
            text, n = re.subn(pattern, replacement, text, count=1, flags=re.S)
            if n != 1:
                raise RuntimeError(f"Recapito {city} non trasformato")

    if text != original:
        path.write_text(text, encoding="utf-8")


def merge_css() -> None:
    base = STYLES.read_text(encoding="utf-8")
    if MARKER in base:
        base = base.split(MARKER, 1)[0].rstrip() + "\n"
    base = ensure_scale(base)

    if not EDITORIAL.exists():
        raise RuntimeError("editorial-v2.css non trovato")
    editorial = EDITORIAL.read_text(encoding="utf-8").replace("!important", "")
    merged = base.rstrip() + "\n\n" + MARKER + "\n" + editorial.strip() + "\n\n" + UNIFIED_CSS + "\n"
    STYLES.write_text(merged, encoding="utf-8")
    EDITORIAL.unlink()


def verify(html_files):
    assert len(html_files) == 15, f"Attese 15 pagine HTML, trovate {len(html_files)}"
    for path in html_files:
        text = path.read_text(encoding="utf-8")
        assert "editorial-v2.css" not in text, path
        assert text.count("<footer") == 1, path
        for required in ("cv-pubblicazioni.html", "rassegna-stampa.html", "documentazione-clinica.html", "seconda-opinione.html"):
            assert required in text, f"{required} assente dal footer di {path}"
    css = STYLES.read_text(encoding="utf-8")
    assert MARKER in css
    assert "--type-home:" in css
    assert not EDITORIAL.exists()
    sedi = (ROOT / "sedi.html").read_text(encoding="utf-8")
    assert sedi.count('class="phone phone-cta"') == 3


def main():
    html_files = sorted(ROOT.glob("*.html")) + sorted((ROOT / "approfondimenti").glob("*.html"))
    merge_css()
    for path in html_files:
        clean_html(path)
    verify(html_files)

    # One-off helper: remove itself and its temporary push workflow from the resulting branch.
    for transient in (ROOT / "tools" / "unify_design_once.py", ROOT / ".github" / "workflows" / "design-unification-once.yml"):
        if transient.exists():
            transient.unlink()

    print(f"Design unificato su {len(html_files)} pagine; CSS consolidato; footer e recapiti verificati.")


if __name__ == "__main__":
    main()
