#include <iostream>
#include <string>
#include "OrderController.hpp"
#include "Article.hpp"
#include "Employee.hpp"
#include "Provider.hpp"
using namespace std;

int main() {
    OrderController controller;
    int option = -1;

    // Algunos datos hardcodeados (empleados y articulos)
    Employee emp1(1, "Pablo Perez", "Encargado de Compras");
    Employee emp2(2, "Laura Fernandez", "Administrativa");
    Article art1(10, "Plancha de Goma Negra", 1500.50);
    Article art2(11, "Manguera Industrial", 750.00);
    Article art3(12, "Burletes para automotor", 320.75);

    do {
        cout << "\n=== MENU PRINCIPAL ===\n";
        cout << "1. Listar proveedores\n";
        cout << "2. Agregar proveedor\n";
        cout << "3. Modificar proveedor\n";
        cout << "4. Eliminar proveedor\n";
        cout << "5. Crear pedido\n";
        cout << "6. Listar pedidos\n";
        cout << "0. Salir\n";
        cout << "Seleccione una opcion: ";
        cin >> option;
        cin.ignore();

        switch (option) {
            case 1:
                controller.read();
                break;

            case 2: {
                int id, phone;
                string name, address;
                cout << "Ingrese ID: "; cin >> id; cin.ignore();
                cout << "Ingrese nombre: "; getline(cin, name);
                cout << "Ingrese direccion: "; getline(cin, address);
                cout << "Ingrese telefono: "; cin >> phone;
                controller.create(id, name, address, phone);
                break;
            }

            case 3: {
                int id, phone;
                string name, address;
                cout << "Ingrese ID a modificar: "; cin >> id; cin.ignore();
                cout << "Nuevo nombre: "; getline(cin, name);
                cout << "Nueva direccion: "; getline(cin, address);
                cout << "Nuevo telefono: "; cin >> phone;
                controller.update(id, name, address, phone);
                break;
            }

            case 4: {
                int id;
                cout << "Ingrese ID a eliminar: "; cin >> id;
                controller.remove(id);
                break;
            }

            case 5: {
                cout << "\n=== CREAR NUEVO PEDIDO ===\n";
                int providerId;
                cout << "Ingrese el ID del proveedor: ";
                cin >> providerId;

                Provider* provider = controller.find(providerId);
                if (!provider) {
                    cout << "Proveedor no encontrado.\n";
                    break;
                }

                cout << "Seleccione el empleado responsable:\n";
                cout << "1. " << emp1.getName() << "\n";
                cout << "2. " << emp2.getName() << "\n";
                int empOption;
                cin >> empOption;
                Employee* empleadoSeleccionado = (empOption == 1) ? &emp1 : &emp2;

                // Crear la orden
                Order* nuevaOrden = controller.createOrder(provider, empleadoSeleccionado);

                cout << "\n Agregue articulos al pedido:\n";
                int opcionArticulo = -1;
                do {
                    cout << "\n1. " << art1.toString();
                    cout << "\n2. " << art2.toString();
                    cout << "\n3. " << art3.toString();
                    cout << "\n0. Finalizar carga\n";
                    cout << "Seleccione un articulo: ";
                    cin >> opcionArticulo;

                    if (opcionArticulo == 0) break;

                    int cantidad;
                    cout << "Cantidad: ";
                    cin >> cantidad;

                    if (opcionArticulo == 1)
                        nuevaOrden->attach(&art1, cantidad);
                    else if (opcionArticulo == 2)
                        nuevaOrden->attach(&art2, cantidad);
                    else if (opcionArticulo == 3)
                        nuevaOrden->attach(&art3, cantidad);

                } while (opcionArticulo != 0);

                cout << "\n Pedido creado exitosamente.\n";
                nuevaOrden->getShow();
                break;
            }

            case 6:
                controller.listOrders();
                break;

            case 0:
                cout << "Saliendo del sistema...\n";
                break;

            default:
                cout << "Opción invalida.\n";
        }

    } while (option != 0);

    return 0;
}
