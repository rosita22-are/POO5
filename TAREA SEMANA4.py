# Clase que representa una habitación del hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        # Atributos de la habitación
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    # Método para reservar la habitación
    def reservar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    # Método para liberar la habitación
    def liberar(self):
        self.disponible = True


# Clase que representa un cliente
class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula


# Clase que gestiona el sistema de reservas
class SistemaReservas:
    def __init__(self):
        self.habitaciones = []
        self.reservas = []

    # Método para agregar habitaciones al sistema
    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    # Método para realizar una reserva
    def realizar_reserva(self, cliente, tipo_habitacion):
        for habitacion in self.habitaciones:
            if habitacion.tipo == tipo_habitacion and habitacion.disponible:
                habitacion.reservar()
                self.reservas.append((cliente, habitacion))
                print(f"Reserva realizada para {cliente.nombre} en la habitación {habitacion.numero}")
                return
        print("No hay habitaciones disponibles de ese tipo.")

    # Método para mostrar las reservas
    def mostrar_reservas(self):
        for cliente, habitacion in self.reservas:
            print(f"Cliente: {cliente.nombre} - Habitación: {habitacion.numero} ({habitacion.tipo})")


# Programa principal
if __name__ == "__main__":
    # Crear sistema de reservas
    sistema = SistemaReservas()

    # Crear habitaciones
    h1 = Habitacion(101, "Simple", 30)
    h2 = Habitacion(102, "Doble", 50)

    # Agregar habitaciones al sistema
    sistema.agregar_habitacion(h1)
    sistema.agregar_habitacion(h2)

    # Crear cliente
    cliente1 = Cliente("Juan Pérez", "0102030405")

    # Realizar reserva
    sistema.realizar_reserva(cliente1, "Simple")

    # Mostrar reservas
    sistema.mostrar_reservas()
