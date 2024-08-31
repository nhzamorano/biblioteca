from estrategiamulta import EstrategiaMulta
class MultaVariable(EstrategiaMulta):
    def calcular_multa(self, dias_retraso):
        tasa_variable = dias_retraso * 1.5
        return tasa_variable