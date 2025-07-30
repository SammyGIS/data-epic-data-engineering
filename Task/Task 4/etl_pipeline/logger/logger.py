"""
Author: Ajeyomi Adeodyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 07-03-2025

https://medium.com/@tzhaonj/writing-proper-logs-in-python-for-data-scientists-f1bed1158440
https://realpython.com/python-logging/
"""

import logging


def setup_logging():
    logging.basicConfig(
        filename="../logs.log",
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M",
    )

    return logging.getLogger(__name__)
