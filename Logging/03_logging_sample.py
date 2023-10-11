import logging
import logging.config

logging.config.fileConfig(fname="conf/logger.conf")

logger = logging.getLogger(__name__)


logger.debug("Debug log")
logger.info("Info log")
logger.warning("Warning log")
logger.error("Error log")
logger.critical("Critial log")

logger = logging.getLogger("samplelogger")
logger.debug("Debug log")
logger.info("Info log")
logger.warning("Warning log")
logger.error("Error log")
logger.critical("Critial log")
