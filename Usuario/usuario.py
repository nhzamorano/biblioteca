class Usuario:
    def __init__(self, id, nombre_completo, direccion, numero_celular, correo_electronico, fecha_nacimiento, ocupacion, centro_estudio):
        self.id = id
        self.nombre_completo = nombre_completo
        self.direccion = direccion
        self.numero_celular = numero_celular
        self.correo_electronico = correo_electronico
        self.fecha_nacimiento = fecha_nacimiento
        self.ocupacion = ocupacion
        self.centro_estudio = centro_estudio

    def registrar(self):
        print(f"Registrando usuario {self.nombre_completo}")

    def validar_datos(self):
        print(f"Validando datos del usuario {self.nombre_completo}")
        # Aquí iría la lógica de validación

    def consultar_historial(self):
        print(f"Consultando historial del usuario {self.nombre_completo}")

    def pagar_multa(self, multa):
        print(f"El usuario {self.nombre_completo} ha pagado la multa de {multa}")
