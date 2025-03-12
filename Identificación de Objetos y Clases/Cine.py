import uuid
from datetime import datetime

# 🧑‍💼 Clase Cliente
class Cliente:
    def __init__(self, nombre, correo, telefono, contraseña):
        self._nombre = nombre
        self._correo = correo
        self._telefono = telefono
        self._contraseña = contraseña
        self._reservas = []  # Historial de reservas

    # Getters y Setters con validaciones
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if not value.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = value

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, value):
        if "@" not in value:
            raise ValueError("Correo electrónico inválido.")
        self._correo = value

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("El teléfono debe tener 10 dígitos.")
        self._telefono = value

    @property
    def reservas(self):
        return self._reservas

    def agregar_reserva(self, reserva):
        if not isinstance(reserva, Reserva):
            raise TypeError("Debe ser una instancia de la clase Reserva.")
        self._reservas.append(reserva)

    def mostrar_reservas(self):
        if not self._reservas:
            print(f"{self._nombre} no tiene reservas.")
        for reserva in self._reservas:
            print(reserva)

# 🎬 Clase Película
class Pelicula:
    def __init__(self, titulo, genero, duracion, clasificacion, formato):
        self._titulo = titulo
        self._genero = genero
        self._duracion = duracion
        self._clasificacion = clasificacion
        self._formato = formato

    # Getters
    @property
    def titulo(self):
        return self._titulo

    @property
    def genero(self):
        return self._genero

    @property
    def duracion(self):
        return self._duracion

    @property
    def clasificacion(self):
        return self._clasificacion

    @property
    def formato(self):
        return self._formato

    def __str__(self):
        return f"{self._titulo} - {self._genero} ({self._formato}) - {self._duracion} min - {self._clasificacion}"

# 🎟️ Clase Sala
class Sala:
    def __init__(self, numero, capacidad, formato):
        self._numero = numero
        self._capacidad = capacidad
        self._formato = formato
        self._horarios = []  # Lista de horarios programados

    # Getters y Setters
    @property
    def numero(self):
        return self._numero

    @property
    def capacidad(self):
        return self._capacidad

    @property
    def formato(self):
        return self._formato

    @property
    def horarios(self):
        return self._horarios

    def agregar_horario(self, horario):
        if not isinstance(horario, Horario):
            raise TypeError("El horario debe ser una instancia de la clase Horario.")
        # Verifica si hay empalme de horarios
        for h in self._horarios:
            if h.fecha_hora == horario.fecha_hora:
                raise ValueError("Ya hay una función programada a esa hora.")
        self._horarios.append(horario)

    def __str__(self):
        return f"Sala {self._numero} - {self._formato} - Capacidad: {self._capacidad} asientos"

# ⏳ Clase Horario
class Horario:
    def __init__(self, fecha_hora, pelicula, sala):
        self._fecha_hora = fecha_hora
        self._pelicula = pelicula
        self._sala = sala

    # Getters
    @property
    def fecha_hora(self):
        return self._fecha_hora

    @property
    def pelicula(self):
        return self._pelicula

    @property
    def sala(self):
        return self._sala

    def __str__(self):
        return f"{self._pelicula.titulo} - Sala {self._sala.numero} - {self._fecha_hora.strftime('%d/%m/%Y %H:%M')}"

# ✅ Clase Reserva
class Reserva:
    def __init__(self, cliente, horario, boletos):
        if boletos <= 0:
            raise ValueError("Debe reservar al menos un boleto.")
        if boletos > horario.sala.capacidad:
            raise ValueError("No hay suficientes asientos disponibles.")

        self._codigo = str(uuid.uuid4())[:8]  # Código único de reserva
        self._cliente = cliente
        self._horario = horario
        self._boletos = boletos

        # Actualiza la capacidad de la sala
        horario.sala._capacidad -= boletos

    # Getters
    @property
    def codigo(self):
        return self._codigo

    @property
    def cliente(self):
        return self._cliente

    @property
    def horario(self):
        return self._horario

    @property
    def boletos(self):
        return self._boletos

    def __str__(self):
        return (f"Reserva {self._codigo} - Cliente: {self._cliente.nombre} - Película: {self._horario.pelicula.titulo} "
                f"- Sala {self._horario.sala.numero} - Boletos: {self._boletos}")

# 🎬 Ejemplo de uso
pelicula1 = Pelicula("El Gran Show", "Drama", 120, "PG-13", "2D")
sala1 = Sala(1, 50, "2D")
horario1 = Horario(datetime(2025, 3, 15, 20, 0), pelicula1, sala1)
sala1.agregar_horario(horario1)

cliente1 = Cliente("Juan Patricio", "juanpi@email.com", "1234567890", "paydelimon666")

# Realizar una reserva
try:
    reserva1 = Reserva(cliente1, horario1, 3)
    cliente1.agregar_reserva(reserva1)
    print("✅ ¡Reserva realizada con éxito!")
except (ValueError, TypeError) as e:
    print(f"❌ Error: {e}")

# Mostrar reservas del cliente
print("\n📅 Reservas del cliente:")
cliente1.mostrar_reservas()

# Verificar sala y horario
print("\n🎥 Información de la sala y horarios:")
print(sala1)
for horario in sala1.horarios:
    print(horario)
