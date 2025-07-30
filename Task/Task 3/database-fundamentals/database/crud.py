"""
Author: Ajeyomi Adeodyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 07-03-2025
"""

# set all depencies (module) part
import sys
sys.path.append('../')

from sqlalchemy.schema import CreateSchema
import database.model as model
from database.utils  import db_info
from database.db_setup import engine

def create_schema():
    """Create schema"""
    with engine.connect() as connection:
        connection.execute(CreateSchema(db_info.SCHEMA_NAME.value,if_not_exists=True))
        connection.commit()

def create_table():
    """Create tables in the schema."""
    create_schema() # ensure schema exists
    model.Base.metadata.create_all(bind=engine)


