#ifndef ORDERITEM_HPP
#define ORDERITEM_HPP

#include "Article.hpp"
using namespace std;

class OrderItem {
private:
    Article* article;
    int quantity;

public:
    OrderItem(Article* article, int quantity);

    Article* getArticle() const;
    int getQuantity() const;
    double subTotal() const;
};

#endif
