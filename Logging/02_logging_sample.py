import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

s_handler = logging.StreamHandler()
f_handler = logging.FileHandler("logging2.log", encoding="utf-8")

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
