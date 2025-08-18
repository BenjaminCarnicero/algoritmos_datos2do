# 1.10 Realizar una calculadora que consuma estos métodos.

"""
Los métodos de instancia “normales” que ya hemos visto como metodo()
Métodos de clase usando el decorador @classmethod
Métodos estáticos usando el decorador @staticmethod
"""

class Math:
    @staticmethod
    def sumar(num1, num2):
        return num1 + num2

    @staticmethod
    def restar(num1, num2):
        return num1 - num2

    @staticmethod
    def multiplicar(num1, num2):
        return num1 * num2

    @staticmethod
    def dividir(num1, num2):
        return num1 / num2


print(Math.sumar(5, 7))
print(Math.restar(9, 3))
print(Math.multiplicar(15, 9))
print(Math.dividir(10, 2))


"""
Defino cada funcion, suma resta, etc. Como metodos estaticos ya que solo van a cumplir una funcionalidad en concreto.
Simplemente llamo al metodo que quiero desde la clase y le asigno como argumento los dos numeros que quiero que realice la cuenta.
"""