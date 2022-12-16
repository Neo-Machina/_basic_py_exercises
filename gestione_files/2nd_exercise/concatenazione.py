# 2. Scrivere un programma che concateni e stampi ogni riga di un file con la riga
# corrispondente di un secondo file.

try:
    with open('gestione_files/2nd_exercise/text.txt', 'r') as file1, open('gestione_files/2nd_exercise/text2.tx', 'r') as file2:
        for line1, line2 in zip(file1, file2):
            print(line1+line2)    
except OSError as err:
    print("OS error: {0}".format(err))   
    print('Inserisci un path del file corretto!')
            