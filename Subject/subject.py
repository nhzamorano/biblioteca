class Subject:
    def __init__(self):
        self.observadores = []

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def remover_observador(self, observador):
        self.observadores.remove(observador)

    def notificar_observadores(self):
        for observador in self.observadores:
            observador.update()
