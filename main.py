from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="Examen Corte 1",
    description="¡Este examen está hecho para la universidad CUES!",
    version="1.1"
)

app.include_router(router)
