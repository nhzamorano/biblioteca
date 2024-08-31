class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

    def agregar_categoria(self):
        print(f"Categoría {self.nombre} agregada")

    def eliminar_categoria(self):
        print(f"Categoría {self.nombre} eliminada")