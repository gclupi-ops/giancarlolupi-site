# giancarlolupi.com

Sito professionale del Dott. Giancarlo Lupi, neurochirurgo.

## Pubblicazione

Il sito è statico ed è predisposto per GitHub Pages dalla root del branch `main`.

### Fase 1 — anteprima
Pubblicare da `main` / root mantenendo **temporaneamente** il dominio `www.giancarlolupi.com` ancora su Wix. In questa fase non va configurato il custom domain su GitHub Pages.

URL di anteprima previsto: `https://gclupi-ops.github.io/giancarlolupi-site/`.

### Fase 2 — passaggio del dominio
Solo dopo la verifica dell'anteprima:
1. configurare `www.giancarlolupi.com` come custom domain in GitHub Pages;
2. modificare i record web DNS su Wix senza toccare MX/TXT della posta;
3. verificare HTTPS e tutte le pagine;
4. annullare la pubblicazione del vecchio sito Wix;
5. disattivare il rinnovo del piano Wix mantenendo attivo il dominio.

## Struttura
- `index.html` — Home
- `medico.html` — profilo professionale
- `colonna.html` — colonna vertebrale
- `neurochirurgia.html` — aree neurochirurgiche
- `approfondimenti.html` — indice editoriale
- `approfondimenti/` — pillole cliniche e Neurochirurgia oggi
- `sedi.html` — sedi e prenotazioni
- `.nojekyll` — pubblicazione statica senza elaborazione Jekyll
- `robots.txt` e `sitemap.xml` — SEO di base

## Aggiornamenti editoriali

- Negli editoriali non mostrare tempi di lettura stimati (es. “9 minuti”): nella testata mantenere categoria e data.
Le pillole settimanali sono predisposte per aggiornare la Home e la sezione Approfondimenti mantenendo fonti scientifiche, tono divulgativo e call to action clinicamente appropriate.
