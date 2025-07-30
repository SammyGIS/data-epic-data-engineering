"""
Author: Ajeyomi Adeodyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 19-03-2025


# https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.null_count.html
# https://docs.pola.rs/api/python/dev/reference/expressions/api/polars.Expr.str.to_datetime.html
"""

import polars as pl


def load_data(data):
    """Read JSON data as a Polars DataFrame."""
    try:
        df = pl.read_json(data)
        return df
    except Exception as e:
        raise RuntimeError(f"Error loading JSON data: {e}")


def transform_data(df: pl.DataFrame) -> pl.DataFrame:
    """Transform DataFrame by exploding lists, extracting fields, renaming columns, and handling nulls."""
    try:
        # Drop duplicates based on the movie_id column
        df = df.unique(subset=["id"], keep="first")

        # Convert release_date to date format
        df = df.with_columns(
            pl.col("releaseDate").str.to_date("%Y-%m-%d", strict=False)
        )

        # Explode list columns
        df = df.explode("countriesOfOrigin")
        df = df.explode("interests")
        df = df.explode("genres")

        # Rename columns using aliases
        df = df.with_columns(
            pl.col("id").alias("movie_id"),
            pl.col("releaseDate").alias("release_date"),
            pl.col("primaryTitle").alias("primary_title"),
            pl.col("originalTitle").alias("original_title"),
            pl.col("primaryImage").alias("primary_image"),
            pl.col("contentRating").alias("content_rating"),
            pl.col("isAdult").alias("is_adult"),
            pl.col("runtimeMinutes").alias("runtime_minutes"),
            pl.col("startYear").alias("start_year"),
            pl.col("grossWorldwide").alias("gross_worldwide"),
            pl.col("filmingLocations").alias("filming_locations"),
            pl.col("countriesOfOrigin").alias("countries_of_origin"),
            pl.col("averageRating").alias("average_rating"),
            pl.col("numVotes").alias("num_votes"),
        )

        # Explode and extract fields from production_companies
        df = df.explode("productionCompanies")
        df = df.with_columns(
            pl.col("productionCompanies")
            .struct.field("id")
            .alias("production_company_id"),
            pl.col("productionCompanies")
            .struct.field("name")
            .alias("production_company_name"),
        )
        df = df.drop("productionCompanies")  # Remove original dictionary column

        # Fill null values with "Unknown"
        df = df.fill_null("Unknown")

        return df
    except Exception as e:
        raise RuntimeError(f"Error in transform_data: {e}")


# Data modeling functions
def table_movie(df: pl.DataFrame) -> pl.DataFrame:
    """Create movie table."""
    try:
        movies_df = df.select(
            [
                "movie_id",
                "url",
                "primary_title",
                "original_title",
                "type",
                "description",
                "primary_image",
                "content_rating",
                "is_adult",
                "runtime_minutes",
            ]
        )
        return movies_df
    except Exception as e:
        raise RuntimeError(f"{e}")


def table_date(df: pl.DataFrame) -> pl.DataFrame:
    """Create date table."""
    try:
        movies_date = df.select(["movie_id", "start_year", "release_date"])
        return movies_date
    except Exception as e:
        raise RuntimeError(f"{e}")


def table_finance(df: pl.DataFrame) -> pl.DataFrame:
    """Create finance table."""
    try:
        movies_finance_df = df.select(["movie_id", "budget", "gross_worldwide"])
        return movies_finance_df
    except Exception as e:
        raise RuntimeError(f"{e}")


def table_location(df: pl.DataFrame) -> pl.DataFrame:
    """Create location table."""
    try:
        movies_location_df = df.select(
            ["movie_id", "filming_locations", "countries_of_origin"]
        )
        return movies_location_df
    except Exception as e:
        raise RuntimeError(f"{e}")


def table_production(df: pl.DataFrame) -> pl.DataFrame:
    """Create production table."""
    try:
        movies_production_df = df.select(
            ["movie_id", "production_company_id", "production_company_name"]
        )
        return movies_production_df
    except Exception as e:
        raise RuntimeError(f"{e}")


def table_user(df: pl.DataFrame) -> pl.DataFrame:
    """Create user table."""
    try:
        movie_user_df = df.select(["movie_id", "average_rating", "num_votes"])
        return movie_user_df
    except Exception as e:
        raise RuntimeError(f"{e}")


def table_genre(df: pl.DataFrame) -> pl.DataFrame:
    """Create genre table."""
    try:
        movie_genre = df.select(["movie_id", "genres", "interests"])
        return movie_genre
    except Exception as e:
        raise RuntimeError(f"{e}")
