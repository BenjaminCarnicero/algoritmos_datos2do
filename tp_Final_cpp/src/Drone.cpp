#include "Drone.hpp"

Drone::Drone(string id, DroneAPI* api)
    : id(id), api(api) {}

void Drone::takeOff() { api->takeOff(); }
void Drone::land() { api->land(); }
void Drone::ascend(int meters) { api->ascend(meters); }
void Drone::descend(int meters) { api->descend(meters); }
void Drone::turnRight() { api->turnRight(); }
void Drone::turnLeft() { api->turnLeft(); }
void Drone::accelerate() { api->accelerate(); }
void Drone::brake() { api->brake(); }
void Drone::unloadPackage() { api->unloadPackage(); }
void Drone::takePhoto() { api->takePhoto(); }
void Drone::notifyDelivery() { api->notifyDelivery(); }

