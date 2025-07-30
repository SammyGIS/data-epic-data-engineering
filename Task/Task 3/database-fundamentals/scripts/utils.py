import os
import psycopg2
from dotenv import load_dotenv
from logger.logger import setup_logging

# Setup logger
logger = setup_logging()

# Load environment variables
load_dotenv()

URL = os.getenv("POSTGRESS_URL")

# Database connection function
def postgres_connect(url):
    try:
        conn = psycopg2.connect(url)
        logger.info("Database connected successfully")
        return conn
    except Exception as e:
        logger.critical(f"Database Connection Failed: {e}")


# Establish connection
conn = postgres_connect(URL)
