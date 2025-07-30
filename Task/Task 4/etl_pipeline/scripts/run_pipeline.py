"""
Author: Ajeyomi Adedoyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 19-03-2025

ETL Pipeline for extracting, transforming, and loading IMDb data.
"""

import sys

sys.path.append("../")

from dotenv import load_dotenv
import os

from database.crud import create_table
from src.web_scraper import extract_imdb_data
from src.data_transform import (
    load_data,
    transform_data,
    table_date,
    table_finance,
    table_genre,
    table_location,
    table_movie,
    table_production,
    table_user,
)
from src.db_loader import load_data_db
from src.config import (
    movie_query,
    date_query,
    user_query,
    genre_query,
    production_query,
    location_query,
    finance_query,
)

from logger.logger import setup_logging

# Setup logger
logger = setup_logging()

# Load environment variables
load_dotenv()

API_KEY = os.getenv("api_key")
HOST = os.getenv("host")


def etl_pipeline():
    """Executes the ETL pipeline."""
    try:
        logger.info("Creating database tables...")
        create_table()
    except Exception as e:
        logger.error(f"Error creating tables: {e}")
        return

    try:
        logger.info("Extracting IMDb data...")
        raw_json_file = extract_imdb_data(
            api_key=API_KEY, host=HOST, output_path="../data"
        )
    except Exception as e:
        logger.error(f"Error extracting data: {e}")
        return

    try:
        logger.info("Loading raw data...")
        raw_data = load_data(raw_json_file)
    except Exception as e:
        logger.critical(f"Error loading raw data: {e}")
        return

    # Data transformation and modeling
    logger.info("Transforming data...")
    transformed_data = transform_data(raw_data)

    if transformed_data.is_empty():
        logger.debug("ETL pipeline terminated due to empty dataset.")
        return

    try:
        logger.info("Loading data into the database...")
        load_data_db(table_movie(transformed_data), movie_query)
        load_data_db(table_date(transformed_data), date_query)
        load_data_db(table_user(transformed_data), user_query)
        load_data_db(table_genre(transformed_data), genre_query)
        load_data_db(table_production(transformed_data), production_query)
        load_data_db(table_location(transformed_data), location_query)
        load_data_db(table_finance(transformed_data), finance_query)
        logger.info("ETL pipeline completed successfully.")
    except Exception as e:
        logger.error(f"Error loading data into database: {e}")


if __name__ == "__main__":
    etl_pipeline()
