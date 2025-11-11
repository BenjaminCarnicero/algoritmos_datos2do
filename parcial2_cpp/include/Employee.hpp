#pragma once
#include <string>
using namespace std;

class Employee {
    private:
        int id;
        string name;
        string jobTitle;

    public:
        Employee(int id, string name, string jobTitle);
        int getId() const;
        string getName() const;
        string getJobTitle() const;
        string toString() const;
};
