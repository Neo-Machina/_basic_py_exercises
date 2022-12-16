# 1. Definire una lista con più data type e la suddividerla in più sottoliste di un unico
# datatype e le stampi. Vogliamo tenere conto di dati di tipo int, float e string, ciò che
# non rientra in questi datatype verrà inserito in una lista comune.
import ast

list = [
    [],
    [],
    [],
    []
]

keep_going = True
while keep_going:
    try: 
        data = ast.literal_eval(input('Inserisci un dato:\n'))
        
        match data:
            case str():
                list[0].append(data)
            case int():
                list[1].append(data)
            case float():
                list[2].append(data)
            case other:
                list[3].append(data)
        
        question = input('Vuoi ancora aggiungere altri elementi? Yes/No \n')
        
        if question.capitalize() == 'No':
            keep_going = False
        
        while not question.capitalize() == 'Yes' and not question.capitalize() == 'No':
            question = input('Vuoi ancora aggiungere altri elementi? Yes/No \n')
        
            if question.capitalize() == 'Yes':
                break
            elif question.capitalize() == 'No':
                keep_going = False
                break
            
    except ValueError:
        print('Il programma non accetta questo tipo di dato')

print('lista aggiornata',list)








        



