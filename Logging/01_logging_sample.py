import logging

logging.basicConfig(
    level=logging.ERROR, filename="sample.log",
    filemode="w", format="%(asctime)s-%(process)d-%(levelname)s-%(message)s"
)