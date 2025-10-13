#include <iostream>
#include <memory>
using namespace std;

// -------------------- PRODUCTOS ABSTRACTOS --------------------
class Chair {
public:
    virtual void sitOn() = 0;
    virtual ~Chair() = default;
};

class Sofa {
public:
    virtual void lieOn() = 0;
    virtual ~Sofa() = default;
};

class CoffeeTable {
public:
    virtual void placeOn() = 0;
    virtual ~CoffeeTable() = default;
};

// -------------------- PRODUCTOS CONCRETOS --------------------
// Modern
class ModernChair : public Chair {
public:
    void sitOn() override { cout << "Sitting on a Modern Chair" << endl; }
};
class ModernSofa : public Sofa {
public:
    void lieOn() override { cout << "Lying on a Modern Sofa" << endl; }
};
class ModernCoffeeTable : public CoffeeTable {
public:
    void placeOn() override { cout << "Placing coffee on a Modern Coffee Table" << endl; }
};

// Victorian
class VictorianChair : public Chair {
public:
    void sitOn() override { cout << "Sitting on a Victorian Chair" << endl; }
};
class VictorianSofa : public Sofa {
public:
    void lieOn() override { cout << "Lying on a Victorian Sofa" << endl; }
};
class VictorianCoffeeTable : public CoffeeTable {
public:
    void placeOn() override { cout << "Placing tea on a Victorian Coffee Table" << endl; }
};

// ArtDeco
class ArtDecoChair : public Chair {
public:
    void sitOn() override { cout << "Sitting on an ArtDeco Chair" << endl; }
};
class ArtDecoSofa : public Sofa {
public:
    void lieOn() override { cout << "Lying on an ArtDeco Sofa" << endl; }
};
class ArtDecoCoffeeTable : public CoffeeTable {
public:
    void placeOn() override { cout << "Placing magazines on an ArtDeco Coffee Table" << endl; }
};

// -------------------- FÁBRICA ABSTRACTA --------------------
class FurnitureFactory {
public:
    virtual unique_ptr<Chair> createChair() = 0;
    virtual unique_ptr<Sofa> createSofa() = 0;
    virtual unique_ptr<CoffeeTable> createCoffeeTable() = 0;
    virtual ~FurnitureFactory() = default;
};

// -------------------- FÁBRICAS CONCRETAS --------------------
class ModernFactory : public FurnitureFactory {
public:
    unique_ptr<Chair> createChair() override { return make_unique<ModernChair>(); }
    unique_ptr<Sofa> createSofa() override { return make_unique<ModernSofa>(); }
    unique_ptr<CoffeeTable> createCoffeeTable() override { return make_unique<ModernCoffeeTable>(); }
};

class VictorianFactory : public FurnitureFactory {
public:
    unique_ptr<Chair> createChair() override { return make_unique<VictorianChair>(); }
    unique_ptr<Sofa> createSofa() override { return make_unique<VictorianSofa>(); }
    unique_ptr<CoffeeTable> createCoffeeTable() override { return make_unique<VictorianCoffeeTable>(); }
};

class ArtDecoFactory : public FurnitureFactory {
public:
    unique_ptr<Chair> createChair() override { return make_unique<ArtDecoChair>(); }
    unique_ptr<Sofa> createSofa() override { return make_unique<ArtDecoSofa>(); }
    unique_ptr<CoffeeTable> createCoffeeTable() override { return make_unique<ArtDecoCoffeeTable>(); }
};

// -------------------- CLIENTE --------------------
class FurnitureStore {
private:
    unique_ptr<FurnitureFactory> factory;

public:
    FurnitureStore(unique_ptr<FurnitureFactory> f) : factory(move(f)) {}

    void showCollection() {
        auto chair = factory->createChair();
        auto sofa = factory->createSofa();
        auto table = factory->createCoffeeTable();

        chair->sitOn();
        sofa->lieOn();
        table->placeOn();
    }
};

// -------------------- MAIN --------------------
int main() {
    cout << "--- Collection Moderna ---" << endl;
    FurnitureStore modernStore(make_unique<ModernFactory>());
    modernStore.showCollection();

    cout << "\n--- Collection Victoriana ---" << endl;
    FurnitureStore victorianStore(make_unique<VictorianFactory>());
    victorianStore.showCollection();

    cout << "\n--- Collection ArtDeco ---" << endl;
    FurnitureStore artDecoStore(make_unique<ArtDecoFactory>());
    artDecoStore.showCollection();

    return 0;
}



/*
Cada producto (Chair, Sofa, CoffeeTable) tiene una interfaz abstracta.

Las clases como ModernChair o VictorianSofa son implementaciones concretas de esas interfaces.

La clase FurnitureFactory define qué métodos deben tener las fábricas (crear silla, sofá y mesa).

Cada fábrica concreta (ModernFactory, VictorianFactory, ArtDecoFactory) implementa esos métodos para su familia.

El cliente (FurnitureStore) usa la fábrica sin preocuparse de qué tipo de muebles crea.
Solo llama a los métodos de la fábrica y obtiene los productos listos.
*/