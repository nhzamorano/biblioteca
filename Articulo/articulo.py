class Articulo:
    def __init__(self, id, titulo, autor, year_publicacion, editorial, isbn, palabras_clave, categoria, cantidad_ejemplares):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.year_publicacion = year_publicacion
        self.editorial = editorial
        self.isbn = isbn
        self.palabras_clave = palabras_clave
        self.categoria = categoria
        self.cantidad_ejemplares = cantidad_ejemplares

    def consultar_disponibilidad(self):
        print(f"Consultando disponibilidad del artículo {self.titulo}")

    def marcar_perdido(self):
        print(f"Artículo {self.titulo} marcado como perdido")

    def marcar_danado(self):
        print(f"Artículo {self.titulo} marcado como dañado")