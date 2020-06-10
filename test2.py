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
    pytest.main(["test2.py", '--capture=sys'])


def test_case1():
    print("This is info message!\n")
    print("This is debug message!\n")
    print("This is warning message!\n")
    print("This is error message!\n")
    logging.error("This is error message too!\n")
    assert 1==2

if __name__ == "__main__":
    main()
