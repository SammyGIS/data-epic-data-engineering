"""
Author: Ajeyomi Adeodyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 07-03-2025


https://www.geeksforgeeks.org/introduction-to-psycopg2-module-in-python/
"""
import sys
sys.path.append('../')

import pandas as pd
from scripts.config import (DATA_PATH, customer_query,
                    order_items_query, order_query, product_query)
from scripts.utils import conn
from logger.logger import setup_logging

# Setup logger
logger = setup_logging()

def read_data(data_path: str) -> pd.DataFrame:
    """Read CSV data into a DataFrame"""
    try:
        df = pd.read_csv(data_path)
        logger.info("Data read successfully")
        return df
    except Exception as e:
        logger.error(f"Error reading data: {e}")
        return pd.DataFrame()  # Return empty DataFrame on failure

def transform_data(data: pd.DataFrame) -> pd.DataFrame:
    """Perform basic data transformation"""
    if data.empty:
        logger.warning("No data to transform")
        return data

    data.columns = [col.lower() for col in data.columns]
    df = data.drop_duplicates().reset_index(drop=True).copy()

    df['order_id'] = df.index + 1  # More efficient way to generate order_id
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

    return df

def create_customer_dataframe(df):
    """Extract data for the customer table"""
    return df[["customer_id", "gender"]].drop_duplicates().copy()

def create_order_dataframe(df):
    """Extract data for the order table"""
    columns = ["order_id", "customer_id", "order_date", "order_priority", "payment_method",
               "device_type", "customer_login_type"]
    return df[columns].drop_duplicates().copy()

def create_product_dataframe(df):
    """Extract unique products"""
    product_df = df[["product_category", "product"]].drop_duplicates().reset_index(drop=True).copy()
    product_df['product_id'] = product_df.index + 1
    return product_df[["product_id", "product_category", "product"]]

def create_orderitems_dataframe(df):
    """Extract data for the order items table"""
    columns = ["quantity", "discount", "sales", "profit", "shipping_cost", "product", "order_id"]
    order_items_df = df[columns].drop_duplicates().copy()

    unique_product_df = create_product_dataframe(df)
    order_items_df = order_items_df.merge(unique_product_df, on="product", how="left")

    return order_items_df[["product_id", "order_id", "quantity", "discount", "sales", "profit", "shipping_cost"]]

def load_data_db(data: pd.DataFrame, query: str, con):
    """Load data into the database using an SQL query."""
    if data.empty:
        logger.warning("No data to load")
        return

    try:
        with con.cursor() as cur:
            cur.executemany(query, [tuple(row.fillna(0)) for _, row in data.iterrows()])
            con.commit()
        logger.info("Data loaded successfully")
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        con.rollback()

def etl_pipeline():
    data = read_data(DATA_PATH)
    transformed_data = transform_data(data)

    if transformed_data.empty:
        logger.error("ETL pipeline terminated due to empty dataset")
        return

    with conn as con:
        load_data_db(create_customer_dataframe(transformed_data), customer_query, con)
        load_data_db(create_order_dataframe(transformed_data), order_query, con)
        load_data_db(create_product_dataframe(transformed_data), product_query, con)
        load_data_db(create_orderitems_dataframe(transformed_data), order_items_query, con)
