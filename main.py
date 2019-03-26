"""
This will be the main entry point, connecting GUI with the backend created earlier.
"""
import logging

import qt_gui


def config_logger(logging_level):
    logging.basicConfig(level=logging_level, style="%", format="%(asctime)s %(levelname)s %(module)s %(funcName)s: %(lineno)d %(message)s", datefmt="%H:%M:%S")

def main():
    config_logger(logging.DEBUG)
    # qt_gui.init_multi_gui()
    qt_gui.init_gui()


if __name__ == '__main__':
    main()
