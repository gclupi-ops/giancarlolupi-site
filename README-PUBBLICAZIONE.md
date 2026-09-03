# Nuovo sito giancarlolupi.com – prototipo statico

## Che cos'è
Sito statico completo, senza Wix, senza database e senza dipendenze esterne obbligatorie.
Può essere pubblicato gratuitamente su GitHub Pages o Cloudflare Pages mantenendo `www.giancarlolupi.com`.

## Scelte già applicate
- Prenotazioni indirizzate alle segreterie delle strutture, non al cellulare personale.
- Recapiti verificati a settembre 2026:
  - San Rossore Pisa: 050 586217
  - USI Valdera-Ponsacco: 0583 495482
  - Centro Medico Ponticello Massa: 0585 41847, selezione 2
- Niente modulo di caricamento referti/documentazione sanitaria nella prima versione.
- Niente cookie di profilazione o analytics.
- Architettura editoriale: "Un minuto per la schiena" + "Neurochirurgia oggi".
- SEO di base: title, description, canonical, sitemap, robots.txt, dati strutturati Physician.

## Prima della pubblicazione definitiva
1. Sostituire l'illustrazione della home o affiancarla con un ritratto professionale recente.
2. Aggiornare e validare la biografia/CV 2026.
3. Decidere se il cellulare 347 7019405 debba restare completamente fuori dal sito o comparire solo come contatto secondario.
4. Verificare privacy/note legali con il professionista di riferimento.
5. Bonificare e deindicizzare il vecchio sottodominio `book.giancarlolupi.com` prima del passaggio.
6. Configurare Search Console dopo la migrazione.

## Pubblicazione gratuita – opzione consigliata
### Cloudflare Pages
- caricare questa cartella in un repository GitHub;
- creare un progetto Cloudflare Pages collegato al repository;
- impostare come directory di pubblicazione la root;
- aggiungere `www.giancarlolupi.com` come custom domain solo dopo la verifica dell’anteprima GitHub Pages;
- modificare i DNS solo quando il nuovo sito è pronto;
- mantenere il vecchio Wix attivo fino al cut-over finale.

### GitHub Pages
Funziona ugualmente per questo sito. Cloudflare Pages è preferibile per gestione DNS/CDN e redirect.

## Come aggiungere una pillola settimanale
1. Duplicare uno dei file nella cartella `/approfondimenti/`.
2. Aggiornare titolo, introduzione, testo, fonti e data.
3. Inserire la nuova card in `approfondimenti.html`.
4. Aggiungere la card più recente in `index.html`.
5. Aggiungere l'URL a `sitemap.xml`.

In una seconda versione si può automatizzare questo flusso con articoli in Markdown e pubblicazione automatica da GitHub.

## Testimonianze dei pazienti
È stata aggiunta una sezione sobria basata sulla lettura qualitativa delle recensioni pubblicate su QSalute per la Neurochirurgia dell'Ospedale di Pisa. Non vengono presentate come prova di efficacia, non vengono promessi risultati e non sono riportate citazioni selettive celebrative. La sezione sintetizza quattro temi ricorrenti: chiarezza, appropriatezza, accompagnamento e lavoro di équipe, con link alla fonte originale.

## Visual system v3 — settembre 2026
La grafica è stata riprogettata con criteri mutuati dai design system di grandi realtà internazionali, senza copiarne l'identità:
- gerarchia tipografica editoriale con Source Serif 4 per i titoli e Source Sans 3 per interfaccia e testo;
- palette ridotta: bianco, grafite, blu digitale accessibile, grigi freddi;
- contrasto dei colori principali conforme ai requisiti WCAG AA;
- card con bordi sottili e ombre minime, evitando l'estetica "centro medico commerciale";
- fotografia professionale reale nella home e nella pagina del medico;
- CTA primaria unica e riconoscibile;
- maggiore spazio bianco e griglia più ampia;
- footer istituzionale scuro;
- componenti editoriali coerenti per le rubriche settimanali.

### Nota font e privacy
La v3 carica Source Sans 3 e Source Serif 4 da Google Fonts per il prototipo. Prima della messa online in UE è opportuno decidere se mantenerli così oppure self-hostarli sul server per eliminare la richiesta a Google. I file font non sono inclusi nel pacchetto.
