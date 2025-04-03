from fastapi import FastAPI
from typing import Optional
import json

# Posibles cambios:
#   Puedo encapsular la busqueda de usuarios en una sola función

app = FastAPI(
    title="Examen Corte 1",
    description="¡Este examen esta hecho para la universidad CUES!",
    version="1.0"
)

# Cargamos y Escribimos los archivos json
def cargar_empleados():
     with open("empleados.json", "r") as archivo:
          return json.load(archivo)
empleados = cargar_empleados()

def guardar_empleados():
    with open("empleados.json", "w") as archivo:
        json.dump(empleados, archivo, indent=2)


#!Codigo FastAPI

# Terminado
@app.get('/empleados', tags=['Empleados'])
def listar_empleados():
    return empleados


# Terminado
@app.get('/ver', tags=['Empleados'])
def ver_empleado(id: Optional[int] = None,nombre: Optional[str] = None):
          for index, emp in enumerate(empleados):
            if (id is not None and emp['id'] == id) or (nombre is not None and emp['nombre'] == nombre):
              empleado = empleados[index]
              return {
                  "finded": True,
                  "empleado": empleado
              }
            return {"finded": False}

# Terminado
@app.post('/crear', tags=['Empleados'])
def crear_empleado(nombre: str, puesto: str):
        nuevo_id = max(emp['id'] for emp in empleados) + 1 if empleados else 0
        nuevo_empleado={
        "id": nuevo_id,
        "nombre": nombre,
        "puesto": puesto
        }
        empleados.append(nuevo_empleado)
        guardar_empleados()
        return nuevo_empleado


@app.put('/actualizar', tags=['Empleados'])
def actualizar_empleado(id: int, nombre: Optional[str] = None, puesto: Optional[str] = None):
    for index, emp in enumerate(empleados):
        if emp['id'] == id:
        # Actualizar solo los campos proporcionados
            if nombre is not None:
                empleados[index]['nombre'] = nombre
            if puesto is not None:
                empleados[index]['puesto'] = puesto

            guardar_empleados()  # Guardar cambios en JSON

            return {
                "updated": True,
                "empleado": empleados[index]
            }

    return {"updated": False}  # Si no encuentra el ID

# Terminado
@app.delete('/eliminar', tags=['Empleados'])
def eliminar_empleado(id: Optional[int] = None,nombre: Optional[str] = None):
        for index, emp in enumerate(empleados):
          if (id is not None and emp['id'] == id) or (nombre is not None and emp['nombre'] == nombre):
              empleado_eliminado = empleados[index]
              empleados.pop(index)
              guardar_empleados()
              return {
                  "deleted": True,
                  "empleado": empleado_eliminado
              }
        return {"deleted": False}




