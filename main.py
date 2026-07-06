from fastapi import FastAPI
from core.logging import LoggingMiddleware

app = FastAPI()

app.add_middleware(LoggingMiddleware)


@app.get("/")
def read_root():
    return {"msg": "Hello, World!"}
