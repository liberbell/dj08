import logging

logging.basicConfig(
    level=logging.WARNING, filename="sample.log",
    filemode="w", format="%(asctime)s-%(process)d-%(levelname)s-%(message)s"
)

logging.debug("debug.log")
logging.info("info.log")
logging.warning("warning.log")
logging.error("error.log")
logging.critical("critical.log")