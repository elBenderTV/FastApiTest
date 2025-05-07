from fastapi import APIRouter
from typing import Optional
from gestor import GestorEmpleados

router = APIRouter(tags=["Empleados"])
gestor = GestorEmpleados()

@router.get("/empleados")
def listar_empleados():
    return [emp.to_dict() for emp in gestor.empleados]

@router.get("/ver")
def ver_empleado(id: Optional[int] = None, nombre: Optional[str] = None):
    emp = gestor.buscar(id=id, nombre=nombre)
    if emp:
        return {"found": True, "empleado": emp.to_dict()}
    return {"found": False}

@router.post("/crear")
def crear_empleado(nombre: str, puesto: str):
    nuevo = gestor.crear(nombre, puesto)
    return nuevo.to_dict()

@router.put("/actualizar")
def actualizar_empleado(id: int, nombre: Optional[str] = None, puesto: Optional[str] = None):
    emp = gestor.actualizar(id, nombre, puesto)
    if emp:
        return {"updated": True, "empleado": emp.to_dict()}
    return {"updated": False}

@router.delete("/eliminar")
def eliminar_empleado(id: Optional[int] = None, nombre: Optional[str] = None):
    emp = gestor.eliminar(id=id, nombre=nombre)
    if emp:
        return {"deleted": True, "empleado": emp.to_dict()}
    return {"deleted": False}
