#include "DroneController.hpp"
#include <iostream>
using namespace std;

DroneController::DroneController(Drone* d)
    : drone(d) {}

void DroneController::startMission() {
    cout << "Iniciando mision...\n";
    drone->takeOff();
    drone->ascend(10);
    drone->turnRight();
    drone->accelerate();
    drone->takePhoto();
    drone->descend(10);
    drone->land();
    cout << "! ! ! MISION CUMPLIDA ! ! !\n";
}

void DroneController::takeOff()        { drone->takeOff(); }
void DroneController::land()           { drone->land(); }
void DroneController::ascend(int m)    { drone->ascend(m); }
void DroneController::descend(int m)   { drone->descend(m); }
void DroneController::turnRight()      { drone->turnRight(); }
void DroneController::turnLeft()       { drone->turnLeft(); }
void DroneController::accelerate()     { drone->accelerate(); }
void DroneController::brake()          { drone->brake(); }
void DroneController::dropPackage()    { drone->unloadPackage(); }
void DroneController::takePhoto()      { drone->takePhoto(); }
void DroneController::notifyDelivery() { drone->notifyDelivery(); }
