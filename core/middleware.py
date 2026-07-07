import time
import uuid
from loguru import logger
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid.uuid4())
        request.state.request_id = request_id

        start = time.perf_counter()

        with logger.contextualize(request_id=request_id):
            try:
                response: Response = await call_next(request)
            except Exception:
                duration = (time.perf_counter() - start) * 1000
                logger.exception(
                    f"{request.method} {request.url.path} "
                    f"- unhandled exception - duration={duration:.2f}ms"
                )
                raise

            duration = (time.perf_counter() - start) * 1000
            log_level = "WARNING" if response.status_code >= 400 else "INFO"
            logger.log(
                log_level,
                f"{request.method} {request.url.path} "
                f"- status={response.status_code} "
                f"- duration={duration:.2f}ms",
            )

            response.headers["X-Request-ID"] = request_id
            return response
