from Multa.estrategiamulta import EstrategiaMulta
class MultaFija(EstrategiaMulta):
    def calcular_multa(self, dias_retraso):
        tasa_fija = 5
        return tasa_fija