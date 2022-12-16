# 5. Si crei un dizionario dove il valore è di tipo stringa. Si deve ottenere il numero di
# caratteri complessivi di ciascun valore del dizionario ed infine stampare la loro
# somma.

dictionary = dict(nome = 'Giovanni', cognome = 'Bianchi')
tot_characters = 0

for string in dictionary.values():
    print(len(string))
    tot_characters += len(string)

print(tot_characters)
        
        
        
        

