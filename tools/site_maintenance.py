from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://www.giancarlolupi.com"
YEAR = "2026"
LASTMOD = "2026-09-03"
OG_IMAGE = f"{SITE}/assets/giancarlo-lupi-profile.webp"
INDEPENDENCE_NOTE = (
    "Sito professionale personale · indipendente dalle strutture presso cui viene svolta attività clinica"
)

PUBLIC_HTML = [
    ROOT / "index.html",
    ROOT / "colonna.html",
    ROOT / "neurochirurgia.html",
    ROOT / "medico.html",
    ROOT / "cv-pubblicazioni.html",
    ROOT / "seconda-opinione.html",
    ROOT / "documentazione-clinica.html",
    ROOT / "approfondimenti.html",
    ROOT / "rassegna-stampa.html",
    ROOT / "sedi.html",
    ROOT / "privacy.html",
    ROOT / "404.html",
    ROOT / "approfondimenti" / "mal-di-schiena-quando-preoccuparsi.html",
    ROOT / "approfondimenti" / "risonanza-mal-di-schiena.html",
    ROOT / "approfondimenti" / "robotica-neurochirurgia.html",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def get_title(text: str) -> str:
    m = re.search(r"<title>(.*?)</title>", text, re.I | re.S)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else "Giancarlo Lupi | Neurochirurgo"


def get_description(text: str) -> str:
    patterns = [
        r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']*)["\']',
        r'<meta\s+content=["\']([^"\']*)["\']\s+name=["\']description["\']',
    ]
    for pattern in patterns:
        m = re.search(pattern, text, re.I)
        if m:
            return m.group(1).strip()
    return "Sito professionale personale di Giancarlo Lupi, neurochirurgo."


def get_canonical(text: str, path: Path) -> str:
    m = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']+)["\']', text, re.I)
    if m:
        return m.group(1)
    if path.name == "404.html":
        return SITE + "/"
    if path.parent.name == "approfondimenti":
        return f"{SITE}/approfondimenti/{path.name}"
    if path.name == "index.html":
        return SITE + "/"
    return f"{SITE}/{path.name}"


def normalize_footer(text: str) -> str:
    footer_bottom = (
        '<div class="footer-bottom">'
        f'<span>© {YEAR} Giancarlo Lupi. Tutti i diritti riservati.</span>'
        f'<span>{INDEPENDENCE_NOTE}</span>'
        "</div>"
    )
    return re.sub(
        r'<div class="footer-bottom">.*?</div>',
        footer_bottom,
        text,
        flags=re.I | re.S,
    )


def normalize_navigation_language(text: str) -> str:
    replacements = {
        ">Prenota una visita<": ">Sedi e contatti<",
        ">Sedi e prenotazioni<": ">Sedi e contatti<",
        ">Recapiti e prenotazioni →<": ">Recapiti per visite →<",
        "Area editoriale · archivio avviato il 3 settembre 2026 · aggiornamento settimanale":
            "Area editoriale · archivio avviato il 3 settembre 2026 · aggiornamenti periodici",
        "Area editoriale · aggiornamento settimanale":
            "Area editoriale · aggiornamenti periodici",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def normalize_institutional_bylines(text: str) -> str:
    replacements = {
        "Neurochirurgia AOUP": "Neurochirurgo",
        "Neurochirurgo AOUP": "Neurochirurgo",
        "AOUP · Neurochirurgia": "Neurochirurgo",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def normalize_reading_times(text: str) -> str:
    text = text.replace(">8 min<", ">4 min<")
    text = text.replace(">7 min<", ">3 min<")
    text = text.replace(">9 min<", ">4 min<")
    text = text.replace("8 min di lettura", "4 min di lettura")
    text = text.replace("7 min di lettura", "3 min di lettura")
    text = text.replace("9 min di lettura", "4 min di lettura")
    return text


def normalize_profile_image(text: str, path: Path) -> str:
    pattern = r'<img\s+[^>]*src=["\'](?:\.\./)?assets/giancarlo-lupi-profile\.webp["\'][^>]*>'

    def repl(match: re.Match) -> str:
        tag = match.group(0)
        tag = re.sub(r'\s+(?:width|height|fetchpriority)=["\'][^"\']*["\']', "", tag, flags=re.I)
        attrs = ' width="700" height="525"'
        if path.name == "index.html" and path.parent == ROOT:
            attrs += ' fetchpriority="high"'
        return tag[:-1] + attrs + ">"

    return re.sub(pattern, repl, text, flags=re.I)


def ensure_open_graph(text: str, path: Path) -> str:
    text = re.sub(r'\s*<meta\s+property=["\']og:[^>]+>', "", text, flags=re.I)
    title = get_title(text)
    description = get_description(text)
    canonical = get_canonical(text, path)
    og_type = "article" if path.parent.name == "approfondimenti" else "website"
    tags = (
        f'\n<meta property="og:title" content="{title}">'
        f'\n<meta property="og:description" content="{description}">'
        f'\n<meta property="og:type" content="{og_type}">'
        f'\n<meta property="og:locale" content="it_IT">'
        f'\n<meta property="og:url" content="{canonical}">'
        f'\n<meta property="og:image" content="{OG_IMAGE}">'
        f'\n<meta property="og:image:width" content="700">'
        f'\n<meta property="og:image:height" content="525">'
        f'\n<meta property="og:image:alt" content="Giancarlo Lupi, neurochirurgo">'
        f'\n<meta name="twitter:card" content="summary_large_image">\n'
    )
    return text.replace("</head>", tags + "</head>", 1)


def make_qsalute_unambiguous(text: str) -> str:
    text = text.replace(
        '<div class="kicker">Il percorso visto dai pazienti</div>',
        '<div class="kicker">Testimonianze sulla Neurochirurgia di Pisa</div>',
    )
    text = text.replace(
        '<h2 style="font-size:46px">Ciò che resta della cura.</h2>',
        '<h2 style="font-size:46px">Il percorso raccontato dai pazienti.</h2>',
    )
    text = text.replace(
        "testimonianze pubblicate sulla pagina QSalute della Neurochirurgia di Pisa, dato rilevato il 3 settembre 2026. Il numero dà contesto, non misura l'efficacia clinica.",
        "testimonianze pubblicate sulla pagina QSalute della Neurochirurgia di Pisa, dato rilevato il 3 settembre 2026. Non sono recensioni personali del Dott. Giancarlo Lupi e non costituiscono una misura di efficacia clinica.",
    )
    return text


def process_public_html(path: Path) -> None:
    text = read(path)
    text = normalize_footer(text)
    text = normalize_navigation_language(text)
    text = normalize_institutional_bylines(text)
    text = normalize_reading_times(text)
    text = normalize_profile_image(text, path)
    if path.name == "index.html" and path.parent == ROOT:
        text = make_qsalute_unambiguous(text)
    text = ensure_open_graph(text, path)
    write(path, text)


for html_path in PUBLIC_HTML:
    process_public_html(html_path)

write(
    ROOT / "assets" / "script.js",
    """const btn = document.querySelector('.menu-btn');\nconst nav = document.querySelector('.navlinks');\n\nif (btn && nav) {\n  btn.addEventListener('click', () => {\n    const open = nav.classList.toggle('open');\n    btn.setAttribute('aria-expanded', open ? 'true' : 'false');\n  });\n}\n""",
)

styles = read(ROOT / "assets" / "styles.css")
styles = styles.replace("--muted:#6d747a;", "--muted:#5f666c;")
styles = styles.replace(
    '--sans:Inter,"Helvetica Neue",Arial,sans-serif;',
    '--sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;',
)
styles = styles.replace(
    '--serif:"Iowan Old Style","Palatino Linotype","Book Antiqua",Georgia,"Times New Roman",serif;',
    '--serif:Georgia,"Times New Roman",serif;',
)
write(ROOT / "assets" / "styles.css", styles)

legacy_redirects = {
    "cvitae": "/cv-pubblicazioni.html",
    "map": "/sedi.html",
    "rassegna-stampa": "/rassegna-stampa.html",
    "calendario-appuntamenti": "/documentazione-clinica.html",
}
redirect_template = (
    '<!doctype html><html lang="it"><head><meta charset="utf-8">'
    '<meta name="robots" content="noindex">'
    '<link rel="canonical" href="https://www.giancarlolupi.com{target}">'
    '<meta http-equiv="refresh" content="0;url={target}">'
    '<title>Pagina spostata</title>'
    '<script>location.replace({target_js});</script></head>'
    '<body><p>La pagina è stata spostata. <a href="{target}">Continua</a>.</p></body></html>'
)
for old, target in legacy_redirects.items():
    directory = ROOT / old
    directory.mkdir(exist_ok=True)
    target_js = repr(target).replace("'", '"')
    write(directory / "index.html", redirect_template.format(target=target, target_js=target_js))

sitemap_items = [
    ("/", "monthly"),
    ("/colonna.html", "monthly"),
    ("/neurochirurgia.html", "monthly"),
    ("/medico.html", "monthly"),
    ("/cv-pubblicazioni.html", "yearly"),
    ("/seconda-opinione.html", "monthly"),
    ("/documentazione-clinica.html", "yearly"),
    ("/approfondimenti.html", "weekly"),
    ("/rassegna-stampa.html", "yearly"),
    ("/sedi.html", "monthly"),
    ("/privacy.html", "monthly"),
    ("/approfondimenti/mal-di-schiena-quando-preoccuparsi.html", "weekly"),
    ("/approfondimenti/risonanza-mal-di-schiena.html", "weekly"),
    ("/approfondimenti/robotica-neurochirurgia.html", "weekly"),
]
lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for url, changefreq in sitemap_items:
    lines.append(
        f"<url><loc>{SITE}{url}</loc><lastmod>{LASTMOD}</lastmod><changefreq>{changefreq}</changefreq></url>"
    )
lines.append("</urlset>")
write(ROOT / "sitemap.xml", "\n".join(lines))

print("Manutenzione tecnica completata senza riscrivere i contenuti clinici o MIGRAZIONE-SEO.md")
