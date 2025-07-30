"""
Author: Ajeyomi Adeodyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 07-03-2025
"""

# set all depencies (module) part
import sys

sys.path.append("../")

import database.model as model
from database.db_setup import engine


def create_table():
    """Create tables in the schema."""
    model.Base.metadata.create_all(bind=engine)
