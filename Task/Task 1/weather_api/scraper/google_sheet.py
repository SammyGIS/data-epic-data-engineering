"""
Author: Ajeyomi Adedoyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 21-02-2025

https://blog.finxter.com/how-to-append-data-in-a-google-sheet-with-python/
"""

from weather_api.utils.google_sheet_utils import connect_to_sheet

def load_data_to_sheet(df, google_sheet_name, service_key_path):
    """
    Loads data from a Pandas DataFrame and appends it to a Google Sheet.
    Parameters:
    - df (pd.DataFrame): The DataFrame containing data.
    - google_sheet_name (str): Name of the Google Sheet.
    - worksheet_index (int): Index of the worksheet (default is the first sheet).
    """
    try:
        sheet = connect_to_sheet(google_sheet_name,service_key_path)
        # Convert DataFrame to list of lists
        data = df.values.tolist()

        # Batch update
        sheet.append_rows(data, value_input_option="RAW")

        print("Data appended successfully!")
    except Exception as e:
        print(f"An Error  occured: {e}")