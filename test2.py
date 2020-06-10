import os
import logging


def init_logger():
    log_format = "[%(filename)s %(lineno)d %(levelname)s] %(message)s "
    date_format = '%Y-%m-%d  %H:%M:%S %a '
    logging.basicConfig(level=logging.WARN,
                        format=log_format,
                        datefmt=date_format,
                        )


def main():
    init_logger()
    os.system("pytest test2.py -s")


def test_case1():
    logging.info("This is info message!\n")
    logging.debug("This is debug message!\n")
    logging.warning("This is warning message!\n")
    logging.error("This is error message!\n")
    assert 1==2
    
    
