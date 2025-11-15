#include <gtest/gtest.h>
#include "Drone.hpp"
#include "MockDroneAPI.hpp"

TEST(DroneTest, TakeOffCallsAPI) {
    MockDroneAPI api;
    Drone drone("TEST", &api);

    drone.takeOff();

    EXPECT_TRUE(api.takeOffCalled);
}

TEST(DroneTest, UnloadPackageCallsAPI) {
    MockDroneAPI api;
    Drone drone("TEST", &api);

    drone.unloadPackage();

    EXPECT_TRUE(api.unloadCalled);
}
