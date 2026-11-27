# Piano editoriale novembre–dicembre 2026

Approvato da Gian il 3 novembre 2026, con recupero dell'uscita del 30 ottobre e controllo delle duplicazioni su tutto il sito. Per questo ciclo non occorre una nuova scelta fra tre temi. La qualità clinica e la verifica del deploy restano necessarie a ogni uscita.

## Regola permanente

Le domande documentate dei pazienti e dei familiari guidano i contenuti. Le novità scientifiche aggiornano la risposta. Prima di ogni uscita leggere i testi correnti dell'archivio, le FAQ e le pagine cliniche pertinenti, non soltanto i titoli. Registrare: domanda, pagine già pertinenti, risposta già disponibile, elemento aggiuntivo, fonte della domanda e fonti cliniche. Se la risposta esiste già, aggiornare la pagina e mantenere il suo URL: non creare una seconda pagina con un titolo diverso. Se il nuovo dubbio è circoscritto e autonomo, scrivere un approfondimento e collegare i contenuti in entrambe le direzioni. Non ripetere lunghi preamboli su indicazioni e tecniche già spiegate.

Fonti dei quesiti: consulti pubblici sintetizzati senza dettagli identificativi e studi sui bisogni informativi. Non utilizzare le risposte dei forum come prova clinica; non attribuire agli autori coperture assicurative sconosciute. Riscontri di metodo: PMID 30172898, 36866445, 36580586. Il perimetro assicurativo orienta la pertinenza alla casa di cura, senza sezioni assicurative obbligatorie né promesse di rimborso.

## Calendario operativo

| Uscita editoriale | Contenuto | Modalità e novità |
|---|---|---|
| 30 ottobre, recupero il 3 novembre | Difficoltà a deglutire dopo chirurgia cervicale: decorso e segnali da controllare | Nuova pagina `approfondimenti/disfagia-dopo-chirurgia-cervicale.html`; la disfagia era soltanto menzionata negli articoli del 9 e 23 ottobre. Pubblicazione effettiva 3 novembre; verificarne commit e deploy. |
| 6 novembre | Collare dopo chirurgia cervicale: perché le indicazioni cambiano e come concordarne la sospensione | Precisazione specifica del recupero cervicale. Non ripetere ACDF/protesi/foraminotomia. Distinguere collare morbido/rigido, procedure e stabilità; nessuna sospensione autonoma né calendario universale. |
| 13 novembre | Il dolore è diminuito, ma formicolio e debolezza restano: come si valuta il recupero del nervo | Approfondimento di un breve passaggio già presente. Distinguere radice e midollo, sintomo preesistente e deficit nuovo, dolore e funzione. |
| 20 novembre | Dolore dopo artrodesi lombare: quando sospettare una mancata fusione e quando cercare altre cause | Nuova domanda rispetto alla guida sul ricovero: consolidamento biologico, correlazione dolore/imaging e prudenza prima di una revisione. |
| 27 novembre | La sciatica è tornata dopo l'intervento: recidiva, cicatrice o un problema diverso? | Percorso post-discectomia; non ripetere storia naturale dell'ernia primaria né guida alle infiltrazioni. |
| 4 dicembre | Idrocefalo normoteso: che cosa può migliorare davvero con una derivazione | Tema soltanto accennato in Neurochirurgia: selezione e risultati separati per cammino, cognizione e continenza. |
| 11 dicembre | Ernia dorsale: perché tempi e rischi non sono quelli di un'ernia lombare | Nessun articolo specifico precedente: midollo, sede/calcificazione, indicazione e accesso senza classifiche universali. |
| 18 dicembre | Vivere con una derivazione liquorale: controlli, valvola e sintomi da non ignorare | Fase successiva all'intervento, separata dall'articolo del 4 dicembre; istruzioni RM verificate per dispositivo. |
| 25 dicembre | Dimissione dopo artrodesi lombare: scheda pratica per paziente e familiare | **Aggiornamento della pagina del 19 ottobre**, non nuova guida generica. Conservare URL e datePublished, aggiornare dateModified, Home, voce archivio e sitemap. Aggiungere schema personalizzabile dei recapiti e delle istruzioni da concordare senza prescrizioni standard. |

Il collare occupa il 6 novembre perché la disfagia viene anticipata al recupero del 30 ottobre; le altre date approvate rimangono invariate. Le uscite future non sono già pubblicate. A fine ciclo, senza ulteriori decisioni di Gian, tornare alle tre proposte con scelta esplicita; non proseguire un calendario non concordato.

## Verifica dell'uscita del 30 ottobre

Prima del recupero, `main` e produzione corrispondevano al commit `483af74198d8b39a04b825afd0853a5ac0616c4f`, pubblicato il 23 ottobre 2026 alle 12:24 UTC. Il deploy `6adb51dce75b2c9b948041ad` era `ready`, contesto production. Non risultavano nuovi commit del 30 ottobre.

Il risultato registrato dell'automazione editoriale del 30 ottobre conteneva tre proposte con fonti: disfagia dopo ACDF; consolidamento dopo artrodesi; valvole e iperdrenaggio nell'idrocefalo normoteso. Chiedeva una scelta prima di scrivere. Il controllo delle 15 aveva registrato attesa della scelta. Questi elementi spiegano l'assenza dell'uscita senza indicare un fallimento del deploy. Non dimostrano che la notifica sia stata ricevuta o letta.

## Inventario e sovrapposizioni rilevate il 3 novembre

Audit della versione corrente: tutti i 25 file HTML del repository, compresi 13 approfondimenti, Home, archivio, pagine cliniche, FAQ, seconda opinione, documentazione, profilo/CV, rassegna, sedi, privacy e 404; sitemap e cronologia recente. Non è una revisione integrale della correttezza clinica di tutte le citazioni storiche né di versioni archiviate esternamente.

| Pagina in /approfondimenti/ | Risposta già disponibile | Decisione per il nuovo ciclo |
|---|---|---|
| ernia-cervicale-fusione-protesi-foraminotomia.html | Indicazioni, alternative, studi comparativi, rischi e breve richiamo a disfagia, collare e deficit residui | Collegare per le basi; sviluppare soltanto i quesiti postoperatori specifici. |
| artrodesi-lombare-posteriore-intervento-recupero.html | Impianti, preparazione, degenza, dimissione, attività, riabilitazione, lavoro, rischi e domande | Non duplicare il recupero generale. Il 20/11 riguarda dolore e pseudoartrosi; il 25/12 integra questa stessa pagina. |
| mielopatia-cervicale-quando-operare.html | Segni midollari, gravità, tempi, tecniche, recupero incompleto, rischi anteriore/posteriore | Non riscrivere quando operare; il 13/11 distingue recupero radicolare e midollare con link. |
| stenosi-canale-lombare-sintomi-quando-operare.html | Claudicatio, diagnosi differenziale vascolare, RM, terapia, decompressione e fusione | Guida di riferimento; evitare nuovo articolo generico sulla stenosi. |
| stenosi-lombare-chirurgia-mini-invasiva.html | Confronti degli accessi, limiti, selezione, rapporto fra decompressione e stabilità | Non riproporre mini-invasività come tema autonomo nel ciclo. |
| sciatica-infiltrazioni-benefici-durata.html | Tipo di infiltrazione, benefici, durata, limiti, rischi e alternative chirurgiche | La recidiva postoperatoria del 27/11 deve affrontare diagnosi e rivalutazione specifiche. |
| ernia-lombare-gigante-chirurgia-o-attesa.html | Storia naturale, riassorbimento, dimensione RM, conservativo e urgenze | Non ripetere ernia primaria; distinguere recidiva e anatomia dorsale. |
| mal-di-schiena-quando-preoccuparsi.html | Valutazione generale, red flags, ruolo clinico e RM | Collegare quando pertinente, senza altro articolo generale sulle urgenze. |
| risonanza-mal-di-schiena.html | Reperti asintomatici, concordanza, esami che cambiano la gestione | Negli articoli nuovi descrivere solo il quesito specifico dell'esame postoperatorio. |
| intelligenza-artificiale-risonanza-colonna.html | Acquisizione e interpretazione, validazione e limiti della tecnologia | Fuori dal ciclo attuale; non usare una novità tecnologica per ripetere il tema. |
| robotica-neurochirurgia.html | Guida delle viti, accuratezza, radiazioni e outcome | Fuori dal ciclo attuale. |
| aneurisma-cerebrale-scoperto-per-caso.html | Rischio, crescita, sorveglianza e trattamento | Non riproporre una guida generale; diverso dal perimetro concordato. |
| embolizzazione-meningea-media-ematoma-subdurale-cronico.html | Trial MMAE, recidive, selezione e ruolo rispetto a chirurgia | Non duplicare; i subdurali nello shunt vanno spiegati nel diverso contesto clinico. |

`colonna.html` copre già indicazioni generali e FAQ su RM, urgenze, fusione, tempi e seconda opinione. `neurochirurgia.html` copre le basi di idrocefalo, tumori, vascolare e trigemino: per l'idrocefalo mancano approfondimenti dedicati su selezione e vita con shunt. `seconda-opinione.html` e `documentazione-clinica.html` rispondono già a quando chiedere un parere e cosa portare. Home e archivio devono presentare l'uscita senza ripetere l'articolo per intero. Profilo, CV, rassegna e sedi svolgono funzioni informative diverse e non sono nuovi temi da riscrivere.

## Scheda di ricerca del recupero del 30 ottobre

- Domanda del paziente: difficoltà a deglutire dopo accesso cervicale anteriore, timore che sia un segno di problema.
- Riscontro pubblico: [quesito MioDottore](https://www.miodottore.it/domande-risposte/buongiorno-sono-stato-operato-da-11-giorni-di-artrodesi-cervicale-con-accesso-anteriore-c5-c6-da-do); fonte usata per il bisogno informativo, non per le risposte terapeutiche.
- Riscontro di metodo: [bisogni informativi in chirurgia spinale, PMID 30172898](https://pubmed.ncbi.nlm.nih.gov/30172898/).
- Fonti cliniche: PMID 41452954 (134 pazienti, 67 cervicali), 38369769 (130), 38157009 (21, videofluoroscopia), 42359471 (umbrella review, 31/32 revisioni di affidabilità criticamente bassa), 38657173 e 24436882; CUH/NHS per indicazioni ai pazienti.
- Limiti: studi prospettici piccoli, esiti e tempi differenti; abstract verificati, nessuna pretesa di lettura integrale dei full text non acquisiti. La percentuale di sintomi non equivale a complicanza grave. Nessuna soglia universale di durata, autodiagnosi o trattamento farmacologico standard.
- Novità: percorso di valutazione della deglutizione, andamento, sicurezza del pasto, accesso a rivalutazione. Nessuna ripetizione del confronto chirurgico del 23 ottobre.

## Fonti iniziali per il 6 novembre

Domande documentate: [quanto tenere il collare anche la notte](https://www.miodottore.it/domande-risposte/avendo-dovuto-fare-un-intervento-x-cervicobrachialgia-vertebra-c5-e-ci-x-quanto-tempo-va-tenut); [quando togliere il collare dopo discectomia](https://www.medicitalia.it/consulti/neurochirurgia/297297-esiti-discectomia-cervicale.html). Le risposte dei consulti non costituiscono fonti cliniche.

Ricerca clinica da aggiornare alla redazione: [RCT su ACDF strumentata a uno/due livelli, PMID 29456914](https://pubmed.ncbi.nlm.nih.gov/29456914/); [meta-analisi 2024, PMID 38454504](https://pubmed.ncbi.nlm.nih.gov/38454504/); [revisione 2024, PMID 39283966](https://pubmed.ncbi.nlm.nih.gov/39283966/). Non estendere dati su ACDF degenerativa selezionata a fratture, instabilità, procedure posteriori complesse o ogni tipo di impianto. Non suggerire di togliere un collare prescritto sulla base del solo articolo.

## Pubblicazione e monitoraggio

Per ogni data preparare una nuova pagina soltanto se il dubbio non è già risolto; il 25 dicembre aggiornare l'URL esistente. Aggiornare Home, archivio e sitemap coerentemente, con una sola voce per URL. Mantenere la data reale di prima pubblicazione; usare dateModified per integrazioni sostanziali e indicare visibilmente che cosa è stato aggiornato. L'uscita editoriale arretrata non retrodata la pubblicazione.

Creare un commit coerente su main e verificare produzione Netlify (site ID 76071065-2f40-4cb4-8690-a8ab6b9f6cdd), stato ready e commit pertinente. Non dichiarare pubblicato sulla sola presenza dei file GitHub. Monitor: non richiedere tre proposte per il calendario approvato; segnalare il punto preciso mancante o fallito e la versione online; non generare allarme se il lavoro è in corso. Non modificare DNS, dominio o convenzioni.


## Scheda di ricerca e pubblicazione del 6 novembre

- **Domanda:** dopo chirurgia cervicale, per quanto tempo va tenuto il collare, anche di notte, e come si decide quando sospenderlo?
- **Riscontri pubblici:** quesito MioDottore su durata e notte; consulto Medicitalia sulla sospensione dopo discectomia. Le risposte online non sono state usate come prova clinica.
- **URL esistenti pertinenti:** `ernia-cervicale-fusione-protesi-foraminotomia.html` conteneva soltanto il richiamo a un calendario individuale; `disfagia-dopo-chirurgia-cervicale.html` e `mielopatia-cervicale-quando-operare.html` trattavano problemi diversi.
- **Risposta già data:** uso del collare dipendente da procedura, estensione, decorso e indicazioni del chirurgo; nessuna spiegazione di collare morbido/rigido, notte, cura della pelle o sospensione.
- **Elemento aggiuntivo:** finalità del dispositivo, evidenza dopo ACDF selezionata e laminoplastica, limiti dell'estrapolazione a trauma/instabilità, gestione pratica e criteri di sospensione concordata.
- **Modalità:** nuova pagina `approfondimenti/collare-dopo-chirurgia-cervicale.html`, con collegamento reciproco dalla guida sulle opzioni chirurgiche.
- **Fonti cliniche principali:** PMID 29456914, 38454504, 39283966, 27879567, 30113664, 35333123; documento istituzionale CUH per cura del collare rigido.
- **Limiti:** campioni piccoli, procedure e dispositivi eterogenei, pochi trial; prove su ACDF degenerativa a uno/due livelli non applicabili a fratture, instabilità o ricostruzioni complesse. Il full text della meta-analisi 2024 è stato consultato; per alcune fonti è stato verificato l'abstract PubMed.
- **QSalute:** 141 testimonianze, dato verificato il 6 novembre 2026; invariato rispetto alla Home, quindi nessuna modifica.
- **Data editoriale e prima pubblicazione:** 6 novembre 2026.


## Scheda di ricerca e pubblicazione del 13 novembre

- **Domanda:** il dolore al braccio è diminuito, ma formicolio e debolezza persistono: è un recupero lento, un deficit residuo o un problema da rivalutare?
- **Riscontri pubblici:** [quesito MioDottore su ricomparsa di dolore e formicolio dopo chirurgia cervicale](https://www.miodottore.it/domande-risposte/buonasera-sono-stato-operato-dicembre-2024-discectomia-con-rimozione-completa-disco-e-inserimento); [discussione pubblica Mayo Clinic Connect](https://connect.mayoclinic.org/discussion/laminectomy-cervical-with-fusion-and-instrumentation-1-4-levels/?pg=3) sul diverso andamento di dolore, debolezza e sensibilità. Usati per individuare il bisogno informativo, non come prova clinica. Riscontro di metodo: [PMID 30172898](https://pubmed.ncbi.nlm.nih.gov/30172898/) sui bisogni informativi in chirurgia spinale.
- **URL esistenti pertinenti:** `ernia-cervicale-fusione-protesi-foraminotomia.html` descriveva in una frase il possibile recupero lento o incompleto; `mielopatia-cervicale-quando-operare.html` distingueva radice e midollo e ricordava che forza, cammino e parestesie non migliorano necessariamente insieme; `colonna.html` citava esame neurologico, RM ed elettrofisiologia in termini generali.
- **Risposta già data:** dolore, disturbo sensitivo e debolezza possono avere tempi diversi; il recupero può essere incompleto, soprattutto dopo compressione protratta. Mancavano confronto con il deficit preoperatorio, traiettoria seriale, ruolo e limiti di RM/TC/EMG e criteri per anticipare la rivalutazione.
- **Elemento aggiuntivo:** distinzione fra sintomo preesistente e deficit nuovo, radicolopatia e mielopatia; valutazione seriale di forza, sensibilità, destrezza, cammino e riflessi; uso mirato di imaging ed elettrodiagnostica; segnali urgenti; dati, interpretazione e opinione professionale separati.
- **Modalità:** nuova pagina `approfondimenti/formicolio-debolezza-dopo-chirurgia-cervicale.html`, perché il dubbio postoperatorio è autonomo; collegamenti reciproci dalle guide su radicolopatia e mielopatia. Nessuna duplicazione delle indicazioni o delle tecniche chirurgiche.
- **Fonti cliniche principali:** PMID 42184389 (616 pazienti dopo ACDF), 40955710 (sensibilità dopo chirurgia per DCM, coorte multicentrica), 42379939 (traiettorie dopo chirurgia per DCM, 935 pazienti), 24494180 (recupero neurologico dopo ACDF monolivello), ACR Appropriateness Criteria 2024 per imaging dopo chirurgia cervicale, AANEM PMID 16921635 per EMG, indicazioni CUH sul recupero postoperatorio.
- **Limiti:** evidenza prevalentemente osservazionale; diagnosi, procedure e misure eterogenee; tempi medi non applicabili al singolo paziente. Gli abstract PubMed sono stati verificati per gli studi clinici; documento ACR e indicazioni CUH consultati online. Nessun automatismo fra parestesie persistenti e compressione residua, né fra impianto e causa del deficit.
- **QSalute:** 141 testimonianze, dato pubblico verificato il 13 novembre 2026; invariato, quindi nessuna modifica alla Home.
- **Data editoriale e prima pubblicazione:** 13 novembre 2026.


## Scheda di ricerca e pubblicazione del 20 novembre

- **Domanda documentata:** dolore persistente o ricomparso dopo artrodesi lombare; il paziente chiede se l'osso sia consolidato, se serva TC e se una mancata fusione implichi una revisione.
- **Riscontri pubblici, usati solo per identificare il bisogno:** [consulto Medicitalia su intorpidimento dopo artrodesi lombare](https://www.medicitalia.it/consulti/neurochirurgia/937217-intorpidimento-dopo-artrodesi-lombare.html) e [quesito MioDottore su dolore persistente dopo fusione L5-S1, RM non conclusiva e rivalutazione](https://www.miodottore.it/domande-risposte/buongiorno-dottore-volevo-un-suo-consulto-per-quando-riguarda-la-mia-situazione-ho-fatto-l-interven). Due fonti indipendenti; sintesi senza dettagli identificativi. Le risposte online non sono prove cliniche.
- **Riscontro sui bisogni informativi:** [Renovanz et al., PMID 30172898](https://pubmed.ncbi.nlm.nih.gov/30172898/), question prompt list validata in 118 pazienti di chirurgia spinale, con prognosi/follow-up fra i bisogni non soddisfatti; [analisi delle domande online, PMID 37214263](https://pubmed.ncbi.nlm.nih.gov/37214263/), documenta interesse per valutazione e dettagli tecnici. Questi studi orientano la comunicazione, non stimano la prevalenza del dubbio.
- **URL pertinenti esistenti:** approfondimenti/artrodesi-lombare-posteriore-intervento-recupero.html tratta già indicazione, preparazione, degenza, recupero, riabilitazione, lavoro, rischi e menziona pseudoartrosi; approfondimenti/risonanza-mal-di-schiena.html spiega concordanza clinico-radiologica e reperti incidentali; colonna.html tratta valutazione neurologica e imaging in generale.
- **Risposta già presente:** l’artrodesi richiede mesi per consolidare e la pseudoartrosi è una complicanza; non erano spiegati in dettaglio il significato di dolore persistente/ricorrente, diagnosi differenziale post-fusione, selezione degli esami, limiti della TC e criteri di revisione.
- **Elemento aggiuntivo:** distinzione fra dolore, non-union radiologica e fallimento clinico; cause alternative; percorso clinico e scelta mirata di radiografie, TC, RM, laboratorio o SPECT/TC; limiti diagnostici; indicazioni e aspettative della revisione.
- **Modalità:** nuova pagina approfondimenti/dolore-dopo-artrodesi-lombare-pseudoartrosi.html, con collegamenti reciproci alla guida sul recupero dopo artrodesi. Non duplica il percorso generale postoperatorio.
- **Fonti cliniche principali:** ACR Appropriateness Criteria Low Back Pain, 2021 update (variant 5); Peters et al., meta-analisi diagnostica 2019, PMID 30796507; González-Gallardo et al., revisione sistematica 2025, DOI 10.1177/21925682251336715; Peng & Pao, revisione narrativa TC 2026, PMID 41515634; Boonsirikamchai et al., meta-analisi fattori di rischio 2024, PMID 38831392; Issa et al., outcomes revisione 2024, DOI 10.1007/s00586-024-08358-8; Adogwa et al., coorte 2011, PMID 21699473.
- **Limiti:** studi diagnostici con campioni chirurgicamente selezionati, criteri radiologici non uniformi e rischio di bias; la revisione 2026 è narrativa. I risultati sulle revisioni derivano da coorti retrospettive e selezionate e non garantiscono outcome individuali. ACR, review 2025/2026, meta-analisi diagnostica 2019, meta-analisi dei fattori di rischio 2024 e studio Issa 2024 sono stati consultati nel full text; per Adogwa 2011 è stato consultato l'abstract PubMed. Le domande pubbliche sono state sintetizzate, senza usarne le risposte come prova.
- **QSalute:** 141 testimonianze, verificato il 20 novembre 2026; invariato. La Home mantiene il numero e aggiorna la data di verifica.
- **Data editoriale e prima pubblicazione:** 20 novembre 2026.
- **Pubblicazione verificata:** commit articolo e correzioni `5c85bc85fdb2ec07b41a03ee35e06dd2a5c5faea`; deploy Netlify `6afff5cbb5bcd66ff8f7b3c7` `ready`, production, associato esattamente al commit. Netlify conferma la nuova pagina nei file generati; il browser web non è riuscito a recuperare direttamente gli URL in questo run.


## Scheda di ricerca e pubblicazione del 27 novembre

- **Domanda del paziente:** dopo una discectomia lombare il dolore sciatico è tornato, oppure non è mai scomparso del tutto: si tratta di una nuova ernia, di cicatrice, di materiale residuo o di un problema diverso?
- **Riscontri pubblici del bisogno informativo:** [consulto Medicitalia sulla ricomparsa immediata dopo microdiscectomia L5-S1](https://www.medicitalia.it/consulti/neurochirurgia/609634-sciatica-ernia-lombare.html) e [quesito MioDottore su dolore e possibile tessuto fibro-cicatriziale dopo microdiscectomia](https://www.miodottore.it/domande-risposte/operato-il-24-4-18-di-ernia-l5-s1-dopo-piu-di-5-mesi-avverto-sempre-dolore-coscia-sx-e-gluteo-sx-con). Due piattaforme indipendenti; domande sintetizzate senza dettagli identificativi. Le risposte dei consulti non sono state usate come prova clinica e non consentono di stimare la prevalenza del problema.
- **Riscontri sui bisogni informativi:** [Renovanz et al., PMID 30172898](https://pubmed.ncbi.nlm.nih.gov/30172898/), question prompt list validata in 118 pazienti di chirurgia spinale, con prognosi e follow-up fra le aree di bisogno informativo; [Kasthuri et al., PMID 37214263](https://pubmed.ncbi.nlm.nih.gov/37214263/), analisi di 576 domande online sulla chirurgia spinale, con frequenza di quesiti su dettagli tecnici, valutazione dell'intervento e restrizioni. Sono studi sui bisogni comunicativi, non sulla frequenza della recidiva.
- **URL pertinenti letti integralmente:** `approfondimenti/sciatica-infiltrazioni-benefici-durata.html` spiega indicazioni, benefici e limiti delle epidurali ma non la diagnosi differenziale dopo discectomia; `approfondimenti/ernia-lombare-gigante-chirurgia-o-attesa.html` tratta storia naturale e trattamento dell'ernia primaria, non la recidiva postoperatoria; `approfondimenti/risonanza-mal-di-schiena.html` spiega la concordanza clinico-radiologica in generale; `approfondimenti/mal-di-schiena-quando-preoccuparsi.html` tratta i segnali d'allarme generali; `colonna.html` contiene FAQ su sciatica e urgenze ma non sul dolore ricomparso dopo discectomia; `seconda-opinione.html` e `documentazione-clinica.html` spiegano quando chiedere un parere e cosa portare.
- **Risposta già presente:** la guida sulle infiltrazioni tratta la sciatica primaria e il ruolo antalgico; la guida sull'ernia grande tratta la decisione conservativa o chirurgica prima del primo intervento. Le pagine generali ricordano concordanza clinico-radiologica e red flags. Nessuna risponde in modo specifico alla distinzione fra dolore persistente, residuo discale, vera recidiva, fibrosi epidurale e nuova causa.
- **Elemento aggiuntivo:** definizione operativa di recidiva; intervallo libero dal dolore senza soglia temporale universale; diagnosi differenziale; confronto delle immagini pre/postoperatorie; indicazioni e limiti della RM con e senza contrasto; scelta fra trattamento conservativo, revisione discale e fusione senza automatismi; complicanze e aspettative dopo revisione.
- **Modalità scelta:** nuovo approfondimento autonomo `approfondimenti/sciatica-ricomparsa-dopo-discectomia.html`. Collegamenti reciproci dalla guida sulle infiltrazioni, dalla guida sull'ernia lombare primaria e dalla FAQ di `colonna.html`. Non è stata modificata la guida sulle infiltrazioni perché il suo tema resta distinto.
- **Fonti cliniche principali:** Harhangi et al., Global Spine Journal 2026, studio internazionale su 510 specialisti, full text consultato; ACR Appropriateness Criteria Low Back Pain, Variant 5, consultata la tabella ufficiale; Passavanti et al., Skeletal Radiology 2020, abstract PubMed consultato; Zileli et al., WFNS Spine Committee recommendations 2024, full text consultato; Rucker et al., meta-analisi 2026 su 10 studi e 939 pazienti, consultato abstract PubMed soltanto; Samir et al., meta-analisi 2025/2026 su 25 studi e 1.031.348 pazienti, full text consultato.
- **Limiti:** il consenso del 2026 è evidenza di livello V, con campionamento non probabilistico e senza tasso di risposta calcolabile; la meta-analisi Rucker comprende pochi studi e non riporta in modo uniforme il timing, con consultazione del solo abstract; lo studio Passavanti valuta la concordanza diagnostica di due lettori e non fornisce un test infallibile; le stime di reintervento non equivalgono a incidenza di recidiva vera. La WFNS è una raccomandazione di consenso basata su letteratura eterogenea, non una linea guida con prove di alta certezza.
- **QSalute:** 141 testimonianze, numero pubblico verificato il 27 novembre 2026; invariato rispetto alla rilevazione precedente. Nessuna modifica al dato o alla data in Home.
- **Data editoriale:** 27 novembre 2026. **Data della prima pubblicazione effettiva:** non ancora verificata; `datePublished` è stato lasciato fuori dai dati strutturati fino alla conferma del deploy production.
- **File aggiornati:** nuova pagina, Home, archivio, sitemap, `colonna.html`, guida su infiltrazioni, guida su ernia lombare primaria e questo registro.
- **Controllo archivio:** la nuova guida compare una sola volta come articolo in evidenza; non è stata duplicata nella lista cronologica. La Home mostra abstract e fonti; il conteggio QSalute resta invariato.
- **Stato di pubblicazione:** i file sono presenti su `main` con commit finale `e858f34b0231dd8a51e722b9f054650c31e3824f`. La verifica Netlify non è stata possibile in questa esecuzione non interattiva: gli strumenti Netlify hanno richiesto autorizzazione interattiva. Il recupero web dell’URL nuovo non è riuscito e la Home pubblica consultabile mostrava ancora la sezione editoriale del 13 novembre. Pertanto la pagina non viene dichiarata pubblicata; verificare il deploy production prima di aggiungere `datePublished` e la data effettiva.
