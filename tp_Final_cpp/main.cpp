#include <iostream>
#include "Drone.hpp"
#include "DroneController.hpp"
#include "RealDroneAPI.hpp"
#include "ConsoleUtils.hpp"

using namespace std;


/*
Como en el parcial no tenemos acceso a la API real del dron físico, 
la simulamos creando una clase llamada DroneAPI que representa las funciones que tendría un SDK externo real.
Nuestro dron llama a esa API y el controlador gestiona las acciones. 
Gracias a este diseño puedo reemplazar la API real en el futuro sin tocar la lógica del sistema.
*/

int main() {

    RealDroneAPI api;
    Drone drone("IBAG151", &api);
    DroneController controller(&drone);

    int opcion = -1;
    int metros = 0;

    while (opcion != 0) {

        ConsoleUtils::clear();

        cout << "===== MENU DRON =====\n";
        cout << "1. Despegar\n";
        cout << "2. Aterrizar\n";
        cout << "3. Subir metros\n";
        cout << "4. Bajar metros\n";
        cout << "5. Girar derecha\n";
        cout << "6. Girar izquierda\n";
        cout << "7. Acelerar\n";
        cout << "8. Frenar\n";
        cout << "9. Descargar paquete\n";
        cout << "10. Sacar foto\n";
        cout << "11. Notificar entrega\n";
        cout << "12. Mision completa\n";
        cout << "0. Salir\n";
        cout << "Opcion: ";
        cin >> opcion;

        ConsoleUtils::clear();

        switch (opcion) {
            case 1: controller.takeOff(); ConsoleUtils::pause(); break;
            case 2: controller.land(); ConsoleUtils::pause(); break;
            case 3:
                cout << "Metros: "; cin >> metros;
                controller.ascend(metros);
                ConsoleUtils::pause();
                break;
            case 4:
                cout << "Metros: "; cin >> metros;
                controller.descend(metros);
                ConsoleUtils::pause();
                break;
            case 5: controller.turnRight(); ConsoleUtils::pause(); break;
            case 6: controller.turnLeft(); ConsoleUtils::pause(); break;
            case 7: controller.accelerate(); ConsoleUtils::pause(); break;
            case 8: controller.brake(); ConsoleUtils::pause(); break;
            case 9: controller.dropPackage(); ConsoleUtils::pause(); break;
            case 10: controller.takePhoto(); ConsoleUtils::pause(); break;
            case 11: controller.notifyDelivery(); ConsoleUtils::pause(); break;
            case 12: controller.startMission(); ConsoleUtils::pause(); break;

            case 0:
                cout << "Saliendo...\n";
                break;

            default:
                cout << "Opción invalida.\n";
                ConsoleUtils::pause();
        }
    }

    return 0;
}
