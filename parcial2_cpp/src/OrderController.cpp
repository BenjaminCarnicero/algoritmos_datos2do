#include "OrderController.hpp"
#include <iostream>
using namespace std;

OrderController::OrderController() : nextOrderId(1) {}

void OrderController::create(int id, string name, string address, int phone) {
    providers.push_back(new Provider(id, name, address, phone));
    cout << "Proveedor agregado correctamente.\n";
}

void OrderController::read() const {
    if (providers.empty()) {
        cout << "No hay proveedores cargados.\n";
        return;
    }

    cout << "\n=== LISTA DE PROVEEDORES ===\n";
    for (auto p : providers) {
        cout << p->toString() << endl;
    }
}

void OrderController::update(int id, string name, string address, int phone) {
    for (auto p : providers) {
        if (p->getId() == id) {
            p->setName(name);
            p->setAddress(address);
            p->setPhone(phone);
            cout << "Proveedor actualizado correctamente.\n";
            return;
        }
    }
    cout << "Proveedor no encontrado.\n";
}


void OrderController::remove(int id) {
    for (auto it = providers.begin(); it != providers.end(); ++it) {
        if ((*it)->getId() == id) {
            delete *it;
            providers.erase(it);
            cout << "Proveedor eliminado.\n";
            return;
        }
    }
    cout << "Proveedor no encontrado.\n";
}

// Buscar proveedor
Provider* OrderController::find(int id) {
    for (auto p : providers) {
        if (p->getId() == id)
            return p;
    }
    return nullptr;
}

// Gestion de ordenes
Order* OrderController::createOrder(Provider* provider, Employee* employee) {
    Order* order = new Order(nextOrderId++, provider, employee);
    orders.push_back(order);
    return order;
}

void OrderController::listOrders() const {
    if (orders.empty()) {
        cout << "No hay ordenes registradas.\n";
        return;
    }

    cout << "\n=== LISTA DE ORDENES ===\n";
    for (auto o : orders) {
        o->getShow();
    }
}
