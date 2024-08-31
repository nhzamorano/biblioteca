# test_biblioteca.py

from datetime import datetime, timedelta
from Usuario.usuario import Usuario
from Articulo.articulo import Articulo
from categoria.categoria import Categoria
from ejemplar.ejemplar import Ejemplar
from Prestamo.prestamo import Prestamo
from Multa.multa import Multa
from Multa.multafija import MultaFija
from Reportes.reporteconpdf import ReporteConPDF
from Biblioteca.biblioteca import Biblioteca

def test_biblioteca():
    # Crear un usuario
    usuario = Usuario(
        id=1,
        nombre_completo="Juan Pérez",
        direccion="Calle Falsa 123",
        numero_celular="123456789",
        correo_electronico="juan@example.com",
        fecha_nacimiento="1990-01-01",
        ocupacion="Estudiante",
        centro_estudio="Universidad Ficticia"
    )
    usuario.registrar()
    usuario.validar_datos()
    usuario.consultar_historial()

    # Crear un artículo
    articulo = Articulo(
        id=1,
        titulo="Programación en Python",
        autor="Guido van Rossum",
        year_publicacion=2020,
        editorial="Editorial Ficticia",
        isbn="123-4567891234",
        palabras_clave=["Python", "Programación"],
        categoria="Tecnología",
        cantidad_ejemplares=5
    )
    articulo.consultar_disponibilidad()

    # Crear una categoría
    categoria = Categoria(nombre="Tecnología")
    categoria.agregar_categoria()

    # Crear un ejemplar
    ejemplar = Ejemplar(id_ejemplar=1, estado="Disponible")
    ejemplar.cambiar_estado("Prestado")

    # Crear un préstamo
    fecha_prestamo = datetime.now()
    fecha_devolucion = fecha_prestamo + timedelta(days=15)
    prestamo = Prestamo(
        id_prestamo=1,
        usuario=usuario,
        ejemplar=ejemplar,
        fecha_prestamo=fecha_prestamo,
        fecha_devolucion=fecha_devolucion,
        tipo_prestamo="Normal"
    )
    prestamo.registrar_prestamo()

    # Crear una multa con estrategia fija
    multa = Multa(
        id_multa=1,
        usuario=usuario,
        monto=0,
        dias_retraso=10,
        estrategia_multa=MultaFija()
    )
    multa.calcular_multa()
    multa.aplicar_multa()

    # Generar un reporte en PDF
    reporte_pdf = ReporteConPDF()
    reporte_pdf.generar()

    # Obtener la instancia de la biblioteca
    biblioteca = Biblioteca.get_instance()
    biblioteca.gestionar_usuario(usuario)
    biblioteca.gestionar_articulo(articulo)
    biblioteca.gestionar_prestamo(prestamo)

if __name__ == "__main__":
    test_biblioteca()



