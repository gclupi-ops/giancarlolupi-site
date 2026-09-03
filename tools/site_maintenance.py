from pathlib import Path
import re, json

ROOT = Path(__file__).resolve().parents[1]


def footer(prefix=""):
    return f'''<footer>
  <div class="container">
    <div class="footer-grid">
      <div>
        <a class="brand" href="{prefix}index.html">
          <span class="monogram">GL</span>
          <span><strong>Giancarlo Lupi</strong><span>Neurochirurgo · MD PhD</span></span>
        </a>
        <p style="max-width:430px;margin-top:18px">Sito professionale personale dedicato a neurochirurgia, colonna vertebrale, informazione clinica e innovazione. I contenuti non sostituiscono la valutazione medica individuale.</p>
      </div>
      <div>
        <div class="footer-title">Navigazione</div>
        <p><a href="{prefix}medico.html">Il medico</a><br>
        <a href="{prefix}colonna.html">Colonna vertebrale</a><br>
        <a href="{prefix}neurochirurgia.html">Neurochirurgia</a><br>
        <a href="{prefix}approfondimenti.html">Approfondimenti</a><br>
        <a href="{prefix}sedi.html">Sedi e prenotazioni</a></p>
      </div>
      <div>
        <div class="footer-title">Visite</div>
        <p>Pisa · Ponsacco · Massa<br>
        <a href="{prefix}sedi.html">Recapiti e prenotazioni →</a></p>
        <p><a href="{prefix}privacy.html">Privacy e note informative</a></p>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year></span> Giancarlo Lupi. Tutti i diritti riservati.</span>
      <span>Sito professionale personale · indipendente dalle strutture presso cui viene svolta attività clinica</span>
    </div>
  </div>
</footer>'''


def replace_footer(path):
    text = path.read_text(encoding="utf-8")
    prefix = "../" if path.parent.name == "approfondimenti" else ""
    text = re.sub(r"<footer>.*?</footer>", footer(prefix), text, flags=re.S)
    text = text.replace('  "email":"g.lupi@ao-pisa.toscana.it",\n', '')
    text = text.replace('"email":"g.lupi@ao-pisa.toscana.it",', '')
    text = text.replace('g.lupi@ao-pisa.toscana.it', '')
    text = text.replace('Nessun cookie di profilazione nel prototipo', 'Sito professionale personale')
    path.write_text(text, encoding="utf-8")


for html in ROOT.rglob("*.html"):
    replace_footer(html)

# Privacy: testo definitivo coerente con l'attuale assenza di moduli/analytics.
privacy = ROOT / "privacy.html"
text = privacy.read_text(encoding="utf-8")
text = text.replace(
    '<section class="page-hero"><div class="container"><div class="breadcrumb"><a href="index.html">Home</a> / Privacy</div><div class="kicker">Note informative</div><h1>Privacy e utilizzo del sito.</h1><p>Pagina tecnica iniziale del prototipo. Prima della pubblicazione definitiva deve essere verificata e completata in base agli strumenti effettivamente attivati.</p></div></section>',
    '<section class="page-hero"><div class="container"><div class="breadcrumb"><a href="index.html">Home</a> / Privacy</div><div class="kicker">Note informative</div><h1>Privacy e utilizzo del sito.</h1><p>Informazioni essenziali sul funzionamento di questo sito professionale personale e sui servizi esterni collegati.</p></div></section>'
)
section = re.search(r'<section class="section"><div class="container prose">.*?</div></section>', text, re.S)
privacy_body = '''<section class="section"><div class="container prose">
<h2>Finalità informativa</h2>
<p>I contenuti hanno finalità informativa e divulgativa e non sostituiscono visita, diagnosi o indicazione terapeutica individuale.</p>
<h2>Dati personali</h2>
<p>Nella configurazione attuale il sito non contiene moduli di contatto, aree riservate, newsletter o sistemi per il caricamento di documentazione sanitaria. Le prenotazioni vengono effettuate tramite i recapiti delle strutture indicati nella pagina <a href="sedi.html">Sedi e prenotazioni</a>.</p>
<p>Per ragioni di riservatezza, non inviare spontaneamente referti, immagini diagnostiche o altri dati sanitari tramite recapiti non espressamente predisposti dalla struttura di riferimento.</p>
<h2>Cookie e analytics</h2>
<p>Il sito non utilizza cookie di profilazione né servizi analytics propri. Qualora in futuro venissero introdotti strumenti che comportino trattamento di dati personali o tracciamento, questa informativa verrà aggiornata prima della loro attivazione.</p>
<h2>Servizi e link esterni</h2>
<p>I collegamenti a siti di strutture sanitarie, Google Maps, WhatsApp e altre fonti esterne portano a servizi gestiti da soggetti terzi, ai quali si applicano le rispettive informative privacy e condizioni d'uso.</p>
<div class="callout"><strong>Aggiornamento.</strong> Informativa aggiornata il 3 settembre 2026. Il sito è professionale e personale e non costituisce un canale istituzionale dell'Azienda Ospedaliero-Universitaria Pisana o delle strutture private presso cui vengono svolte visite.</div>
</div></section>'''
if section:
    text = text[:section.start()] + privacy_body + text[section.end():]
privacy.write_text(text, encoding="utf-8")

# Sedi: orari Ponsacco e dati strutturati delle sedi di attività.
sedi = ROOT / "sedi.html"
text = sedi.read_text(encoding="utf-8")
wa = '<div class="contact-actions"><a class="contact-link" href="https://wa.me/393516216891" target="_blank" rel="noopener">Scrivi su WhatsApp ↗</a></div>'
if 'Orari della struttura: lun–ven 07:00–19:30' not in text:
    text = text.replace(wa, wa + '<div class="details">Orari della struttura: lun–ven 07:00–19:30 · sab 07:00–13:30</div>')

sedi_schema = {
  "@context":"https://schema.org",
  "@graph":[
    {"@type":"Physician","@id":"https://www.giancarlolupi.com/#physician","name":"Giancarlo Lupi","url":"https://www.giancarlolupi.com/","medicalSpecialty":"Neurosurgery","areaServed":["Pisa","Ponsacco","Massa"],"workLocation":[{"@id":"https://www.giancarlolupi.com/#san-rossore"},{"@id":"https://www.giancarlolupi.com/#usi-valdera"},{"@id":"https://www.giancarlolupi.com/#ponticello"}]},
    {"@type":"MedicalClinic","@id":"https://www.giancarlolupi.com/#san-rossore","name":"Casa di Cura San Rossore","address":{"@type":"PostalAddress","streetAddress":"Viale delle Cascine 152/F","postalCode":"56122","addressLocality":"Pisa","addressRegion":"PI","addressCountry":"IT"},"telephone":"+39 050 586217","url":"https://casadicurasanrossore.it/"},
    {"@type":"MedicalClinic","@id":"https://www.giancarlolupi.com/#usi-valdera","name":"USI Valdera-Ponsacco","address":{"@type":"PostalAddress","streetAddress":"Via di Gello 175","postalCode":"56038","addressLocality":"Ponsacco","addressRegion":"PI","addressCountry":"IT"},"url":"https://www.usi.it/le-sedi/ponsacco","contactPoint":{"@type":"ContactPoint","telephone":"+39 351 621 6891","contactType":"appointments","availableLanguage":"it"},"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"07:00","closes":"19:30"},{"@type":"OpeningHoursSpecification","dayOfWeek":"Saturday","opens":"07:00","closes":"13:30"}]},
    {"@type":"MedicalClinic","@id":"https://www.giancarlolupi.com/#ponticello","name":"Centro Medico Ponticello","address":{"@type":"PostalAddress","streetAddress":"Via Ponticello Sud 4","postalCode":"54100","addressLocality":"Massa","addressRegion":"MS","addressCountry":"IT"},"telephone":"+39 0585 41847","url":"https://centromedicoponticello.it/"}
  ]
}
text = re.sub(r'<script type="application/ld\+json">.*?</script>', '<script type="application/ld+json">\n'+json.dumps(sedi_schema, ensure_ascii=False, indent=2)+'\n</script>', text, count=1, flags=re.S)
sedi.write_text(text, encoding="utf-8")

# Home: storico editoriale e data del dato QSalute.
home = ROOT / "index.html"
text = home.read_text(encoding="utf-8")
text = text.replace('Area editoriale · aggiornamento settimanale','Area editoriale · archivio avviato il 3 settembre 2026 · aggiornamento settimanale')
text = text.replace('testimonianze pubblicate sulla pagina QSalute della Neurochirurgia di Pisa. Il numero dà contesto, non misura l\'efficacia clinica.','testimonianze pubblicate sulla pagina QSalute della Neurochirurgia di Pisa, dato rilevato il 3 settembre 2026. Il numero dà contesto, non misura l\'efficacia clinica.')
home.write_text(text, encoding="utf-8")

# Archivio editoriale: chiarisce la data di avvio senza retrodatare gli articoli.
archive = ROOT / "approfondimenti.html"
text = archive.read_text(encoding="utf-8")
text = text.replace('<div class="kicker">Area editoriale</div>', '<div class="kicker">Area editoriale · archivio avviato il 3 settembre 2026</div>', 1)
archive.write_text(text, encoding="utf-8")

# Dati strutturati di base del professionista sulle pagine principali.
physician_schema = {"@context":"https://schema.org","@type":"Physician","@id":"https://www.giancarlolupi.com/#physician","name":"Giancarlo Lupi","medicalSpecialty":"Neurosurgery","url":"https://www.giancarlolupi.com/","areaServed":["Pisa","Ponsacco","Massa"]}
for filename in ["index.html","medico.html","colonna.html","neurochirurgia.html","approfondimenti.html"]:
    path = ROOT / filename
    text = path.read_text(encoding="utf-8")
    pattern = r'<script type="application/ld\+json">\s*\{.*?"@type"\s*:\s*"Physician".*?</script>'
    if re.search(pattern, text, re.S):
        text = re.sub(pattern, '<script type="application/ld+json">\n'+json.dumps(physician_schema, ensure_ascii=False, indent=2)+'\n</script>', text, count=1, flags=re.S)
    path.write_text(text, encoding="utf-8")

# MedicalWebPage per gli articoli sanitari.
article_meta = {
  "mal-di-schiena-quando-preoccuparsi.html":("Mal di schiena: quando è un disturbo comune e quando richiede un approfondimento neurochirurgico?","Low back pain"),
  "risonanza-mal-di-schiena.html":("Risonanza magnetica e mal di schiena: vedere di più non significa sempre capire di più","Magnetic resonance imaging of the spine"),
  "robotica-neurochirurgia.html":("Robotica, navigazione e realtà aumentata nella chirurgia vertebrale: dove siamo davvero","Spine surgery technology")
}
for filename, (headline, about) in article_meta.items():
    path = ROOT / "approfondimenti" / filename
    text = path.read_text(encoding="utf-8")
    url = f"https://www.giancarlolupi.com/approfondimenti/{filename}"
    schema = {"@context":"https://schema.org","@type":"MedicalWebPage","@id":url+"#article","url":url,"headline":headline,"datePublished":"2026-09-03","dateModified":"2026-09-03","inLanguage":"it-IT","about":{"@type":"MedicalEntity","name":about},"author":{"@type":"Physician","@id":"https://www.giancarlolupi.com/#physician","name":"Giancarlo Lupi","medicalSpecialty":"Neurosurgery","url":"https://www.giancarlolupi.com/medico.html"},"medicalAudience":{"@type":"MedicalAudience","audienceType":"Patient"}}
    if '"@type": "MedicalWebPage"' not in text and '"@type":"MedicalWebPage"' not in text:
        text = text.replace('</head>', '<script type="application/ld+json">\n'+json.dumps(schema, ensure_ascii=False, indent=2)+'\n</script>\n</head>')
    path.write_text(text, encoding="utf-8")

# Fallback di migrazione per le principali URL Wix. Un vero 301 verrà impostato al cut-over del dominio.
redirects = {
  "cvitae":"/medico.html",
  "map":"/sedi.html",
  "rassegna-stampa":"/approfondimenti.html",
  "calendario-appuntamenti":"/sedi.html"
}
redirect_template = '''<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="robots" content="noindex"><link rel="canonical" href="https://www.giancarlolupi.com{target}"><meta http-equiv="refresh" content="0;url={target}"><title>Pagina spostata</title><script>location.replace({target_js});</script></head><body><p>La pagina è stata spostata. <a href="{target}">Continua</a>.</p></body></html>'''
for old, target in redirects.items():
    directory = ROOT / old
    directory.mkdir(exist_ok=True)
    (directory / "index.html").write_text(redirect_template.format(target=target, target_js=json.dumps(target)), encoding="utf-8")

(ROOT / "MIGRAZIONE-SEO.md").write_text('''# Migrazione SEO dal sito Wix\n\nURL principali rilevate sul sito precedente e destinazione prevista:\n\n- `/cvitae` → `/medico.html`\n- `/map` → `/sedi.html`\n- `/rassegna-stampa` → `/approfondimenti.html`\n- `/calendario-appuntamenti` → `/sedi.html`\n\nGitHub Pages non consente di configurare veri redirect HTTP 301 lato server. Le pagine fallback incluse nel repository evitano link morti, ma al passaggio del dominio è preferibile applicare veri 301 tramite un hosting/edge che li supporti.\n\nIl `sitemap.xml` è già predisposto sul dominio definitivo. Dopo il cut-over: inviare la sitemap in Google Search Console e controllare indicizzazione, canonical e pagine 404.\n''', encoding="utf-8")

print('Manutenzione completata')
