
from abc import ABC, abstractmethod

# Interfaz abstracta
class Drone(ABC):

    @abstractmethod
    def despegar(self): pass

    @abstractmethod
    def aterrizar(self): pass

    @abstractmethod
    def acelerar(self): pass

    @abstractmethod
    def frenar(self): pass

    @abstractmethod
    def doblar_derecha(self): pass

    @abstractmethod
    def doblar_izquierda(self): pass

    @abstractmethod
    def sacar_foto(self): pass

# Implementacion concreta: Tricoptero
class Tricoptero(Drone):
    def despegar(self): print("Tricoptero despegando")
    def aterrizar(self): print("Tricoptero aterrizando")
    def acelerar(self): print("Tricoptero acelerando")
    def frenar(self): print("Tricoptero frenando")
    def doblar_derecha(self): print("Tricoptero girando a la derecha")
    def doblar_izquierda(self): print("Tricoptero girando a la izquierda")
    def sacar_foto(self): print("Tricoptero sacando foto")

# Implementacion concreta: Cuadricoptero
class Cuadricoptero(Drone):
    def despegar(self): print("Cuadricoptero despegando")
    def aterrizar(self): print("Cuadricoptero aterrizando")
    def acelerar(self): print("Cuadricoptero acelerando")
    def frenar(self): print("Cuadricoptero frenando")
    def doblar_derecha(self): print("Cuadricoptero girando a la derecha")
    def doblar_izquierda(self): print("Cuadricoptero girando a la izquierda")
    def sacar_foto(self): print("Cuadricoptero sacando foto")

# Cliente
def operar_drone(drone: Drone):
    drone.despegar()
    drone.acelerar()
    drone.doblar_derecha()
    drone.sacar_foto()
    drone.frenar()
    drone.aterrizar()

# Ejecucion
if __name__ == "__main__":
    drone1 = Tricoptero()
    drone2 = Cuadricoptero()

    print("Operando drone 1:")
    operar_drone(drone1)

    print("\nOperando drone 2:")
    operar_drone(drone2)
