#pragma once
#include <string>
using namespace std;

class Article {
    private:
        int id;
        string name;
        double unitPrice;

    public:
        Article(int id, string name, double unitPrice);
        int getId() const;
        string getName() const;
        double getPrice() const;
        string toString() const;
};
