#ifndef ORDER_HPP
#define ORDER_HPP

#include <string>
#include <list>
#include "Provider.hpp"
#include "Employee.hpp"
#include "OrderItem.hpp"
using namespace std;

class Order {
private:
    int id;
    Provider* provider;
    Employee* employee;
    list<OrderItem*> itemsList;
    string createdAt;
    string status;

public:
    Order(int id, Provider* provider, Employee* employee);
    ~Order();

    void attach(Article* article, int quantity);
    void remove(int articleId);
    double getTotal() const;
    void getShow() const;
};

#endif

