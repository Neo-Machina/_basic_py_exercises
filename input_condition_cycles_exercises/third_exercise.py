# 3. Si realizzi un programma nel quale si selezionano dei biglietti
# di ingresso di un museo. Tramite questo programma bisogna
# scegliere tra 3 tipologie di biglietti (adulti, bambini e anziani)
# ed inoltre si potranno contare il numero di biglietti in totale.

tot_num_adulti = 0
tot_num_bambini = 0
tot_num_anziani = 0

while True:
    scelta = input("Seleziona il tipo di biglietto:\n 1:Adulti \n 2:Bambini \n 3:Anziani \n 0:Abbandona il programma\n -->")
    
    while not scelta.isdigit():
        scelta = input("Seleziona il tipo di biglietto:\n 1:Adulti \n 2:Bambini \n 3:Anziani \n 0:Abbandona il programma\n -->")
        
    scelta = int(scelta)
    
    if scelta == 1:
        num_adulti = input("Inserisci il numero biglietti Adulti:\n -->")
        while not num_adulti.isdigit():
            num_adulti = input("Inserisci il numero biglietti Adulti:\n -->")
        tot_num_adulti = tot_num_adulti + int(num_adulti)
    elif scelta == 2:  
        num_bambini = input("Inserisci il numero biglietti Bambini:\n -->")
        while not num_bambini.isdigit():
            numeroBambini = input("Inserisci il numero biglietti Bambini:\n -->")
        tot_num_bambini = tot_num_bambini + int(num_bambini)
    elif scelta == 3:  
        num_anziani = input("Inserisci il numero biglietti Anziani:\n -->")
        while not num_anziani.isdigit():
            num_anziani = input("Inserisci il numero biglietti Anziani:\n -->")
        tot_num_anziani = tot_num_anziani + int(num_anziani)
    elif scelta == 0:  
        break
    else:
        print('Devi scegliere un numero tra 0 e 3')
       
print(f"Biglietti adulti {tot_num_adulti}")
print(f"Biglietti bambini {tot_num_bambini}")
print(f"Biglietti anziani {tot_num_anziani}")
print("Biglietti totali", int(tot_num_adulti + tot_num_bambini + tot_num_anziani))