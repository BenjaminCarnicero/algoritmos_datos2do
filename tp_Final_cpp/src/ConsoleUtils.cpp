#include "ConsoleUtils.hpp"
#include <iostream>
#include <cstdlib>

using namespace std;

void ConsoleUtils::clear() {
#ifdef _WIN32
    system("cls");
#else
    system("clear");
#endif
}

void ConsoleUtils::pause() {
    cout << "\n. . . ";
    cin.ignore();
    cin.get();
}
