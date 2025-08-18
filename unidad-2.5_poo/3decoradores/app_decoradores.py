'''Para la App Anterior
3.1 Implementar dos métodos en alguna Clase y usar @property
3.2 Implementar Encapsulamiento vía “__”
3.3 Implementar los setter()'''


#@property transforma un metodo en un atributo.

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
            print("La especie debe ser una cadena no vacía.")

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

    # Setter de edad: validamos que sea un número positivo
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




#@#@#@#@##@



#Consola
#@#@#@#@

mi_perro = Perro("mamifero", 10, "Benjamin")
mi_vaca = Vaca("mamifero", 4)
mi_abeja = Abeja("insecto", 1)

# Accedemos a los atributos con property
print(mi_perro.duenio) # Acceso controlado con @property
print(mi_perro.edad)
print(mi_vaca.especie)
print(mi_abeja.edad)

# Modificamos atributos usando setters
mi_perro.edad = -5      # Intenta cambiar edad con valor invalido → da error controlado
mi_perro.edad = 12      # Cambia edad correctamente
print(mi_perro.edad)

mi_perro.duenio = ""    # Intenta cambiar dueño con cadena vacia → da error controlado
mi_perro.duenio = "Lucas"
mi_vaca.edad = 5
mi_abeja.especie = "himenóptero"

# Verificamos los cambios
print(mi_perro.duenio)
print(mi_vaca.edad)
print(mi_abeja.especie)
