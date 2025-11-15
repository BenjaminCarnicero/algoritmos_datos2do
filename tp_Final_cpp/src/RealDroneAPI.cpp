#include "RealDroneAPI.hpp"

void RealDroneAPI::takeOff()        { cout << "[API] Despegando...\n"; }
void RealDroneAPI::land()          { cout << "[API] Aterrizando...\n"; }
void RealDroneAPI::ascend(int m)   { cout << "[API] Subiendo " << m << "metros\n"; }
void RealDroneAPI::descend(int m)  { cout << "[API] Bajando " << m << "metros\n"; }
void RealDroneAPI::turnRight()     { cout << "[API] Girando hacia la derecha...\n"; }
void RealDroneAPI::turnLeft()      { cout << "[API] Girando hacia la izquierda...\n"; }
void RealDroneAPI::accelerate()    { cout << "[API] Acelerando...\n"; }
void RealDroneAPI::brake()         { cout << "[API] Frenando...\n"; }
void RealDroneAPI::unloadPackage() { cout << "[API] Descargando paquete...\n"; }
void RealDroneAPI::takePhoto()     { cout << "[API] Foto tomada correctamente\n"; }
void RealDroneAPI::notifyDelivery(){ cout << "[API] Entrega notificada.\n"; }
