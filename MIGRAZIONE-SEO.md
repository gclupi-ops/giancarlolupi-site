# Migrazione SEO dal sito Wix

URL principali rilevate sul sito precedente e destinazione prevista:

- `/cvitae` → `/medico.html`
- `/map` → `/sedi.html`
- `/rassegna-stampa` → `/approfondimenti.html`
- `/calendario-appuntamenti` → `/sedi.html`

GitHub Pages non consente di configurare veri redirect HTTP 301 lato server. Le pagine fallback incluse nel repository evitano link morti, ma al passaggio del dominio è preferibile applicare veri 301 tramite un hosting/edge che li supporti.

Il `sitemap.xml` è già predisposto sul dominio definitivo. Dopo il cut-over: inviare la sitemap in Google Search Console e controllare indicizzazione, canonical e pagine 404.
