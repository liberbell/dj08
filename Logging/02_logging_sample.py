import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

s_handler = logging.StreamHandler()
f_handler = logging.FileHandler("logging2.log", encoding="utf-8")

s_handler.setLevel(logging.DEBUG)
f_handler.setLevel(logging.ERROR)

s_formatter = logging.Formatter("%(name)s-%(levelname)s-%(message)s")
f_formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")

s_handler.setFormatter(s_formatter)
f_handler.setFormatter(f_formatter)

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
