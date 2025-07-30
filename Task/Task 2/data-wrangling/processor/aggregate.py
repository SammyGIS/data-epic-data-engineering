"""
Author: Ajeyomi Adedoyin Samuel
Date: 01-03-2025
Email: adedoyinsamuel25@gmail.com

https://gist.github.com/niftycode/a747648db1b79396b8e4814946a4dba2
https://docs.pola.rs/api/python/dev/reference/api/polars.read_excel.html



### **Task 4: Data Aggregation**

1. Group dataset by a categorical column (e.g., `category`).
2. Compute **mean, sum, count** for a numeric column.
3. Implement aggregation using both **Pandas** and **Polars**.
4. Expose results via a FastAPI endpoint (`/aggregate`).

"""

import pandas as pd
import polars as pl


class PandasAggregation:
    def __init__(self, dataframe: pd.DataFrame):
        """Initialize the class with a Pandas DataFrame."""
        self.dataframe = dataframe

    # Pandas aggregate functions
    def pd_transaction_per_country(self,df: pd.DataFrame) -> pd.Series:
        """Counts the number of transactions per country."""
        try:
            return df.groupby("Country")["Invoice"].count()
        except Exception as e:
            print(f"Error: {e}")

    def pd_transaction_revenue_per_country(self,df: pd.DataFrame) -> pd.Series:
        """Calculates the total transaction amount per country."""
        try:
            return df.groupby("Country")["Amount"].sum()
        except Exception as e:
            print(f"Error: {e}")

    def pd_unique_customers_per_country(self, df: pd.DataFrame) -> pd.Series:
        """Counts the number of unique customers per country."""
        try:
            return df.groupby("Country")["Customer ID"].nunique()
        except Exception as e:
            print(f"Error: {e}")

    def pd_average_order_value_per_country(self, df: pd.DataFrame) -> pd.Series:
        """Computes the average order value per country."""
        try:
            return df.groupby("Country")["Amount"].mean()
        except Exception as e:
            print(f"Error: {e}")

    def pd_transactions_per_customer(self, df: pd.DataFrame) -> pd.Series:
        """Counts the number of transactions per customer."""
        try:
            return df.groupby("Customer ID")["Invoice"].nunique()
        except Exception as e:
            print(f"Error: {e}")

    def pd_total_amount_spent_per_customer(self, df: pd.DataFrame) -> pd.Series:
        """Calculates the total amount spent per customer."""
        try:
            return df.groupby("Customer ID")["Amount"].sum()
        except Exception as e:
            print(f"Error: {e}")

    def pd_average_order_value_per_customer(self, df: pd.DataFrame) -> pd.Series:
        """Computes the average order value per customer."""
        try:
            return df.groupby("Customer ID")["Amount"].mean()
        except Exception as e:
            print(f"Error: {e}")

            
class PolarsAggregation:

    def __init__(self, dataframe: pd.DataFrame):
            """Initialize the class with a Pandas DataFrame."""
            self.dataframe = dataframe
        
    
    # Polars aggregate functions
    def pol_transaction_per_country(self, df: pl.DataFrame) -> pl.DataFrame:
        """Counts the number of transactions per country."""
        try:
            return df.group_by("Country").agg(pl.col("Invoice").count())
        except Exception as e:
            print(f"Error: {e}")
        
    def pol_transaction_revenue_per_country(self, df: pl.DataFrame) -> pl.DataFrame:
        """Calculates the total transaction amount per country."""
        try:
            return df.group_by("Country").agg(pl.col("Amount").sum())
        except Exception as e:
            print(f"Error: {e}")
        
    def pol_unique_customers_per_country(self, df: pl.DataFrame) -> pl.DataFrame:
        """Counts the number of unique customers per country."""
        try:
            return df.group_by("Country").agg(pl.col("Customer ID").n_unique())
        except Exception as e:
            print(f"Error : {e}")
        
    def pol_average_order_value_per_country(df: pl.DataFrame) -> pl.DataFrame:
        """Computes the average order value per country."""
        try:
            return df.group_by("Country").agg(pl.col("Amount").mean())
        except Exception as e:
            print(f"Error: {e}")
        
    def pol_transactions_per_customer(self, df: pl.DataFrame) -> pl.DataFrame:
        """Counts the number of transactions per customer."""
        try:
            return df.group_by("Customer ID").agg(pl.col("Invoice").n_unique())
        except Exception as e:
            print(f"Error: {e}")
        
    def pol_total_amount_spent_per_customer(self, df: pl.DataFrame) -> pl.DataFrame:
        """Calculates the total amount spent per customer."""
        try:
            return df.group_by("Customer ID").agg(pl.col("Amount").sum())
        except Exception as e:
            print(f"Error: {e}")
        
    def pol_average_order_value_per_customer(self, df: pl.DataFrame) -> pl.DataFrame:
        """Computes the average order value per customer."""
        try:
            return df.group_by("Customer ID").agg(pl.col("Amount").mean())
        except Exception as e:
            print(f"Error: {e}")
        