from pydantic import BaseModel
from typing import List

# Definición del modelo Cliente
class Cliente(BaseModel):
    id_cliente: int
    nombre_cliente: str
    email_cliente: str

# Definición del modelo Producto
class Producto(BaseModel):
    id_producto: int
    nombre_producto: str
    precio_producto: float

# Definición del modelo Pedido
class Pedido(BaseModel):
    id_pedido: int
    id_cliente: int
    productos: List[int]
