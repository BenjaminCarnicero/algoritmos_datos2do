# 1.8 Asignarles atributos de clase e instancia

#Atributos de instancia: Pertenecen a la instancia de la clase (Perro). Particulares de cada instancia (cada perro).

#Atributos de clase: Pertenecen a la clase. Comunes para todos los objetos por igual.


class Perro:
    pass #para que no de error.
    especie = "mamifero" #atributo de clase (dentro de la clase)

    def __init__(self, nombre, raza): #constructor, llamado al crear el objeto.
    print("Creando al perro {nombre}, {raza}")

    self.nombre = nombre #Atributos de instancia (dentro del constructor)
    self.raza = raza

    '''
    Self se pasa como paremtro de entrada del metodo, siempre tiene que estar ahi.
    paso mi_perro como parametro directamente, y seguido, le asigno nombre y raza, en este ejemplo concreto.
    '''