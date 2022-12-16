# 1. Scrivere un programma che conta quante volte una parola è contenuta in un file.
from collections import Counter

try:
    with open('gestione_files/first_exercise/text.tx', 'r') as file:
        list = file.readlines()
        
        list = Counter(list)
        print(list)
        list = dict(list)
        
        for key,value in list.items():
            key = key.replace('\n', '')
            print(f'La parola {key} è ripetuta {value} volta/e')
    
except OSError as err:
    print("OS error: {0}".format(err))   
    print('Inserisci un path del file corretto!')
    
    
