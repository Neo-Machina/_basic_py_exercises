# 3. Scrivere una funzione che prenda in input una stringa; La funzione
# dovrà ritornare il numero di vocali della stringa in output.


def conta_vocali(string):
    vocali=0
    for element in string:
        if element in "aeiouAEIOU":
           vocali = vocali+1
    return vocali

parola= str(input("Inserisci una parola: \n"))
print(conta_vocali(parola))


