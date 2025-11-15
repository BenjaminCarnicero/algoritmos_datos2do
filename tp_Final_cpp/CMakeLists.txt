cmake_minimum_required(VERSION 3.14)
project(DroneProject)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Para que VSCode entienda los includes (muy importante)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Include de tus headers
include_directories(include)

# ====== Archivos fuente explícitos ======
set(SOURCES
    src/Drone.cpp
    src/DroneController.cpp
    src/ConsoleUtils.cpp
    src/RealDroneAPI.cpp
)

# Ejecutable principal
add_executable(drone_app main.cpp ${SOURCES})

# ====== GOOGLE TEST (Forma correcta con FetchContent) ======
include(FetchContent)

FetchContent_Declare(
    googletest
    URL https://github.com/google/googletest/archive/refs/heads/main.zip
)

FetchContent_MakeAvailable(googletest)

enable_testing()

# Archivos de test
file(GLOB TEST_SOURCES tests/*.cpp)

# Ejecutable de pruebas
add_executable(run_tests ${TEST_SOURCES} ${SOURCES})

target_link_libraries(run_tests gtest gtest_main pthread)

target_include_directories(run_tests PRIVATE
    ${gtest_SOURCE_DIR}/include
)