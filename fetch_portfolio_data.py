import os
import logging
import requests
import mysql.connector
from mysql.connector import Error
from datetime import datetime
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables
load_dotenv()

# Constants
API_URL = "https://www.alphavantage.co/query?"
FUNCTION = "TIME_SERIES_DAILY"
DATATYPE = "json"

# List of stock symbols to fetch data for
SYMBOLS = ["aapl", "googl", "msft", "amzn", "tsla"]  # Add your portfolio symbols here

# Inform users about adding portfolio symbols
logging.info("If you have a portfolio, add your stock symbols to the 'SYMBOLS' list in the script.")

def create_table(cursor, symbol):
    """
    Creates a MySQL table for the given stock symbol if it doesn't exist.
    """
    table_name = f"{symbol}_stock"
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        timestamp DATE NOT NULL,
        high DECIMAL(10,2) NOT NULL,
        volume BIGINT NOT NULL
    )
    """)

def get_last_update_date(cursor, symbol):
    """
    Gets the last update date from the database for the given stock symbol.
    """
    table_name = f"{symbol}_stock"
    cursor.execute(f"SELECT MAX(timestamp) FROM {table_name}")
    result = cursor.fetchone()
    return result[0] if result[0] else None

def get_stock_data(api_url):
    """
    Fetches stock data from the API.
    """
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data.get("Time Series (Daily)", {})
    else:
        logging.error(f"Error fetching data: {response.status_code}")
        return {}

def filter_new_data(time_series, last_update_date):
    """
    Filters stock data to include only entries newer than the last update date.
    """
    filtered_data = []
    last_update_datetime = datetime.combine(last_update_date, datetime.min.time()) if last_update_date else None
    for date, daily_data in time_series.items():
        current_date = datetime.strptime(date, "%Y-%m-%d")
        if last_update_datetime is None or current_date > last_update_datetime:
            filtered_data.append((
                date,
                float(daily_data["2. high"]),
                int(daily_data["5. volume"]),
            ))
    return filtered_data

def insert_data(cursor, data, symbol):
    """
    Inserts new stock data into the database for the given symbol.
    """
    table_name = f"{symbol}_stock"
    query = f"""
    INSERT INTO {table_name} (timestamp, high, volume)
    VALUES (%s, %s, %s)
    """
    cursor.executemany(query, data)

def main():
    api_key = os.getenv("API_KEY")
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        cursor = connection.cursor()

        for symbol in SYMBOLS:
            # Prepare the API URL
            final_api_url = f"{API_URL}function={FUNCTION}&symbol={symbol}&outputsize=full&apikey={api_key}&datatype={DATATYPE}"
            logging.info(f"Fetching data for {symbol}...")
            
            # Ensure table exists
            create_table(cursor, symbol)

            # Fetch and process data
            time_series = get_stock_data(final_api_url)
            if time_series:
                last_update_date = get_last_update_date(cursor, symbol)
                new_data = filter_new_data(time_series, last_update_date)
                if new_data:
                    insert_data(cursor, new_data, symbol)
                    connection.commit()
                    logging.info(f"Inserted {len(new_data)} new records for {symbol}.")
                else:
                    logging.info(f"No new data to update for {symbol}.")
            else:
                logging.warning(f"No data returned for {symbol}.")

    except Error as e:
        logging.error(f"Database error: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    main()