#ifndef REALDRONEAPI_HPP
#define REALDRONEAPI_HPP

#include "DroneAPI.hpp"
#include <iostream>
using namespace std;

class RealDroneAPI : public DroneAPI {
public:
    void takeOff() override;
    void land() override;
    void ascend(int m) override;
    void descend(int m) override;
    void turnRight() override;
    void turnLeft() override;
    void accelerate() override;
    void brake() override;
    void unloadPackage() override;
    void takePhoto() override;
    void notifyDelivery() override;
};

#endif
