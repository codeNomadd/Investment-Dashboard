import os
import logging
import requests
from mysql.connector import connect, Error
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://www.alphavantage.co/query?"
FUNCTION = "TIME_SERIES_DAILY"
DATATYPE = "json"

def get_db_connection():
    return connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def update_stock_data(symbols):
    api_key = os.getenv("API_KEY")
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        for symbol in symbols:
            table_name = f"{symbol}_stock"
            create_table_query = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                timestamp DATE NOT NULL,
                high DECIMAL(10,2) NOT NULL,
                volume BIGINT NOT NULL
            )
            """
            cursor.execute(create_table_query)

            # Fetch stock data
            api_url = f"{API_URL}function={FUNCTION}&symbol={symbol}&apikey={api_key}&datatype={DATATYPE}"
            response = requests.get(api_url).json()
            time_series = response.get("Time Series (Daily)", {})

            for date, daily_data in time_series.items():
                query = f"""
                INSERT INTO {table_name} (timestamp, high, volume)
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY UPDATE high = VALUES(high), volume = VALUES(volume)
                """
                cursor.execute(query, (date, float(daily_data["2. high"]), int(daily_data["5. volume"])))

            connection.commit()
    except Error as e:
        logging.error(f"Error updating stock data: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
