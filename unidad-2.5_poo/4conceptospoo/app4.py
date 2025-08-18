#########################################################

"""
- Aplicación de conceptos POO en la app Animal
- Encapsulamiento:
Aplicado en todas las clases (Animal, Perro, Vaca, Abeja) mediante atributos privados (__edad, __especie, __duenio) y el uso de @property y @setter para acceder y modificar esos valores de forma controlada.

- Abstracción:
La clase Animal actúa como una clase base genérica. Define métodos como hablar() y moverse() sin implementación concreta (pass), dejando que las clases hijas los implementen según su comportamiento.

- Cohesión:
Cada clase tiene un propósito claro y métodos bien definidos según el tipo de animal. Perro incluye atributos específicos como duenio, Abeja tiene su método picar(), y todos definen su forma de moverse o hablar.

- Acoplamiento:
Las clases están bien separadas y no dependen unas de otras. Perro, Vaca y Abeja solo heredan de Animal y se manejan de forma autónoma, lo cual reduce el acoplamiento entre módulos.

- Efecto mariposa (evitado):
Gracias al encapsulamiento y bajo acoplamiento, cualquier cambio en una clase no afecta a las demás. Por ejemplo, cambiar el comportamiento de Perro no afecta en nada a Vaca o Abeja.

"""


class Animal:
    def __init__(self, especie, edad):
        self.__especie = especie
        self.__edad = edad

    @property
    def especie(self):
        return self.__especie

    @especie.setter
    def especie(self, nueva_especie):
        if isinstance(nueva_especie, str) and nueva_especie != "":
            self.__especie = nueva_especie
        else:
            print("La especie debe ser una cadena no vacia.")

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("La edad debe ser mayor a 0.")

    def hablar(self):
        pass

    def moverse(self):
        pass

    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)


# PERRO
class Perro(Animal):
    def __init__(self, especie, edad, duenio):
        super().__init__(especie, edad)
        self.__duenio = duenio  # Encapsulado con doble guion bajo
        self.__edad = edad      # Encapsulamos edad tambien

    def hablar(self):
        print("Guau!")

    def moverse(self):
        print("Caminando con 4 patas")

    # Getter del atributo edad usando @property
    @property
    def edad(self):
        return self.__edad

    # Setter de edad: validamos que sea un numero positivo
    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("La edad debe ser mayor a 0.")

    # Getter del atributo duenio
    @property
    def duenio(self):
        return self.__duenio

    # Setter de duenio: validamos que sea una cadena no vacia
    @duenio.setter
    def duenio(self, nuevo_duenio):
        if isinstance(nuevo_duenio, str) and nuevo_duenio != "":
            self.__duenio = nuevo_duenio
        else:
            print("El nombre del duenio debe ser una cadena no vacia.")


# VACA
class Vaca(Animal):
    def hablar(self):
        print("Muuu!")

    def moverse(self):
        print("Caminando con 4 patas")


# ABEJA
class Abeja(Animal):
    def hablar(self):
        print("Bzzzz!")

    def moverse(self):
        print("Volando")

    def picar(self):
        print("Picar!")


# Consola

mi_perro = Perro("mamifero", 10, "Benjamin")
mi_vaca = Vaca("mamifero", 4)
mi_abeja = Abeja("insecto", 1)

# Accedemos a los atributos con property
print(mi_perro.duenio)
print(mi_perro.edad)
print(mi_vaca.especie)
print(mi_abeja.edad)

# Modificamos atributos usando setters
mi_perro.edad = -5
mi_perro.edad = 12
print(mi_perro.edad)

mi_perro.duenio = ""
mi_perro.duenio = "Lucas"
mi_vaca.edad = 5
mi_abeja.especie = "himenoptero"

# Verificamos los cambios
print(mi_perro.duenio)
print(mi_vaca.edad)
print(mi_abeja.especie)
