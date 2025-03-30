# Stock Market API

A RESTful API service for fetching and managing stock market data using the Alpha Vantage API. This service provides endpoints to track stock prices, volumes, and historical data for multiple stock symbols.

## Features

- Real-time stock data fetching from Alpha Vantage API
- MySQL database storage for historical data
- RESTful API endpoints for data access
- Support for multiple stock symbols
- Automatic data updates and caching
- Rate limit handling for API requests

## Prerequisites

- Python 3.x
- MySQL Server 8.0+
- Alpha Vantage API Key (Get one at: https://www.alphavantage.co/support/#api-key)

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/codeNomadd/Investment-Dashboard.git
cd Investment-Dashboard
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up MySQL database:
```sql
mysql -u root -p
CREATE DATABASE investment;
```

5. Configure environment variables:
```bash
cp .env.example .env
```
Then edit `.env` with your settings:
```env
# Alpha Vantage API Configuration
ALPHA_VANTAGE_API_KEY=your_api_key_here

# MySQL Database Configuration
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=investment

# Stock Symbols to Track (comma-separated)
STOCK_SYMBOLS=AAPL,MSFT,GOOGL,AMZN,META
```

## Project Structure

```
Investment-Dashboard/
├── app/                    # Main application package
│   ├── models/            # Database models
│   │   └── stock.py      # Stock data model
│   ├── services/          # API endpoints and business logic
│   │   └── stock_service.py  # Stock data service
│   ├── utils/             # Utility functions
│   │   └── stock_data.py # Data fetching utilities
│   └── __init__.py        # App initialization
├── tests/                 # Test files
│   └── test_stock_data.py # Stock data tests
├── .env                   # Environment variables (create from .env.example)
├── requirements.txt       # Python dependencies
└── run.py                # Application entry point
```

## API Endpoints

### GET /api/stocks
Returns a list of all tracked stock symbols.

**Response:**
```json
{
    "symbols": ["AAPL", "MSFT", "GOOGL", "AMZN", "META"]
}
```

### GET /api/stocks/<symbol>
Fetches and updates data for a specific stock symbol.

**Parameters:**
- `symbol`: Stock symbol (e.g., AAPL, MSFT)

**Response:**
```json
{
    "message": "Data updated for AAPL",
    "data": {
        "symbol": "AAPL",
        "high_price": 223.81,
        "volume": 39818617,
        "date": "2024-03-28"
    }
}
```

### POST /api/stocks/update
Updates data for all tracked stock symbols.

**Response:**
```json
{
    "message": "All stocks updated successfully",
    "updated_symbols": ["AAPL", "MSFT", "GOOGL", "AMZN", "META"]
}
```

## Running the Application

1. Ensure MySQL is running:
```bash
brew services start mysql  # On macOS
sudo service mysql start  # On Linux
```

2. Activate virtual environment:
```bash
source venv/bin/activate
```

3. Start the application:
```bash
python run.py
```

The API will be available at `http://localhost:5000`

## Testing

### Running Tests
```bash
pytest
```

### Manual Testing with curl
Test the API endpoints:
```bash
# Get all stocks
curl http://localhost:5000/api/stocks

# Get specific stock
curl http://localhost:5000/api/stocks/AAPL

# Update all stocks
curl -X POST http://localhost:5000/api/stocks/update
```

## Error Handling

The API includes comprehensive error handling for:
- Invalid stock symbols
- Alpha Vantage API rate limits
- Database connection issues
- Missing or invalid API keys

## Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'feat: add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.

## Support

For support:
- Open an issue in the GitHub repository
- Contact: irmuun8881@gmail.com 