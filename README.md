# Stock Market API

A RESTful API service for fetching and managing stock market data using the Alpha Vantage API. This service provides endpoints to track stock prices, volumes, and historical data for multiple stock symbols.

## Features

- Real-time stock data fetching from Alpha Vantage API
- MySQL database storage for historical data
- RESTful API endpoints for data access
- Support for multiple stock symbols
- Automatic data updates

## Prerequisites

- Python 3.x
- MySQL Server
- Alpha Vantage API Key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/stock-api.git
cd stock-api
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
CREATE DATABASE investment;
```

5. Configure environment variables:
Create a `.env` file in the project root with the following content:
```env
# Alpha Vantage API Configuration
ALPHA_VANTAGE_API_KEY=your_api_key_here

# MySQL Database Configuration
DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=investment

# Stock Symbols to Track (comma-separated)
STOCK_SYMBOLS=AAPL,MSFT,GOOGL,AMZN,META
```

## Project Structure

```
stock_api/
├── app/                    # Main application package
│   ├── models/            # Database models
│   ├── services/          # API endpoints and business logic
│   ├── utils/             # Utility functions
│   └── __init__.py        # App initialization
├── tests/                 # Test files
├── .env                   # Environment variables
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
    "message": "Data updated for AAPL"
}
```

### POST /api/stocks/update
Updates data for all tracked stock symbols.

**Response:**
```json
{
    "message": "All stocks updated successfully"
}
```

## Running the Application

1. Make sure your virtual environment is activated
2. Start the application:
```bash
python run.py
```

The API will be available at `http://localhost:5000`

## Database Schema

### Stocks Table
```sql
CREATE TABLE stocks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    symbol VARCHAR(10) NOT NULL,
    date DATE NOT NULL,
    high_price DECIMAL(10,2) NOT NULL,
    volume BIGINT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY unique_stock_date (symbol, date)
);
```

## Development

### Running Tests
```bash
pytest
```

### Adding New Features
1. Create a new branch: `git checkout -b feature/your-feature`
2. Make your changes
3. Run tests: `pytest`
4. Commit your changes: `git commit -m "Add your feature"`
5. Push to your branch: `git push origin feature/your-feature`
6. Create a Pull Request

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository or contact the maintainers. 