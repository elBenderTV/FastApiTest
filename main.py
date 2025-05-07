from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="API de Inventario de Ciberseguridad",
    description="API para manejar clientes, productos y pedidos en una empresa de ciberseguridad",
    version="1.0"
)

app.include_router(router)
