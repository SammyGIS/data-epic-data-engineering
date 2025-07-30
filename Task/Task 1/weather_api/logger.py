"""
Author: Ajeyomi Adedoyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 21-02-2025

https://www.geeksforgeeks.org/logging-in-python/
"""


import logging

# set up logging
logging.basicConfig(filename="log.txt",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()

# setting the threshold of looger to debug
logger.setLevel(logging.DEBUG)