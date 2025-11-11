#include "OrderItem.hpp"

OrderItem::OrderItem(Article* article, int quantity)
    : article(article), quantity(quantity) {}

Article* OrderItem::getArticle() const {
    return this->article;
}

int OrderItem::getQuantity() const {
    return this->quantity;
}

double OrderItem::subTotal() const {

    return this->article->getPrice() * quantity;
}
