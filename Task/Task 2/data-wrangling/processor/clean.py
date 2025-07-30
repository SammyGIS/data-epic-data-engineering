"""
Author: Ajeyomi Adedoyin Samuel
Date: 01-03-2025
Email: adedoyinsamuel25@gmail.com

https://docs.pola.rs/api/python/dev/reference/api/polars.read_excel.html
"""

import sys 
# set all depencies (module) part
sys.path.append('../')

import pandas as pd
import polars as pl
from processor.utils import polars_read_data, pandas_read_data


def pd_transform_data(data_path:str) -> pd.DataFrame:
    """Perform Transformation on the data using pandas"""
    try:
        # read data
        df = pandas_read_data(data_path)

        # copy the original file without modification
        df = df.copy()

        # Convert negative values in Price and Quantity to positive
        df = df[(df['Price'] < 0) | (df['Quantity'] < 0)]

        # create the amount field which is pirce* quantiy
        df['Amount'] = df["Price"] * df["Quantity"]

        # Fill missing CustomerID with "Unknown"
        df["Customer ID"] = df["Customer ID"].fillna("Unknown")

        return df.to_dict()
    
    except Exception as e:
        print(f"Error {e}")


def pl_transform_data(data_path:str) -> pl.DataFrame:
    """Perform Transformation on the data using Polars"""
    try:
        # read data
        df = polars_read_data(data_path)
        
        return(
            df.filter((pl.col("Price")> 0) & (pl.col("Quantity")>0))
            .with_columns([
                (pl.col("Price")* pl.col("Quantity")).alias("Amount"),
                pl.col("Customer ID").fill_null("Unknown")
            ])
        ).to_dict(as_series=False)
    
    except Exception as e:
        print(f"Error {e}")