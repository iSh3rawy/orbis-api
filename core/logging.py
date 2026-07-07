import sys
from loguru import logger
from core.config import settings


def configure_logging():
    logger.remove()

    logger.add(
        sys.stdout,
        level="DEBUG" if settings.DEBUG else "INFO",
        format=(
            "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> "
            "| <level>{level:<7}</level> "
            "| <cyan>{extra[request_id]}</cyan> "
            "| <cyan>{name}</cyan>.<cyan>{function}</cyan>:<cyan>{line}</cyan> "
            "- <level>{message}</level>"
        ),
        colorize=True,
        backtrace=True,
        diagnose=settings.DEBUG,
        enqueue=True,
    )

    logger.add(
        "logs/app.log",
        level="INFO",
        rotation="00:00",
        retention="14 days",
        compression="zip",
        format=(
            "{time:YYYY-MM-DD HH:mm:ss.SSS} | {level:<7} | {extra[request_id]} | "
            "{name}.{function}:{line} - {message}"
        ),
        enqueue=True,
        backtrace=True,
        diagnose=False,
    )

    logger.configure(extra={"request_id": "-"})
