import logging


def config_logger(logging_level):
    logging.basicConfig(level=logging_level, style="%",
                        format="%(asctime)s %(levelname)s %(module)s %(funcName)s: %(lineno)d %(message)s",
                        datefmt="%H:%M:%S")
