class Ejemplar:
    def __init__(self, id_ejemplar, estado):
        self.id_ejemplar = id_ejemplar
        self.estado = estado

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        print(f"Estado del ejemplar {self.id_ejemplar} cambiado a {self.estado}")
