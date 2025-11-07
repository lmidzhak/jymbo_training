from loguru import logger
import logging
from datetime import datetime


class InterceptHandler(logging.Handler):
    def emit(self, record):
        try:
            level = "API" if record.levelno < logging.ERROR else record.levelno
        except KeyError:
            level = record.levelno

        frame, depth = logging.currentframe(), 2
        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        if record.levelno < logging.ERROR and (
                "aiogram" in record.name
        ):
            return

        if record.name in ["API", "BOT"] and record.levelno < logging.ERROR:
            return

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


logger.level("API", no=37, color="<blue><bold>")
logger.level("DB", no=38, color="<red><bold>")
logger.level("BOT", no=39, color="<red><bold>")

logging.basicConfig(handlers=[InterceptHandler()], level=logging.INFO)

for logger_name in ("uvicorn", "uvicorn.error", "fastapi", "uvicorn.access"):
    uvicorn_logger = logging.getLogger(logger_name)
    uvicorn_logger.handlers = [InterceptHandler()]
    uvicorn_logger.propagate = False

logging.getLogger("uvicorn.access").setLevel(logging.ERROR)
logging.getLogger("aiogram").setLevel(logging.INFO)

logging.getLogger("uvicorn").setLevel(logging.INFO)
logging.getLogger("uvicorn.error").setLevel(logging.INFO)

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

logger.add(f"logs/api_{timestamp}.log",
           rotation="1 week",
           retention="1 month",
           level="API",
           format="{time:YYYY-MM-DD HH:mm:ss.S} | {level} | {message}")
logger.add(f"logs/db_{timestamp}.log",
           rotation="1 week",
           retention="1 month",
           level="API",
           format="{time:YYYY-MM-DD HH:mm:ss.S} | {level} | {message}")
logger.add(f"logs/bot_{timestamp}.log",
           rotation="1 week",
           retention="1 month",
           level="BOT",
           format="{time:YYYY-MM-DD HH:mm:ss.S} | {level} | {message}")


def api_log(message):
    logger.log("API", message)


def db_log(message):
    logger.log("DB", message)


def bot_log(message):
    logger.log("BOT", message)
