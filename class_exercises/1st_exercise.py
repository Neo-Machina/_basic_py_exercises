# Progettiamo una semplice classe:
# che rappresenti un libro
# che abbia i seguenti attributi:
# Titolo (stringa)
# Autore (stringa)
# Numero di pagine
# che abbia i seguenti metodi
# Loading [MathJax]/jax/output/HTML-CSS/jax.js
# Info() : restituisce una stringa con le informazioni relative al libro

class Libro:

    def init (self, Titolo = "nessuno", Autore = "nessuno", Numero_pagine = 0):

        self.Titolo = Titolo
        self.Autore = Autore
        self.Numero_pagine = Numero_pagine

    def Info (self):

        print(f"Il titolo del libro è: {self.Titolo}, L'autore del libro è: {self.Autore}, Il numero di pagine è: {self.Numero_pagine} ")

libro1 = Libro ("Peter pan", "J. M. Barrie", 300)
libro2 = Libro("Promessi sposi", "Manzoni", 500)
libro3 = Libro()

libro1.Info()
libro2.Info()
libro3.Info()
    
