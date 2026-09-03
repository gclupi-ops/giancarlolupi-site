# Migrazione SEO e hosting definitivo

## Stato attuale

Migrazione del dominio principale completata il **3 settembre 2026**.

- Hosting definitivo: **Netlify**
- Repository sorgente: `gclupi-ops/giancarlolupi-site`
- Branch: `main`
- Deploy Netlify: `https://musical-crumble-e96475.netlify.app/`
- Dominio canonico: `https://www.giancarlolupi.com/`
- Apex `https://giancarlolupi.com/` reindirizzato con 301 al dominio `www`
- HTTPS: certificato Let's Encrypt attivo per apex e `www`
- Google Search Console: proprietà Domain `giancarlolupi.com` verificata tramite TXT DNS
- Sitemap ufficiale: `https://www.giancarlolupi.com/sitemap.xml`, letta con successo da Google Search Console
- Il repository GitHub resta la sorgente unica del sito.

Netlify viene usato per CDN/HTTPS e per i redirect HTTP definiti nel file `_redirects`.

## URL Wix e destinazioni definitive

| Vecchio URL | Nuovo URL | Stato |
|---|---|---|
| `/` | `/` | invariato |
| `/cvitae` | `/cv-pubblicazioni.html` | 301 forzato |
| `/cvitae/` | `/cv-pubblicazioni.html` | 301 forzato |
| `/map` | `/sedi.html` | 301 forzato |
| `/map/` | `/sedi.html` | 301 forzato |
| `/rassegna-stampa` | `/rassegna-stampa.html` | 301 forzato |
| `/rassegna-stampa/` | `/rassegna-stampa.html` | 301 forzato |
| `/calendario-appuntamenti` | `/documentazione-clinica.html` | 301 forzato |
| `/calendario-appuntamenti/` | `/documentazione-clinica.html` | 301 forzato |

Le vecchie cartelle statiche `cvitae/`, `map/`, `rassegna-stampa/` e `calendario-appuntamenti/` sono state eliminate dal repository. Non devono essere ricreate: su Netlify potrebbero ombreggiare i redirect HTTP. Anche `tools/site_maintenance.py` è stato modificato per mantenerle assenti.

## Sottodomini `book`, `book2` e `m`

Nel 2025 Google aveva acquisito sitemap anomale sul sottodominio `book.giancarlolupi.com`, contenenti migliaia di URL estranei all'attività medica. Il 3 settembre 2026:

1. le sitemap spam sono state rimosse dal report Sitemap di Search Console;
2. è stata inviata in Search Console una richiesta di rimozione temporanea dell'intero prefisso `https://book.giancarlolupi.com/`;
3. i record DNS `book.giancarlolupi.com` e `book2.giancarlolupi.com`, entrambi diretti al precedente IP `81.88.62.4`, sono stati eliminati;
4. è stato eliminato anche il CNAME storico `m.giancarlolupi.com` verso Wix;
5. gli URL spam non vengono reindirizzati alla Home del sito principale.

**Scelta definitiva:** non viene mantenuto alcun sistema di prenotazione via web. Le visite vengono organizzate esclusivamente tramite i recapiti delle strutture indicati nella pagina `sedi.html`. Non ricreare `book`, `book2` o altri sottodomini di prenotazione senza una nuova decisione esplicita.

## DNS attuale rilevante

- `giancarlolupi.com` A → `75.2.60.5`
- `www.giancarlolupi.com` CNAME → `musical-crumble-e96475.netlify.app`
- TXT di verifica Google Search Console presente
- nameserver autorevoli ancora Wix
- `book`, `book2` e `m`: nessun record DNS

## Search Console

La proprietà Domain `giancarlolupi.com` è verificata. La sitemap ufficiale è stata letta correttamente e inizialmente rilevava 12 URL; dopo l'aggiunta delle pagine `seconda-opinione.html` e `rassegna-stampa.html` la sitemap contiene 14 URL e Google aggiornerà il conteggio al successivo recupero.

Mantenere il record TXT di verifica DNS. Monitorare nelle settimane successive:

- indicizzazione delle nuove pagine;
- sostituzione delle vecchie URL Wix tramite i 301;
- deindicizzazione del contenuto spam del vecchio `book`;
- eventuali URL storici/orfani non ancora mappati.

## File di produzione

- `_redirects`: canonicalizzazione hostname, chiusura del sottodominio Netlify e redirect forzati delle principali URL Wix.
- `_headers`: header di sicurezza Netlify.
- `sitemap.xml`: sitemap del nuovo sito con `lastmod`.
- `robots.txt`: riferimento alla sitemap definitiva.
- `404.html`: pagina di errore del sito.
- `tools/site_maintenance.py`: manutenzione tecnica coerente con Netlify; mantiene assenti i fallback statici, uniforma la voce “Seconda opinione” nel menu, i tempi di lettura e il markup FAQ.
- `.github/workflows/site-maintenance.yml`: esecuzione **solo manuale** (`workflow_dispatch`) per evitare regressioni automatiche.

## Controlli ancora da completare prima della chiusura definitiva di Wix

- verificare periodicamente i redirect 301 delle URL storiche;
- verificare indicizzazione di `seconda-opinione.html` e `rassegna-stampa.html`;
- monitorare la richiesta di rimozione di `book.giancarlolupi.com` fino a completamento;
- mantenere attivo il dominio e la zona DNS anche dopo l'eventuale disattivazione del piano del vecchio sito Wix.
