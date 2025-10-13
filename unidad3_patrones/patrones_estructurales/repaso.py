class OldRoad:
    def get_road(self):
        return "Ruta antigua: Buenos Aires - Mar del Plata"

class RoadAdapter:
    def __init__(self, old_road):
        self.old_road = old_road

    def get_new_format(self):
        # se adapta el formato viejo al nuevo sistema
        old_format = self.old_road.get_road()
        return f"[Actualizada] {old_format} - Formato actualizado."

# Uso
old = OldRoad()
adapted = RoadAdapter(old)
print(adapted.get_new_format())


################################
##adapter
# Sistema antiguo
class Artista:
    def __init__(self, nombre, genero):
        self.nombre = nombre
        self.genero = genero

    def mostrar_info(self):
        return f"{self.nombre} ({self.genero})"


# API nueva devuelve diccionarios (JSON)
class APIArtistas:
    def obtener_artista(self):
        return {"nombre": "MiloJ", "genero": "Folklore"}


# Adapter para compatibilizar ambos sistemas
class ArtistaAdapter:
    def __init__(self, api_artista):
        self.api_artista = api_artista

    def obtener_objeto_artista(self):
        datos = self.api_artista.obtener_artista()
        return Artista(datos["nombre"], datos["genero"])


# Uso del Adapter
api = APIArtistas()
adaptador = ArtistaAdapter(api)
artista = adaptador.obtener_objeto_artista()

print(artista.mostrar_info())




################################
# Clase base
class Evento:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def descripcion(self):
        return f"Evento: {self.nombre} - Precio base: ${self.precio}"


# Decoradores
class DescuentoPreventa:
    def __init__(self, evento):
        self.evento = evento

    def descripcion(self):
        nuevo_precio = self.evento.precio * 0.8
        return self.evento.descripcion() + f" | Descuento preventa: ${nuevo_precio}"


class AccesoVIP:
    def __init__(self, evento):
        self.evento = evento

    def descripcion(self):
        return self.evento.descripcion() + " | Acceso VIP incluido"


# Uso
evento = Evento("Musicandelaria Fest", 10000)
evento_con_descuento = DescuentoPreventa(evento)
evento_vip = AccesoVIP(evento_con_descuento)

print(evento_vip.descripcion())




################################




## decorator
class Road:
    def __init__(self, origin, destination, points):
        self.origin = origin
        self.destination = destination
        self.points = points

    def description(self):
        return f"{self.origin} -> {self.destination} ({self.points} puntos)"

class LongRoadDecorator:
    def __init__(self, road):
        self.road = road

    def description(self):
        return self.road.description() + " + BONUS por ruta larga (+15 puntos)"

# Uso
route = Road("Mar del Plata", "Bariloche", 30)
better_route = LongRoadDecorator(route)
print(better_route.description())




# Composite
class Component:
    def show(self):
        pass

class Leaf(Component):
    def __init__(self, name):
        self.name = name
    def show(self):
        print(self.name)

class Group(Component):
    def __init__(self, name):
        self.name = name
        self.components = []

    def add(self, component):
        self.components.append(component)

    def show(self):
        print(f"Grupo: {self.name}")
        for component in self.components:
            component.show()

# Uso
button = Leaf("Boton")
image = Leaf("Imagen")
window = Group("Ventana Principal")
window.add(button)
window.add(image)
window.show()
