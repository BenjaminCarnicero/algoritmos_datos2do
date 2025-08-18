class Perro:
    def hablar(self):
        print("El perro dice: ¡Guau!")

class Gato:
    def hablar(self):
        print("El gato dice: ¡Miau!")

class Vaca:
    def hablar(self):
        print("La vaca dice: ¡Muuu!")

class Pato:
    def hablar(self):
        print("El pato dice: ¡Cuac!")

# Lista de animales
animales = [Perro(), Gato(), Vaca(), Pato()]

# Duck Typing: no importa que clase es, solo que tenga el metodo .hablar()
for animal in animales:
    animal.hablar()
