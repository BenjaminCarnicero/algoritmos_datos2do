#ifndef MOCK_DRONE_API_HPP
#define MOCK_DRONE_API_HPP

#include "DroneAPI.hpp"

class MockDroneAPI : public DroneAPI {
public:
    bool takeOffCalled = false;
    bool landCalled = false;
    bool ascendCalled = false;
    bool unloadCalled = false;

    void takeOff() override { takeOffCalled = true; }
    void land() override { landCalled = true; }
    void ascend(int) override { ascendCalled = true; }
    void descend(int) override {}
    void turnRight() override {}
    void turnLeft() override {}
    void accelerate() override {}
    void brake() override {}
    void unloadPackage() override { unloadCalled = true; }
    void takePhoto() override {}
    void notifyDelivery() override {}
};

#endif
