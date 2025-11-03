#include <iostream>
using namespace std;

// Modelo
class Calculator {
public:
    float add(float a, float b) { return a + b; }
    float subtract(float a, float b) { return a - b; }
    float multiply(float a, float b) { return a * b; }
    float divide(float a, float b) {
        if (b == 0) {
            cout << "Error: division por cero." << endl;
            return 0;
        }
        return a / b;
    }
};

// controlador, coordina entre la vista y el modelo
class CalculatorController {
private:
    Calculator model;
public:
    float executeOperation(int option, float a, float b) {
        switch (option) {
            case 1: return model.add(a, b);
            case 2: return model.subtract(a, b);
            case 3: return model.multiply(a, b);
            case 4: return model.divide(a, b);
            default:
                cout << "Opción invalida." << endl;
                return 0;
        }
    }
};

// vista, interfaz de usuario
int main() {
    float number1, number2;
    int option;

    cout << "Ingrese el primer numero: ";
    cin >> number1;
    cout << "Ingrese el segundo numero: ";
    cin >> number2;
    cout << "Seleccione operacion: 1-Suma 2-Resta 3-Multiplicacion 4-Division: ";
    cin >> option;

    CalculatorController controller;
    float result = controller.executeOperation(option, number1, number2);
    cout << "Resultado: " << result << endl;

    return 0;
}