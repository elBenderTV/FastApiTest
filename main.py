from fastapi import FastAPI, HTTPException
from models import Cliente, Producto, Pedido
from gestor_archivos import GestorArchivos

app = FastAPI(
    title="API Examen Corte III",
    description="API RESTful con Pydantic, FastAPI y archivos JSON",
    version="1.0"
)

clientes = GestorArchivos("bd/clientes.json", Cliente)
productos = GestorArchivos("bd/productos.json", Producto)
pedidos = GestorArchivos("bd/pedidos.json", Pedido)

# ---- Clientes ----
@app.get("/clientes", tags=["Clientes"])
def listar_clientes():
    return clientes.get_all()

@app.get("/clientes/{id}", tags=["Clientes"])
def obtener_cliente(id: int):
    cliente = clientes.get_by_id(id)
    if cliente:
        return cliente
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

@app.post("/clientes", tags=["Clientes"])
def crear_cliente(cliente: Cliente):
    if clientes.get_by_id(cliente.id):
        raise HTTPException(status_code=400, detail="ID ya existe")
    return clientes.add(cliente)

@app.put("/clientes/{id}", tags=["Clientes"])
def actualizar_cliente(id: int, datos: dict):
    cliente = clientes.update(id, datos)
    if cliente:
        return cliente
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

@app.delete("/clientes/{id}", tags=["Clientes"])
def eliminar_cliente(id: int):
    cliente = clientes.delete(id)
    if cliente:
        return cliente
    raise HTTPException(status_code=404, detail="Cliente no encontrado")


# ---- Productos ----

@app.get("/productos", tags=['Productos'])
def listar_productos():
    return productos.get_all()

@app.get("/productos/{id}", tags=['Productos'])
def obtener_producto(id: int):
    prod = productos.get_by_id(id)
    if prod:
        return prod
    raise HTTPException(status_code=404, detail="Producto no encontrado")

@app.post("/productos", tags=['Productos'])
def crear_producto(producto: Producto):
    if productos.get_by_id(producto.id):
        raise HTTPException(status_code=400, detail="ID ya existe")
    return productos.add(producto)

@app.put("/productos/{id}", tags=['Productos'])
def actualizar_producto(id: int, datos: dict):
    prod = productos.update(id, datos)
    if prod:
        return prod
    raise HTTPException(status_code=404, detail="Producto no encontrado")

@app.delete("/productos/{id}", tags=['Productos'])
def eliminar_producto(id: int):
    prod = productos.delete(id)
    if prod:
        return prod
    raise HTTPException(status_code=404, detail="Producto no encontrado")

# ---- Pedidos ----

@app.get("/pedidos", tags=['Pedidos'])
def listar_pedidos():
    return pedidos.get_all()

@app.get("/pedidos/{id}", tags=['Pedidos'])
def obtener_pedido(id: int):
    pedido = pedidos.get_by_id(id)
    if pedido:
        return pedido
    raise HTTPException(status_code=404, detail="Pedido no encontrado")

@app.post("/pedidos", tags=['Pedidos'])
def crear_pedido(pedido: Pedido):
    if pedidos.get_by_id(pedido.id):
        raise HTTPException(status_code=400, detail="ID ya existe")
    return pedidos.add(pedido)

@app.put("/pedidos/{id}", tags=['Pedidos'])
def actualizar_pedido(id: int, datos: dict):
    pedido = pedidos.update(id, datos)
    if pedido:
        return pedido
    raise HTTPException(status_code=404, detail="Pedido no encontrado")

@app.delete("/pedidos/{id}", tags=['Pedidos'])
def eliminar_pedido(id: int):
    pedido = pedidos.delete(id)
    if pedido:
        return pedido
    raise HTTPException(status_code=404, detail="Pedido no encontrado")
