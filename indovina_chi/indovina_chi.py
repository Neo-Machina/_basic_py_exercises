# Testo d'esame "Indovina Chi"

# Si realizzi un programma Python per simulare una partita (semplificata) a Indovina Chi.

# Indovina Chi è un gioco caratterizzato da 24 personaggi/caricature. Ogni personaggio ha dei tratti distintivi (sesso,
# lunghezza e colore dei capelli, occhiali, cappello, baffi, barba o calvizie).

# L'obiettivo del gioco è indovinare il personaggio scelto dall'avversario ponendo una serie di domande a cui l'avversario
# potrà rispondere con "SI" o "NO".

# Il programma da realizzare prevede di svolgere una partita semplificata, nella quale si suppone che il giocatore vinca
# se, dopo aver filtrato i personaggi con una serie di domande, è rimasto un solo personaggio.

# In particolare, il programma dovrà:

# 1. leggere le caratteristiche dei personaggi dal file `personaggi.txt` e memorizzarle. Tale file riporta i singoli campi
#    separati da un `";"` e contiene una prima riga di intestazione, utile per identificare i campi riportati per ogni
#    personaggio.

# 2. leggere le domande dell'utente da un secondo file (ad esempio, "domande1.txt" o "domande2.txt"). Il file delle
#    domande contiene, una per riga, le domande poste dall'utente, nel formato

#         nome_caratteristica=valore_caratteristica

# (ad esempio, Barba=SI, o Lunghezza Capelli=Corti).

# 3. stampare a video tutti i personaggi presenti e le relative informazioni

# 4. mostrare, in seguito a ogni domanda, i personaggi che rispondono a quella caratteristica e alle precedenti (ad
#    esempio, se la domanda è "Colore Capelli=Biondo", verranno mostrati solo i personaggi biondi), stampando il numero
#    della domanda e la domanda, seguiti dall'elenco dei personaggi

# 5. stampare a video il risultato finale: in particolare, se alla fine delle domande sarà rimasto un solo personaggio, il
#    giocatore ha vinto. Altrimenti, il giocatore ha perso. Sia in caso di vincita che in caso di sconfitta, il programma
#    stamperà a video un messaggio nel quale comunica l'esito della partita.

# Nota bene: man mano che il giocatore fa domande, l'insieme dei personaggi si riduce sempre di più. Ad esempio, se il
# giocatore seleziona prima i personaggi biondi, poi quelli con occhiali, i personaggi che resteranno saranno biondi e con
# occhiali (non con capelli castani, rossi, ecc.).

# with open('indovina_chi/personaggi.txt','r') as file:
#     contenuto=file.read()
#     linee=contenuto.splitlines()
#     header=linee.pop(0)
#     header=header.split(';')
         
#     lista=[]
#     for linea in linee:
#         lista.append(linea)
#         lista_dizionario=[]
#         for persona in lista:
#             dettagli_persona = persona.split(";")
#             dizionario=dict(zip(header,dettagli_persona))
#             lista_dizionario.append(dizionario)


# with open('indovina_chi/domande1.txt','r') as file1:
#     contenuto = file1.read()
#     testo = contenuto.splitlines()
#     for riga in testo:
#         domanda = riga.split('=')
#         for persona in lista_dizionario.copy():
#             if persona[domanda[0]] != domanda[1]:
#                 lista_dizionario.remove(persona)
                
#         print(domanda)
#         print(lista_dizionario)
            
            
#     if len(lista_dizionario)==1:
#         print('Hai vinto')
#     else:
#         print('Peccato hai perso!')

FILE_PERSONAGGI = 'indovina_chi/personaggi.txt'
FILE_DOMANDE = 'indovina_chi/domande1.txt'


def main():
    personaggi = leggi_personaggi(FILE_PERSONAGGI)
    print(personaggi)

    gioca_partita(FILE_DOMANDE, personaggi)


def leggi_personaggi(nome_file):
    f = open(nome_file, 'r', encoding='utf-8')

    proprieta = f.readline().rstrip().split(';')

    personaggi = []

    for line in f:
        valori = line.rstrip().split(';')
        personaggio = {}
        for i in range(len(proprieta)):
            personaggio[proprieta[i]] = valori[i]
        personaggi.append(personaggio)
    return personaggi


def gioca_partita(nome_file_partita, personaggi):
    personaggi_in_gioco = list(personaggi)  # faccio una copia per non modificare l'elenco completo

    f = open(nome_file_partita, 'r', encoding='utf-8')
    mosse = 0
    for line in f:
        proprieta, valore = line.rstrip().split('=')
        mosse += 1
        print(f'Mossa {mosse} - Domanda: {proprieta} = {valore} ?')

        personaggi_in_gioco = [p for p in personaggi_in_gioco if p[proprieta] == valore]
        print('Personaggi selezionati:')
        for personaggio in personaggi_in_gioco:
            for proprieta in personaggio:
                print(f'{proprieta}={personaggio[proprieta]}', end='  ')
            print()

    # alla fine del file quanti ne rimangono?
    if len(personaggi_in_gioco) == 1:
        print("Hai vinto!")
    else:
        print("Hai perso...")


main()


    