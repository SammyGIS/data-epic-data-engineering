"""
Author: Ajeyomi Adeodyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 19-03-2025

"""

import polars as pl
import os
import psycopg2
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

URL = os.getenv("POSTGRESS_URL")

from logger.logger import setup_logging

# Setup logger
logger = setup_logging()


# Database connection function
def postgres_connect(url):
    try:
        conn = psycopg2.connect(url)
        logger.info("Database connected successfully")
        return conn
    except Exception as e:
        logger.error(f"Database Connection Failed: {e}")
        return None


def load_data_db(data: pl.DataFrame, query: str, con=postgres_connect(URL)):
    """Load data into the database using an SQL query."""
    if data.is_empty():
        return
    try:
        with con.cursor() as cur:
            cur.executemany(
                query, [tuple(row) for row in data.fill_null(0).iter_rows()]
            )
            con.commit()
        logger.info("Data loaded to data successfully")

    except Exception as e:
        logger.critical(f"An Errror Occured {e}")
