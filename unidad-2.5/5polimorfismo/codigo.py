'''
5.1 analizar y describir le siguiente código:
for animal in Perro(), Gato():
animal.hablar()
# Guau!
# Miau!
'''
class Perro:
    def hablar(self):
        print("Guau!")

class Gato:
    def hablar(self):
        print("Miau!")


for animal in Perro(), Gato():
    animal.hablar()
# Guau!
# Miau!
"""
for animal in Perro(), Gato():
Acá estamos creando los objetos: uno de la clase Perro y otro de la clase Gato.

Python los mete automáticamente en una tupla, y el bucle for recorre cada uno.
----------------------------------------------------------------------------------
animal.hablar()
Como ambas clases tienen un método hablar(), Python no se fija si vienen de una misma clase padre.

Solo le importa que cada objeto tenga ese método. Y como lo tienen, lo ejecuta.
-----------------------------------------------------------------------------------
Polimorfismo + duck typing puro:

Polimorfismo: diferentes objetos (Perro, Gato) responden de forma distinta al mismo mensaje (hablar()).

Duck typing: no importa qué tipo de objeto es, solo que se comporte como se espera (en este caso, que tenga .hablar()).
"""