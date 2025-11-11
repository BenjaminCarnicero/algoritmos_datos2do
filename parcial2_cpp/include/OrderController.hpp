#ifndef ORDER_CONTROLLER_HPP
#define ORDER_CONTROLLER_HPP

#include <list>
#include "Provider.hpp"
#include "Order.hpp"
#include "Employee.hpp"
using namespace std;

class OrderController {
private:
    list<Provider*> providers;
    list<Order*> orders;
    int nextOrderId;

public:
    OrderController();

    // CRUD de Proveedores
    void create(int id, string name, string address, int phone);
    void read() const;
    void update(int id, string name, string address, int phone);
    void remove(int id);

    // Buscar proveedor por ID
    Provider* find(int id);

    // Gestión de órdenes
    Order* createOrder(Provider* provider, Employee* employee);
    void listOrders() const;
};

#endif
