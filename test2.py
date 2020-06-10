import os
import time
import pytest
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
    logging.warning("Start test")
    while True:
        print("Hello world!")
        time.sleep(5)
    pytest.main(["test2.py", '-s', '--tb=line'])


def test_case1():
    logging.info("This is info message!\n")
    logging.debug("This is debug message!\n")
    logging.warning("This is warning message!\n")
    logging.error("This is error message!\n")
    assert 1==2

if __name__ == "__main__":
    main()
