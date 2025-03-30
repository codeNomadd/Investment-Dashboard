# Stock Data Fetcher

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)

A simple Python script to fetch stock market data from Alpha Vantage API and store it in MySQL for Tableau visualization.

## Dashboard Preview

![Investment Dashboard](dashboard/Tableau%20Dashboard.png)

## Project Overview

This project consists of two main components:
1. A Python script that fetches daily stock data and stores it in MySQL
2. A Tableau dashboard for visualizing the stored data

## Quick Setup

1. Install MySQL and create a database:
```sql
CREATE DATABASE stocks;
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables in `.env`:
```env
# Alpha Vantage API Configuration
ALPHA_VANTAGE_API_KEY=your_api_key_here

# MySQL Database Configuration
DB_HOST=localhost
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=stocks

# Stock Symbols to Track
STOCK_SYMBOLS=AAPL,MSFT,GOOGL,AMZN
```

4. Run the script:
```bash
python stock_fetcher.py
```

## Data Structure

The script creates a `stocks` table with the following schema:
```sql
CREATE TABLE stocks (
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
);
```

## Dashboard Components

### 1. Portfolio Performance Timeline
- **Interactive time series visualization** tracking total portfolio value (2022-2024)
- Milestone annotations highlight key events and decisions
- Helps identify long-term trends and pattern recognition
- **Value Add**: Enables investors to correlate market events with portfolio performance

### 2. Asset Allocation Overview
- **Dynamic pie chart** displaying current portfolio composition
- Color-coded segments with percentage breakdowns
- Hover tooltips reveal detailed asset information
- **Value Add**: Quick assessment of portfolio diversification and rebalancing needs

### 3. Relative Performance Index
- **Normalized performance chart** comparing top 5 holdings
- Baseline-adjusted growth trajectories
- Custom date range selection
- **Value Add**: Easily identify outperforming and underperforming assets

### 4. Monthly Performance Analysis
- **Waterfall chart** showing month-over-month gains/losses
- Color-coded bars (green for gains, red for losses)
- Cumulative trend line overlay
- **Value Add**: Track investment momentum and identify seasonal patterns

### 5. Smart Asset Legend
- Interactive sidebar with asset details
- Real-time price updates and daily changes
- Brand logos for quick visual recognition
- **Value Add**: Consolidated view of key metrics for each holding

### 6. Advanced Filtering
- Flexible date range selection
- Asset-specific filtering capabilities
- Market cap and sector filters
- **Value Add**: Focused analysis of specific time periods or asset groups

## Dashboard Insights

The dashboard is designed to answer critical investment questions:
- How is my portfolio performing over time?
- Am I properly diversified across assets?
- Which holdings are driving returns?
- What are my monthly investment patterns?
- Where should I consider rebalancing?

## Current Features
- Real-time stock price charts
- Price trend indicators
- Volume analysis
- Basic technical indicators

## Automation

To automatically update stock data daily, add a cron job:

```bash
# Run at 6 PM every weekday
0 18 * * 1-5 cd /path/to/project && python stock_fetcher.py
```

## Dependencies

- Python 3.x
- MySQL 8.0+
- Alpha Vantage API key
- Required Python packages:
  - requests
  - mysql-connector-python
  - python-dotenv

## License

This project is licensed under the MIT License - see LICENSE.txt for details. 