# 4. Realizzare una funzione che prenda in input una stringa e controlli
# se essa è palindroma.

def palindroma(parola):
    parola = parola.lower().replace(' ', '')
    return parola == parola[::-1]

parola= input("Inserisci una parola: \n")
print(palindroma(parola))