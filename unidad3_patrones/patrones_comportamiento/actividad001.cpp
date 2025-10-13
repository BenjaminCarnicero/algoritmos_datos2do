#include <iostream>
#include <string>
using namespace std;

//
// ---------------------------- INTERFAZ ESTRATEGIA ----------------------------
//

// La clase base "Strategy" define la interfaz común para todas las estrategias.
class EstrategiaRuta {
public:
    // Método que cada estrategia concreta debe implementar
    virtual void calcularRuta(string origen, string destino) = 0;

    // Destructor virtual (buena práctica cuando hay herencia)
    virtual ~EstrategiaRuta() {}
};

//
// ---------------------------- ESTRATEGIAS CONCRETAS ----------------------------
//

// Estrategia 1: Ruta peatonal
class RutaPeatonal : public EstrategiaRuta {
public:
    void calcularRuta(string origen, string destino) override {
        cout << " Calculando ruta PEATONAL desde " << origen << " hasta " << destino << "..." << endl;
        cout << "Ruta sugerida: calles angostas y zonas peatonales. Tiempo estimado: 25 min." << endl;
    }
};

// Estrategia 2: Ruta en coche
class RutaCoche : public EstrategiaRuta {
public:
    void calcularRuta(string origen, string destino) override {
        cout << " Calculando ruta en COCHE desde " << origen << " hasta " << destino << "..." << endl;
        cout << "Ruta sugerida: autopista y avenidas principales. Tiempo estimado: 10 min." << endl;
    }
};

// Estrategia 3: Ruta en transporte público
class RutaTransportePublico : public EstrategiaRuta {
public:
    void calcularRuta(string origen, string destino) override {
        cout << " Calculando ruta en TRANSPORTE PUBLICO desde " << origen << " hasta " << destino << "..." << endl;
        cout << "Ruta sugerida: linea 221 hasta estacion central, luego metro linea verde. Tiempo estimado: 18 min." << endl;
    }
};

//
// ---------------------------- CONTEXTO ----------------------------
//

class Navegador {
private:
    EstrategiaRuta* estrategia; // Puntero a la estrategia actual

public:
    // Constructor
    Navegador() : estrategia(nullptr) {}

    // Cambiar la estrategia (por ejemplo: peatonal, coche, etc.)
    void setEstrategia(EstrategiaRuta* nuevaEstrategia) {
        estrategia = nuevaEstrategia;
    }

    // Ejecutar el cálculo de ruta con la estrategia seleccionada
    void calcular(string origen, string destino) {
        if (estrategia)
            estrategia->calcularRuta(origen, destino);
        else
            cout << " No hay estrategia seleccionada." << endl;
    }
};

//
// ---------------------------- CLIENTE (main) ----------------------------
//

int main() {
    Navegador app;  // Creamos el contexto

    // Creamos las estrategias concretas
    RutaPeatonal peaton;
    RutaCoche coche;
    RutaTransportePublico transporte;

    string origen, destino;
    int opcion;

    cout << "==============================" << endl;
    cout << "   NAVEGADOR DE RUTAS" << endl;
    cout << "==============================" << endl;

    cout << "Ingrese punto de origen: ";
    getline(cin, origen);
    cout << "Ingrese punto de destino: ";
    getline(cin, destino);

    do {
        cout << "\nSeleccione el medio de transporte:" << endl;
        cout << "1. Peatonal" << endl;
        cout << "2. Coche" << endl;
        cout << "3. Transporte Publico" << endl;
        cout << "0. Salir" << endl;
        cout << "Opcion: ";
        cin >> opcion;

        switch (opcion) {
            case 1:
                app.setEstrategia(&peaton);
                app.calcular(origen, destino);
                break;
            case 2:
                app.setEstrategia(&coche);
                app.calcular(origen, destino);
                break;
            case 3:
                app.setEstrategia(&transporte);
                app.calcular(origen, destino);
                break;
            case 0:
                cout << "Saliendo del programa..." << endl;
                break;
            default:
                cout << " Opcion no valida." << endl;
        }

    } while (opcion != 0);

    return 0;
}


/*
Estrategia base (EstrategiaRuta): define el método abstracto calcularRuta().
Todas las estrategias concretas deben implementarlo.

Estrategias concretas (RutaPeatonal, RutaCoche, RutaTransportePublico):
implementan el cálculo de ruta según su tipo.

Contexto (Navegador): contiene un puntero a una estrategia.
No sabe cuál estrategia concreta usa; simplemente llama a calcular().

Cliente (main): el usuario (por consola) elige la estrategia a usar, y el contexto cambia de comportamiento en tiempo de ejecución.
*/