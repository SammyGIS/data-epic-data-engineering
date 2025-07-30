"""
Author: Ajeyomi Adedoyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 21-02-2025

https://codilime.com/blog/testing-apis-with-pytest-mocks-in-python/
https://laerciosantanna.medium.com/mastering-web-scraping-a-guide-to-crafting-reliable-python-scrapers-with-pytest-1d45db7af92b
"""
from scraper.scraper import transform_data, extract_data
from scraper.google_sheet import load_data_to_sheet
from utils.utils import connect_to_sheet

import requests
import pytest

def test_extract_data():
    extract_data()
    assert 
    pass

def test_transform_data():
    pass

def test_load_data_to_sheet():
    pass