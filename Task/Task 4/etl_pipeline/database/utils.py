"""
Author: Ajeyomi Adeodyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 07-03-2025


https://docs.sqlalchemy.org/en/14/orm/declarative_tables.html
"""

from enum import Enum


class db_info(Enum):
    """Tables name where data is stored in the db"""

    TABLE_MOVIE = "movie"
    TABLE_DATE = "date"
    TABLE_FINANCE = "finance"
    TABLE_LOCATION = "location"
    TABLE_PRODUCTION = "production"
    TABLE_USER_RATING = "user_rating"
    TABLE_GENRE = "genre"
