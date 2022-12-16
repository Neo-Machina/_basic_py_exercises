# 2. Si realizzi una funzione che prenda in input un numero inserito dalla
# linea di comando dell’utente; Questa funzione ritornerà la tupla
# contenente tabellina (tavola pitagorica) del numero inserito in input.

def funzione1(numero, lista):

    for i in range(1, 11):

        ris = numero * i

        lista+=[ris]

    tupla = tuple(lista)

    return tupla

numero = int(input("Inserisci un numero: "))
lista = []
print(funzione1(numero, lista))