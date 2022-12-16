#4. Scrivere un programma che prenda un file (nome-file.ext) in input e ne conti il
# numero di parole presenti.
try:
    with open(input('Inserisci file: '), 'r')as file:
        conteggio=file.read()
        conteggio=conteggio.split()
        print(conteggio)
    print(len(conteggio))
    
except OSError as err:
    print("OS error: {0}".format(err))   
    print('Inserisci un path del file corretto!')
# gestione_files/4th_exercise/text.txt = input