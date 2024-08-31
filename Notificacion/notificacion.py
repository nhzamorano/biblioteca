from observer.observer import Observer
class Notificacion(Observer):
    def __init__(self, id_notificacion, usuario, tipo_notificacion, contenido):
        self.id_notificacion = id_notificacion
        self.usuario = usuario
        self.tipo_notificacion = tipo_notificacion
        self.contenido = contenido

    def enviar_notificacion(self):
        print(f"Enviando notificación a {self.usuario} con contenido: {self.contenido}")

    def update(self):
        print(f"Notificación actualizada: {self.tipo_notificacion} - {self.contenido}")
