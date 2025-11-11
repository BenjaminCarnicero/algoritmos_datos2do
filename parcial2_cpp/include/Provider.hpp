#ifndef PROVIDER_HPP
#define PROVIDER_HPP

#include <string>
using namespace std;

class Provider {
private:
    int id;
    string name;
    string address;
    int phone;

public:
    Provider(int id, string name, string address, int phone);

    // Getters
    int getId() const;
    string getName() const;
    string getAddress() const;
    int getPhone() const;

    // Setters
    void setName(string newName);
    void setAddress(string newAddress);
    void setPhone(int newPhone);

    string toString() const;
};

#endif

