# Migrazione SEO e hosting definitivo

## Hosting

Hosting definitivo scelto: **Netlify**.

- Repository sorgente: `gclupi-ops/giancarlolupi-site`
- Branch: `main`
- Deploy di prova: `https://musical-crumble-e96475.netlify.app/`
- Dominio definitivo previsto: `https://www.giancarlolupi.com/`
- Il repository GitHub resta la sorgente unica del sito.

Netlify viene usato per CDN/HTTPS e per i redirect HTTP 301 definiti nel file `_redirects`.

## URL Wix pubblicamente rilevate e destinazioni

| Vecchio URL | Nuovo URL | Stato |
|---|---|---|
| `/` | `/` | invariato |
| `/cvitae` | `/cv-pubblicazioni.html` | 301 |
| `/cvitae/` | `/cv-pubblicazioni.html` | 301 |
| `/map` | `/sedi.html` | 301 |
| `/map/` | `/sedi.html` | 301 |
| `/rassegna-stampa` | `/approfondimenti.html` | 301 |
| `/rassegna-stampa/` | `/approfondimenti.html` | 301 |
| `/calendario-appuntamenti` | `/documentazione-clinica.html` | 301 |
| `/calendario-appuntamenti/` | `/documentazione-clinica.html` | 301 |

La tabella deriva dalle pagine Wix ancora pubblicamente raggiungibili/indicizzate e dalla navigazione del vecchio sito. Prima del cut-over va confrontata con gli URL presenti in Google Search Console, perché possono esistere URL storici o orfani non più collegati dal menu.

## Sottodominio `book.giancarlolupi.com`

Sono stati rilevati nei risultati dei motori di ricerca URL anomali/spam sul sottodominio `book.giancarlolupi.com` (prodotti estranei all'attività medica). Questo sottodominio **non deve restare collegato al vecchio hosting dopo la migrazione**.

Prima del cut-over:

1. verificare in Wix/DNS quale record genera `book.giancarlolupi.com`;
2. verificare se il sottodominio serve ancora a qualche funzione legittima;
3. se non serve, rimuovere o sostituire il relativo record DNS;
4. usare Google Search Console per richiedere la rimozione temporanea degli URL spam e monitorarne la deindicizzazione;
5. non redirigere in massa gli URL spam verso la Home principale, per evitare di trasferire segnali indesiderati al dominio principale.

## Sequenza di cut-over

1. Completare e collaudare il deploy Netlify.
2. Aggiungere in Netlify `www.giancarlolupi.com` come dominio personalizzato e impostarlo come dominio principale.
3. Aggiungere anche `giancarlolupi.com` come alias/apex e lasciare che Netlify lo rediriga al dominio principale.
4. Verificare Google Search Console come proprietà Domain `giancarlolupi.com` tramite record TXT DNS, senza modificare i record email.
5. Esportare/controllare gli URL indicizzati e completare `_redirects`.
6. Su Wix modificare solo i record web necessari per puntare il dominio a Netlify; **non toccare MX, SPF, DKIM, DMARC o altri record email**.
7. Verificare HTTPS, canonical, sitemap, robots.txt, redirect 301 e pagina 404.
8. Inviare `https://www.giancarlolupi.com/sitemap.xml` in Search Console.
9. Monitorare copertura, indicizzazione e vecchi URL per almeno alcune settimane.
10. Solo dopo la verifica completa, rendere offline il vecchio sito Wix e disattivare il rinnovo del piano sito, mantenendo attivo il dominio.

## File già predisposti

- `_redirects`: redirect 301 dalle principali URL Wix.
- `_headers`: header di sicurezza Netlify.
- `sitemap.xml`: sitemap del nuovo sito.
- `robots.txt`: riferimento alla sitemap definitiva.
- `404.html`: pagina di errore del sito.

## Controlli dopo il passaggio

Verificare almeno:

- Home e navigazione desktop/mobile;
- `/cvitae` → `/cv-pubblicazioni.html` con 301;
- `/map` → `/sedi.html` con 301;
- `/rassegna-stampa` → `/approfondimenti.html` con 301;
- `/calendario-appuntamenti` → `/documentazione-clinica.html` con 301;
- canonical HTTPS su `www.giancarlolupi.com`;
- sitemap e robots;
- assenza di errori 404 inattesi;
- funzionamento di telefono, WhatsApp, Google Maps e siti esterni;
- funzionamento della posta elettronica dopo il cambio DNS;
- stato del sottodominio `book.giancarlolupi.com` e deindicizzazione degli URL spam.
