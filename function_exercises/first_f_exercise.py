# 1. Si creino due funzioni: La prima creerà una lista contenente l’inverso
# della stringa; La seconda funzione ritornerà la lista sottoforma di una
# tupla. Si prenda in input dall’utente una stringa, si stampi a schermo
# una tupla contenente la stringa presa in input al contrario.

def funzione1(parola, lista1):

    parola_reversed = parola[::-1]

    lista1.append(parola_reversed)

    return lista1

def funzione2(lista1):

    tupla = tuple(lista1)

    return tupla

parola = str(input("Inserisci una parola:"))
lista1 = []
funzione1(parola, lista1)
print(funzione2(lista1))