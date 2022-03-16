class Contact:
    def __init__(self, nombre, apellido, apodo, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.apodo = apodo
        self.telefono = telefono

    def Upload(self):
        return {"nombre": self.nombre, "apellido": self.apellido, "apodo": self.apodo, "telefono": self.telefono}