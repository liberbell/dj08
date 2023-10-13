import logging
import logging.config
import time

logging.config.fileConfig(fname="conf/rotation_logger.conf")

logger = logging.getLogger(__name__)

for _ in range(1000):
    logger.debug("Debug log")
    logger.info("Info log")
    logger.warning("Warning log")
    logger.error("Error log")
    logger.critical("Critical log")
    time.sleep(1)