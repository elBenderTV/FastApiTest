import json
from models import Empleado

class GestorEmpleados:
    def __init__(self, ruta_archivo="empleados.json"):
        self.ruta_archivo = ruta_archivo
        self.empleados = self.cargar()

    def cargar(self):
        try:
            with open(self.ruta_archivo, "r") as archivo:
                datos = json.load(archivo)
            return [Empleado(**emp) for emp in datos]
        except FileNotFoundError:
            return []

    def guardar(self):
        with open(self.ruta_archivo, "w") as archivo:
            json.dump([emp.to_dict() for emp in self.empleados], archivo, indent=2)

    def buscar(self, id=None, nombre=None):
        for emp in self.empleados:
            if (id is not None and emp.id == id) or (nombre is not None and emp.nombre == nombre):
                return emp
        return None

    def crear(self, nombre, puesto):
        nuevo_id = max([emp.id for emp in self.empleados], default=-1) + 1
        nuevo_emp = Empleado(nuevo_id, nombre, puesto)
        self.empleados.append(nuevo_emp)
        self.guardar()
        return nuevo_emp

    def actualizar(self, id, nombre=None, puesto=None):
        emp = self.buscar(id=id)
        if emp:
            if nombre:
                emp.nombre = nombre
            if puesto:
                emp.puesto = puesto
            self.guardar()
            return emp
        return None

    def eliminar(self, id=None, nombre=None):
        emp = self.buscar(id=id, nombre=nombre)
        if emp:
            self.empleados.remove(emp)
            self.guardar()
            return emp
        return None
