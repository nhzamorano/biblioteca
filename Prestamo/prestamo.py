from Multa.estrategiamulta import EstrategiaMulta
class Prestamo:
    def __init__(self, id_prestamo, usuario, ejemplar, fecha_prestamo, fecha_devolucion, tipo_prestamo):
        self.id_prestamo = id_prestamo
        self.usuario = usuario
        self.ejemplar = ejemplar
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.tipo_prestamo = tipo_prestamo

    def registrar_prestamo(self):
        print(f"Préstamo registrado para el usuario {self.usuario.nombre_completo} con el ejemplar {self.ejemplar.id_ejemplar}")

    def marcar_devolucion(self):
        print(f"Devolución marcada para el ejemplar {self.ejemplar.id_ejemplar}")

    def calcular_multa(self, estrategia: EstrategiaMulta):
        dias_retraso = (self.fecha_devolucion - self.fecha_prestamo).days
        multa = estrategia.calcular_multa(dias_retraso)
        print(f"Multa calculada: {multa}")