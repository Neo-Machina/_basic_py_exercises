# 2. Scrivere un codice che permetta di comprare una macchina,
# se l’età è di almeno 18 anni e si ha la patente, allora
# la macchina potrà essere acquistata, altrimenti no. L’età
# e il possedimento della patente dovranno essere inseriti
# dall’utente dalla linea di comando.

while True:
    try:
        age = int(input('Tell me your age: \n'))
        break
    except ValueError:
        print('Il valore inserito non è un numero')


while True:
    driving_license = input('Do you have the driving_license: yer or no? \n')
    if driving_license.capitalize() == 'Yes' or driving_license.capitalize() == 'No':
        break

if age >= 18 and driving_license.capitalize() == 'Yes':
    print('You can buy a car!')
else:
    print('You can\'t buy a car!')
    
