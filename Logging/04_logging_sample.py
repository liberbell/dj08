import logging
import logging.handlers

logger = logging.getLogger(__name__)

r_handler = logging.handlers.RotatingFileHandler(
    "logs/rotation_file.log",
    maxBytes=1000,
    backupCount=5,
    encoding="utf-8"
)