"""
Author: Ajeyomi Adeodyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 07-03-2025


"""

import sys

sys.path.append("../")

from database.db_setup import Base
from database.utils import db_info

from sqlalchemy import (
    Column,
    String,
    Integer,
    Boolean,
    BigInteger,
    VARCHAR,
    Date,
    DECIMAL,
    ForeignKey,
)
from sqlalchemy.orm import relationship


class Movie(Base):
    __tablename__ = db_info.TABLE_MOVIE.value

    movie_id = Column(String(20), primary_key=True, nullable=False)
    url = Column(VARCHAR(500))
    primary_title = Column(String(255), nullable=False)
    original_title = Column(String(255))
    type = Column(String(50))
    description = Column(VARCHAR(500))
    primary_image = Column(String(500))
    content_rating = Column(String(10))
    is_adult = Column(Boolean)
    runtime_minutes = Column(Integer)

    dates = relationship("Date", back_populates=db_info.TABLE_MOVIE.value)
    finance = relationship("Finance", back_populates=db_info.TABLE_MOVIE.value)
    location = relationship("Location", back_populates=db_info.TABLE_MOVIE.value)
    production = relationship("Production", back_populates=db_info.TABLE_MOVIE.value)
    user_ratings = relationship("UserRating", back_populates=db_info.TABLE_MOVIE.value)
    genres = relationship("Genre", back_populates=db_info.TABLE_MOVIE.value)


class Date(Base):
    __tablename__ = db_info.TABLE_DATE.value

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    movie_id = Column(
        String(20), ForeignKey(f"{db_info.TABLE_MOVIE.value}.movie_id"), nullable=False
    )
    start_year = Column(Integer)
    release_date = Column(Date)

    movie = relationship("Movie", back_populates=db_info.TABLE_DATE.value)


class Finance(Base):
    __tablename__ = db_info.TABLE_FINANCE.value

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    movie_id = Column(
        String(20), ForeignKey(f"{db_info.TABLE_MOVIE.value}.movie_id"), nullable=False
    )
    budget = Column(BigInteger)
    gross_worldwide = Column(BigInteger)

    movie = relationship("Movie", back_populates=db_info.TABLE_FINANCE.value)


class Location(Base):
    __tablename__ = db_info.TABLE_LOCATION.value

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    movie_id = Column(
        String(20), ForeignKey(f"{db_info.TABLE_MOVIE.value}.movie_id"), nullable=False
    )
    filming_locations = Column(String(500))
    countries_of_origin = Column(String(100))

    movie = relationship("Movie", back_populates=db_info.TABLE_LOCATION.value)


class Production(Base):
    __tablename__ = db_info.TABLE_PRODUCTION.value

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    production_company_id = Column(String(20), nullable=False)
    movie_id = Column(
        String(20), ForeignKey(f"{db_info.TABLE_MOVIE.value}.movie_id"), nullable=False
    )
    production_company_name = Column(String(255), nullable=False)

    movie = relationship("Movie", back_populates=db_info.TABLE_PRODUCTION.value)


class UserRating(Base):
    __tablename__ = db_info.TABLE_USER_RATING.value

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    movie_id = Column(
        String(20), ForeignKey(f"{db_info.TABLE_MOVIE.value}.movie_id"), nullable=False
    )
    average_rating = Column(DECIMAL(3, 1))
    num_votes = Column(Integer)

    movie = relationship("Movie", back_populates=db_info.TABLE_USER_RATING.value)


class Genre(Base):
    __tablename__ = db_info.TABLE_GENRE.value

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    movie_id = Column(
        String(20), ForeignKey(f"{db_info.TABLE_MOVIE.value}.movie_id"), nullable=False
    )
    interest = Column(String(100))
    genre = Column(String(100), nullable=False)

    movie = relationship("Movie", back_populates=db_info.TABLE_GENRE.value)
