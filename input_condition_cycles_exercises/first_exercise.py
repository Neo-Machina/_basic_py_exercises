# 1. Prendere un input, se è un numero negativo richiedere un nuovo
# input, se è 0 stampa 0 a schermo, se è positivo stampa tutti
# i numeri pari da 0 a quel numero. Una volta finita la stampa
# torna in attesa di un input

while True:
    numero = int(input('Dimmi un numero : \n'))
    if numero < 0:
        int(input('Dimmi un numero positivo: \n'))
        continue
    elif numero == 0:
        print(f'stampo {numero}')
    else:
        for counter in range(0, numero + 1):
            print(f'numero {counter}')
        continue