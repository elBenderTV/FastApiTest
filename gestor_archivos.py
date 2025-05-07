import json
from typing import Type, List, TypeVar
from pydantic import BaseModel

T = TypeVar('T', bound=BaseModel)

class GestorArchivos:
    def __init__(self, ruta_archivo: str, modelo: Type[T]):
        self.ruta_archivo = ruta_archivo
        self.modelo = modelo
        self.datos: List[T] = self._cargar()

    def _cargar(self) -> List[T]:
        try:
            with open(self.ruta_archivo, "r") as archivo:
                datos = json.load(archivo)
                print("Datos cargados desde JSON:", datos)
            return [self.modelo(**item) for item in datos]
        except FileNotFoundError:
            return []

    def _guardar(self):
        with open(self.ruta_archivo, "w") as archivo:
            json.dump([item.dict() for item in self.datos], archivo, indent=2)

    def get_all(self) -> List[T]:
        return self.datos

    def get_by_id(self, id: int) -> T | None:
        for item in self.datos:
            if item.id_cliente == id:  # Asumiendo que la propiedad id es siempre la clave primaria
                return item
        return None

    def add(self, objeto: T) -> None:
        self.datos.append(objeto)
        self._guardar()

    def update(self, id: int, datos: dict) -> T | None:
        item = self.get_by_id(id)
        if item:
            for key, value in datos.items():
                setattr(item, key, value)
            self._guardar()
            return item
        return None

    def delete(self, id: int) -> bool:
        item = self.get_by_id(id)
        if item:
            self.datos.remove(item)
            self._guardar()
            return True
        return False
