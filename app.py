# Funciones externas
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

# Funciones locales
from routes import route

# Inicializar app
app = FastAPI()


@app.exception_handler(StarletteHTTPException)
# Excepción url no encontrada
async def custom_http_exception_handler(request, exc):
    return RedirectResponse("/docs")

# Incluir rutas
app.include_router(route, prefix="/api", tags=["api"],)
