#ifndef DRONE_API_HPP
#define DRONE_API_HPP

#include <string>
using namespace std;

/*
 Interface que simula la API externa del dron.
 El dron REAL seria controlado por esta API.
*/
class DroneAPI {
public:
    virtual ~DroneAPI() {}

    virtual void takeOff() = 0;
    virtual void land() = 0;
    virtual void ascend(int meters) = 0;
    virtual void descend(int meters) = 0;
    virtual void turnRight() = 0;
    virtual void turnLeft() = 0;
    virtual void accelerate() = 0;
    virtual void brake() = 0;
    virtual void unloadPackage() = 0;
    virtual void takePhoto() = 0;
    virtual void notifyDelivery() = 0;
};

#endif
