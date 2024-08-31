class Biblioteca:
    _instance = None

    @staticmethod
    def get_instance():
        if Biblioteca._instance is None:
            Biblioteca._instance = Biblioteca()
        return Biblioteca._instance

    def gestionar_usuario(self, usuario):
        print(f"Gestionando usuario: {usuario.nombre_completo}")
        #print("-------------------------------------------------")

    def gestionar_articulo(self, articulo):
        print(f"Gestionando artículo: {articulo.titulo}")
        #print("-------------------------------------------------")

    def gestionar_prestamo(self, prestamo):
        print(f"Gestionando préstamo del usuario: {prestamo.usuario.nombre_completo}")
        #print("-------------------------------------------------")