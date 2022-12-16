# Implementare una classe “Studente” con le seguenti caratteristiche:
# 1. Costruttore: richiede in input nome, cognome, età numero di
# telefono
# 2. Il numero di telefono deve essere un numero a 10 cifre
# 3. Getter e setter per tutti gli attributi
# 4. Metodi per aggiungere, e rimuovere corsi dalla lista, corsi dello
# studente e metodo per stampare la lista

class Studente:
    def __init__(self, nome=input('Nome: '), cognome=input('Cognome: '), numerotelefono=input('Numero di telefono: '), eta=input('Età: '), listacorsi=['Matematica', 'Fisica']):
        self.nome=nome
        self.cognome=cognome
        self.numerotelefono=numerotelefono
        self.eta=eta
        self.listacorsi=listacorsi
    def __str__(self):
        return f'Nome:{self.nome}\nCognome:{self.cognome}\nEtà:{self.eta}\nNumero di Telefono:{self.numerotelefono}\nLista Corsi:{self.listacorsi}'

    def add_corso(self):
        while True:
            scelta=input('Vuoi aggiungere un corso?(Si o No)\n')
            if scelta.lower()=='si':
                corso=input('Aggiungi nome corso:\n')
                self.listacorsi.append(corso.capitalize())
            elif scelta.lower()=='no':
                break
        
    def remove_corso(self):
        while True:
            scelta=input('Vuoi rimuovere un corso?(si o no)\n')
            print(self.listacorsi)
            if scelta.lower()=='si':
                corso=input('Rimuovi nome corso:\n')
                for materia in self.listacorsi:
                    if materia==corso.capitalize():
                        self.listacorsi.remove(corso.capitalize())
            elif scelta.lower()=='no':
                break
        
    def print_list(self):
        print(self.listacorsi)
        

    @property
    def numerotelefono(self):
        return self.__numerotelefono

    @numerotelefono.setter
    def numerotelefono(self,numerotelefono):
        self.__numerotelefono=numerotelefono
        while len(self.__numerotelefono) != 10 or not self.__numerotelefono.isdigit():
                print('Il numero di telefono deve contenere 10 cifre\n ')
                self.__numerotelefono=input('Numero di telefono: ')
        return int(self.__numerotelefono)

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,nome):
        self.__nome=nome
    
    @property
    def cognome(self):
        return self.__cognome
    @cognome.setter
    def cognome(self,cognome):
        self.__cognome=cognome
    
    @property
    def eta(self):
        return self.__eta
    @eta.setter
    def eta(self,eta):
        self.__eta=eta
        while  not self.__eta.isdigit():
                print('L\'età deve essere un numero\n ')
                self.__eta=input('Età: ')
        return int(self.__eta)
        
studente1=Studente()
studente1.add_corso()
studente1.remove_corso()
studente1.print_list()