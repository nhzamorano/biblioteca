from Multa.estrategiamulta import EstrategiaMulta
class Multa:
    def __init__(self, id_multa, usuario, monto, dias_retraso, estrategia_multa: EstrategiaMulta):
        self.id_multa = id_multa
        self.usuario = usuario
        self.monto = monto
        self.dias_retraso = dias_retraso
        self.estrategia_multa = estrategia_multa

    def calcular_multa(self):
        self.monto = self.estrategia_multa.calcular_multa(self.dias_retraso)
        print(f"Multa calculada: {self.monto}")

    def aplicar_multa(self):
        print(f"Aplicando multa de {self.monto} al usuario {self.usuario.nombre_completo}")
        self.usuario.pagar_multa(self.monto)
