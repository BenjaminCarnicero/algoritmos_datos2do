#include "Order.hpp"
#include <iostream>
#include <iomanip>
#include <ctime>
using namespace std;

Order::Order(int id, Provider* provider, Employee* employee)
    : id(id), provider(provider), employee(employee), status("PEDIDO CONFIRMADO") {
    time_t now = time(0);
    createdAt = ctime(&now);
    createdAt.pop_back();
}

Order::~Order() {
    for (auto item : itemsList)
        delete item;
    itemsList.clear();
}

void Order::attach(Article* article, int quantity) {
    OrderItem* newItem = new OrderItem(article, quantity);
    itemsList.push_back(newItem);
}

void Order::remove(int articleId) {
    for (auto it = itemsList.begin(); it != itemsList.end(); ++it) {
        Article* art = (*it)->getArticle();
        if (art->getId() == articleId) {
            delete *it;
            itemsList.erase(it);
            break;
        }
    }
}

double Order::getTotal() const {
    double total = 0;
    for (auto item : itemsList)
        total += item->subTotal();
    return total;
}

void Order::getShow() const {
    cout << "---------------------------------------" << endl;
    cout << "ORDEN #" << id << " | Estado: " << status << endl;
    cout << "Fecha: " << createdAt << endl;
    cout << provider->toString() << endl;
    cout << employee->toString() << endl;
    cout << "---------------------------------------" << endl;

    for (auto item : itemsList) {
        Article* art = item->getArticle();
        cout << "- " << art->getName()
             << " | Cantidad: " << item->getQuantity()
             << " | Precio Unitario: $" << fixed << setprecision(2) << art->getPrice()
             << " | Subtotal: $" << fixed << setprecision(2) << item->subTotal() << endl;
    }

    cout << "TOTAL: $" << fixed << setprecision(2) << getTotal() << endl;
    cout << "---------------------------------------" << endl;
}
