#### HERENCIA

"""
La clase Perro es la hija de Animal usando __bases__
print(Perro.__bases__)
# consola>>> (<class '__main__.Animal'>,)

De manera similar podemos ver que clases descienden de una en concreto con __subclasses__.
print(Animal.__subclasses__())
# consola>>> [<class '__main__.Perro’>]
"""

# Definimos una clase padre
class Animal:
    pass

# Creamos una clase hija que hereda de la padre
class Perro(Animal):
    pass