"""
Author: Ajeyomi Adeodyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 07-03-2025


https://fastapi.tiangolo.com/reference/apirouter/#fastapi.APIRouter
"""

from fastapi import FastAPI
import uvicorn

from datetime import datetime
from database.crud import create_table
from scripts.load_data import etl_pipeline
from api.routes import router

from logger.logger import setup_logging

# Setup logger
logger = setup_logging()

app = FastAPI(
    title="E-commerce API",
    description="This is an e-commerce API endpoint that provides data and analytics.",
    version="0.1.0",
    contact={
        "name": "Adedoyin Samuel",
        "email": "adedoyinsamuel25@gmail.com",
    }
)
app.include_router(router)

def startup_tasks():
    """Initialize database and ETL process before running the server"""
    logger.info("Initializing database...")
    create_table()
    
    logger.info("Running ETL pipeline...")
    etl_pipeline()

if __name__ == "__main__":
    start_time = datetime.now()
    logger.info(f"Process started at {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    startup_tasks()
    end_time = datetime.now()
    logger.info(f"Process ended at {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info(f"Total processing time: {end_time - start_time}")
    logger.info("Starting Uvicorn server...")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)