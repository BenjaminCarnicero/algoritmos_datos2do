#include "Employee.hpp"
#include <sstream>

// Constructor: inicializa los datos del empleado
Employee::Employee(int id, string name, string jobTitle)
    : id(id), name(name), jobTitle(jobTitle) {}

// Devuelve el ID del empleado
int Employee::getId() const {
    return this->id;
}


string Employee::getName() const {
    return this->name;
}

string Employee::getJobTitle() const {
    return this->jobTitle;
}


string Employee::toString() const {
    stringstream ss;
    ss << "Empleado: " << name << " (" << jobTitle << ")";
    return ss.str();
}
