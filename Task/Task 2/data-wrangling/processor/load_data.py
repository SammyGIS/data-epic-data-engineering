"""
Author: Ajeyomi Adedoyin Samuel
Date: 01-03-2025
Email: adedoyinsamuel25@gmail.com

https://gist.github.com/niftycode/a747648db1b79396b8e4814946a4dba2
https://docs.pola.rs/api/python/dev/reference/api/polars.read_excel.html


### **Task 2: Data Loading**
"""
import requests
import zipfile
import os

def download_data(url, file_name):
    """Download a file from a URL and save it locally."""

    # Create a 'data' folder if it doesn't exist
    os.makedirs("data", exist_ok=True)

    file_path = os.path.join("data", file_name)

    # check if the data exists
    if os.path.exists(file_path):
        print(f"{file_name} already exists")
        return file_path
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)

        with open(file_path, 'wb') as f:
            f.write(response.content)

        print(f"Download complete: {file_name}")
        

    except requests.exceptions.RequestException as e:
        print(f"Download failed: {e}")


def extract_zip_file(zip_file, extract_to="data"):
    """Extract a ZIP file to the specified directory and return a string of extracted .xlsx files."""
    # check if the data exists
    try:
        with zipfile.ZipFile(zip_file, 'r') as file:
            file.extractall(extract_to)
        
        # List all extracted files and filter for .xlsx files
        extracted_files = [f for f in os.listdir(extract_to) if f.endswith(".xlsx")]
        
        print(f"Extraction complete: {zip_file} → {extract_to}")
        return ", ".join(extracted_files) if extracted_files else "No .xlsx files found"

    except Exception as e:
        print(f"Extraction failed: {e}")


def download_extract_zip_file(url, file_name)-> str:
    zip_file_path = download_data(url, file_name)
    file_path = extract_zip_file(zip_file_path)
    return os.path.join("data",file_path)