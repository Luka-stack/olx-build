import logging
from logging.handlers import RotatingFileHandler
from starlette.middleware.base import BaseHTTPMiddleware


log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# File Loger
# file_handler = RotatingFileHandler('app.log', maxBytes=1000000, backupCount=5)
# file_handler.setFormatter(log_formatter)

# Console Logger
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# logger.addHandler(file_handler)
logger.addHandler(console_handler)

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        logger.info(f"Request: {request.method} {request.url}")
        response = await call_next(request)
        logger.info(f"Response: {response.status_code}")
        return response