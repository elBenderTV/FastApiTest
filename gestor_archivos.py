import json
import os
from typing import TypeVar, Generic, List, Type
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)

class GestorArchivos(Generic[T]):
    def __init__(self, archivo: str, modelo: Type[T]):
        self.archivo = archivo
        self.modelo = modelo
        self.datos: List[T] = self._cargar()

    def _cargar(self) -> List[T]:
        if not os.path.exists(self.archivo):
            return []
        with open(self.archivo, "r") as f:
            try:
                datos = json.load(f)
                return [self.modelo(**item) for item in datos]
            except json.JSONDecodeError:
                return []

    def _guardar(self):
        with open(self.archivo, "w") as f:
            json.dump([d.model_dump() for d in self.datos], f, indent=2)

    def get_all(self) -> List[T]:
        return self.datos

    def get_by_id(self, id: int) -> T | None:
        return next((d for d in self.datos if d.id == id), None)

    def add(self, obj: T) -> T:
        self.datos.append(obj)
        self._guardar()
        return obj

    def update(self, id: int, nuevos_datos: dict) -> T | None:
        obj = self.get_by_id(id)
        if obj:
            datos_actualizados = obj.model_copy(update=nuevos_datos)
            self.datos = [datos_actualizados if d.id == id else d for d in self.datos]
            self._guardar()
            return datos_actualizados
        return None

    def delete(self, id: int) -> T | None:
        obj = self.get_by_id(id)
        if obj:
            self.datos = [d for d in self.datos if d.id != id]
            self._guardar()
            return obj
        return None
