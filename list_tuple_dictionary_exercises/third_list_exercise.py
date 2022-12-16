# 3. Stampare in output [0, 2, 4, 6, 8, 'and', 1, 3, 5, 7, 9] con l’utilizzo della funzione
# range. (CONCATENAZIONE)

first_numbers = list(range(0, 9, 2))

second_numbers = list(range(1, 10, 2))

final_list = first_numbers + second_numbers

final_list.insert(5, 'and')

print((final_list))