import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)
logging.debug("debug2.log")
logging.info("info2.log")
logging.warning("warning2.log")
logging.error("error2.log")
logging.critical("critical2.log")
