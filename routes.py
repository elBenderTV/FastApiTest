from fastapi import APIRouter
from typing import Optional
from gestor_archivos import GestorArchivos
from models import Cliente, Producto, Pedido

# Inicialización de los gestores para cada recurso
gestor_clientes = GestorArchivos("db/clientes.json", Cliente)
gestor_productos = GestorArchivos("db/productos.json", Producto)
gestor_pedidos = GestorArchivos("db/pedidos.json", Pedido)

router = APIRouter()

# --- Endpoints para Clientes ---
@router.get("/clientes", tags=["Clientes"])
def listar_clientes():
    return [cliente.dict() for cliente in gestor_clientes.datos]

@router.get("/clientes", tags=["Clientes"])
def ver_cliente(id_cliente: int):
    cliente = gestor_clientes.get_by_id(id_cliente)
    if cliente:
        return cliente.dict()
    return {"error": "Cliente no encontrado"}

@router.post("/clientes", tags=["Clientes"])
def crear_cliente(cliente: Cliente):
    return gestor_clientes.add(cliente)

@router.put("/clientes", tags=["Clientes"])
def actualizar_cliente(id_cliente: int, cliente: Cliente):
    return gestor_clientes.update(id_cliente, cliente.dict())

@router.delete("/clientes", tags=["Clientes"])
def eliminar_cliente(id_cliente: int):
    return gestor_clientes.delete(id_cliente)

# --- Endpoints para Productos ---
@router.get("/productos", tags=["Productos"])
def listar_productos():
    return [producto.dict() for producto in gestor_productos.datos]

@router.get("/productos", tags=["Productos"])
def ver_producto(id: int):
    producto = gestor_productos.get_by_id(id)
    if producto:
        return producto.dict()
    return {"error": "Producto no encontrado"}

@router.post("/productos", tags=["Productos"])
def crear_producto(producto: Producto):
    return gestor_productos.add(producto)

@router.put("/productos", tags=["Productos"])
def actualizar_producto(id: int, producto: Producto):
    return gestor_productos.update(id, producto.dict())

@router.delete("/productos", tags=["Productos"])
def eliminar_producto(id: int):
    return gestor_productos.delete(id)

# --- Endpoints para Pedidos ---
@router.get("/pedidos", tags=["Pedidos"])
def obtener_pedidos():
    pedidos_enriquecidos = []
    for pedido in gestor_pedidos.datos:  # Aquí recorres los pedidos
        # Buscar cliente
        cliente = next((c for c in gestor_clientes.datos if c.id_cliente == pedido.id_cliente), None)
        nombre_cliente = cliente.nombre_cliente if cliente else "Desconocido"

        # Buscar productos
        lista_productos = []
        for id_prod in pedido.productos:
            producto = next((p for p in gestor_productos.datos if p.id_producto == id_prod), None)
            if producto:
                lista_productos.append({
                    "id_producto": producto.id_producto,
                    "nombre_producto": producto.nombre_producto
                })
            else:
                lista_productos.append({"id_producto": id_prod, "nombre_producto": "Desconocido"})

        pedidos_enriquecidos.append({
            "id_pedido": pedido.id_pedido,  # Corrección aquí: usa id_pedido en lugar de id
            "id_cliente": pedido.id_cliente,
            "nombre_cliente": nombre_cliente,
            "productos": lista_productos
        })
    return pedidos_enriquecidos

@router.get("/pedido", tags=["Pedidos"])
def ver_pedido(id_pedido: int):
    pedido = gestor_pedidos.get_by_id(id_pedido)
    if pedido:
        return pedido.dict()
    return {"error": "Pedido no encontrado"}

@router.post("/pedidos", tags=["Pedidos"])
def crear_pedido(pedido: Pedido):
    return gestor_pedidos.add(pedido)

@router.put("/pedidos", tags=["Pedidos"])
def actualizar_pedido(id_pedido: int, pedido: Pedido):
    return gestor_pedidos.update(id_pedido, pedido.dict())

@router.delete("/pedidos", tags=["Pedidos"])
def eliminar_pedido(id_pedido: int):
    return gestor_pedidos.delete(id_pedido)
