#ifndef DRONE_HPP
#define DRONE_HPP

#include <string>
#include "DroneAPI.hpp"
using namespace std;

class Drone {
private:
    string id;
    DroneAPI* api;

public:
    Drone(string id, DroneAPI* api);

    void takeOff();
    void land();
    void ascend(int meters);
    void descend(int meters);
    void turnRight();
    void turnLeft();
    void accelerate();
    void brake();
    void unloadPackage();
    void takePhoto();
    void notifyDelivery();
};

#endif
