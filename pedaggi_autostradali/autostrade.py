# # Testo d'esame "Pedaggi autostradali"

# Un file `pedaggi.txt` riporta, uno per riga, la lista completa dei caselli di una determinata autostrada con il relativo
# pedaggio, nel formato:

# 	casello1;casello2;pedaggio

# dove `casello1` e `casello2` sono due stringhe che rappresentano rispettivamente il casello di entrata e quello di uscita di
# una tratta autostradale, mentre `pedaggio` è un numero reale che rappresenta il costo del relativo pedaggio. Le tratte
# autostradali sono riportate in ordine sparso e non consecutivo. Ovvero, se una riga (ad esempio) riporta il pedaggio
# della tratta tra Torino e Chivasso, non è detto che la riga successiva riporti la tratta da Chivasso al casello
# successivo. Si assuma che il file non sia vuoto e che sia privo di errori di formato o ambiguità (ad esempio, non è
# possibile che lo stesso casello di entrata compaia più volte associato a diversi caselli di uscita, e viceversa).

# Un secondo file `percorsi.txt` riporta una lista di percorsi, uno per riga, nel formato:

# 	partenza;destinazione

# dove `partenza` e `destinazione` sono due stringhe che rappresentano il punto di partenza e il punto di destinazione di un
# percorso. Anche in questo caso, si assuma che il file sia privo di errori di formato.

# Si scriva un programma Python che:

# 1. per ciascun percorso del file `percorsi.txt`, stabilisca se la destinazione è raggiungibile mediante l'autostrada
#    in questione. Cioè, stabilisca se esiste una successione di tratte consecutive che ha come primo ingresso il punto di
#    partenza e come ultima uscita il punto di destinazione. Se questa successione di tratte esiste, occorre stampare a
#    video il numero di tratte di cui si compone e il costo totale del relativo pedaggio, con due cifre decimali. In caso
#    contrario, occorre segnalare che la destinazione non è raggiungibile.

# 2. stampi a video il percorso che (tra quelli individuati come raggiungibili al punto 1) ha il pedaggio totale minimo. (In caso non ci sia alcun percorso raggiungibile, occorre stampare un messaggio apposito).

def main():
    try:
        fileCaselli = open('pedaggi_autostradali\pedaggi.txt', 'r')
    except IOError:
        exit('Errore apertura file pedaggi')

    # legge i caselli in un dizionario avente il casello di ingresso per chiave
    caselli = leggiCaselli(fileCaselli)
    fileCaselli.close()

    try:
        filePercorsi = open('pedaggi_autostradali\percorsi.txt', 'r')
    except IOError:
        exit('Errore apertura file percorsi')

    primo = True

    for line in filePercorsi:
        campi = line.strip().split(';')
        partenza = campi[0]
        destinazione = campi[1]

        # cerca la tratta (successione di caselli) che parte da partenza e termina con destinazione
        (n_segmenti, costo) = cercaTratta(partenza, destinazione, caselli)

        # se la tratta esiste, n_segmenti > 0
        if n_segmenti > 0:
            print("Percorso %s-%s: %d caselli, tariffa totale %.2f euro " % (partenza, destinazione, n_segmenti, costo))

            # se è il primo percorso valido, è anche quello con tariffa minima
            if primo:
                costoMin = costo
                partenzaMin = partenza
                destinazioneMin = destinazione
                primo = False

            # aggiorna il percorso con tariffa minima
            if costo < costoMin:
                costoMin = costo
                partenzaMin = partenza
                destinazioneMin = destinazione

        else:
            print("Percorso %s-%s: non raggiungibile" % (partenza, destinazione))

    filePercorsi.close()

    # se primo è False, è stata trovata almeno una tratta valida, quindi si può stampare
    if not primo:
        print('\nIl percorso con la minima tariffa è %s-%s' % (partenzaMin, destinazioneMin))
    else:
        print('\nNon è stato trovato nessun percorso valido!')


# Dato il file dei caselli, già aperto, restituisce un dizionario che ha per chiave il casello di entrata e per valore un dizionario con casello di uscita e tariffa
def leggiCaselli(infile):
    caselli = {}
    for line in infile:
        campi = line.strip().split(";")
        if campi[0] not in caselli:
            caselli[campi[0]] = {
                'uscita': campi[1],
                'tariffa': float(campi[2])
            }
    return caselli


# Cerca nel dizionario dei caselli la tratta (i.e. la successione di segmenti) che ha come primo ingresso il casello inizio e come ultima uscita il casello fine. Restituisce il numero di segmenti e la tariffa totale della tratta (entrambi 0, se la tratta non esiste)
def cercaTratta(inizio, fine, caselli):
    nSegmenti = 0
    tariffaTotale = 0

    termina = False
    while not termina:
        if inizio in caselli:
            nSegmenti += 1
            segmento = caselli[inizio]
            tariffaTotale += segmento['tariffa']
            if segmento['uscita'] == fine:
                # la tratta è stata trovata: termina e restituisci i risultati al chiamante
                termina = True
            else:
                # continua a cercare: il nuovo segmento inizia con l'uscita del passo precedente
                inizio = segmento['uscita']
        else:
            # la tratta non è stata trovata: termina mettendo nSegmenti e tariffaTotale a 0
            termina = True
            nSegmenti = 0
            tariffaTotale = 0

    return (nSegmenti, tariffaTotale)


main()  # inizio esecuzione
