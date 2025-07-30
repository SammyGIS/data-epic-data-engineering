"""
Author: Ajeyomi Adeodyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 19-03-2025
"""

import requests
import json
import os

from src.config import URL

from logger.logger import setup_logging

# Setup logger
logger = setup_logging()


def extract_imdb_data(
    api_key: str, host: str, output_path: str, data_name: str = "data.json"
) -> json:
    """Extract data from the IMDb Rapid API and save it as a JSON file."""
    try:
        headers = {"x-rapidapi-key": api_key, "x-rapidapi-host": host}

        response = requests.get(URL, headers=headers)
        response.raise_for_status()

        os.makedirs(output_path, exist_ok=True)

        with open(os.path.join(output_path, data_name), "w") as f:
            json.dump(response.json(), f, indent=4)

        logger.info(
            f"Data successfully saved to {os.path.join(output_path, data_name)}"
        )

        return os.path.join(output_path, data_name)

    except Exception as e:
        logger.error(f"An error occurred: {e}")
