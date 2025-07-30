"""
Author: Ajeyomi Adedoyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 21-02-2025

https://fastapi.tiangolo.com/advanced/response-directly/
"""
import sys

import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials



# set all depencies (module) part
sys.path.append('../')

def connect_to_sheet(sheet_name, service_key_path):
    """
    Establish a connection to a Google Sheet.

    Args:
        sheet_name (str): The name of the Google Sheet.
        service_key_path (str): Path to the service account key file.

    Returns:
        gspread.models.Worksheet: The first sheet of the Google Sheet.
    """
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive",
    ]

    # Authenticate using the service account key
    creds = ServiceAccountCredentials.from_json_keyfile_name(service_key_path, scope)
    client = gspread.authorize(creds)

    # Open the Google Sheet and return the first worksheet
    sheet = client.open(sheet_name).sheet1
    return sheet

def get_all_record(sheet):
    """
    Retrieve all records from a Google Sheet and convert them into a DataFrame.

    Args:
        sheet (gspread.models.Worksheet): The Google Sheet worksheet object.

    Returns:
        pd.DataFrame: A DataFrame containing all records from the sheet.
    """
    data = sheet.get_all_records()  # Get all records from the sheet
    df = pd.DataFrame(data)  # Convert records to a Pandas DataFrame
    return df