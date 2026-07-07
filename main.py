from fastapi import FastAPI
from core.logging import configure_logging
from core.middleware import LoggingMiddleware
from core.error_handlers import register_exception_handlers

configure_logging()

app = FastAPI()


app.add_middleware(LoggingMiddleware)
register_exception_handlers(app)


@app.get("/")
def read_root():
    return {"msg": "Hello, World!"}
