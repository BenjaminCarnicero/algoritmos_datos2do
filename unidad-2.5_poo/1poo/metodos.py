# METODOS

'''
Para saber más: El uso de "self" es totalmente arbitrario. Se trata de una convención acordada por los usuarios de
Python, usada para referirse a la instancia que llama al método, pero podría ser cualquier otro nombre.
Lo mismo ocurre con "cls", que veremos a continuación.
'''
class Clase:

    def metodo(self):
        return 'Método normal (instancia)', self

'''
En vista a esto, los métodos de instancia:
Puede manipular atributo de instancia y atriubuto de clase.
Pueden acceder y modificar los atributos del objeto.
Pueden acceder a otros métodos.
Dado que desde el objeto self se puede acceder a la clase con `self.class`, también pueden modificar el estado de la clase'''

    #@decoradores.
    #METODOS DE CLASE
    @classmethod
    def metododeclase(cls):
        return 'Método de clase', cls
    """
    Reciben como parametro cls.
    Pueden acceder a la clase, pero no a la instancia. Son solo de clase.
    No pueden acceder a los atributos de la instancia.
    Pero si pueden modificar los atributos de la clase.
    Cualquier metodo, lo unico que puede hacer es manipular atributos.
    """

    @staticmethod
    def metodoestatico():
        return "Método estático“

'''
Por último, los métodos estáticos se pueden definir con el decorador @staticmethod y no aceptan como parámetro ni la instancia ni
la clase. Es por ello por lo que no pueden modificar el estado ni de la clase ni de la instancia. Pero por supuesto pueden aceptar
parámetros de entrada.
Se podrían ver como funciones normales, con la salvedad de que van ligadas a una clase
concreta.'''