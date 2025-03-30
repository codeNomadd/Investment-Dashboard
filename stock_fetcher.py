import os
from datetime import datetime
import requests
import mysql.connector
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class StockDataFetcher:
    def __init__(self):
        self.api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
        self.base_url = "https://www.alphavantage.co/query"
        self.db = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', ''),
            database=os.getenv('DB_NAME', 'stocks')
        )
        self.cursor = self.db.cursor()
        self.setup_database()

    def setup_database(self):
        """Create stocks table if it doesn't exist"""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS stocks (
                id INT AUTO_INCREMENT PRIMARY KEY,
                symbol VARCHAR(10) NOT NULL,
                date DATE NOT NULL,
                open_price FLOAT NOT NULL,
                high_price FLOAT NOT NULL,
                low_price FLOAT NOT NULL,
                close_price FLOAT NOT NULL,
                volume BIGINT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE KEY unique_stock_date (symbol, date)
            )
        """)
        self.db.commit()

    def fetch_stock_data(self, symbol):
        """Fetch stock data from Alpha Vantage"""
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "apikey": self.api_key
        }
        
        response = requests.get(self.base_url, params=params)
        return response.json()

    def save_stock_data(self, symbol, data):
        """Save stock data to database"""
        time_series = data.get("Time Series (Daily)", {})
        
        for date_str, values in time_series.items():
            query = """
                INSERT INTO stocks 
                (symbol, date, open_price, high_price, low_price, close_price, volume)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                open_price = VALUES(open_price),
                high_price = VALUES(high_price),
                low_price = VALUES(low_price),
                close_price = VALUES(close_price),
                volume = VALUES(volume)
            """
            
            values = (
                symbol,
                date_str,
                float(values["1. open"]),
                float(values["2. high"]),
                float(values["3. low"]),
                float(values["4. close"]),
                int(values["5. volume"])
            )
            
            self.cursor.execute(query, values)
        
        self.db.commit()

    def update_all_stocks(self, symbols):
        """Update data for all provided stock symbols"""
        for symbol in symbols:
            print(f"Fetching data for {symbol}...")
            try:
                data = self.fetch_stock_data(symbol)
                if "Error Message" in data:
                    print(f"Error for {symbol}: {data['Error Message']}")
                    continue
                self.save_stock_data(symbol, data)
                print(f"Successfully updated {symbol}")
            except Exception as e:
                print(f"Error updating {symbol}: {str(e)}")

    def close(self):
        """Close database connection"""
        self.cursor.close()
        self.db.close()

def main():
    # List of stock symbols to track
    symbols = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']  # Add your symbols here
    
    fetcher = StockDataFetcher()
    try:
        fetcher.update_all_stocks(symbols)
    finally:
        fetcher.close()

if __name__ == "__main__":
    main() 