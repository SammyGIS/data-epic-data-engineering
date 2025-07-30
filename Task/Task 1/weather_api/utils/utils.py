from datetime import  datetime
from datetime import timedelta
import json
from weather_api.utils.google_sheet_utils import connect_to_sheet, get_all_record


def get_current_time():
    """
    Get the current date and the full hour (current or next) based on the 30-minute rule.

    Returns:
        tuple: (current_date as str, full_hour as str in HH:00 format)
    """
    now = datetime.now()
    if now.minute < 30:
        full_hour = now.replace(minute=0, second=0, microsecond=0)
    else:
        full_hour = (now + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)

    return str(now.date()), full_hour.strftime("%H:00")

def check_if_current_data_indb(sheet_name, service_key_path):
    """
    Check if weather data for the current date exists in the database (Google Sheets).

    Args:
        sheet_name (str): Name of the Google Sheet.
        service_key_path (str): Path to the service key for authentication.

    Returns:
        bool: True if current date data is found, False otherwise.
    """
    data = get_all_record(connect_to_sheet(sheet_name, service_key_path))
    current_date, _ = get_current_time()

    if data.empty:
        return False  # Explicitly return False

    return not data[data["date"] == current_date].empty

def query_current_weather_info(state_capital: str, service_key_path, sheet_name, get_current_time):
    """
    Query weather information for a given state capital from Google Sheets.

    Args:
        state_capital (str): Name of the state capital.
        service_key_path (str): Path to the service key for authentication.
        sheet_name (str): Name of the Google Sheet.
        get_current_time (function): Function to fetch the current date and time.

    Returns:
        list or str: List of matching weather records in dictionary format or an error message in JSON.
    """
    try:
        # Convert input to lowercase and strip spaces
        state_capital = state_capital.lower().strip()

        # Get all records from Google Sheets
        data = get_all_record(connect_to_sheet(sheet_name, service_key_path))

        # Get the current date and time
        current_date, current_time = get_current_time()

        # Ensure required columns exist
        required_columns = {"state", "date", "time"}
        if not required_columns.issubset(data.columns):
            missing_cols = required_columns - set(data.columns)
            raise ValueError(f"Missing required columns: {', '.join(missing_cols)}")

        # Convert 'state' column to lowercase
        data["state"] = data["state"].str.lower()

        # Filter the DataFrame for matching date, time, and state
        match = data[
            (data["date"] == current_date)
            & (data["time"] == current_time)
            & (data["state"] == state_capital)
        ]

        # Return the filtered data as JSON
        return match.to_dict(orient="records")

    except Exception as e:
        return json.dumps({"error": str(e)}, indent=4)