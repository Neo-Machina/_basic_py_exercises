# # Testo d'esame "Fantacalcio"

# Nel gioco del fantacalcio, occorre formare una squadra virtuale composta da calciatori reali. I calciatori reali sono
# elencati nel file `fantacalcio.txt`, così organizzato:

# 	cognome, squadra, ruolo, quotazione

# I calciatori sono elencati nel file in ordine alfabetico per cognome. Il ruolo del calciatore è uno fra i seguenti:
# portiere, difensore, centrocampista, attaccante. La quotazione è un numero intero strettamente positivo e rappresenta il
# valore (in FantaMilioni) del calciatore.

# La rosa della squadra virtuale è composta da 25 calciatori:

# - 3 portieri
# - 8 difensori
# - 8 centrocampisti
# - 6 attaccanti.

# Il budget disponibile per formare la squadra è 260 FantaMilioni.

# Si scriva un programma per formare la rosa della squadra virtuale. Sono destinati 20 FantaMilioni ai portieri, 40 ai
# difensori, 80 ai centrocampisti e 120 agli attaccanti. Per ogni ruolo, il programma acquista il calciatore più costoso
# fra quelli che rispettano le due condizioni seguenti:

# - la quotazione del calciatore è inferiore o uguale al budget
# - dopo l'acquisto, devono rimanere disponibili almeno tanti FantaMilioni quanti sono i calciatori dello stesso ruolo
#   ancora da acquistare.

# La seconda condizione assicura di poter acquistare tutti i calciatori richiesti per ruolo. Infatti, per ogni ruolo ci
# sono molti calciatori con valutazione 1 FantaMilione. Ad esempio, il budget per l'acquisto del primo attaccante è 120 –
# 5 = 115 FantaMilioni. Se la quotazione dell'attaccante acquistato è 56, il budget rimanente è 120 – 56 = 64. Il budget
# per l'acquisto del secondo attaccante è quindi 64 – 4 = 60. Per ogni ruolo, il programma stampa a video l'elenco dei
# calciatori acquistati e la loro quotazione.

# **N.B.:** Dopo aver acquistato un calciatore, occorre rimuoverlo dalla lista dei calciatori reali per evitare di
# acquistarlo una seconda volta.

# A parità di quotazione, non ci sono criteri su quale calciatore acquistare (la scelta è libera).

# Se il budget per un ruolo non è completamente consumato, si può scegliere se aggiungerlo al budget per il ruolo
# successivo oppure perderlo (entrambe le soluzioni vanno bene).

def leggi_file(nome_file):
    """
    Acquisisci le informazioni sui calciatori
    :param nome_file: Nome del file che contiene le informazioni sui calciatori
    :return: una lista di giocatori; ciascun giocatore è rappresentato da un dizionario
    contenente i 4 campi: nome, squadra, ruolo, costo
    """
    file = open(nome_file, 'r', encoding='utf-8')
    elenco_giocatori = []
    for riga in file:
        campi = riga.split(',')
        record = {
            'nome': campi[0].strip(),
            'squadra': campi[1].strip(),
            'ruolo': campi[2].strip(),
            'costo': int(campi[3])
        }
        elenco_giocatori.append(record)
    file.close()
    return elenco_giocatori


def scegli_rosa(info_ruolo, elenco_giocatori):
    """
    Sceglie in modo "ottimale" i giocatori per un determinato ruolo
    (secondo il criterio specificato nel testo).
    :param info_ruolo: dizionario che contiene la descrizione dei vincoli
    per la scelta dei giocatori: budget, num (numero di giocatori da scegliere), ruolo
    :param elenco_giocatori: lista contenente tutti i giocatori (non viene modificata)
    :return: lista di giocatori contenente quelli selezionati per l'acquisto
    """

    # estraggo i dati per comodità
    budget = info_ruolo['budget']
    num = info_ruolo['num']

    # seleziono solo i giocatori che hanno il ruolo specificato
    giocatori = [g for g in elenco_giocatori if g['ruolo'] == info_ruolo['ruolo']]
    # print(giocatori)

    rosa = []
    for i in range(num):  # ripeto tante volte quanti sono i giocatori desiderati
        costo_max = 0
        # cerco il giocatore di costo massimo
        for g in giocatori:
            # budget - (num - 1 - i) tiene conto del fatto che devo
            # 'riservare' un certo numero di milioni (num-1) la prima volta,
            # (num-2) la seconda volta, ecc... per i futuri giocatori
            if g['costo'] > costo_max and g['costo'] <= budget - (num - 1 - i):
                mio = g  # giocatore scelto
                costo_max = g['costo']
        # print(f'Budget: {budget}  -- Acquisto {mio}')
        rosa.append(mio)
        budget = budget - mio['costo']
        giocatori.remove(mio)  # per evitare di prendere due volte lo stesso
    return rosa


def main():

    # parametri di funzionamento del programma: elenco ruoli e relative cartteristiche
    info_ruoli = [
        {
            'ruolo': 'portiere',
            'num': 3,
            'budget': 20
        },
        {
            'ruolo': 'difensore',
            'num': 8,
            'budget': 40
        },
        {
            'ruolo': 'centrocampista',
            'num': 8,
            'budget': 80
        },
        {
            'ruolo': 'attaccante',
            'num': 6,
            'budget': 120
        }
    ]

    giocatori = leggi_file('fantacalcio/fantacalcio.txt')
    # print(giocatori)

    for info_ruolo in info_ruoli:
        rosa = scegli_rosa(info_ruolo, giocatori)

        # Stampa la rosa di giocatori per quel ruolo
        print(f'Ruolo: {info_ruolo["ruolo"]}')
        for g in rosa:
            print(g['nome'], g['costo'], end='  ')
        print()


main()