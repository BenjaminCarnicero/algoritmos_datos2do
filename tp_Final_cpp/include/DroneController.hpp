#ifndef DRONE_CONTROLLER_HPP
#define DRONE_CONTROLLER_HPP

#include "Drone.hpp"

class DroneController {
private:
    Drone* drone;

public:
    DroneController(Drone* d);  // Solo declaración
    void startMission();        // Declaración agregada

    // Métodos para llamar a la API
    void takeOff();
    void land();
    void ascend(int meters);
    void descend(int meters);
    void turnRight();
    void turnLeft();
    void accelerate();
    void brake();
    void dropPackage();
    void takePhoto();
    void notifyDelivery();
};

#endif
