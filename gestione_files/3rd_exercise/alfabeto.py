# 3. Scrivere un programma che scriva tutte le lettere dell'alfabeto divise in n righe
# specificate dall'utente di un file.

import string
def righe_file(riga):
   with open("gestione_files/3rd_exercise/text.txt", "w") as file:
    alfabeto = string.ascii_uppercase
    for passo in range(0, len(alfabeto), riga):
        lettere = [alfabeto[passo:passo + riga] + "\n"]
        file.writelines(lettere)

def errori(righe):
    while True:
        try:
            righe=int(input('Numero righe: '))
        except ValueError:
            print('Numero di righe non valido')
        else:
            return righe
            
riga=None
riga=errori(riga)
righe_file(riga)


