# 1.9 Asignar métodos de Instancia, Clase y estáticos

class Perro:
    pass #para que no de error.
    especie = "mamifero" #atributo de clase (dentro de la clase)

    def __init__(self, nombre, raza): #constructor, llamado al crear el objeto.
    print("Creando al perro {nombre}, {raza}")

    self.nombre = nombre #Atributos de instancia (dentro del constructor)
    self.raza = raza  #este self es el equivalente a poner this.

    ### Ahora creo metodos que le den funcionalidad a mi clase:
    def ladrar(self):
        print("Guau")

    def caminar(self, pasos):
        print(f"Caminando {pasos} pasos")

mi_perro = Perro("Toby", "Bulldog")
mi_perro.ladrar()
mi_perro.caminar(10)

"""
Ahora mi perro ladra y camina segun lo que yo le pida que haga.
Por ejemplo, llamo al objeto mi_perro y le paso como parametro 10 pasos.
O le pido directamente que ladre (entre otros posibles metodos: acciones de un perro).
"""


# @decoradores:
