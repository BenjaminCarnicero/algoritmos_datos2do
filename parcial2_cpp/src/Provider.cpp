#include "Provider.hpp"
#include <sstream>

Provider::Provider(int id, string name, string address, int phone)
 : id(id), name(name), address(address), phone(phone) {}

int Provider::getId() const {return this->id; }
string Provider::getName() const { return this->name; }
string Provider::getAddress() const { return this->address; }
int Provider::getPhone() const { return this->phone; }

void Provider::setName(string newName) { name = newName; }
void Provider::setAddress(string newAddress) { address = newAddress; }
void Provider::setPhone(int newPhone) { phone = newPhone; }

string Provider::toString() const {
    stringstream ss;
    ss << "Proveedor: " << name << " | Direccion: " << address << " | Telefono: " << phone;
    return ss.str();
}
