# 1. Definire una lista con più data type e la suddividerla in più sottoliste di un unico
# datatype e le stampi. Vogliamo tenere conto di dati di tipo int, float e string, ciò che
# non rientra in questi datatype verrà inserito in una lista comune.

list = [
    'Luca', 11, 'Maria',
    True, 33, {1: 'gatto'},
    ('codice', 17, False), 34.90, 65.98,
    'Andrea', False, True,
    (True, 'stringa', 9), 16.84, 
    {0: 'cane'}, 67
]

list2 = [
    [],
    [],
    [],
    []
]

for element in list:
    if type(element) == str:
        list2[0].append(element)
    elif type(element) == int:
        list2[1].append(element)
    elif type(element) == float:
        list2[2].append(element)
    else: 
        list2[3].append(element)
        
print('Lista suddivisa in più sottoliste di un unico datatype: \n', list2)