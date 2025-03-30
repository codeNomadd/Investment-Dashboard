from stock_data import update_stock_data
import os
from dotenv import load_dotenv

def test_stock_data():
    # Load environment variables
    load_dotenv()
    
    # Get stock symbols from environment
    symbols = os.getenv('STOCK_SYMBOLS', '').split(',')
    
    # Test with a single symbol first
    test_symbol = symbols[0] if symbols else 'AAPL'
    print(f"Testing with symbol: {test_symbol}")
    
    try:
        # Update stock data
        update_stock_data([test_symbol])
        print(f"Successfully updated stock data for {test_symbol}")
    except Exception as e:
        print(f"Error updating stock data: {e}")

if __name__ == "__main__":
    test_stock_data() 