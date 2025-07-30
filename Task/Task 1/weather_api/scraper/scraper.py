"""
Author: Ajeyomi Adedoyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 21-02-2025

https://medium.com/geekculture/web-scraping-tables-in-python-using-beautiful-soup-8bbc31c5803e
https://www.geeksforgeeks.org/re-search-in-python/

"""

import sys
# set all depencies (module) part
sys.path.append('../')


import re
from typing import Any, List
from datetime import datetime
from datetime import timedelta
import html
import time
from weather_api.config import STATES,URL
from weather_api.logger import logger

import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_full_url(url: str, state: str, date: str) -> str:
    """
    Construct the full URL by formatting it with the state and date.

    Args:
        url (str): The base URL.
        state (str): The state for which weather data is needed.
        date (str): The date in the required format.

    Returns:
        str: The formatted URL with state and date.
    """
    try:
        full_url = url.format(state, date)
        return full_url
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

def generate_7days_dates() -> List[str]:
    """
    Generate a list of dates for today and the next 7 days in 'YYYYMMDD' format.

    Returns:
        List[str]: A list of date strings.
    """
    dates = []
    try:
        for i in range(8):
            day = timedelta(days=i)
            updated_date = datetime.today().date() + day
            dates.append(updated_date.strftime("%Y%m%d"))  # Format as 'YYYYMMDD'
        return dates
    except Exception as e:
        logger.exception("An error occurred",{e})
        return []

def extract_data(url: str) -> Any:
    """
    Extract the HTML table containing weather data from the given URL.

    Args:
        url (str): The URL to fetch data from.

    Returns:
        Any: The extracted HTML table element.
    """
    try:
        response = requests.get(url)
        if response.status_code != 200:
            logger.error(f"Website not loading, Error: {response.status_code}")
            return None

        soup = BeautifulSoup(response.content, "html.parser")
        return soup.find("table", id="wt-hbh")
    except Exception as e:
        logger.exception(f"An error occurred: {e}")
        return None

def get_wind_direction(data: List[Any]) -> str:
    """
    Extract wind direction from an HTML element.

    Args:
        data (List[Any]): The HTML data containing wind direction information.

    Returns:
        str: The extracted wind direction or an empty string if not found.
    """
    try:
        str_data = str(data)
        match = re.search(r'title="(.*?)"', str_data)
        return match.group(1) if match else ""
    except Exception as e:
        logger.exception("An error occurred",{e})
        return ""

def transform_data(html_table:html, helper_function=None) -> pd.DataFrame:
    """
    Transform extracted HTML table data into a structured Pandas DataFrame.

    Args:
        html_table (Any): The HTML table containing weather data.
        helper_function (function, optional): A helper function to extract wind direction.

    Returns:
        pd.DataFrame: A DataFrame containing processed weather data.
    """
    time_list = []
    temp  = []
    weather  = []
    feels  = []
    wind  = []
    wind_dir  = []
    humidity  = []
    chance  = []
    amount  = []

    try:
        for row in html_table.find_all("tr"):
            cells = row.find_all("td")
            timeline = row.find_all("th")

            if len(cells) == 9:
                time_list.append(timeline[0].text.strip()[:5])
                temp.append(cells[1].text.strip().split("°C")[0])
                weather.append(cells[2].text.strip())
                feels.append(cells[3].text.strip().split("°C")[0])
                wind.append(cells[4].text.strip().split(" ")[0])
                wind_dir.append(helper_function(cells[5]) if helper_function else "")
                humidity.append(cells[6].text.strip())
                chance.append(cells[7].text.strip())
                amount.append(cells[8].text.strip())

        data_dict = {
            "time": time_list,
            "temp_C": temp,
            "weather": weather,
            "feels_C": feels,
            "wind_km/h": wind,
            "wind_direction": wind_dir,
            "humidity_%": humidity,
            "precipitation_chance_%": chance,
            "precipitation_amount": amount,
        }

        return pd.DataFrame(data_dict)
    except Exception as e:
        logger.exception("An error occurred",{e})
        return pd.DataFrame()

def extract_transform_main() -> pd.DataFrame:
    """
    Main function to extract and transform weather data for multiple states and dates.

    Returns:
        pd.DataFrame: A DataFrame containing processed weather data for all states and dates.
    """
    start_time = time.time()
    logger.info(f"Start time: {datetime.now()}")

    all_data = []  # List to store processed data

    for date in generate_7days_dates():
        for state in STATES:
            url = get_full_url(url=URL, state=state, date=date)
            raw_data = extract_data(url)

            if raw_data:
                processed_data = transform_data(raw_data, get_wind_direction)
                processed_data["state"] = state
                processed_data["url"] = url
                processed_data["date"] = datetime.strptime(date, "%Y%m%d").strftime("%Y-%m-%d")
                all_data.append(processed_data)

    # Combine all data into a single DataFrame
    final_data = pd.concat(all_data, ignore_index=True) if all_data else pd.DataFrame()

    end_time = time.time()
    logger.info(f"End time: {datetime.now()}")
    logger.info(f"Total processing time: {end_time - start_time:.2f} seconds")

    return final_data

if __name__ == "__main__":
    extract_transform_main()