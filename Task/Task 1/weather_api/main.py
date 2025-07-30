"""
Author: Ajeyomi Adedoyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 21-02-2025

https://www.geeksforgeeks.org/using-google-sheets-as-database-in-python/

"""


import sys
# set all depencies (module) part
sys.path.append("../")


from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import uvicorn
from weather_api.scraper import scraper, google_sheet

from weather_api.utils.utils import (
    get_current_time,
    check_if_current_data_indb,
    query_current_weather_info,
)
from weather_api.config import GOOGLE_SHEET_NAME, SERVICE_KEY_PATH



app = FastAPI(
    title="Weather API",
    description="This API provides real-time weather data for state capitals, "
    "fetching and storing the data in Google Sheets.",
    version="1.0.0",
    contact={
        "name": "Adedoyin Samuel",
        "email": "adedoyinsamuel25@gmail.com",
    },
)


def main():
    """
    Extracts and transforms weather data, then loads it into a Google Sheet.
    """
    data = scraper.extract_transform_main()
    google_sheet.load_data_to_sheet(data, GOOGLE_SHEET_NAME, SERVICE_KEY_PATH)


@app.get("/current_weather/{state_capital}")
def get_data(state_capital: str):
    """
    Retrieves the current weather information for the specified state capital.

    Args:
        state_capital (str): The name of the state capital to fetch weather data for.

    Returns:
        JSONResponse: A JSON object containing the weather data.
    """
    data = query_current_weather_info(
        state_capital, SERVICE_KEY_PATH, GOOGLE_SHEET_NAME, get_current_time
    )
    json_compatible_item_data = jsonable_encoder(data)
    return JSONResponse(content=json_compatible_item_data)


if __name__ == "__main__":
    # check db  and send data to db
    if not check_if_current_data_indb(GOOGLE_SHEET_NAME, SERVICE_KEY_PATH):
        main()

    # run fastapi
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
