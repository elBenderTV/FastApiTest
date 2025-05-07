class Empleado:
    def __init__(self, id: int, nombre: str, puesto: str):
        self.id = id
        self.nombre = nombre
        self.puesto = puesto

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "puesto": self.puesto
        }