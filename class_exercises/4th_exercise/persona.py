'''Si ha la necessità di definire tre classi in Python: persona, studente, lavoratore. Le ultime due classi elencate, ovvero studente e lavoratore sono classe derivate 
dalla classe persona. Scrivere il codice Python che permette di definire le tre classi su elencate (tenendo conto del concetto di ereditarietà)
e un piccolo main che ne richiama i metodi definiti.
NOTA IMPORTANTE: si definiscano solo gli attributi (3 per la classe persona, 1 specifico di studente, 1 specifico di lavoratore) e i metodi init e str.
'''
class Persona:
    def __init__(self, nome, cognome, eta):
        self.nome=nome
        self.cognome=cognome
        self.eta=eta
    def __str__(self):
        return f'Nome: {self.nome}\nCognome:{self.cognome}\nEtà:{self.eta}'

class Studente(Persona):
    def __init__(self,nome, cognome, eta, corso_laurea):
        super().__init__(nome, cognome, eta)
        self.corso_laurea=corso_laurea
    def __str__(self):
       return f'Nome: {self.nome}\nCognome:{self.cognome}\nEtà:{self.eta}\nCorso di Laurea:{self.corso_laurea}'

class Lavoratore(Persona):
    def __init__(self,nome, cognome, eta, occupazione):
        super().__init__(nome, cognome, eta)
        self.occupazione=occupazione
    def __str__(self):
        return  f'Nome: {self.nome}\nCognome:{self.cognome}\nEtà:{self.eta}\nOccupazione :{self.occupazione}'