# Modelo
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            print("Error: division por cero.")
            return 0
        return a / b

# Controlador
class CalculatorController:
    def __init__(self):
        self.model = Calculator()

    def execute_operation(self, option, a, b):
        if option == 1:
            return self.model.add(a, b)
        elif option == 2:
            return self.model.subtract(a, b)
        elif option == 3:
            return self.model.multiply(a, b)
        elif option == 4:
            return self.model.divide(a, b)
        else:
            print("Opcion invalida.")
            return 0

# Vista, interfaz de usuario
def main():
    number1 = float(input("Ingrese el primer numero: "))
    number2 = float(input("Ingrese el segundo numero: "))
    option = int(input("Seleccione operacion: 1-Suma 2-Resta 3-Multiplicacion 4-Division: "))

    controller = CalculatorController()
    result = controller.execute_operation(option, number1, number2)
    print("Resultado:", result)

main()