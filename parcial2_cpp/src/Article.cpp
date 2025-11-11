#include "Article.hpp"
#include <sstream> // Cadenas de texto

Article::Article(int id, string name, double unitPrice)
    : id(id), name(name), unitPrice(unitPrice) {}

// Devuelve el ID del artículo
int Article::getId() const {
    return this->id;
}

// Devuelve el nombre del artículo
string Article::getName() const {
    return this->name;
}

// Devuelve el precio unitario del artículo
double Article::getPrice() const {
    return this->unitPrice;
}

// Devuelve una descripción formateada del artículo
string Article::toString() const {
    stringstream ss;
    ss << "ID: " << id << " | Nombre: " << name << " | Precio: $" << unitPrice;
    return ss.str();
}
