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
