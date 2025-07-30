"""
Author: Ajeyomi Adedoyin Samuel
Date: 01-03-2025
Email: adedoyinsamuel25@gmail.com

https://medium.com/@chodvadiyasaurabh/building-a-file-upload-and-download-api-with-python-and-fastapi-3de94e4d1a35
https://stackoverflow.com/questions/67295253/how-to-download-a-file-using-fastapi?noredirect=1
"""
import pandas as pd
import polars as pl

def pandas_read_data(file_path:str) -> pd.DataFrame:
    """Read data from an Excel file"""
    try:
        pandas_df = pd.read_excel(file_path)
        return pandas_df
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None
    
def polars_read_data(file_path: str) -> pl.DataFrame:
    """Reads an Excel file with Polars"""
    try:
        polars_df = pl.read_excel(file_path, has_header=True)
        return polars_df
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def pd_download_data(df:pd.DataFrame, download_format: str, file_name: str = "online_retail"):
    try:
        if download_format == ".parquet":
            df.to_parquet(f"{file_name}.parquet")

        elif download_format == ".json":
            df.to_json(f"{file_name}.json", orient="records")
        else:
            raise ValueError("Invalid format. Use '.parquet' or '.json'.")
        print(f"File saved as {file_name}{download_format}")

    except Exception as e:
        print(f"Error: {e}")

def pl_download_data(df:pd.DataFrame, download_format: str, file_name: str = "online_retail"):
    try:
        if download_format == ".parquet":
            df.to_parquet(f"{file_name}.parquet")

        elif download_format == ".json":
            df.to_json(f"{file_name}.json", orient="records")
        else:
            raise ValueError("Invalid format. Use '.parquet' or '.json'.")
        print(f"File saved as {file_name}{download_format}")

    except Exception as e:
        print(f"Error: {e}")