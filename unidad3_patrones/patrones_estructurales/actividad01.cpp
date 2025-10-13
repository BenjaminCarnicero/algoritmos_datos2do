/*Tendremos una interfaz base Alojamiento que define el método calcularPrecio().

Las clases concretas como HotelBasico, Hostel, Departamento implementan esa interfaz.

Luego creamos decoradores, que agregan servicios extra (por ejemplo: desayuno, spa, estacionamiento, etc.) sin modificar las clases originales.
*/

#include <iostream>
#include <string>
using namespace std;


// Interfaz base: define el comportamiento general
// ----------------------------------------------------
class Alojamiento {
public:
    virtual string getDescripcion() const = 0;
    virtual double calcularPrecio() const = 0;
    virtual ~Alojamiento() {}
};


// Clases concretas (componentes base)
// ----------------------------------------------------
class HotelBasico : public Alojamiento {
public:
    string getDescripcion() const override {
        return "Hotel estandar";
    }
    double calcularPrecio() const override {
        return 100.0; // precio base
    }
};

class Hostel : public Alojamiento {
public:
    string getDescripcion() const override {
        return "Hostel economico";
    }
    double calcularPrecio() const override {
        return 50.0;
    }
};

class Departamento : public Alojamiento {
public:
    string getDescripcion() const override {
        return "Departamento completo";
    }
    double calcularPrecio() const override {
        return 120.0;
    }
};


// Clase Decorador base (envoltorio general)
// ----------------------------------------------------
class AlojamientoDecorator : public Alojamiento {
protected:
    Alojamiento* alojamiento;
public:
    AlojamientoDecorator(Alojamiento* a) : alojamiento(a) {}
    virtual ~AlojamientoDecorator() { delete alojamiento; }
};


// Decoradores concretos: agregan características nuevas
// ----------------------------------------------------
class Desayuno : public AlojamientoDecorator {
public:
    Desayuno(Alojamiento* a) : AlojamientoDecorator(a) {}
    string getDescripcion() const override {
        return alojamiento->getDescripcion() + " + Desayuno incluido";
    }
    double calcularPrecio() const override {
        return alojamiento->calcularPrecio() + 20.0;
    }
};

class Spa : public AlojamientoDecorator {
public:
    Spa(Alojamiento* a) : AlojamientoDecorator(a) {}
    string getDescripcion() const override {
        return alojamiento->getDescripcion() + " + Acceso al Spa";
    }
    double calcularPrecio() const override {
        return alojamiento->calcularPrecio() + 40.0;
    }
};

class Estacionamiento : public AlojamientoDecorator {
public:
    Estacionamiento(Alojamiento* a) : AlojamientoDecorator(a) {}
    string getDescripcion() const override {
        return alojamiento->getDescripcion() + " + Estacionamiento privado";
    }
    double calcularPrecio() const override {
        return alojamiento->calcularPrecio() + 15.0;
    }
};



// MAIN
// ----------------------------------------------------
int main() {
    // Creamos un alojamiento base
    Alojamiento* miAlojamiento = new HotelBasico();

    // Le agregamos extras con decoradores
    miAlojamiento = new Desayuno(miAlojamiento);
    miAlojamiento = new Spa(miAlojamiento);
    miAlojamiento = new Estacionamiento(miAlojamiento);

    cout << "Alojamiento seleccionado: " << miAlojamiento->getDescripcion() << endl;
    cout << "Precio total: $" << miAlojamiento->calcularPrecio() << endl;

    delete miAlojamiento;
    return 0;
}



/* Alojamiento: es una interfaz que define los métodos que todos los tipos de alojamiento deben implementar.

HotelBasico, Hostel, Departamento: son clases concretas que representan alojamientos base.

AlojamientoDecorator: es una clase envoltorio abstracta, que guarda un puntero a un Alojamiento.

Desayuno, Spa, Estacionamiento: son decoradores concretos que extienden el comportamiento del alojamiento (agregan precio y descripción).

En el main, vas agregando decoradores sobre el objeto base, como si fueran capas.
*/