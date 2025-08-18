'''
2.1 Desarrollar una APP por consola que Cree una estructura como la de la figura:
2.2 Implementar la Herencia
2.3 Implementar __bases__ y __subclases__
2.4 Implementar base()
2.5 Crear Objetos y mostrar por consola.
'''
### ANIMAL
class Animal:

    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    # Método genérico pero con implementación particular
    def hablar(self):
        pass # Método vacío

    # Método genérico pero con implementación particular
    def moverse(self):
        pass # Método vacío

    # Método genérico con la misma implementación
    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)


###### CLASES QUE HEREDAN DE ANIMAL ######
'''
Metodos heredados de la clase padre pero modificados: hablar() y moverse().
Metodos heredados directamente de la clase padre (sin modificaciones): describeme().
Metodos creados en la clase hija, no existentes en la clase padre: picar()
'''
### PERRO
class Perro(Animal):
    # Si tengo que agregar un nuevo atributo especifico pafa perro, como su duenio, lo defino dentro de su clase.
    #super() sirve para llamar al __init__ de la clase padre que ya aceptaba la especie y edad, y sólo asignar la variable nueva manualmente.
    def __init__(self, especie, edad, duenio):
        super().__init__(especie, edad)
        self.duenio = duenio

    def hablar(self):
        print("Guau!")

    def moverse(self):
        print("Caminando con 4 patas")

### VACA
class Vaca(Animal):

    def hablar(self):
        print("Muuu!")

    def moverse(self):
        print("Caminando con 4 patas")


### ABEJA
class Abeja(Animal):

    def hablar(self):
        print("Bzzzz!")

    def moverse(self):
        print("Volando")


# Nuevo método (creado en la clase hija, no existente en la clase padre)
    def picar(self):
        print("Picar!")



### Creacion de objetos

'''Una vez que tengo mis clases estructuradas con sus respectivos metodos:
Ya puedo crear objetos para llamar a esos metodos y mostrarlos por consola por ejemplo'''

#Los atributos para cada animal(el constructor recibe los parametros especie y edad)
mi_perro = Perro('mamífero', 10, 'Benjamin')

mi_vaca = Vaca('mamífero', 23)

mi_abeja = Abeja('insecto', 1)

###
print(mi_perro.especie)
print(mi_perro.edad)
print(mi_perro.duenio)

#hablar()
mi_perro.hablar() # Guau!

mi_vaca.hablar() # Muuu!


#describeme()
mi_vaca.describeme() # Soy un Animal del tipo Vaca

mi_abeja.describeme() # Soy un Animal del tipo Abeja


#picar()
mi_abeja.picar() # Picar!
