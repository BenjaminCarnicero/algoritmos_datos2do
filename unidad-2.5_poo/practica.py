# 1.1
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}")


# 1.2
class Auto:
    ruedas = 4  # atributo de clase

    def __init__(self, color):
        self.color = color  # atributo de instancia


#1.3
class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


#1.4
class Producto:
    def __init__(self, precio):
        self._precio = precio

    @property
    def precio(self):
        return self._precio


# 1.5
class Ejemplo:
    contador = 0

    def __init__(self, nombre):
        self.nombre = nombre

    @classmethod
    def aumentar_contador(cls):
        cls.contador += 1

    @staticmethod
    def mostrar_mensaje():
        print("Esto es un metodo estatico")


### 1.6

class Animal:
    especie = "mamifero"  # atributo de clase

    def __init__(self, nombre):
        self.nombre = nombre  # atributo de instancia

    def hablar(self):  # metodo de instancia
        print(f"{self.nombre} hace un sonido.")

    @classmethod
    def info_clase(cls):  # metodo de clase
        print(f"Todos los animales son: {cls.especie}")

    @staticmethod
    def info_general():  # metodo estatico
        print("Los animales pueden ser domesticos o salvajes.")


perro = Animal("Firulais")
perro.hablar()
Animal.info_clase()
Animal.info_general()



#2.1
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

class Estudiante(Persona):  # Estudiante hereda de Persona
    def estudiar(self):
        print(f"{self.nombre} está estudiando")


#2.2
print(Estudiante.__bases__)  # (<class '__main__.Persona'>,)



print(Persona.__subclasses__())  # [<class '__main__.Estudiante'>]


#2.3
class Estudiante(Persona):
    def saludar(self):  # sobrescribo el método del padre
        print(f"{self.nombre} dice: ¡Hola profe!")



#2.4
class Estudiante(Persona):
    def __init__(self, nombre, curso):
        super().__init__(nombre)  # Llama al constructor de Persona
        self.curso = curso



#2.5
class Mamifero:
    def amamantar(self):
        print("Amamantando crías")

class Volador:
    def volar(self):
        print("Volando alto")

class Murcielago(Mamifero, Volador):
    pass


#2.6

print(Murcielago.__mro__)


(<class '__main__.Murcielago'>, <class '__main__.Mamifero'>, <class '__main__.Volador'>, <class 'object'>)



# Decoradores
#3.2

class Persona:
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

p = Persona("Benjamin")
print(p.nombre)  # Sin parentesis, aunque nombre() es un metodo



#3.3

class Producto:
    def __init__(self, precio):
        self._precio = precio

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self._precio = nuevo_precio
        else:
            print("El precio debe ser positivo")



#3.4
class Usuario:
    def __init__(self):
        self.__clave = "1234"



#4.1
class Calculadora:
    def sumar(self, a, b): ...
    def restar(self, a, b): ...
    def multiplicar(self, a, b): ...


# 4.7
class Usuario:
    def __init__(self):
        self.__clave = "secreta"

    @property
    def clave(self):
        return self.__clave

    @clave.setter
    def clave(self, nueva_clave):
        if len(nueva_clave) >= 6:
            self.__clave = nueva_clave





### 5.1
class Gato:
    def hablar(self):
        return "Miau"

class Perro:
    def hablar(self):
        return "Guau"

def hacer_hablar(animal):
    print(animal.hablar())

hacer_hablar(Gato())   # Miau
hacer_hablar(Perro())  # Guau


### 5.2

#Java
class Animal {
    void hablar() {
        System.out.println("Hace un sonido");
    }
}

class Perro extends Animal {
    void hablar() {
        System.out.println("Guau");
    }
}


#### 5.3 ####
class Impresora:
    def imprimir(self):
        print("Imprimiendo documento")

class Fax:
    def imprimir(self):
        print("Enviando fax")

def procesar_dispositivo(dispositivo):
    dispositivo.imprimir()

procesar_dispositivo(Impresora())  # Imprimiendo documento
procesar_dispositivo(Fax())        # Enviando fax





#### 6.4 ####

class ControlRemoto:
    def subir_volumen(self):
        pass

    def bajar_volumen(self):
        pass


### 6.7
from abc import ABC, abstractmethod

class ControlRemoto(ABC):
    @abstractmethod
    def subir_volumen(self):
        pass

    @abstractmethod
    def bajar_volumen(self):
        pass


#subclase
class Samsung(ControlRemoto):
    def subir_volumen(self):
        print("Volumen +")






#@#@#@
#6.8
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod #El decorador obliga a cumplir con el “contrato” de la clase abstracta
    def hablar(self):
        pass


# Si hago esto da error:
class Perro(Animal):
    pass

p = Perro()  # ERROR: no implemento hablar()


#forma correcta:
class Perro(Animal):
    def hablar(self):
        print("Guau")


#6.9
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass



###6.10
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2



#6.11 sequence

from collections.abc import Sequence

class MiLista(Sequence):
    def __init__(self, datos):
        self._datos = datos

    def __getitem__(self, index):
        return self._datos[index]

    def __len__(self):
        return len(self._datos)


#@#@#@
mis_datos = MiLista([1, 2, 3])
print(mis_datos[0])    # 1
print(len(mis_datos))  # 3



###DUCKTYPING###
# 7.4 #
class Perro:
    def hablar(self):
        print("Guau")

class Gato:
    def hablar(self):
        print("Miau")

class Vaca:
    def hablar(self):
        print("Muuu")

lista = [Perro(), Gato(), Vaca()]

for animal in lista:
    animal.hablar()
# Guau
# Miau
# Muuu