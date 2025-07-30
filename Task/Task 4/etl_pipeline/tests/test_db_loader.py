"""
Author: Ajeyomi Adeodyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 19-03-2025

"""
from src.db_loader import postgres_connect
from src.db_loader import load_data_db
import pytest
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

URL = os.getenv("POSTGRESS_URL")


def test_postgres_connect_successfully():
    connection = postgres_connect(URL)
    assert connection.status == 1

def test_postgres_connect_failled():
    connection = postgres_connect("")
    assert connection is None

def test_load_data_db():

    pass
