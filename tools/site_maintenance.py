from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]

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
    ROOT / "approfondimenti" / "intelligenza-artificiale-risonanza-colonna.html",
]

FAQS = {
    "colonna.html": [
        ("Un'ernia del disco alla risonanza significa che devo operarmi?",
         "No. Il reperto deve essere coerente con sintomi ed esame neurologico. Molte ernie migliorano con trattamento conservativo; la chirurgia viene considerata quando esiste un beneficio ragionevole atteso o un'indicazione urgente."),
        ("Quando la sciatica diventa urgente?",
         "Una perdita di forza nuova o rapidamente progressiva, disturbi sfinterici nuovi o anestesia perineale richiedono una valutazione urgente e non devono attendere una visita programmata."),
        ("Una stenosi o una spondilolistesi richiedono sempre una stabilizzazione?",
         "No. La necessità di una fusione dipende da instabilità, deformità, stenosi associata, sintomi e caratteristiche individuali. In alcuni casi è sufficiente una decompressione; in altri non è indicata chirurgia."),
        ("Quanto dura l'intervento e quando si torna a guidare o al lavoro?",
         "Non esiste un numero valido per tutte le procedure. Durata, ricovero e recupero cambiano in base al tipo di intervento, stato neurologico, attività lavorativa e decorso. È più corretto definire intervalli personalizzati dopo aver stabilito la procedura realmente indicata."),
        ("Ha senso chiedere una seconda opinione se mi hanno già proposto un intervento?",
         "Sì, soprattutto se vuoi verificare indicazione, alternative o tempi. È utile portare le immagini complete e la proposta già ricevuta."),
    ],
    "neurochirurgia.html": [
        ("Un meningioma scoperto per caso deve essere sempre operato?",
         "No. Molti meningiomi incidentali possono essere osservati con controlli radiologici. Crescita, sintomi, edema, sede, età e rischio procedurale orientano la scelta."),
        ("Un aneurisma cerebrale non rotto deve essere sempre trattato?",
         "No. Dimensioni, sede, morfologia, fattori di rischio e caratteristiche del paziente vanno confrontati con il rischio delle opzioni terapeutiche e con quello dell'osservazione."),
        ("Quanto dura il ricovero e quando si torna alle attività normali?",
         "Non esiste una risposta unica per la neurochirurgia cranica. Tipo di procedura, sede della lesione, condizioni neurologiche e decorso post-operatorio cambiano in modo sostanziale tempi di ricovero e recupero. Gli intervalli utili vanno definiti dopo aver stabilito la strategia concreta."),
        ("Perché è importante portare le immagini e non soltanto il referto?",
         "Il referto sintetizza l'esame; la decisione neurochirurgica richiede spesso di valutare direttamente sede, rapporti anatomici, caratteristiche della lesione e confronto con studi precedenti."),
        ("Posso chiedere una seconda opinione dopo che mi è stato proposto un intervento?",
         "Sì. Può servire a confermare l'indicazione, chiarire alternative e tempi o individuare la necessità di ulteriori approfondimenti."),
    ],
}


def add_second_opinion_to_nav(text, path):
    prefix = "../" if path.parent.name == "approfondimenti" else ""
    href = prefix + "seconda-opinione.html"
    match = re.search(r'(<nav class="navlinks"[^>]*>)(.*?)(</nav>)', text, re.I | re.S)
    if not match or f'href="{href}"' in match.group(2):
        return text
    current = ' aria-current="page"' if path.name == "seconda-opinione.html" else ""
    link = f'<a href="{href}"{current}>Seconda opinione</a>'
    body = re.sub(
        rf'(<a href="{re.escape(prefix)}neurochirurgia\.html"[^>]*>Neurochirurgia</a>)',
        r'\1' + link,
        match.group(2),
        count=1,
        flags=re.I,
    )
    return text[:match.start(2)] + body + text[match.end(2):]


def enforce_new_editorial_metadata(text, path):
    if path == ROOT / "index.html":
        text = text.replace(
            '<div class="journal-meta"><span>Diagnostica · Tecnologia</span><span>05 settembre 2026</span><span>9 min</span></div>',
            '<div class="journal-meta"><span>Diagnostica · Tecnologia</span><span>05 settembre 2026</span></div>')
    elif path == ROOT / "approfondimenti.html":
        text = text.replace(
            '<div class="archive-feature-meta"><span>Diagnostica · Tecnologia</span><span>05 settembre 2026</span><span>9 minuti</span></div>',
            '<div class="archive-feature-meta"><span>Diagnostica · Tecnologia</span><span>05 settembre 2026</span></div>')
    return text


def add_faq_schema(text, path):
    def strip_existing(match):
        return "" if '"FAQPage"' in match.group(1) else match.group(0)

    text = re.sub(r'<script type="application/ld\+json">(.*?)</script>',
                  strip_existing, text, flags=re.I | re.S)
    faqs = FAQS.get(path.name)
    if not faqs:
        return text
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }
    tag = '<script type="application/ld+json">' + json.dumps(
        schema, ensure_ascii=False, separators=(",", ":")) + "</script>"
    return text.replace("</head>", tag + "</head>", 1)


def promote_qsalute_on_home(text, path):
    if path != ROOT / "index.html":
        return text

    # Richiamo diretto dalla hero, leggibile ma distinto dalle CTA di prenotazione/contatto.
    if 'class="hero-proof"' not in text:
        hero_note = re.search(r'(<p class="hero-note">.*?</p>)', text, re.I | re.S)
        if hero_note:
            proof = ('<p class="hero-proof"><a href="#testimonianze">'
                     'Leggi la sintesi delle 141 testimonianze su QSalute →</a>'
                     '<span>Neurochirurgia di Pisa · non recensioni personali</span></p>')
            text = text[:hero_note.end()] + proof + text[hero_note.end():]

    # CSS locale della Home per il richiamo e l’ancora.
    if '.hero-proof{' not in text:
        css = ('\n.hero-proof{margin-top:18px;padding-top:15px;border-top:1px solid var(--line);display:flex;flex-wrap:wrap;gap:7px 14px;align-items:baseline;font-size:13px}'
               '.hero-proof a{color:var(--blue);font-weight:700;text-decoration:none}'
               '.hero-proof a:hover{text-decoration:underline}'
               '.hero-proof span{color:var(--muted);font-size:11px;letter-spacing:.02em}'
               '#testimonianze{scroll-margin-top:96px}'
               '.voice-summary{max-width:520px;margin:0 0 18px;color:var(--muted);font-size:15px;line-height:1.65}\n')
        text = text.replace('</style>', css + '</style>', 1)

    # Individua il blocco QSalute, lo rende semanticamente più chiaro e lo porta in alto.
    match = re.search(
        r'<section class="section warm"(?:[^>]*)><div class="container patient-voice">.*?</section>',
        text, re.I | re.S)
    if not match:
        return text

    block = match.group(0)
    text = text[:match.start()] + text[match.end():]

    block = re.sub(r'<section class="section warm"(?:[^>]*)>',
                   '<section class="section warm" id="testimonianze" aria-labelledby="testimonianze-title">',
                   block, count=1)
    block = block.replace(
        '<div class="kicker">Testimonianze sulla Neurochirurgia di Pisa</div><h2 style="font-size:46px">Il percorso raccontato dai pazienti.</h2>',
        '<div class="kicker">QSalute · sintesi delle testimonianze</div><h2 id="testimonianze-title" style="font-size:46px">Cosa raccontano i pazienti della Neurochirurgia di Pisa.</h2><p class="voice-summary">Una sintesi per temi ricorrenti: chiarezza, appropriatezza, relazione ed équipe.</p>')

    marker = '\n<section class="section soft">'
    if marker in text:
        text = text.replace(marker, '\n' + block + marker, 1)
    else:
        # Fallback prudente: reinserisce il blocco prima dell’area editoriale.
        text = text.replace('\n<section class="journal"', '\n' + block + '\n<section class="journal"', 1)
    return text


for path in PUBLIC_HTML:
    text = path.read_text(encoding="utf-8")
    text = add_second_opinion_to_nav(text, path)
    text = enforce_new_editorial_metadata(text, path)
    text = add_faq_schema(text, path)
    text = promote_qsalute_on_home(text, path)
    path.write_text(text, encoding="utf-8")

# I fallback HTML erano necessari soltanto durante GitHub Pages.
# Su Netlify devono restare assenti: i redirect HTTP sono definiti in _redirects.
for legacy in ("cvitae", "map", "rassegna-stampa", "calendario-appuntamenti"):
    fallback = ROOT / legacy / "index.html"
    if fallback.exists():
        fallback.unlink()

print("Manutenzione tecnica completata")
