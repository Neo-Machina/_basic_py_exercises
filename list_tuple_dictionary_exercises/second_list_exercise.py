# 2. Data la lista: list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40], aggiungere
# l’elemento 7000 in seguito al 6000 e rimuovere l’elemento 20. (INDICI)

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].insert(2, 7000)

list1.pop(1)

print(list1)

# ///////////////////////
# --Exercise with inputs--
# //////////////////////

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
print(f'Current Numbers List {list1}')

added_num = input("Please enter the number 7000:\n")

while (not added_num.isdigit()) or (not added_num == '7000'):
    added_num = input("Please enter the number 7000:\n")
added_num = int(added_num)

added_index = input(f'Please enter the index 2:\n')

while (not added_index.isdigit()) or (not added_index == '2'):
    added_index = input(f'Please enter the index 2:\n')
added_index = int(added_index)

list1[2][2].insert( added_index, added_num)

removed_num = input("Please enter the number 20:\n")

while (not removed_num.isdigit()) or (not removed_num == '20'):
    removed_num = input("Please enter the number 20:\n")
removed_num = int(removed_num)

removed_index = input(f'Please enter the index 1:\n')

while (not removed_index.isdigit()) or (not removed_index == '1'):
    removed_index = input(f'Please enter the index 1:\n')
removed_index = int(removed_index)

list1.pop(1)

print(f'This is the updated list:\n {list1} \n You added the number 7000 after the number 6000 and removed the number 20')
