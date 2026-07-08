from fastapi import FastAPI
from core.logging import configure_logging
from core.middleware import LoggingMiddleware
from core.error_handlers import register_exception_handlers
from core.config import settings

from modules.auth.router import router as auth_router

configure_logging()

app = FastAPI()

API_PREFIX = f"/api/v{settings.API_VERSION}"

app.include_router(auth_router, prefix=API_PREFIX)

app.add_middleware(LoggingMiddleware)
register_exception_handlers(app)


@app.get("/")
def read_root():
    return {"msg": "Hello, World!"}
