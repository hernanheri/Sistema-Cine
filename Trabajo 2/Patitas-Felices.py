# Clase Producto
class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self._nombre = nombre
        self._categoria = categoria
        self._precio = precio
        self._cantidad = cantidad

    # Getters y Setters
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, value):
        self._categoria = value

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        if value < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = value

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, value):
        if value < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self._cantidad = value

    def __str__(self):
        return f"{self._nombre} ({self._categoria}) - ${self._precio} - Stock: {self._cantidad}"


# Clase Cliente
class Cliente:
    def __init__(self, nombre, identificacion):
        self._nombre = nombre
        self._identificacion = identificacion
        self._historial_compras = []

    # Getters y Setters
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def identificacion(self):
        return self._identificacion

    @identificacion.setter
    def identificacion(self, value):
        self._identificacion = value

    @property
    def historial_compras(self):
        return self._historial_compras

    def agregar_compra(self, venta):
        self._historial_compras.append(venta)

    def mostrar_historial(self):
        print(f"Historial de compras de {self._nombre}:")
        for venta in self._historial_compras:
            print(venta)


# Clase Venta
class Venta:
    def __init__(self, cliente, productos):
        self._cliente = cliente
        self._productos = productos
        self._monto_total = self.calcular_monto_total()

    # Getters y Setters
    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, value):
        self._cliente = value

    @property
    def productos(self):
        return self._productos

    @productos.setter
    def productos(self, value):
        self._productos = value

    @property
    def monto_total(self):
        return self._monto_total

    def calcular_monto_total(self):
        total = 0
        for producto in self._productos:
            if producto.cantidad <= 0:
                raise ValueError(f"No hay suficiente stock de {producto.nombre}.")
            total += producto.precio
            producto.cantidad -= 1  # Reducir el inventario
        return total

    def __str__(self):
        return f"Venta a {self._cliente.nombre} - Monto: ${self._monto_total}"


# Ejemplo de uso
# Crear productos
producto1 = Producto("Croquetas para perro", "Alimento", 20.0, 10)
producto2 = Producto("Juguete para gato", "Juguete", 10.0, 5)

# Crear cliente
cliente1 = Cliente("Juan Perez", "12345678")

# Realizar una venta
try:
    venta1 = Venta(cliente1, [producto1, producto2])
    cliente1.agregar_compra(venta1)
    print("Venta realizada con éxito!")
except ValueError as e:
    print(f"Error: {e}")

# Mostrar información
print("\nProductos disponibles:")
print(producto1)
print(producto2)

print("\nHistorial del cliente:")
cliente1.mostrar_historial()