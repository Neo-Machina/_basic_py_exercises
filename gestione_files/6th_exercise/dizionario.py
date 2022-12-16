# Scrivere un programma che salvi i primi 7 caratteri di ogni riga di un file in un
# dizionario con chiave numerica. Se la riga ha meno di 7 caratteri va saltata. Una volta
# salvate dovranno essere aggiunte allo stesso file in ordine inverso.

try:
    with open('gestione_files/6th_exercise/text.tx','r') as file:
        lista=file.readlines()
        grandezza=(len(lista))
        id=range(1,grandezza)
        dizionario= []
        for parola in lista:
            parola=parola[0:7]
            if len(parola)>=7:
                dizionario.append(parola)
            
        dizionario=dict(zip(id,dizionario))
        
    with open('gestione_files/6th_exercise/text.txt','a') as file2:
        for values in reversed(dizionario.values()):
            file2.write('\n')
            file2.writelines(values)

except OSError as err:
    print("OS error: {0}".format(err))   
    print('Inserisci un path del file corretto!')
