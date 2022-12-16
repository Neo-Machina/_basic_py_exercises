class Persona:
    def __init__(self,nome,cognome):
        self.nome = nome
        self.cognome = cognome
    
    def __str__(self):
        return f'nome: {self.nome}, cognome {self.cognome}'
    def __eq__(self, altro):
        if isinstance(altro, Persona):           
            return (self.nome.upper(), self.cognome.upper()) == (altro.nome.upper(), altro.cognome.upper())
        return NotImplemented
            
        
p1 = Persona('Alessandro','Bosco')
p2 = Persona('alessandro','bosco')

print(p1)
print(p2)

print(p1 == p2)
print(p1 == None)

