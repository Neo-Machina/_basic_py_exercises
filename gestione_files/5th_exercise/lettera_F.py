# Scrivere un programma che conti quante righe di un file non iniziano con la lettera
# "F".
try:
    with open('gestione_files/5th_exercise/text.tx','r') as file:
        riga=file.readlines()
        counter=0
        for lettera in riga:
            if lettera[0]!='F':
                counter+=1
    
    print(f'Il numero delle righe che non iniziano con "F" è: {counter}')  

except OSError as err:
    print("OS error: {0}".format(err))   
    print('Inserisci un path del file corretto!') 